import bpy
from bpy.types import Node
from manim_node_editor.nodes import ManimNode

class ManimSceneNode(Node, ManimNode):
    bl_idname = 'ManimSceneNodeType'
    bl_label = 'Manim Scene'
    bl_icon = 'SCENE_DATA'
    
    scene_name : bpy.props.StringProperty(
        name="Scene Name",
        default="MyScene",
        description="Name of the Manim scene class",
    )  # type: ignore
    
    background_color: bpy.props.FloatVectorProperty(
        name="Background Color",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Background color of the scene",
    )  # type: ignore
    
    duration: bpy.props.FloatProperty(
        name="Duration",
        default=3.0,
        min=0.1,
        description="Duration of the scene in seconds",
    )  # type: ignore
    
    def init(self, context):
        self.outputs.new('ManimNodeSocket', "Scene")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "scene_name")
        layout.prop(self, "background_color")
        layout.prop(self, "duration")
    
    def draw_label(self):
        return self.bl_label



class Manim3DSceneNode(Node, ManimNode):
    bl_idname = 'Manim3DSceneNodeType'
    bl_label = '3D Scene'
    bl_icon = 'VIEW_PERSPECTIVE'
    
    scene_name: bpy.props.StringProperty(
        name="Scene Name",
        default="My3DScene",
        description="Name of the Manim 3D scene class",
    )  # type: ignore
    
    background_color: bpy.props.FloatVectorProperty(
        name="Background Color",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Background color of the scene",
    )  # type: ignore   
    
    ambient_camera_rotation: bpy.props.BoolProperty(
        name="Ambient Camera Rotation",
        default=False,
        description="Enable ambient camera rotation",
    )  # type: ignore
    
    def init(self, context):
        self.outputs.new('ManimNodeSocket', "3D Scene")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "scene_name")
        layout.prop(self, "background_color")
        layout.prop(self, "ambient_camera_rotation")
    
    def draw_label(self):
        return self.bl_label


class ManimAddNode(Node, ManimNode):
    bl_idname = 'ManimAddNodeType'
    bl_label = 'Add'
    bl_icon = 'PLUS'
    
    def init(self, context):
        self.inputs.new('ManimSequenceSocket', "Sequence")
        self.inputs.new('ManimObjectSocket', "Objects", use_multi_input=True)
        self.outputs.new('ManimSequenceSocket', "Sequence")
    
    def draw_buttons(self, context, layout):
        pass

    
    def draw_label(self):
        return self.bl_label
    
class ManimWaitNode(Node, ManimNode):
    bl_idname = 'ManimWaitNodeType'
    bl_label = 'Wait'

    seconds: bpy.props.FloatProperty(
        name="Seconds",
        default=1.0,
        min=0.0,
        description="Wait time in seconds",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimSequenceSocket', "Sequence")
        self.outputs.new('ManimSequenceSocket', "Sequence")
        self.inputs.new('NodeSocketFloat', "Seconds").default_value = 1
    
    def draw_buttons(self, context, layout):
        pass
    
    def draw_label(self):
        return self.bl_label
    
class ManimPlayNode(Node, ManimNode):
    bl_idname = 'ManimPlayNodeType'
    bl_label = 'Play'
    bl_icon = 'PLAY'
    
    def init(self, context):
        self.inputs.new('ManimSequenceSocket', "Sequence")
        self.inputs.new('ManimAnimationSocket', "Animations", use_multi_input=True)
        self.outputs.new('ManimSequenceSocket', "Sequence")
    
    def draw_buttons(self, context, layout):
        pass
    
    def draw_label(self):
        return self.bl_label
    

class ManimStartSequenceNode(Node, ManimNode):
    bl_idname = 'ManimStartSequenceNodeType'
    bl_label = 'Start Sequence'
    
    def init(self, context):
        self.outputs.new('ManimSequenceSocket', "Sequence")
    
    def draw_buttons(self, context, layout):
        pass
    
    def draw_label(self):
        return self.bl_label
    
class ManimEndSequenceNode(Node, ManimNode):
    bl_idname = 'ManimEndSequenceNodeType'
    bl_label = 'End Sequence'
    
    def init(self, context):
        self.inputs.new('ManimSequenceSocket', "Sequence")
    
    def draw_buttons(self, context, layout):
        pass
    
    def draw_label(self):
        return self.bl_label
    

node_classes = [
    ManimSceneNode,
    Manim3DSceneNode,
    ManimAddNode,
    ManimWaitNode,
    ManimPlayNode,
    ManimStartSequenceNode,
    ManimEndSequenceNode,
]
