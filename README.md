# 🗂️ FileTree Visualizer

A Python tool that converts folder structures into visual trees — and can build folder structures from ASCII tree definitions.

---

## 🚀 Installation (for CLI usage)

1. Clone the repo:
git clone https://github.com/yourusername/filetree-visualizer.git
cd filetree-visualizer

2. Install the CLI globally
pip install -e


## Features
- 📁 Convert real folders into tree diagrams
- 🧾 Build folders/files from tree structure text
- ⚙️ CLI-based and extensible for GUI/Web

## Usage
# Show tree from real folder
python main.py --show path/to/folder

# Build folder from ASCII tree
python main.py --build examples/sample_tree.txt
