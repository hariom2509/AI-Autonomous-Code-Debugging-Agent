import re


import re


def extract_patch(patch_text):

    if not patch_text:
        return []

    patch_lines = []

    # Case 1: diff format
    for line in patch_text.split("\n"):
        line = line.strip()
        if line.startswith("+") or line.startswith("-"):
            patch_lines.append(line)

    if patch_lines:
        return patch_lines

    # Case 2: Replace instruction format
    match = re.search(
        r"Replace\s+`(.+?)`\s+with\s+`(.+?)`",
        patch_text
    )

    if match:
        old_line = match.group(1)
        new_line = match.group(2)

        return [
            f"- {old_line}",
            f"+ {new_line}"
        ]

    return []

def apply_patch(file_path, patch_lines):

    with open(file_path, "r") as f:
        lines = f.readlines()

    updated_lines = []

    old_line = None
    new_line = None

    for p in patch_lines:
        if p.startswith("-"):
            old_line = p[1:].strip()
        if p.startswith("+"):
            new_line = p[1:].strip()

    for line in lines:

        # compare ignoring indentation
        if old_line and old_line in line.strip():

            indent = line[:len(line) - len(line.lstrip())]

            updated_lines.append(indent + new_line + "\n")

        else:
            updated_lines.append(line)

    with open(file_path, "w") as f:
        f.writelines(updated_lines)