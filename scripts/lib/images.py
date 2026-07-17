from pathlib import Path


def convert_image_paths(text, image_base):

    replacements = []

    for line in text.splitlines():

        # HTML images
        if '<img src="' in line:

            start = line.find('src="') + 5
            end = line.find('"', start)

            old_path = line[start:end]
            filename = Path(old_path).name

            new_path = (
                "{{ '"
                + image_base
                + "/"
                + filename
                + "' | relative_url }}"
            )

            line = (
                line[:start]
                + new_path
                + line[end:]
            )

        # Markdown images
        elif "](" in line:

            start = line.find("](") + 2
            end = line.find(")", start)

            old_path = line[start:end]

            if old_path:
                filename = Path(old_path).name

                new_path = (
                    "{{ '"
                    + image_base
                    + "/"
                    + filename
                    + "' | relative_url }}"
                )

                line = (
                    line[:start]
                    + new_path
                    + line[end:]
                )

        replacements.append(line)

    return "\n".join(replacements)