import sys
from pathlib import Path

from reader import BuildReader


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py build.xml")
        return

    filename = sys.argv[1]

    reader = BuildReader(filename)

    tree = reader.read()

    root = tree.getroot()

    print("=" * 50)
    print("PoB Build Loaded Successfully")
    print("=" * 50)
    print()

    print(f"Root Tag : {root.tag}")
    print(f"Children : {len(root)}")
    print(f"Source   : {Path(filename).resolve()}")

    print()

    print("Top Level Sections")

    for child in root:
        print("  -", child.tag)


if __name__ == "__main__":
    main()