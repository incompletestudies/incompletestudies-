#slug.py         → Text → slug
# Create URL-friendly names

import re


def make_slug(text):

    text = text.lower()

    # remove punctuation
    text = re.sub(
        r"[^a-z0-9\s-]",
        "",
        text
    )

    # replace spaces with -
    text = re.sub(
        r"\s+",
        "-",
        text
    )

    # remove duplicate -
    text = re.sub(
        r"-+",
        "-",
        text
    )

    return text.strip("-")