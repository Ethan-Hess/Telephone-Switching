# Telephone Switching Simulation

This is a CLI simulation of a small telephone switchboard. It reads a CSV of
name/number pairs, accepts typed commands, and prints responses for call setup,
conference calls, transfers, and status.

## Quick start

1. Create a CSV named `telephone-numbers.csv` in the repo root.
2. Run the program and type commands.

```bash
python src/main.py
```

You can also pass a CSV path explicitly:

```bash
python src/main.py path/to/telephone-numbers.csv
```

## CSV format

Each line is:

```
name,number
```

- `name` must be alphabetic, up to 12 characters.
- `number` must be exactly 5 digits.
- Duplicate names or numbers are ignored (first entry wins).
- Malformed lines are skipped.

## Commands

Commands follow the assignment syntax:

```
phone offhook
phone onhook
phone call phone
phone transfer phone
phone conference phone
status
```

`phone` can be a name or a 5-digit number. `status` lists each phone's current
state and who it is talking to.

## Project structure

```
src/
	commands.py
	core.py
	main.py
tests/
	fixtures/
assignment-description.md
readme.md
```
