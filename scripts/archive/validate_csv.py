
#Imports
import csv
import sys

from pathlib import Path
from config import CONTENT_TYPES
from lib.slug import make_slug


# a helper function
def validate_relationships(row, relationships):

    identifier = CONTENT_TYPES[content_type]["identifier"]

    source_name = row[identifier]

    for field, target_type in relationships.items():

        value = row.get(field)

        if not value:
            continue

        items = [
            item.strip()
            for item in value.split(";")
        ]

        output_dir = (
            CONTENT_TYPES[target_type]["output"]
        )

        missing = []
        existing = []

        for item in items:

            slug = make_slug(item)

            target_file = (
                output_dir
                / f"{slug}.md"
            )

            if target_file.exists():
                existing.append(
                    f"{slug} ({target_file})"
                )

            else:
                missing.append(
                    f"{slug} ({target_file})"
                )

        # REPORT AFTER ALL ITEMS ARE CHECKED
        message = f"""
    Relationship check

    Source:
    {source_name}

    Field:
    {field}

    Existing {target_type}:
    """

        message += (
            "\n".join(existing)
            if existing
            else "None"
        )

        message += f"""

    Missing {target_type}:
    """

        message += (
            "\n".join(missing)
            if missing
            else "None"
        )

        if missing:

            raise Exception(message)

        else:

            print(message)






#command arguments
if len(sys.argv) < 2:
    print(
        "Usage: python3 validate_csv.py <content-type>"
    )
    sys.exit(1)


content_type = sys.argv[1]

#Check content type exists
if content_type not in CONTENT_TYPES:
    raise Exception(
        f"Unknown content type: {content_type}"
    )

#Locate the CSV
csv_file = (
    Path("metadata")
    / f"{content_type}.csv"
)
#Check the CSV exists
if not csv_file.exists():

    raise FileNotFoundError(
        f"CSV missing: {csv_file}"
    )

print("Checking CSV:")
print(csv_file.resolve())

#Open the CSV
with open(
    csv_file,
    newline="",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    relationship_fields = (
        CONTENT_TYPES[content_type]
        .get("relationships", {})
    )

#Check required columns
    required = CONTENT_TYPES[content_type]["required_columns"]

    for column in required:

        if column not in reader.fieldnames:

            raise Exception(
                f"Missing CSV column: {column}"
            )


# Check Relationships
    for row in reader:

        validate_relationships(
            row,
            relationship_fields
        )


print("✓ CSV validation passed")