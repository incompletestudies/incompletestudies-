# validate.py = check files are correct


# Imports
import yaml
import sys

from pathlib import Path
from config import CONTENT_TYPES



def validate_required_fields(metadata, content_type):

    required_fields = (
        CONTENT_TYPES[content_type]["required_columns"]
    )

    missing = []

    for field in required_fields:

        if (
            field not in metadata
            or metadata[field] is None
            or metadata[field] == ""
        ):

            missing.append(field)


    if missing:

        raise Exception(
            "Missing required metadata:\n"
            + "\n".join(
                f"  - {item}"
                for item in missing
            )
        )



def validate_collection_items(items, content_type, field_name):

    missing = []

    output_dir = CONTENT_TYPES[content_type]["output"]


    if not items:

        raise Exception(
            f"Missing required list:\n"
            f"  - {field_name} must contain at least one item"
        )


    for item in items:

        if not item:

            missing.append("<empty entry>")

            continue


        path = (
            Path(output_dir)
            / f"{item}.md"
        )


        if not path.exists():

            missing.append(
                str(item)
            )


    if missing:

        raise Exception(
            f"Missing {field_name}:\n"
            + "\n".join(
                f"  - {item}"
                for item in missing
            )
        )



def validate_metadata(metadata, content_type):


    if metadata is None:

        raise Exception(
            "Metadata file is empty"
        )


    validate_required_fields(
        metadata,
        content_type
    )


    if content_type == "posts":


        validate_collection_items(
            metadata.get("authors", []),
            "people",
            "authors"
        )


        validate_collection_items(
            metadata.get("projects", []),
            "projects",
            "projects"
        )



    elif content_type == "people":

        # Future:
        # validate biography
        # validate affiliation
        pass



    elif content_type == "projects":

        # Future:
        # validate description
        # validate status
        pass



# Run from terminal

if __name__ == "__main__":


    if len(sys.argv) < 3:

        print(
            "Usage:"
        )

        print(
            "  python3 validate.py <content-type> <name>"
        )

        print(
            ""
        )

        print(
            "Examples:"
        )

        print(
            "  python3 validate.py posts hello"
        )

        print(
            "  python3 validate.py people alice-smith"
        )

        print(
            "  python3 validate.py projects climate"
        )

        sys.exit(1)



    content_type = sys.argv[1]
    content_name = sys.argv[2]



    if content_type not in CONTENT_TYPES:

        raise Exception(
            f"Unknown content type: {content_type}"
        )



    incoming_dir = (
        CONTENT_TYPES[content_type]["incoming"]
    )


    metadata_file = (
        incoming_dir
        / f"{content_name}.yml"
    )



    print("Checking metadata:")
    print(f"  Path: {metadata_file.resolve()}")
    print(f"  Exists: {metadata_file.exists()}")


    if not metadata_file.exists():

        raise FileNotFoundError(
            f"Metadata file missing: {metadata_file}"
        )



    with open(
        metadata_file,
        "r",
        encoding="utf-8"
    ) as f:

        metadata = yaml.safe_load(f)



    try:

        validate_metadata(
            metadata,
            content_type
        )


    except Exception as error:

        print("")
        print("✗ Validation failed")
        print("")
        print(error)

        sys.exit(1)



    print("")
    print("✓ Validation passed")