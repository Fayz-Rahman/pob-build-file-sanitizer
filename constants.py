"""
Project wide constants.
"""

OUTPUT_SUFFIX = ".ai.xml"

# whole XML elements to remove.
REMOVE_TAGS = {
    "TreeView",
    "Party",
    "Calcs"
}

REMOVE_EMPTY_TAGS = {
    "Notes",
}

# attributes related to pob editor/ui.
REMOVE_ATTRIBUTES = {
    "collapsed",
    "zoomLevel",
    "scrollX",
    "scrollY",
}

XML_DECLARATION = True
ENCODING = "utf-8"