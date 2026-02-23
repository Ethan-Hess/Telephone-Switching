from __future__ import annotations

from typing import List, Optional, Tuple


Command = Tuple[str, ...]


def parse_command(line: str) -> Optional[Command]:
    stripped = line.strip()
    if not stripped:
        return None
    if stripped.lower() in {"status", "status()"}:
        return ("status",)

    tokens = stripped.split()
    if len(tokens) == 2 and tokens[1].lower() in {"offhook", "onhook"}:
        return (tokens[1].lower(), tokens[0])
    if len(tokens) == 3 and tokens[1].lower() in {"call", "transfer", "conference"}:
        return (tokens[1].lower(), tokens[0], tokens[2])
    if stripped.lower() in {"quit", "exit"}:
        return ("quit",)
    return ("invalid",)


def format_outputs(lines: List[str]) -> str:
    return "\n".join(lines)
