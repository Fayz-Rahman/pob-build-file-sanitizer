from __future__ import annotations

from pathlib import Path
import json

from lxml import etree


class PassiveTreeTransformer:

    def __init__(self, tree_json_path: str):
        self.tree_json_path = Path(tree_json_path)

        if not self.tree_json_path.exists():
            raise FileNotFoundError(self.tree_json_path)

        self.lookup = {}

        self._load_tree()

    def _load_tree(self):

        with open(self.tree_json_path, "r", encoding="utf8") as f:
            data = json.load(f)


        for node_id, node in data["nodes"].items():

            self.lookup[int(node_id)] = node

    def enrich(self, xml_tree):

        root = xml_tree.getroot()

        tree_section = root.find("Tree")

        if tree_section is None:
            return xml_tree

        spec = tree_section.find("Spec")

        if spec is None:
            return xml_tree

        allocated = spec.get("nodes", "")

        if not allocated:
            return xml_tree

        allocated_ids = [
            int(x)
            for x in allocated.split(",")
            if x.strip()
        ]

        readable = etree.Element("AllocatedPassiveNodes")

        for node_id in allocated_ids:

            node = self.lookup.get(node_id)

            if node is None:
                continue

            entry = etree.SubElement(readable, "Node")

            entry.set("id", str(node_id))

            #
            # These keys depend on the official json.
            # We'll finalize them once we inspect it.
            #

            if "name" in node:
                entry.set("name", node["name"])

            if "type" in node:
                entry.set("type", node["type"])

        spec.append(readable)

        return xml_tree