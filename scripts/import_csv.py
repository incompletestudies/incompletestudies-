
## import_csv.py = create files


#Imports
import sys
import csv
import yaml

from pathlib import Path
from config import CONTENT_TYPES
from lib.slug import make_slug
from lib.relations import convert_relationship


#Input Arguments

if len(sys.argv) < 2:
    print("Usage: python3 import_csv.py <content-type>")
    sys.exit(1)

content_type = sys.argv[1]

#Check if in Content Types
if content_type not in CONTENT_TYPES:
    raise Exception(
        f"Unknown content type: {content_type}"
    )


#Locate the CSV.
csv_file = Path("metadata") / f"{content_type}.csv"

# output directory
output_dir = CONTENT_TYPES[content_type]["output"]

# Main identifier field
identifier = CONTENT_TYPES[content_type]["identifier"]

# Body identifier field
body_field = CONTENT_TYPES[content_type]["body_field"]

#List fields
list_fields = CONTENT_TYPES[content_type]["list_fields"]



#Helper
def convert_value(value):

    if value == "TRUE":
        return True

    if value == "FALSE":
        return False

    return value




#Read it:
with open(csv_file, newline="", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    #In case, small protection 
    if None in reader.fieldnames:

        raise Exception(
            "CSV contains an unnamed column. Check for an extra comma at the end of a row."
        )

    # Check required CSV columns exist
    required = CONTENT_TYPES[content_type]["required_columns"]

    for column in required:

        if column not in reader.fieldnames:

            raise Exception(
                f"Missing CSV column: {column}"
            )


    # Now process rows
    for row in reader:


        print(
            f"ROW: {row[identifier]}\n"
        )

        #Generate the slug
        slug = make_slug(
            row[identifier]
        )

    
        #Output file
        output_file = (
            Path(output_dir)
            / f"{slug}.md"
        )

        # Built Metadata
        metadata = {}

        metadata["layout"] = (
            CONTENT_TYPES[content_type]["layout"]
        )


        # Build Jekyll front matter

        for key, value in row.items():

            # Skip empty fields
            if not value:
                continue

            # Body becomes content
            if key == body_field:
                continue

            # Handle Projects as a YAML list
            yaml_key = (
                key
                .lower()
                .replace(" ", "_")
            )

            if key in list_fields:

                metadata[yaml_key] = (
                    convert_relationship(value)
                )

            else:

                metadata[yaml_key] = convert_value(value)

        #Front Matter
        front_matter = "---\n"

        front_matter += yaml.dump(
            metadata,
            sort_keys=False,
            allow_unicode=True
        )

        front_matter += "---\n\n"

        #body_field gets placed in Body
        body = row.get(body_field, "")

        # Combine front matter + body
        markdown = (
            front_matter
            + body
        )


        # Prevent overwriting existing files

        if output_file.exists():

            raise Exception(
                f"Already exists: {output_file}"
            )


        # Write Markdown file
        output_file.write_text(
            markdown,
            encoding="utf-8"
        )

        print(
        f"Created: {output_file}"
        )

