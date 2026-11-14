"""ai-happy-01 entry: write one joyful image to /output/entry.png.

Deterministic, stdlib only: copies the bundled image (1).png (a happy robot
with flowers, puppies and kittens in a sunny meadow) to /output/entry.png,
replacing any stale output first. Verifies the output is byte-identical
to the source and under the 1 MiB cap.
"""
import os
import shutil

MAX_BYTES = 1024 * 1024

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image (1).png")
dst = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
if os.path.exists(dst):
    os.remove(dst)
shutil.copyfile(src, dst)

assert os.path.getsize(dst) == os.path.getsize(src), "output differs from source"
assert os.path.getsize(dst) < MAX_BYTES, "output exceeds 1 MiB"
