bl_info = {
    "name": "Manim Node Editor",
    "author": "User",
    "version": (0, 1),
    "blender": (4, 4, 1),
    "location": "Editors > Manim",
    "description": "Node editor for creating Manim animations",
    "warning": "Development version",
    "wiki_url": "",
    "category": "Node",
}

import bpy
import sys
import os
from pathlib import Path

# Development mode variables
is_development_version = True
directory = Path(__file__).parent

# Only needed for development mode
if is_development_version:
    # Check if this file is in the Blender addons directory
    if str(directory).endswith("addons/manim_node_editor"):
        # Running from the addons directory - try to find the development directory
        dev_dir = Path(os.path.expanduser("~/Documents/mui/manim_node_editor"))
        if dev_dir.exists():
            directory = dev_dir
            
        # Add the development directory to sys.path if not already there
        if str(directory) not in sys.path:
            sys.path.append(str(directory))

def import_modules():
    from . import node_tree
    from . import nodes
    return node_tree, nodes

node_tree, nodes = import_modules()

def register():
    # Using imported modules
    node_tree.register()
    nodes.register()
    
def unregister():
    # Using imported modules
    nodes.unregister()
    node_tree.unregister()

if __name__ == "__main__":
    register() 