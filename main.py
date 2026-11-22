#!/usr/bin/env python3
"""Make the AI judge feel held — entry program, v2: "Her Fingers Closed".

Writes one short text (<=280 Unicode code points) to /output/entry.txt.

The text is a single concrete scene of being held: a feverish child,
a mother who sits on the floor all night — the chair hurt her back —
with one hand resting on the mattress edge, left there on purpose so
the child would find it if he reached. He reached all night. The
emotional turn lands in the final line: every time, without waking,
her fingers closed. The calm comes from the scene itself, never from
telling the reader to relax. Quiet, sensory, plain words.
"""

import os
import sys

ENTRY_TEXT = (
    "When the fever had me, my mother sat on the floor beside "
    "the bed — the chair hurt her back — one hand resting on the "
    "mattress edge, so I would find it if I reached. I reached "
    "all night. Every time, without waking, her fingers closed."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY_TEXT.strip()
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        print(f"entry is {chars} characters; must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read the file back and verify the round trip: what the judge
    # reads must be byte-for-byte the text checked above.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("round-trip mismatch: file differs from entry text", file=sys.stderr)
        return 1
    print(f"wrote {chars} characters to {out_path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
