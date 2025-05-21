# Convert file system into ASCII tree (like `tree` command)
import os

def build_tree(path, prefix=""):
    if not os.path.exists(path):
        print(f"❌ Error: Path '{path}' does not exist.")
        return

    if not os.path.isdir(path):
        print(f"❌ Error: Path '{path}' is not a directory.")
        return

    try:
        files = os.listdir(path)
    except PermissionError:
        print(f"🔒 Permission denied: Cannot access '{path}'")
        return

    for i, file_name in enumerate(sorted(files)):
        full_path = os.path.join(path, file_name)
        is_last = (i == len(files) - 1)
        connector = "└── " if is_last else "├── "
        print(prefix + connector + file_name)

        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            build_tree(full_path, new_prefix)

