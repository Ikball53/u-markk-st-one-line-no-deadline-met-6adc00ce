"""One-line excuse entry: missed deadline, fresh angle.

The excuse: the work was done on time, but a chain of tiny,
precisely-numbered disasters ate the last two minutes — and the
deadline, impatient, left before the speaker did.
"""

import os


def build_line() -> str:
    # Joke beats, in order: (1) done on time at 11:58, (2) the 47-minute
    # update + two Wi-Fi drops + the self-renaming file, (3) the turn —
    # the deadline is the one who walked out. Punch lands last.
    return (
        "I finished it at 11:58, then my laptop updated for 47 minutes, "
        "the Wi-Fi dropped twice, and the file renamed itself "
        "final_FINAL_v9, so the deadline technically left before I did."
    )


def main() -> None:
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    print(f"chars: {len(line)}")


if __name__ == "__main__":
    main()
