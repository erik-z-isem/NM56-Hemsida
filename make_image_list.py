from pathlib import Path
import json

IMG_DIR = Path("bilder/fullsize")
OUT_FILE = IMG_DIR / "images.js"

EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"}

def main():
    files = [
        p.name
        for p in IMG_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in EXTS and p.name != OUT_FILE.name
    ]

    # Sort for stable ordering (case-insensitive)
    files.sort(key=str.lower)

    OUT_FILE.write_text(
        "window.IMAGE_FILES = " + json.dumps(files, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )

    print(f"Wrote {len(files)} entries to {OUT_FILE}")

if __name__ == "__main__":
    main()