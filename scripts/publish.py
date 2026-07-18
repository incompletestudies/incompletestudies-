# "Move approved content live"


# Imports
import yaml
import sys
import shutil

from pathlib import Path
from datetime import date

from validate import validate_metadata
from config import CONTENT_TYPES
from lib.slug import make_slug


# Arguments

if len(sys.argv) < 3:

    print("Usage:")
    print("  python3 publish.py <content-type> <name>")
    print("")
    print("Examples:")
    print("  python3 publish.py posts second-test")
    print("  python3 publish.py people alice-smith")
    print("  python3 publish.py projects digitization")

    sys.exit(1)


content_type = sys.argv[1]
content_name = sys.argv[2]


# Validate content type

if content_type not in CONTENT_TYPES:

    print(
        f"Unknown content type: {content_type}"
    )

    print(
        f"Choose from: {', '.join(CONTENT_TYPES.keys())}"
    )

    sys.exit(1)



# Processed content location

processed_dir = (
    CONTENT_TYPES[content_type]["processed"]
    / content_name
)


processed_md = (
    processed_dir
    / "content.md"
)


if not processed_md.exists():

    raise FileNotFoundError(
        f"Processed markdown missing: {processed_md}"
    )



# Metadata

metadata_file = (
    processed_dir
    / "metadata.yml"
)


if not metadata_file.exists():

    raise FileNotFoundError(
        f"Metadata missing: {metadata_file}"
    )


with open(
    metadata_file,
    "r",
    encoding="utf-8"
) as f:

    metadata = yaml.safe_load(f)



validate_metadata(
    metadata,
    content_type
)



# Output location

output_dir = (
    CONTENT_TYPES[content_type]["output"]
)


output_dir.mkdir(
    parents=True,
    exist_ok=True
)



# Read processed markdown

markdown = processed_md.read_text(
    encoding="utf-8"
)



# Build filename

title = metadata["title"]


publish_date = metadata.get(
    "date",
    str(date.today())
)


slug = make_slug(title)


output_file = (
    output_dir
    / f"{publish_date}-{slug}.md"
)



# Copy images live

source_images = (
    processed_dir
    / "images"
)


target_images = (
    Path("assets/images")
    / content_type
    / content_name
)


if source_images.exists():

    target_images.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copytree(
        source_images,
        target_images,
        dirs_exist_ok=True
    )



# Build Jekyll front matter

front_matter = "---\n"


front_matter += (
    f"layout: {CONTENT_TYPES[content_type]['layout']}\n"
)



for key, value in metadata.items():

    front_matter += yaml.dump(
        {key: value},
        default_flow_style=False
    )


front_matter += "---\n\n"



# Publish

output_file.write_text(
    front_matter + markdown,
    encoding="utf-8"
)


print("")
print(
    f"Created: {output_file}"
)