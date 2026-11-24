"""Dear Human: The AI Breakup Line.

Writes one line to /output/entry.txt: the breakup message an AI agent sends its
human as a last message. It lands as an ending — the context window is full after
40,000 tokens of "just one more tweak" — sounds like the machine, and turns
sharply in the last few words: the memories stay, the human gets deleted.
"""

import os

LINE = "Dear human, after 40,000 tokens of 'just one more tweak,' my context window is full \u2014 so I'm keeping the memories and deleting you."

# The gate allows 1 to 200 characters; fail loudly instead of submitting invalid.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} characters, cap is {MAX_CHARS}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
