from pathlib import Path
from lxml import etree


class BuildReader:
    """
    validates xml file.
    """

    def __init__(self, filename: str):
        self.path = Path(filename)

        if not self.path.exists():
            raise FileNotFoundError(self.path)

    def read(self) -> etree._ElementTree:
        parser = etree.XMLParser(
            remove_blank_text=False,
            remove_comments=False,
        )

        return etree.parse(str(self.path), parser)