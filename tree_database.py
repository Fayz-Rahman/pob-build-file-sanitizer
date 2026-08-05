from __future__ import annotations

from pathlib import Path
from typing import Any

from lupa import LuaRuntime


class TreeDatabase:

    def __init__(self, lua_file: str):

        self.path = Path(lua_file)

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        self.lua = LuaRuntime(unpack_returned_tuples=True)

        self.data = self._load()

        self.nodes = self.data["nodes"]
        self.classes = self.data["classes"]

    def _load(self):

        with open(self.path, "r", encoding="utf8") as f:
            return self.lua.execute(f.read())

    def node_count(self):

        return sum(1 for _ in self.iter_nodes())

    def iter_nodes(self):

        for key in self.nodes.keys():

            if isinstance(key, int):
                yield key, self.get_node(key)

    def has_node(self, node_id: int):

        return self.nodes[node_id] is not None

    def get_node(self, node_id: int) -> dict | None:

        lua_node = self.nodes[node_id]

        if lua_node is None:
            return None

        return self._convert_node(node_id, lua_node)

    def _convert_node(self, node_id: int, lua_node) -> dict:

        node = {
            "id": node_id
        }

        for key in lua_node.keys():

            value = lua_node[key]

            node[key] = self._convert(value)

        return node

    def _convert(self, value: Any):

        # Primitive Python values

        if value is None:
            return None

        if isinstance(value, (str, int, float, bool)):
            return value

        # Lua table

        if hasattr(value, "keys"):

            keys = list(value.keys())

            # Array

            if keys and all(isinstance(k, int) for k in keys):

                return [
                    self._convert(value[k])
                    for k in sorted(keys)
                ]

            # Dictionary

            result = {}

            for k in keys:
                result[k] = self._convert(value[k])

            return result

        return value