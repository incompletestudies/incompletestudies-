from lib.slug import make_slug


def convert_relationship(value):

    if not value:
        return []

    items = [
        item.strip()
        for item in value.split(";")
    ]

    return [
        make_slug(item)
        for item in items
    ]