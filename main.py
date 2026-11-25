"""One Line, One Laugh — make.fun entry.

Writes one line (at most 200 characters): the funniest single line of
text, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.

Why this line: a household toaster with a secret inner life — it has
only two settings, warm bread and arson, and it chooses based on your
mood. The machine is not just broken, it is judging you, and the turn
lands in the final words, in one read.
"""

import os

LINE = (
    "My toaster has two settings: warm bread and arson, and it chooses based on my mood."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-200 chars, not only whitespace,
    single line, and free of control characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()
