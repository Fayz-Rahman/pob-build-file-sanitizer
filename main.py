import sys
from pathlib import Path

from reader import BuildReader
from cleaner import Cleaner
from writer import Writer


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py build.xml")
        return

    filename = sys.argv[1]

    reader = BuildReader(filename)

    tree = reader.read()

    cleaner = Cleaner()

    tree = cleaner.clean(tree)

    Writer.write(tree, "cleaned.xml")

    print()
    print("Cleaning complete.")
    print()

    print("Removed tags:")

    for tag in cleaner.report.removed_tags:
        print("  -", tag)

    print()

    print("Removed attributes:")

    for attr in sorted(set(cleaner.report.removed_attributes)):
        print("  -", attr)

    print()
    print("Output written to cleaned.xml")

    print()    

    # root = tree.getroot()

    # print("=" * 50)
    # print("PoB Build Loaded Successfully")
    # print("=" * 50)
    # print()

    # print(f"Root Tag : {root.tag}")
    # print(f"Children : {len(root)}")
    # print(f"Source   : {Path(filename).resolve()}")

    # print()

    # print("Top Level Sections")

    # for child in root:
    #     print("  -", child.tag)


if __name__ == "__main__":
    main()