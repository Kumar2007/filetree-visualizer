# Create folder structure from ASCII-art text
import os

def create_from_ascii(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: Tree structure file '{file_path}' not found.")
        return

    if not os.path.isfile(file_path):
        print(f"❌ Error: '{file_path}' is not a file.")
        return

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    current_path = []
    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            continue

        level = stripped.count("│") + stripped.count("    ")
        name = stripped.split("──")[-1].strip()

        current_path = current_path[:level]
        current_path.append(name)

        full_path = os.path.join(*current_path)

        try:
            if "." in name:
                open(full_path, 'a').close()
            else:
                os.makedirs(full_path, exist_ok=True)
        except Exception as e:
            print(f"❌ Failed to create '{full_path}': {e}")
