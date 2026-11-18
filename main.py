#!/usr/bin/env python3
"""make.fun entry: news-image-20261118.

Writes one image summing up 18 November 2026's world news to
/output/entry.png.

Deterministic by design: it copies the bundled image asset byte for byte,
never re-encoding it, so the output bytes are exactly the asset bytes and
two runs always produce identical output.
No network, no randomness, no clock, no environment-dependent behaviour.
The asset is a JPEG (an allowed format for this competition); it is written
to the harness's fixed output path /output/entry.png, as required.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSET = HERE / "entry.jpg"
OUTPUT = Path("/output/entry.png")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # Byte-for-byte copy: no re-encode, so the digest below is the asset's.
    shutil.copyfile(ASSET, OUTPUT)
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes) sha256={digest}")


if __name__ == "__main__":
    main()
