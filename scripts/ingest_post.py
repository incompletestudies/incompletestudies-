

#Imports
import sys

from docx import Document
from pathlib import Path

from lib.slug import make_slug


# Command Line
if len(sys.argv) < 2:

    print(
        "Usage: python3 scripts/ingest_post.py <docx-file>"
    )

    sys.exit(1)

#store the filename
docx_file = Path(sys.argv[1])

#############################################
# Check the file exists
if not docx_file.exists():

    raise FileNotFoundError(
        f"File not found: {docx_file}"
    )

#Check the extension
if docx_file.suffix.lower() != ".docx":

    raise Exception(
        "Expected a .docx file"
    )

#Print what is being processed
print("Reading DOCX:")
print(docx_file.resolve())

document = Document(docx_file)

# print(
#     f"\nParagraphs: {len(document.paragraphs)}\n"
# )

#Create an empty list
paragraphs = []

#One paragraph at the time getting printed
for paragraph in document.paragraphs:

    text = paragraph.text.strip()

    if not text:
        continue

    paragraphs.append(text)

#print(paragraphs, "\n")


#############################################
#Two new lists
metadata_lines = []
body_lines = []

#Create a flag
in_body = False

#Loop through the paragraphs
for line in paragraphs:
    if line.startswith("-----"):

        in_body = True

        continue

    if in_body:

        body_lines.append(line)

    else:

        metadata_lines.append(line)


# print("\nMETADATA\n")

# for line in metadata_lines:

#     print(line)


# print("\nBODY\n")

# for line in body_lines:

#     print(line)


#############################################
#create the Dictionary
metadata = {}

#metadata extraction loop
for line in metadata_lines:

    #Split at the first colon
    key, value = line.split(":", 1)

    #Clean both values
    key = key.strip().lower()
    value = value.strip()

    #Store It
    metadata[key] = value

# print("\nMETADATA DICTIONARY\n")

# for key, value in metadata.items():

#     print(f"{key}: {value}")

# # Convert relationship fields to slugs

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



#############################################
#Create a required list
required = [
    "title",
    "authors",
    "projects",
    "date"
]
# Define where people/projects live
people_dir = Path("_people")

projects_dir = Path("_projects")


#Metadata Validation
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

# Print Sucess
print("\n✓ Metadata validation passed\n")


#############################################
# Normalize relationships

authors = [
    make_slug(item)
    for item in metadata["authors"]
]


projects = [
    make_slug(item)
    for item in metadata["projects"]
]


# Validate people

for author in authors:

    author_file = (
        people_dir
        / f"{author}.md"
    )

    if not author_file.exists():

        raise Exception(
            f"Missing author: {author_file}"
        )


# Validate projects

for project in projects:

    project_file = (
        projects_dir
        / f"{project}.md"
    )

    if not project_file.exists():

        raise Exception(
            f"Missing project: {project_file}"
        )


# Store normalized values

metadata["authors"] = authors
metadata["projects"] = projects


print("✓ Relationships validated")



#############################################
# Create processed directory

post_slug = make_slug(
    metadata["title"]
)

processed_dir = (
    Path("drafts/processed/posts")
    / post_slug
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


import yaml

metadata_file.write_text(
    yaml.dump(
        metadata,
        sort_keys=False
    ),
    encoding="utf-8"
)


# Save body

content_file = (
    processed_dir
    / "content.md"
)

body = "\n\n".join(body_lines)

content_file.write_text(
    body,
    encoding="utf-8"
)


print(
    f"Created processed post: {processed_dir}"
)