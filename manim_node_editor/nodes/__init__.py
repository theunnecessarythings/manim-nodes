import bpy
from bpy.types import Node
from nodeitems_utils import NodeItem

# Basic node class that all Manim nodes will derive from
class ManimNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'ManimNodeTree'
    

# Helper operators for adding inputs dynamically
class MANIM_OT_add_animation_input(bpy.types.Operator):
    bl_idname = "node.manim_add_animation_input"
    bl_label = "Add Animation Input"
    bl_description = "Add a new animation input socket to the node"
    bl_options = {'REGISTER', 'UNDO'}
    
    node_name = bpy.props.StringProperty()
    
    def execute(self, context):
        # Find the node with the given name
        for node in context.space_data.edit_tree.nodes:
            if node.name == self.node_name:
                # Add a new input socket
                index = len(node.inputs)
                node.inputs.new('ManimNodeSocket', f"Animation {index}")
                break
        
        return {'FINISHED'}

class MANIM_OT_add_mobject_input(bpy.types.Operator):
    bl_idname = "node.manim_add_mobject_input"
    bl_label = "Add Mobject Input"
    bl_description = "Add a new mobject input socket to the node"
    bl_options = {'REGISTER', 'UNDO'}
    
    node_name = bpy.props.StringProperty()
    
    def execute(self, context):
        # Find the node with the given name
        for node in context.space_data.edit_tree.nodes:
            if node.name == self.node_name:
                # Add a new input socket
                index = len(node.inputs)
                node.inputs.new('ManimNodeSocket', f"Mobject {index}")
                break
        
        return {'FINISHED'}

def get_node_classes():
    from . import animation
    from . import cameras
    from . import objects
    from . import scene
    return [
        *animation.node_classes,
        *cameras.node_classes,
        *objects.node_classes,
        *scene.node_classes,
    ]

node_classes = get_node_classes()

def register():
    for cls in node_classes:
        bpy.utils.register_class(cls)
    

def unregister():
    for cls in reversed(node_classes):
        bpy.utils.unregister_class(cls) 