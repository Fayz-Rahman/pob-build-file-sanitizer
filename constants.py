"""
project wide constants
"""

OUTPUT_SUFFIX = ".ai.xml"

# xml tags that only exist to preserve pob editor/ui state
REMOVE_TAGS = {
    "TreeView",
    "UndoRedo",
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