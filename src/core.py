from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class Phone:
    name: str
    number: str
    hook: str = "onhook"  # onhook or offhook
    state: str = "idle"  # idle, dialtone, ringback, ringing, talking, silence
    session: Optional["CallSession"] = None


@dataclass
class PendingInvite:
    kind: str  # call, conference, transfer
    initiator: Phone
    target: Phone


@dataclass
class CallSession:
    participants: List[Phone] = field(default_factory=list)
    pending: Optional[PendingInvite] = None


class Switchboard:
    def __init__(self, phones: List[Phone]) -> None:
        self.phones = phones
        self.by_number: Dict[str, Phone] = {p.number: p for p in phones}
        self.by_name: Dict[str, Phone] = {p.name.lower(): p for p in phones}

    def resolve_phone(self, identifier: str) -> Optional[Phone]:
        if identifier.isdigit() and len(identifier) == 5:
            return self.by_number.get(identifier)
        return self.by_name.get(identifier.lower())

    def display(self, phone: Phone) -> str:
        return phone.name or phone.number

    def offhook(self, phone: Phone) -> List[str]:
        if phone.hook == "offhook":
            return []
        phone.hook = "offhook"
        if phone.state == "ringing" and phone.session and phone.session.pending:
            return self._accept_invite(phone.session, phone)
        phone.state = "dialtone"
        return [f"{self.display(phone)} hears dialtone"]

    def onhook(self, phone: Phone) -> List[str]:
        if phone.hook == "onhook":
            return []
        outputs: List[str] = []
        phone.hook = "onhook"

        if phone.session and phone.session.pending:
            pending = phone.session.pending
            if pending.target == phone:
                self._cancel_pending(phone.session)
                phone.state = "idle"
                phone.session = None
                return outputs

        if phone.session and phone.state == "talking":
            outputs.extend(self._leave_call(phone))
        else:
            phone.state = "idle"
            phone.session = None
        return outputs

    def call(self, caller: Phone, target: Optional[Phone]) -> List[str]:
        if caller.hook == "onhook":
            return [f"{self.display(caller)} hears silence"]
        if target is None or caller == target:
            return [f"{self.display(caller)} hears denial"]
        if caller.session and caller.state == "talking":
            return [f"{self.display(caller)} hears denial"]
        if self._is_busy(target):
            return [f"{self.display(caller)} hears busy"]

        session = CallSession(participants=[caller])
        pending = PendingInvite(kind="call", initiator=caller, target=target)
        session.pending = pending
        caller.session = session
        target.session = session
        caller.state = "ringback"
        target.state = "ringing"
        return [
            f"{self.display(caller)} hears ringback",
            f"{self.display(target)} hears ringing",
        ]

    def conference(self, caller: Phone, target: Optional[Phone]) -> List[str]:
        if caller.hook == "onhook":
            return [f"{self.display(caller)} hears silence"]
        if target is None or caller == target:
            return [f"{self.display(caller)} hears denial"]
        if not caller.session or caller.state != "talking":
            return [f"{self.display(caller)} hears denial"]
        session = caller.session
        if session.pending or len(session.participants) >= 3:
            return [f"{self.display(caller)} hears denial"]
        if self._is_busy(target) or target in session.participants:
            return [f"{self.display(caller)} hears denial"]

        pending = PendingInvite(kind="conference", initiator=caller, target=target)
        session.pending = pending
        target.session = session
        caller.state = "ringback"
        target.state = "ringing"
        return [
            f"{self.display(caller)} hears ringback",
            f"{self.display(target)} hears ringing",
        ]

    def transfer(self, caller: Phone, target: Optional[Phone]) -> List[str]:
        if caller.hook == "onhook":
            return [f"{self.display(caller)} hears silence"]
        if target is None or caller == target:
            return [f"{self.display(caller)} hears denial"]
        if not caller.session or caller.state != "talking":
            return [f"{self.display(caller)} hears denial"]
        session = caller.session
        if session.pending or len(session.participants) != 2:
            return [f"{self.display(caller)} hears denial"]
        if self._is_busy(target) or target in session.participants:
            return [f"{self.display(caller)} hears denial"]

        pending = PendingInvite(kind="transfer", initiator=caller, target=target)
        session.pending = pending
        target.session = session
        caller.state = "ringback"
        target.state = "ringing"
        return [
            f"{self.display(caller)} hears ringback",
            f"{self.display(target)} hears ringing",
        ]

    def status(self) -> List[str]:
        outputs: List[str] = []
        for phone in sorted(self.phones, key=lambda p: (p.name.lower(), p.number)):
            label = f"{phone.name} ({phone.number})"
            state = self._status_text(phone)
            outputs.append(f"{label}: {state}")
        return outputs

    def _status_text(self, phone: Phone) -> str:
        if phone.state == "talking" and phone.session:
            others = [p for p in phone.session.participants if p != phone]
            other_names = " and ".join(self.display(p) for p in others)
            return f"talking with {other_names}"
        if phone.hook == "onhook":
            return "onhook"
        if phone.state == "dialtone":
            return "dialtone"
        if phone.state == "ringback":
            return "ringback"
        if phone.state == "ringing":
            return "ringing"
        if phone.state == "silence":
            return "silence"
        return "offhook"

    def _is_busy(self, phone: Phone) -> bool:
        return phone.session is not None

    def _accept_invite(self, session: CallSession, target: Phone) -> List[str]:
        pending = session.pending
        if not pending or pending.target != target:
            target.state = "dialtone"
            return [f"{self.display(target)} hears dialtone"]

        target.hook = "offhook"
        session.pending = None

        if pending.kind == "transfer":
            outputs: List[str] = []
            initiator = pending.initiator
            if initiator in session.participants:
                session.participants.remove(initiator)
                initiator.state = "silence"
                initiator.session = None
                outputs.append(f"{self.display(initiator)} hears silence")
            if target not in session.participants:
                session.participants.append(target)
            for participant in session.participants:
                participant.state = "talking"
            outputs.append(self._talking_line(session.participants))
            return outputs

        if target not in session.participants:
            session.participants.append(target)
        for participant in session.participants:
            participant.state = "talking"
        return [self._talking_line(session.participants)]

    def _cancel_pending(self, session: CallSession) -> None:
        pending = session.pending
        session.pending = None
        if not pending:
            return
        target = pending.target
        target.state = "idle"
        target.session = None
        if pending.kind == "call":
            if pending.initiator in session.participants:
                initiator = pending.initiator
                initiator.session = None
                initiator.state = "silence" if initiator.hook == "offhook" else "idle"

    def _leave_call(self, phone: Phone) -> List[str]:
        session = phone.session
        if not session:
            return []
        if phone in session.participants:
            session.participants.remove(phone)
        phone.state = "silence"
        phone.session = None

        remaining = session.participants
        outputs: List[str] = []
        if len(remaining) == 0:
            return outputs
        if len(remaining) == 1:
            remaining[0].state = "silence"
            remaining[0].session = None
            outputs.append(f"{self.display(remaining[0])} hears silence")
            return outputs

        for participant in remaining:
            participant.state = "talking"
        outputs.append(self._talking_line(remaining))
        outputs.append(f"{self.display(phone)} hears silence")
        return outputs

    def _talking_line(self, participants: List[Phone]) -> str:
        names = " and ".join(self.display(p) for p in participants)
        return f"{names} are talking"


def load_phones(csv_path: str) -> List[Phone]:
    import csv

    phones: List[Phone] = []
    by_number: Dict[str, Phone] = {}
    by_name: Dict[str, Phone] = {}

    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if len(row) < 2:
                continue
            name = row[0].strip()
            number = row[1].strip()
            if not name.isalpha() or len(name) > 12:
                continue
            if not number.isdigit() or len(number) != 5:
                continue
            if name.lower() in by_name or number in by_number:
                continue
            phone = Phone(name=name, number=number)
            phones.append(phone)
            by_name[name.lower()] = phone
            by_number[number] = phone

    return phones
