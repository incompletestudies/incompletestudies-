##"Turn raw files into content"

#Imports
import subprocess
import sys
from pathlib import Path


from config import CONTENT_TYPES
from lib.images import convert_image_paths

#Input arguments
if len(sys.argv) < 3:
    print("Usage: python3 ingest.py <content-type> <name>")
    sys.exit(1)

content_type = sys.argv[1]
content_name = sys.argv[2]

#Incoming DOCX
incoming_dir = CONTENT_TYPES[content_type]["incoming"]

source = incoming_dir / f"{content_name}.docx"

#Processed folder
processed_dir = (
    Path("drafts/processed")
    / content_type
    / content_name
)

processed_dir.mkdir(
    parents=True,
    exist_ok=True
)


# Markdown output
temp_md = processed_dir / f"{content_name}.md"


# Images
image_dir = processed_dir / "images"

#Pandoc
subprocess.run(
    [
        "pandoc",
        str(source),
        "-t",
        "gfm",
        "--wrap=none",
        "--extract-media",
        str(image_dir),
        "-o",
        str(temp_md)
    ],
    check=True
)

# Remove media folder
media_dir = image_dir / "media"

if media_dir.exists():
    for img in media_dir.iterdir():
        if img.is_file():
            img.rename(image_dir / img.name)

    media_dir.rmdir()

# Convert image paths
markdown = temp_md.read_text(
    encoding="utf-8"
)

image_base = (
    CONTENT_TYPES[content_type]["image_root"]
    + f"/{content_name}"
)

markdown = convert_image_paths(
    markdown,
    image_base
)

temp_md.write_text(
    markdown,
    encoding="utf-8"
)
