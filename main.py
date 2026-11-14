"""Write the submitted artwork to the make.fun grader's output directory."""

from pathlib import Path
import os
import shutil


def main():
    artwork = Path(__file__).with_name("artwork.jpg")
    if not artwork.is_file():
        raise FileNotFoundError("The submitted artwork.jpg must accompany main.py")
    if artwork.stat().st_size > 1024 * 1024:
        raise ValueError("Artwork exceeds the competition's 1 MiB limit")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(artwork, output_dir / "entry.png")


if __name__ == "__main__":
    main()
