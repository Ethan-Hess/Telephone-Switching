from __future__ import annotations

from pathlib import Path
import sys

# Add the src directory to the Python path so local modules can be imported
sys.path.insert(0, str(Path(__file__).parent))

from commands import parse_command
from core import Switchboard, load_phones


def print_help() -> None:
    """Display help for available commands."""
    help_text = """
╔════════════════════════════════════════════════════════════════╗
║                   AVAILABLE COMMANDS                           ║
╠════════════════════════════════════════════════════════════════╣
║ status                  - Display status of all phones         ║
║ <phone> offhook         - Pick up the phone                    ║
║ <phone> onhook          - Hang up the phone                    ║
║ <phone> call <phone>    - Make a call                          ║
║ <phone> transfer <phone> - Transfer a call                     ║
║ <phone> conference <phone> - Add someone to a conference       ║
║ help                    - Show this help message               ║
║ quit / exit             - Exit the program                     ║
╠════════════════════════════════════════════════════════════════╣
║ Notes: Use phone names or 5-digit phone numbers                ║
║        Examples: "Alice call 12345" or "01234 offhook"         ║
╚════════════════════════════════════════════════════════════════╝"""
    print(help_text)


def print_welcome(phones) -> None:
    """Display welcome message, commands, and list available phones."""
    print("\n" + "=" * 60)
    print("           TELEPHONE SWITCHING SIMULATION")
    print("=" * 60)
    print_help()
    print("\nAvailable phones:")
    for phone in phones:
        print(f"  • {phone.name:12} ({phone.number})")
    print()


def run(csv_path: Path) -> int:
    phones = load_phones(str(csv_path))
    switchboard = Switchboard(phones)
    
    print_welcome(phones)

    try:
        while True:
            try:
                line = input("> ").strip()
            except EOFError:
                # Handle EOF gracefully (Ctrl+D or piped input)
                break
            
            if not line:
                continue
                
            command = parse_command(line)
            
            if not command:
                continue
                
            if command[0] == "quit":
                print("Goodbye!")
                return 0
                
            if command[0] == "help":
                print_help()
                continue
                
            if command[0] == "invalid":
                print("❌ Invalid command. Type 'help' for available commands.")
                continue
                
            if command[0] == "status":
                outputs = switchboard.status()
                print("\n" + "\n".join(outputs) + "\n")
                continue

            action = command[0]
            if action in {"offhook", "onhook"}:
                phone = switchboard.resolve_phone(command[1])
                if phone is None:
                    print(f"❌ Unknown phone: {command[1]}")
                    continue
                outputs = getattr(switchboard, action)(phone)
                if outputs:
                    print("\n" + "\n".join(outputs) + "\n")
                continue

            if action in {"call", "conference", "transfer"}:
                phone = switchboard.resolve_phone(command[1])
                target = switchboard.resolve_phone(command[2])
                if phone is None:
                    print(f"❌ Unknown phone: {command[1]}")
                    continue
                if target is None:
                    print(f"❌ Unknown phone: {command[2]}")
                    continue
                outputs = getattr(switchboard, action)(phone, target)
                if outputs:
                    print("\n" + "\n".join(outputs) + "\n")
                continue
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        return 0

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
