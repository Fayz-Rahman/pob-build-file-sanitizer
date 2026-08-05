from pathlib import Path

from lxml import etree

from constants import (
    ENCODING,
    XML_DECLARATION,
)


class Writer:

    @staticmethod
    def write(tree: etree._ElementTree, output: str) -> None:

        tree.write(
            output,
            pretty_print=True,
            encoding=ENCODING,
            xml_declaration=XML_DECLARATION,
        )