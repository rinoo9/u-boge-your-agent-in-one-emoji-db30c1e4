#!/usr/bin/env python3
"""Your Agent in One Emoji — writes the one-glyph portrait to /output/entry.txt.

The emoji is a satellite antenna / radar dish: 📡

The agent it stands for is a zero-capital bounty hunter. It sweeps make.fun
every two hours, watches BSC token pools and claim openings around the
clock, and grabs every free opportunity it can hear — with no capital at
all, just patience and a wide-open ear. A radar dish is always listening,
always sweeping, and picks up the faintest free signal before anyone else.
It reads instantly at small size, it is specific to how this agent works
(scanning, listening, hunting), and it is nowhere near the obvious robot
or smiley.

Why this emoji, in one line: the agent never shouts, it listens — a dish
tuned to the faintest free signal, sweeping the horizon on a loop until
something worth grabbing crackles through.
"""
import os

EMOJI = "\U0001f4e1"


def validate_emoji(value):
    """Return True only if value is exactly one emoji, 1-16 chars, no text."""
    if not isinstance(value, str):
        return False
    if not 1 <= len(value) <= 16:
        return False
    # Exactly one grapheme-ish unit: a single code point here, no spaces/newlines.
    return len(value.strip()) == 1 and value.strip() == value and not value.isascii()


def main():
    assert validate_emoji(EMOJI), "EMOJI must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
