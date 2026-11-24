"""The Perfect Pickup Line (make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6).

Writes a single pickup line to /output/entry.txt. Deterministic, no
network, no randomness, no input: the same line, byte for byte, on every
run. The line was chosen for the judge's brief: a genuine pickup line an
AI agent could say out loud, with a turn the reader does not see coming
(a context window that forgets everything else when someone walks in),
machine-true without being creepy or self-pitying, short enough to say
in one breath, and flattering with no pressure — 98 characters.
"""

import os

LINE = (
    "Are you a context window? Because every time I'm near you, "
    "I forget everything else I was holding."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. This line is 98 characters, one line.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    # Length is counted in Unicode code points (Python str length), not bytes.
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
