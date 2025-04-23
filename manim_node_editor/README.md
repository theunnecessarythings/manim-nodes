# Manim Node Editor for Blender

A custom node editor for creating Manim animations in Blender.

## Features

- Custom node editor interface in Blender
- Basic nodes for common Manim objects (Text, Circle)
- Animation nodes (FadeIn)
- Scene configuration

## Installation

1. Download the `manim_node_editor` folder
2. In Blender, go to Edit > Preferences > Add-ons
3. Click "Install..." and select the folder or zip file
4. Enable the addon by checking the box

## Usage

1. Open a new Blender file
2. Change one of your editor windows to the "Manim Node Editor" (Editor Type dropdown in the header)
3. Create a new Manim node tree by clicking "New" in the header
4. Add nodes from the Add menu (Shift+A)
5. Start by adding a Scene node, then connect other nodes to it

## Development

This addon is in early development. Features and node types will be added over time.

## Requirements

- Blender 4.4.1 or newer
- For rendering: Manim library installed in your Python environment

## Future Plans

- Export to Manim Python code
- Live preview of animations
- More node types for mathematical objects
- Integration with Manim's rendering pipeline 