#relations.py    → Content relationships

#Imports
from lib.slug import make_slug

#Function

# Take human relationship input → return internal slugs
def relationship_to_slugs(value):

    if not value:
        return []


    # Already a list
    if isinstance(value, list):

        return [
            make_slug(item)
            for item in value
        ]


    # String input
    items = [
        item.strip()
        for item in value.split(";")
    ]


    return [
        make_slug(item)
        for item in items
    ]