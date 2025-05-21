# Command-line interface logic
import argparse
from treevisualizer import tree_builder, tree_writer

def main_cli():
    parser = argparse.ArgumentParser(description="File Tree ↔ Visual Tree Tool")
    parser.add_argument("--show", help="Show visual tree from folder path", type=str)
    parser.add_argument("--build", help="Build file tree from text file (ASCII or JSON)", type=str)

    args = parser.parse_args()

    if args.show:
        print("\n📂 Visualizing folder tree:\n")
        tree_builder.build_tree(args.show)
    
    elif args.build:
        print("\n📁 Creating folders from tree structure file...\n")
        tree_writer.create_from_ascii(args.build)

    else:
        parser.print_help()
