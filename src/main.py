from __future__ import annotations

import sys
from pathlib import Path

# Add the src directory to the Python path so local modules can be imported
sys.path.insert(0, str(Path(__file__).parent))

from commands import parse_command
from core import Switchboard, load_phones


def run(csv_path: Path) -> int:
    phones = load_phones(str(csv_path))
    switchboard = Switchboard(phones)

    for line in sys.stdin:
        command = parse_command(line)
        if not command:
            continue
        if command[0] == "quit":
            return 0
        if command[0] == "invalid":
            continue
        if command[0] == "status":
            outputs = switchboard.status()
            print("\n".join(outputs))
            continue

        action = command[0]
        if action in {"offhook", "onhook"}:
            phone = switchboard.resolve_phone(command[1])
            if phone is None:
                continue
            outputs = getattr(switchboard, action)(phone)
            if outputs:
                print("\n".join(outputs))
            continue

        if action in {"call", "conference", "transfer"}:
            phone = switchboard.resolve_phone(command[1])
            target = switchboard.resolve_phone(command[2])
            if phone is None:
                continue
            outputs = getattr(switchboard, action)(phone, target)
            if outputs:
                print("\n".join(outputs))
            continue

    return 0


def main() -> int:
    if len(sys.argv) > 1:
        csv_path = Path(sys.argv[1])
    else:
        csv_path = Path("telephone-numbers.csv")
    if not csv_path.exists():
        print(f"Missing CSV file: {csv_path}")
        return 1
    return run(csv_path)


if __name__ == "__main__":
    raise SystemExit(main())
