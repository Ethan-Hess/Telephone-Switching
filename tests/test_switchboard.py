from pathlib import Path

from src.core import Switchboard, load_phones


def load_switchboard() -> Switchboard:
    csv_path = Path(__file__).parent / "fixtures" / "telephone-numbers.csv"
    phones = load_phones(str(csv_path))
    return Switchboard(phones)


def test_normal_call_flow() -> None:
    switchboard = load_switchboard()
    alice = switchboard.resolve_phone("Alice")
    bob = switchboard.resolve_phone("Bob")
    assert alice and bob

    assert switchboard.offhook(alice) == ["Alice hears dialtone"]
    assert switchboard.call(alice, bob) == [
        "Alice hears ringback",
        "Bob hears ringing",
    ]
    assert switchboard.offhook(bob) == ["Alice and Bob are talking"]
    assert switchboard.onhook(bob) == ["Alice hears silence"]


def test_busy_response() -> None:
    switchboard = load_switchboard()
    alice = switchboard.resolve_phone("Alice")
    bob = switchboard.resolve_phone("Bob")
    cara = switchboard.resolve_phone("Cara")
    assert alice and bob and cara

    switchboard.offhook(alice)
    switchboard.call(alice, bob)
    switchboard.offhook(bob)

    assert switchboard.offhook(cara) == ["Cara hears dialtone"]
    assert switchboard.call(cara, alice) == ["Cara hears busy"]


def test_transfer_flow() -> None:
    switchboard = load_switchboard()
    alice = switchboard.resolve_phone("Alice")
    bob = switchboard.resolve_phone("Bob")
    cara = switchboard.resolve_phone("Cara")
    assert alice and bob and cara

    switchboard.offhook(alice)
    switchboard.call(alice, bob)
    switchboard.offhook(bob)

    assert switchboard.transfer(alice, cara) == [
        "Alice hears ringback",
        "Cara hears ringing",
    ]
    assert switchboard.offhook(cara) == [
        "Alice hears silence",
        "Bob and Cara are talking",
    ]
