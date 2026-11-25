"""One Line, One Laugh.

Writes exactly one funny line to /output/entry.txt, then reads the file
back and verifies it: UTF-8 text, 1 to 200 characters, exactly one line,
and not only whitespace. The output is deterministic: the same bytes on
every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "I put my phone on Do Not Disturb and it immediately disturbed me with a notification saying Do Not Disturb is on."


def validate(text):
    """Check that *text* is a single valid one-liner.

    Raises ValueError with a plain reason when any gate fails.
    """
    if not isinstance(text, str):
        raise ValueError("line must be text")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1 to 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be exactly one line")
    if any(ord(char) < 32 for char in text):
        raise ValueError("line must not contain control characters")
    text.encode("utf-8")
    return True


def main():
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    validate(written)
    if written != LINE:
        raise ValueError("verification failed: file content differs from the line")
    print("Wrote {} characters to {}".format(len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
