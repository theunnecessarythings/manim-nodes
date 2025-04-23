import bpy
from bpy.types import Node
from manim_node_editor.nodes import ManimNode

# Camera Nodes
class ManimCameraNode(Node, ManimNode):
    bl_idname = 'ManimCameraNodeType'
    bl_label = 'Camera'
    bl_icon = 'CAMERA_DATA'
    
    background_color = bpy.props.FloatVectorProperty(
        name="Background Color",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Camera background color",
    )
    
    background_opacity = bpy.props.FloatProperty(
        name="Background Opacity",
        default=1.0,
        min=0.0,
        max=1.0,
        description="Camera background opacity",
    )
    
    pixel_width = bpy.props.IntProperty(
        name="Pixel Width",
        default=1920,
        min=320,
        description="Width in pixels",
    )
    
    pixel_height = bpy.props.IntProperty(
        name="Pixel Height",
        default=1080,
        min=240,
        description="Height in pixels",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Camera")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "background_color")
        layout.prop(self, "background_opacity")
        layout.prop(self, "pixel_width")
        layout.prop(self, "pixel_height")
    
    def draw_label(self):
        return self.bl_label

class ManimMovingCameraNode(Node, ManimNode):
    bl_idname = 'ManimMovingCameraNodeType'
    bl_label = 'Moving Camera'
    bl_icon = 'CON_CAMERASOLVER'
    
    background_color = bpy.props.FloatVectorProperty(
        name="Background Color",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Camera background color",
    )
    
    frame_width = bpy.props.FloatProperty(
        name="Frame Width",
        default=14.0,
        min=1.0,
        description="Width of the camera frame",
    )
    
    frame_height = bpy.props.FloatProperty(
        name="Frame Height",
        default=8.0,
        min=1.0,
        description="Height of the camera frame",
    )
    
    pixel_width = bpy.props.IntProperty(
        name="Pixel Width",
        default=1920,
        min=320,
        description="Width in pixels",
    )
    
    pixel_height = bpy.props.IntProperty(
        name="Pixel Height",
        default=1080,
        min=240,
        description="Height in pixels",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Camera")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "background_color")
        layout.prop(self, "frame_width")
        layout.prop(self, "frame_height")
        layout.prop(self, "pixel_width")
        layout.prop(self, "pixel_height")
    
    def draw_label(self):
        return self.bl_label

class ManimThreeDCameraNode(Node, ManimNode):
    bl_idname = 'ManimThreeDCameraNodeType'
    bl_label = '3D Camera'
    bl_icon = 'VIEW3D'
    
    background_color = bpy.props.FloatVectorProperty(
        name="Background Color",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Camera background color",
    )
    
    phi = bpy.props.FloatProperty(
        name="Phi",
        default=0.0,
        description="Polar angle in radians",
    )
    
    theta = bpy.props.FloatProperty(
        name="Theta",
        default=-90.0,
        description="Azimuthal angle in degrees",
    )
    
    focal_distance = bpy.props.FloatProperty(
        name="Focal Distance",
        default=2.0,
        min=0.1,
        description="Focal distance",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "3D Scene")
        self.outputs.new('ManimNodeSocket', "Camera")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "background_color")
        layout.prop(self, "phi")
        layout.prop(self, "theta")
        layout.prop(self, "focal_distance")
    
    def draw_label(self):
        return self.bl_label
    
node_classes = [
    ManimCameraNode,
    ManimMovingCameraNode,
    ManimThreeDCameraNode,
]