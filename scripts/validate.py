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
            or metadata[field] == []
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


def validate_collection_items(items, target_type, field_name):
    """Validate that all items in a collection exist."""
    
    if items is None:
        raise Exception(
            f"Missing required field: {field_name}\n"
            f"  - Add {field_name}: [...] to the metadata"
        )

    if not items:
        raise Exception(
            f"Missing required list:\n"
            f"  - {field_name} must contain at least one item"
        )

    output_dir = CONTENT_TYPES[target_type]["output"]
    missing = []

    for item in items:
        if not item:
            missing.append("<empty entry>")
            continue

        path = Path(output_dir) / f"{item}.md"

        if not path.exists():
            missing.append(str(item))

    if missing:
        raise Exception(
            f"Missing {field_name}:\n"
            + "\n".join(
                f"  - {item}"
                for item in missing
            )
        )


def validate_season_field(metadata, field_name="season"):
    """Validate season field (handles both single value and list)."""
    
    if field_name not in metadata:
        return  # Optional field
    
    value = metadata[field_name]
    
    # Convert to list if single value
    if isinstance(value, str):
        seasons = [value]
    elif isinstance(value, list):
        seasons = value
    else:
        return  # Skip if not string or list
    
    missing_seasons = []
    for season_slug in seasons:
        if not season_slug:
            continue
        season_path = CONTENT_TYPES["seasons"]["output"] / f"{season_slug}.md"
        if not season_path.exists():
            missing_seasons.append(season_slug)
    
    if missing_seasons:
        raise Exception(
            f"Missing {field_name}:\n"
            + "\n".join(f"  - {s}" for s in missing_seasons)
        )
    
    return len(seasons)


def validate_metadata(metadata, content_type):
    if metadata is None:
        raise Exception("Metadata file is empty")

    validate_required_fields(metadata, content_type)
    print("✓ Required metadata")

    if content_type == "posts":
        validate_collection_items(
            metadata.get("authors", []),
            "people",
            "authors"
        )
        print("✓ Authors exist")

        validate_collection_items(
            metadata.get("projects", []),
            "projects",
            "projects"
        )
        print("✓ Projects exist")

        # ─── Validate season (single value) ───
        season_count = validate_season_field(metadata, "season")
        if season_count:
            print(f"✓ Season exists ({season_count} season)")

    elif content_type == "people":
        # Future: validate biography, affiliation
        pass

    elif content_type == "projects":
        validate_collection_items(
            metadata.get("people", []),
            "people",
            "people"
        )
        print("✓ People exist")

        # ─── Validate seasons (list or single) ───
        season_count = validate_season_field(metadata, "seasons")
        if season_count:
            print(f"✓ Seasons exist ({season_count} seasons)")

        if "tags" in metadata:
            print(f"✓ Tags: {len(metadata['tags'])} tags")


# Run from terminal
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 validate.py <content-type> <name>")
        print("")
        print("Examples:")
        print("  python3 validate.py posts hello")
        print("  python3 validate.py people alice-smith")
        print("  python3 validate.py projects climate")
        sys.exit(1)

    content_type = sys.argv[1]
    content_name = sys.argv[2]

    if content_type not in CONTENT_TYPES:
        raise Exception(f"Unknown content type: {content_type}")

    processed_dir = CONTENT_TYPES[content_type]["processed"] / content_name

    metadata_file = processed_dir / "metadata.yml"

    print("")
    print("Checking metadata:")
    print(f"  Path: {metadata_file.resolve()}")
    print(f"  Exists: {metadata_file.exists()}")
    print("")

    if not metadata_file.exists():
        raise FileNotFoundError(f"Metadata file missing: {metadata_file}")

    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = yaml.safe_load(f)

    try:
        validate_metadata(metadata, content_type)
    except Exception as error:
        print("")
        print("✗ Validation failed")
        print("")
        print(error)
        sys.exit(1)

    print("")
    print("✓ Validation passed")
    print("")