import bpy

def create_test_manim_setup():
    """Creates a test setup with the Manim node editor"""
    
    # Create a new Manim node tree
    node_tree = bpy.data.node_groups.new(name="Manim Test", type="ManimNodeTree")
    
    # Create a scene node
    scene_node = node_tree.nodes.new(type="ManimSceneNodeType")
    scene_node.location = (0, 0)
    scene_node.scene_name = "TestScene"
    
    # Create a text node
    text_node = node_tree.nodes.new(type="ManimTextNodeType")
    text_node.location = (250, 100)
    text_node.text = "Hello, Manim!"
    
    # Create a circle node
    circle_node = node_tree.nodes.new(type="ManimCircleNodeType")
    circle_node.location = (250, -100)
    circle_node.radius = 2.0
    
    # Create fade in nodes for both objects
    fade_in_text = node_tree.nodes.new(type="ManimFadeInNodeType")
    fade_in_text.location = (500, 100)
    
    fade_in_circle = node_tree.nodes.new(type="ManimFadeInNodeType")
    fade_in_circle.location = (500, -100)
    
    # Link the nodes
    node_tree.links.new(scene_node.outputs[0], text_node.inputs[0])
    node_tree.links.new(scene_node.outputs[0], circle_node.inputs[0])
    node_tree.links.new(text_node.outputs[0], fade_in_text.inputs[0])
    node_tree.links.new(circle_node.outputs[0], fade_in_circle.inputs[0])
    
    return node_tree

def setup_node_editor_area():
    """Sets up the node editor area for Manim"""
    # Find an existing area to change, or split to create a new one
    area = None
    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':  # Replace 3D view
            area = a
            break
    
    if area:
        area.type = 'NODE_EDITOR'
        space = area.spaces[0]
        space.tree_type = 'ManimNodeTree'
        
        # If we created a node tree, set it as active
        if bpy.data.node_groups.get("Manim Test"):
            space.node_tree = bpy.data.node_groups["Manim Test"]

def print_menu_categories():
    """Print all available menu categories to verify structure"""
    try:
        from . import node_tree
        
        # Define category descriptions - now separate from the node categories
        category_descriptions = {
            # Animation descriptions
            'ANIMATIONS_ANIMATION': "Animate mobjects",
            'ANIMATIONS_CHANGING': "Animation of a mobject boundary and tracing of points",
            'ANIMATIONS_COMPOSITION': "Tools for displaying multiple animations at once",
            'ANIMATIONS_CREATION': "Animate the display or removal of a mobject from a scene",
            'ANIMATIONS_FADING': "Fading in and out of view",
            'ANIMATIONS_GROWING': "Animations that introduce mobjects to scene by growing them from points",
            'ANIMATIONS_INDICATION': "Animations drawing attention to particular mobjects",
            'ANIMATIONS_MOVEMENT': "Animations related to movement",
            'ANIMATIONS_NUMBERS': "Animations for changing numbers",
            'ANIMATIONS_ROTATION': "Animations related to rotation",
            'ANIMATIONS_SPECIALIZED': "Specialized animations",
            'ANIMATIONS_SPEEDMODIFIER': "Utilities for modifying the speed at which animations are played",
            'ANIMATIONS_TRANSFORM': "Animations transforming one mobject into another",
            'ANIMATIONS_TRANSFORM_MATCHING_PARTS': "Animations that try to transform Mobjects while keeping track of identical parts",
            'ANIMATIONS_UPDATERS': "Animations and utility mobjects related to update functions",
            
            # Camera descriptions
            'CAMERAS_CAMERA': "A camera converts the mobjects contained in a Scene into an array of pixels",
            'CAMERAS_MAPPING_CAMERA': "A camera that allows mapping between objects",
            'CAMERAS_MOVING_CAMERA': "A camera able to move through a scene",
            'CAMERAS_MULTI_CAMERA': "A camera supporting multiple perspectives",
            'CAMERAS_THREE_D_CAMERA': "A camera that can be positioned and oriented in three-dimensional space",
            
            # Object descriptions
            'OBJECTS_FRAME': "Special rectangles",
            'OBJECTS_GEOMETRY': "Various geometric Mobjects",
            'OBJECTS_GRAPH': "Mobjects used to represent mathematical graphs (think graph theory, not plotting)",
            'OBJECTS_GRAPHING': "Coordinate systems and function graphing related mobjects",
            'OBJECTS_LOGO': "Utilities for Manim's logo and banner",
            'OBJECTS_MATRIX': "Mobjects representing matrices",
            'OBJECTS_MOBJECT': "Base classes for objects that can be displayed",
            'OBJECTS_SVG': "Mobjects related to SVG images",
            'OBJECTS_TABLE': "Mobjects representing tables",
            'OBJECTS_TEXT': "Mobjects used to display Text using Pango or LaTeX",
            'OBJECTS_THREE_D': "Three-dimensional mobjects",
            'OBJECTS_TYPES': "Specialized mobject base classes",
            'OBJECTS_UTILS': "Utilities for working with mobjects",
            'OBJECTS_VALUE_TRACKER': "Simple mobjects that can be used for storing (and updating) a value",
            'OBJECTS_VECTOR_FIELD': "Mobjects representing vector fields",
            
            # Scene descriptions
            'SCENES_MOVING_CAMERA_SCENE': "A scene whose camera can be moved around",
            'SCENES_SECTION': "Building blocks of segmented video API",
            'SCENES_SCENE': "Basic canvas for animations",
            'SCENES_SCENE_FILE_WRITER': "The interface between scenes and ffmpeg",
            'SCENES_THREE_D_SCENE': "A scene suitable for rendering three-dimensional objects and animations",
            'SCENES_VECTOR_SPACE_SCENE': "A scene suitable for vector spaces",
            'SCENES_ZOOMED_SCENE': "A scene supporting zooming in on a specified section",
        }
        
        if hasattr(node_tree, 'manim_node_categories'):
            print("\n=== MANIM NODE EDITOR MENU STRUCTURE ===\n")
            
            # Group categories by main menu
            menu_structure = {}
            for category in node_tree.manim_node_categories:
                category_id = category.identifier
                
                # Main category or submenu?
                if '_' not in category_id:
                    print(f"Main Category: {category.label}")
                    if category_id not in menu_structure:
                        menu_structure[category_id] = []
                else:
                    # This is a submenu
                    main_category = category_id.split('_')[0]
                    if main_category not in menu_structure:
                        menu_structure[main_category] = []
                    
                    # Add description to the submenu name if available
                    description = ""
                    if category_id in category_descriptions:
                        description = category_descriptions[category_id]
                    
                    # Add to submenu list with information about contained nodes
                    node_info = []
                    if hasattr(category, 'items'):
                        for item in category.items:
                            if hasattr(item, 'nodetype'):
                                node_info.append(item.nodetype)
                    
                    menu_structure[main_category].append({
                        'identifier': category_id,
                        'label': category.label,
                        'description': description,
                        'nodes': node_info
                    })
            
            # Print the organized menu structure
            for main_category, submenus in menu_structure.items():
                print(f"\n--- {main_category} Submenus ---")
                for submenu in submenus:
                    print(f"  • {submenu['label']}: {submenu['description']}")
                    
                    # Print nodes in this submenu if any
                    if submenu['nodes']:
                        print("    Nodes:")
                        for node in submenu['nodes']:
                            print(f"      - {node}")
                
            print("\n=== END OF MENU STRUCTURE ===\n")
    except Exception as e:
        print(f"Error printing menu categories: {e}")

if __name__ == "__main__":
    # Create the test node tree
    test_tree = create_test_manim_setup()
    
    # Setup the editor area
    setup_node_editor_area()
    
    # Print menu categories to verify structure
    print_menu_categories()
    
    print("Manim node editor test setup completed!") 