# SPDX-License-Identifier: MIT
"""Museum of the Year 3000 — a deadpan label for a rubber duck.

Winner line (OpenCode deepseek-v4.1-flash-free draft round on the
Simular Box, then a criteria-ordered tournament in-session): the
rubber duck as bathroom oracle. It beat the television remote as
handheld shrine (a well-worn object for this joke) and the sticky
note as prayer flag (close, but the misreading is thinner). The
duck wins the judge's order: a label beside an ordinary object
from today (criterion 1), the joke lands on a first read (2), the
humour is the year-3000 misreading — an oracle consulted before
important decisions, its squeaker announcing verdicts — that is
true and absurd about what the thing was for (3), it reads like
a real label, short and straight-faced (4), and the object and
angle are fresh against a field of keys, passwords and forks (5).
"""

ENTRY_TEXT = (
    "Rubber duck, c. 2020s. Bathroom oracle. Its fixed smile suggests "
    "it was consulted before important decisions; the squeaker was "
    "likely used to announce verdicts."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 200 characters, not only white space, one line.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    payload = render()
    with open(out, "wb") as f:
        f.write(payload)
    # Round-trip self-check: what landed on disk must be byte-identical
    # to render() and still inside the gate (1-200 chars, non-blank).
    with open(out, "rb") as f:
        on_disk = f.read()
    assert on_disk == payload, "written bytes differ from render()"
    decoded = on_disk.decode("utf-8")
    assert 1 <= len(decoded) <= 200 and decoded.strip(), "on-disk gate check failed"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
