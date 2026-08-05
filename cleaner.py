from __future__ import annotations

from dataclasses import dataclass, field
from lxml import etree

from constants import (
    REMOVE_ATTRIBUTES,
    REMOVE_EMPTY_TAGS,
    REMOVE_TAGS,
)


@dataclass
class CleaningReport:
    """
    for keeping track of everything removed during cleaning.
    """

    removed_tags: list[str] = field(default_factory=list)
    removed_attributes: list[str] = field(default_factory=list)


class Cleaner:

    def __init__(self) -> None:
        self.report = CleaningReport()

    def clean(self, tree: etree._ElementTree) -> etree._ElementTree:
        root = tree.getroot()

        self._remove_nodes(root)
        self._remove_attributes(root)

        return tree

    def _remove_nodes(self, parent: etree._Element) -> None:

        for child in list(parent):

            if child.tag in REMOVE_TAGS:
                parent.remove(child)
                self.report.removed_tags.append(child.tag)
                continue

            if child.tag in REMOVE_EMPTY_TAGS:
                if (
                    len(child) == 0
                    and not child.attrib
                    and (child.text is None or child.text.strip() == "")
                ):
                    parent.remove(child)
                    self.report.removed_tags.append(child.tag)
                    continue

            self._remove_nodes(child)

    def _remove_attributes(self, node: etree._Element) -> None:

        for attribute in list(node.attrib):

            if attribute in REMOVE_ATTRIBUTES:
                del node.attrib[attribute]
                self.report.removed_attributes.append(attribute)

        for child in node:
            self._remove_attributes(child)