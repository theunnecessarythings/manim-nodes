# Manim Node Editor for Blender

A custom node editor for Blender to create mathematical animations with Manim.

## Overview

This project creates a custom node editor interface within Blender 4.4.1 that allows users to create Manim animations using a visual node-based workflow. It leverages Blender's Python API to create a custom node system that can be used to design mathematical animations.

## Features

- Custom node editor interface in Blender
- Basic nodes for common Manim objects (Text, Circle)
- Animation nodes (FadeIn)
- Scene configuration

## Installation

1. Clone or download this repository
2. Install as a Blender addon:
   - Open Blender 4.4.1
   - Go to Edit > Preferences > Add-ons
   - Click "Install..." and select the `manim_node_editor` folder or zip
   - Enable the addon by checking the box

## Testing the Addon

1. After installing and enabling the addon, you can run the test script:
   - Open Blender's Text Editor
   - Open the `manim_node_editor/test.py` file
   - Run the script (Alt+P)
   - This will create a sample node setup and change one of your 3D views to a Node Editor with the Manim node tree

## Usage

1. Change an editor area to Node Editor (Editor Type dropdown in the header)
2. Set the editor type to "Manim Node Editor" in the header dropdown
3. Create a new node tree using the "New" button
4. Add nodes from the Add menu (Shift+A)
5. Start by creating a Scene node, then add objects and animations

## Development 

This is a development version. Features will be added incrementally.

### Current Nodes

- Scene Node: Represents a Manim scene and its properties
- Text Node: Creates Manim text objects
- Circle Node: Creates Manim circle objects
- FadeIn Animation: Applies fade-in animation to objects

### Future Plans

- Export to Manim Python code
- Live preview of animations
- More node types for mathematical objects
- Integration with Manim's rendering pipeline

## Requirements

- Blender 4.4.1 or newer
- For actual rendering: Manim library installed in your Python environment

## License

MIT 