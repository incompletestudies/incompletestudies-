#ingest_post.py
# ✓ DOCX reading
# ✓ metadata extraction
# ✓ slug conversion
# ✓ relationship validation (with skip option)
# ✓ pandoc conversion
# ✓ image extraction
# ✓ image path conversion
# ✓ processed output

#Imports
import sys
import yaml
import subprocess
import warnings

from docx import Document
from pathlib import Path

from config import CONTENT_TYPES
from lib.slug import make_slug
from lib.images import convert_image_paths
from lib.relations import relationship_to_slugs


# Command Line
if len(sys.argv) < 3:
    print(
        "Usage: python3 ingest.py <content-type> <name> [--skip-relations]"
    )
    sys.exit(1)


content_type = sys.argv[1]
content_name = sys.argv[2]

# Check for skip flag
skip_relations = "--skip-relations" in sys.argv

# Store the filename
docx_file = (
    CONTENT_TYPES[content_type]["incoming"]
    / f"{content_name}.docx"
)

#############################################
# Check the file exists
if not docx_file.exists():
    raise FileNotFoundError(
        f"File not found: {docx_file}"
    )

# Check the extension
if docx_file.suffix.lower() != ".docx":
    raise Exception(
        "Expected a .docx file"
    )

# Print what is being processed
print("\nReading DOCX:")
print(docx_file.resolve())

document = Document(docx_file)

# Create an empty list
paragraphs = []

# One paragraph at the time getting printed
for paragraph in document.paragraphs:
    text = paragraph.text.strip()
    if not text:
        continue
    paragraphs.append(text)

#############################################
# Two new lists
metadata_lines = []
body_lines = []

# Create a flag
in_body = False

# Loop through the paragraphs
for line in paragraphs:
    if line.strip().startswith("-----"):
        in_body = True
        continue

    if in_body:
        body_lines.append(line)
    else:
        metadata_lines.append(line)

#############################################
# Create the Dictionary
metadata = {}

# Metadata extraction loop
for line in metadata_lines:
    # Split at the first colon
    key, value = line.split(":", 1)
    # Clean both values
    key = key.strip().lower()
    value = value.strip()
    # Store It
    metadata[key] = value

# Convert relationship fields to slugs
if "authors" in metadata:
    metadata["authors"] = [
        make_slug(item)
        for item in metadata["authors"].split(";")
    ]

if "projects" in metadata:
    metadata["projects"] = [
        make_slug(item)
        for item in metadata["projects"].split(";")
    ]

if "seasons" in metadata:
    metadata["seasons"] = [
        item.strip().upper()
        for item in metadata["seasons"].split(";")
    ]

if "tags" in metadata:
    metadata["tags"] = [
        make_slug(item)
        for item in metadata["tags"].split(";")
    ]

#############################################
# Create a required list
required = (
    CONTENT_TYPES[content_type]["required_columns"]
)

# Metadata Validation
for field in required:
    # Check if Metadata exists
    if field not in metadata:
        raise Exception(
            f"Missing metadata: {field}"
        )
    # Check if Metadata isn't empty
    if not metadata[field]:
        raise Exception(
            f"Empty metadata: {field}"
        )

# Print Success
print("\n✓ Metadata validation passed")

#############################################
# Normalize and validate relationships

relationships = (
    CONTENT_TYPES[content_type]
    .get("relationships", {})
)

missing_relations = []

for field, target_type in relationships.items():
    if field not in metadata:
        continue

    items = metadata[field]

    if isinstance(items, str):
        items = [
            item.strip()
            for item in items.split(";")
        ]

    slugs = [
        make_slug(item)
        for item in items
    ]

    output_dir = (
        CONTENT_TYPES[target_type]["output"]
    )

    validated_slugs = []

    for slug in slugs:
        target_file = (
            output_dir
            / f"{slug}.md"
        )

        if not target_file.exists():
            missing_relations.append({
                "type": target_type,
                "slug": slug,
                "file": target_file
            })
            if skip_relations:
                warnings.warn(
                    f"⚠️ Missing {target_type}: {slug} (skipped)"
                )
                continue
            else:
                raise Exception(
                    f"Missing {target_type}: {target_file}\n"
                    f"Run with --skip-relations to continue anyway."
                )

        validated_slugs.append(slug)

    metadata[field] = validated_slugs

if skip_relations and missing_relations:
    print(f"\n⚠️ Skipped {len(missing_relations)} missing relationships:")
    for missing in missing_relations:
        print(f"   - {missing['type']}: {missing['slug']}")
    print("\n   (These can be created later)")

print("✓ Relationships validated\n")

#############################################
# Create processed directory

identifier = CONTENT_TYPES[content_type]["identifier"]

slug = make_slug(
    metadata[identifier]
)

processed_dir = (
    CONTENT_TYPES[content_type]["processed"]
    / slug
)

processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

# Save metadata
metadata_file = (
    processed_dir
    / "metadata.yml"
)

metadata_file.write_text(
    yaml.dump(
        metadata,
        sort_keys=False
    ),
    encoding="utf-8"
)

# Image folder
image_dir = (
    processed_dir
    / "images"
)

image_dir.mkdir(
    parents=True,
    exist_ok=True
)

# Convert DOCX body with Pandoc
content_file = (
    processed_dir
    / "content.md"
)

subprocess.run(
    [
        "pandoc",
        str(docx_file),
        "-t",
        "gfm",
        "--wrap=none",
        "--extract-media",
        str(image_dir),
        "--reference-links",
        "--markdown-headings=atx",
        "-o",
        str(content_file)
    ],
    check=True
)

# Read markdown
markdown = content_file.read_text(
    encoding="utf-8"
)

# Remove metadata section
if "-----" in markdown:
    markdown = markdown.split(
        "-----",
        1
    )[1].strip()

# Move images out of Pandoc media folder
media_dir = image_dir / "media"

if media_dir.exists():
    for img in media_dir.iterdir():
        if img.is_file():
            img.rename(
                image_dir / img.name
            )
    media_dir.rmdir()

# Fix image paths
image_base = (
    CONTENT_TYPES[content_type]["image_root"]
    + "/"
    + slug
)

markdown = convert_image_paths(
    markdown,
    image_base
)

# Save final content
content_file.write_text(
    markdown,
    encoding="utf-8"
)

#############################################
# Print final summary
print(f"\n✅ Created processed post: {processed_dir}")

if missing_relations:
    print("\n📝 Remember to create these missing files:")
    for missing in missing_relations:
        print(f"   - _{missing['type']}/{missing['slug']}.md")