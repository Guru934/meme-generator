import random

def load_captions(filepath):
    groups = {}
    current_group = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("[") and line.endswith("]"):
                current_group = line[1:-1]
                groups[current_group] = {"TOP": [], "BOTTOM": []}
                continue

            tag, text = line.split("|", 1)
            groups[current_group][tag].append(text)

    return groups


def get_caption_pair(groups, user_top, user_bottom):
    user_top = user_top.upper() if user_top else ""
    user_bottom = user_bottom.upper() if user_bottom else ""

    # Case 1: both provided
    if user_top and user_bottom:
        return user_top, user_bottom

    matching_groups = []

    for group, captions in groups.items():
        if user_top and user_top in captions["TOP"]:
            matching_groups.append(group)
        elif user_bottom and user_bottom in captions["BOTTOM"]:
            matching_groups.append(group)

    if matching_groups:
        group = random.choice(matching_groups)
    else:
        group = random.choice(list(groups.keys()))

    top = user_top if user_top else random.choice(groups[group]["TOP"])
    bottom = user_bottom if user_bottom else random.choice(groups[group]["BOTTOM"])

    return top, bottom
