

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

#############################################
#Create a required list
required = [
    "title",
    "author",
    "project",
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



# Convert author name to slug
author_slug = make_slug(
    metadata["author"]
)

#print(f"author_slug: {author_slug}")

# Check person exists
author_file = (
    people_dir
    / f"{author_slug}.md"
)


if not author_file.exists():

    raise Exception(
        f"Missing author: {author_file}"
    )

#Convert project name to slug
project_slug = make_slug(
    metadata["project"]
)

#print(f"project_slug: {project_slug}")

#Check project exists
project_file = (
    projects_dir
    / f"{project_slug}.md"
)


if not project_file.exists():

    raise Exception(
        f"Missing project: {project_file}"
    )


print("✓ Relationships validated")

#output directory
posts_dir = Path("_posts")

# Convert title to slug
post_slug = make_slug(
    metadata["title"]
)

#Create filename
output_file = (
    posts_dir
    / f"{metadata['date']}-{post_slug}.md"
)

print(f"\noutput_file: {output_file}")


#Build front matter
front_matter = "---\n"

front_matter += (
    "layout: post\n"
)

front_matter += (
    f"title: {metadata['title']}\n"
)

front_matter += (
    f"author: {author_slug}\n"
)

front_matter += (
    f"project: {project_slug}\n"
)

front_matter += (
    f"date: {metadata['date']}\n"
)

front_matter += "---\n\n"

#Build Body
body = "\n\n".join(body_lines)

#Combine
markdown = (
    front_matter
    + body
)

#Prevent overwriting
if output_file.exists():

    raise Exception(
        f"Already exists: {output_file}"
    )

#Write the post
output_file.write_text(
    markdown,
    encoding="utf-8"
)

print(
    f"Created: {output_file}"
)