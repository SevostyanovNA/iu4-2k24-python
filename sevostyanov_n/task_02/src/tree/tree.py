import os
from colorama import Fore


def print_tree(directory, level=0, max_level=None, symlink_count=0, color_index=0, show_symlinks=False, show_hidden=False):
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"???????? ? ???????: {directory}")
        return

    items.sort()

    for item in items:
        if not show_hidden and item.startswith("."):
            continue

        item_path = os.path.join(directory, item)

        relative_path = os.path.relpath(item_path)

        if os.path.isdir(item_path):
            print(Fore.BLUE + "|   " * level + "+---" + Fore.CYAN + item)
            if max_level is None or level < max_level:
                symlink_count = print_tree(item_path, level + 1, max_level, symlink_count, (color_index + 1) % 6, show_symlinks, show_hidden)
        else:
            print(Fore.BLUE + "|   " * level + "+---" + Fore.GREEN + item)

        if show_symlinks and os.path.islink(item_path):
            symlink_count += 1

    return symlink_count
