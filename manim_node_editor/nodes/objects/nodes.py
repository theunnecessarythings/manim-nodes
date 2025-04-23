import bpy
from bpy.types import Node
from manim_node_editor.nodes import ManimNode

class ManimArcNode(Node, ManimNode):
    bl_idname = 'ManimArcNodeType'
    bl_label = 'Arc'
    bl_icon = 'IPO_EASE_IN_OUT'
    
    radius: bpy.props.FloatProperty(
        name="Radius",
        default=1.0,
        min=0.1,
        description="Radius of the arc",
    )  # type: ignore
    
    start_angle: bpy.props.FloatProperty(
        name="Start Angle",
        default=0.0,
        description="Start angle in radians",
    )  # type: ignore
    
    angle: bpy.props.FloatProperty(
        name="Angle",
        default=3.14159,  # PI
        description="Arc angle in radians",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 0.5, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Arc color",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the arc's stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Arc")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "radius")
        layout.prop(self, "start_angle")
        layout.prop(self, "angle")
        layout.prop(self, "color")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label
    


# Boolean Operations Node - for 2D boolean operations
class ManimBooleanOpsNode(Node, ManimNode):
    bl_idname = 'ManimBooleanOpsNodeType'
    bl_label = 'Boolean Operations'
    bl_icon = 'MOD_BOOLEAN'
    
    operation: bpy.props.EnumProperty(
        name="Operation",
        items=[
            ('UNION', "Union", "Union of two shapes"),
            ('INTERSECTION', "Intersection", "Intersection of two shapes"),
            ('DIFFERENCE', "Difference", "Difference between two shapes"),
            ('SYMMETRIC_DIFFERENCE', "Symmetric Difference", "Symmetric difference between two shapes"),
        ],
        default='UNION',
        description="Boolean operation to perform",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Result color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.inputs.new('ManimNodeSocket', "Shape A")
        self.inputs.new('ManimNodeSocket', "Shape B")
        self.outputs.new('ManimNodeSocket', "Result")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "operation")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

# Labeled Line Node - for labeled lines
class ManimLabeledNode(Node, ManimNode):
    bl_idname = 'ManimLabeledNodeType'
    bl_label = 'Labeled'
    bl_icon = 'OUTLINER_DATA_FONT'
    
    line_type: bpy.props.EnumProperty(
        name="Line Type",
        items=[
            ('LINE', "Line", "Simple labeled line"),
            ('ARROW', "Arrow", "Labeled arrow"),
            ('DOUBLEARROW', "Double Arrow", "Labeled double-headed arrow"),
            ('VECTOR', "Vector", "Labeled vector"),
        ],
        default='LINE',
        description="Type of labeled line to create",
    )  # type: ignore
    
    label_text: bpy.props.StringProperty(
        name="Label",
        default="Label",
        description="Label text",
    )  # type: ignore
    
    start_point: bpy.props.FloatVectorProperty(
        name="Start Point",
        subtype='XYZ',
        default=(-1.0, 0.0, 0.0),
        size=3,
        description="Start point of the line",
    )  # type: ignore
    
    end_point: bpy.props.FloatVectorProperty(
        name="End Point",
        subtype='XYZ',
        default=(1.0, 0.0, 0.0),
        size=3,
        description="End point of the line",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Line color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Labeled")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "line_type")
        layout.prop(self, "label_text")
        layout.prop(self, "start_point")
        layout.prop(self, "end_point")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

# Line Node - for creating lines
class ManimLineNode(Node, ManimNode):
    bl_idname = 'ManimLineNodeType'
    bl_label = 'Line'
    bl_icon = 'SNAP_EDGE'
    
    start_point: bpy.props.FloatVectorProperty(
        name="Start Point",
        subtype='XYZ',
        default=(-1.0, 0.0, 0.0),
        size=3,
        description="Start point of the line",
    )  # type: ignore
    
    end_point: bpy.props.FloatVectorProperty(
        name="End Point",
        subtype='XYZ',
        default=(1.0, 0.0, 0.0),
        size=3,
        description="End point of the line",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Line color",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the line's stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Line")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "start_point")
        layout.prop(self, "end_point")
        layout.prop(self, "color")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

# Polygram Node - for creating geometric shapes
class ManimPolygramNode(Node, ManimNode):
    bl_idname = 'ManimPolygramNodeType'
    bl_label = 'Polygram'
    bl_icon = 'MESH_DATA'
    
    shape_type: bpy.props.EnumProperty(
        name="Shape Type",
        items=[
            ('TRIANGLE', "Triangle", "Regular triangle"),
            ('SQUARE', "Square", "Regular square"),
            ('PENTAGON', "Pentagon", "Regular pentagon"),
            ('HEXAGON', "Hexagon", "Regular hexagon"),
            ('OCTAGON', "Octagon", "Regular octagon"),
            ('STAR', "Star", "Star shape"),
            ('POLYGON', "Polygon", "Regular polygon with specified number of sides"),
        ],
        default='TRIANGLE',
        description="Type of shape to create",
    )  # type: ignore
    
    num_sides: bpy.props.IntProperty(
        name="Number of Sides",
        default=5,
        min=3,
        description="Number of sides for polygon",
    )  # type: ignore
    
    radius: bpy.props.FloatProperty(
        name="Radius",
        default=1.0,
        min=0.1,
        description="Radius of the shape",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Shape color",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Fill opacity of the shape",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Polygram")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "shape_type")
        if self.shape_type == 'POLYGON':
            layout.prop(self, "num_sides")
        layout.prop(self, "radius")
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
    
    def draw_label(self):
        return self.bl_label

# Shape Matchers Node - for marking and annotating mobjects
class ManimShapeMatchersNode(Node, ManimNode):
    bl_idname = 'ManimShapeMatchersNodeType'
    bl_label = 'Shape Matchers'
    bl_icon = 'SNAP_EDGE'
    
    matcher_type: bpy.props.EnumProperty(
        name="Matcher Type",
        items=[
            ('BRACE', "Brace", "Brace annotation"),
            ('UNDERLINE', "Underline", "Underline annotation"),
            ('SURROUND', "Surround", "Surrounding annotation"),
            ('HIGHLIGHT', "Highlight", "Highlight annotation"),
        ],
        default='BRACE',
        description="Type of shape matcher to create",
    )  # type: ignore
    
    text: bpy.props.StringProperty(
        name="Text",
        default="Annotation",
        description="Annotation text",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 0.8, 0.2, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Matcher color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.inputs.new('ManimNodeSocket', "Target")
        self.outputs.new('ManimNodeSocket', "Matcher")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "matcher_type")
        layout.prop(self, "text")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

# Tips Node - for tips on VMobjects
class ManimTipsNode(Node, ManimNode):
    bl_idname = 'ManimTipsNodeType'
    bl_label = 'Tips'
    bl_icon = 'SORTSIZE'
    
    tip_type: bpy.props.EnumProperty(
        name="Tip Type",
        items=[
            ('ARROW', "Arrow", "Arrow tip"),
            ('DOT', "Dot", "Dot tip"),
            ('TRIANGLE', "Triangle", "Triangle tip"),
            ('SQUARE', "Square", "Square tip"),
        ],
        default='ARROW',
        description="Type of tip to add",
    )  # type: ignore
    
    tip_length: bpy.props.FloatProperty(
        name="Tip Length",
        default=0.25,
        min=0.01,
        description="Length of the tip",
    )  # type: ignore
    
    tip_width: bpy.props.FloatProperty(
        name="Tip Width",
        default=0.25,
        min=0.01,
        description="Width of the tip",
    )  # type: ignore
    
    at_start: bpy.props.BoolProperty(
        name="At Start",
        default=False,
        description="Add tip at the start of the VMobject",
    )  # type: ignore
    
    at_end: bpy.props.BoolProperty(
        name="At End",
        default=True,
        description="Add tip at the end of the VMobject",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Tip color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "VMobject")
        self.outputs.new('ManimNodeSocket', "TippedVMobject")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "tip_type")
        layout.prop(self, "tip_length")
        layout.prop(self, "tip_width")
        layout.prop(self, "at_start")
        layout.prop(self, "at_end")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label
    

# Text Node - for creating text in Manim
class ManimTextNode(Node, ManimNode):
    bl_idname = 'ManimTextNodeType'
    bl_label = 'Text'
    bl_icon = 'FONT_DATA'
    
    text: bpy.props.StringProperty(
        name="Text",
        default="Hello, Manim!",
        description="Text content",
    )  # type: ignore
    
    font_size: bpy.props.FloatProperty(
        name="Font Size",
        default=1.0,
        min=0.1,
        description="Font size",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Text color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Text")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "text")
        layout.prop(self, "font_size")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

# Circle Node - for creating circles in Manim
class ManimCircleNode(Node, ManimNode):
    bl_idname = 'ManimCircleNodeType'
    bl_label = 'Circle'
    bl_icon = 'MESH_CIRCLE'
    
    radius: bpy.props.FloatProperty(
        name="Radius",
        default=1.0,
        min=0.1,
        description="Radius of the circle",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 0.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Circle color",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the circle's stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Circle")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "radius")
        layout.prop(self, "color")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label


# MathTex Node - for LaTeX math equations
class ManimMathTexNode(Node, ManimNode):
    bl_idname = 'ManimMathTexNodeType'
    bl_label = 'MathTex'
    bl_icon = 'FILE_FONT'
    
    tex_string: bpy.props.StringProperty(
        name="TeX",
        default="e^{i\\pi} + 1 = 0",
        description="LaTeX math expression",
    )  # type: ignore
    
    font_size: bpy.props.FloatProperty(
        name="Font Size",
        default=1.0,
        min=0.1,
        description="Font size",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Text color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "MathTex")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "tex_string")
        layout.prop(self, "font_size")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label


# Axes Node
class ManimAxesNode(Node, ManimNode):
    bl_idname = 'ManimAxesNodeType'
    bl_label = 'Axes'
    bl_icon = 'ORIENTATION_VIEW'
    
    x_range: bpy.props.FloatVectorProperty(
        name="X Range",
        subtype='XYZ',
        default=(-10.0, 10.0, 1.0),
        size=3,
        description="Range for X axis (min, max, step)",
    )  # type: ignore
    
    y_range: bpy.props.FloatVectorProperty(
        name="Y Range",
        subtype='XYZ',
        default=(-5.0, 5.0, 1.0),
        size=3,
        description="Range for Y axis (min, max, step)",
    )  # type: ignore
    
    axis_config: bpy.props.StringProperty(
        name="Axis Config",
        default="{}",
        description="JSON configuration for axes (advanced)",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Axes")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "x_range")
        layout.prop(self, "y_range")
        layout.prop(self, "axis_config")
    
    def draw_label(self):
        return self.bl_label
    


# NumberPlane Node
class ManimNumberPlaneNode(Node, ManimNode):
    bl_idname = 'ManimNumberPlaneNodeType'
    bl_label = 'Number Plane'
    bl_icon = 'GRID'
    
    x_range: bpy.props.FloatVectorProperty(
        name="X Range",
        subtype='XYZ',
        default=(-10.0, 10.0, 1.0),
        size=3,
        description="Range for X axis (min, max, step)",
    )  # type: ignore
    
    y_range: bpy.props.FloatVectorProperty(
        name="Y Range",
        subtype='XYZ',
        default=(-5.0, 5.0, 1.0),
        size=3,
        description="Range for Y axis (min, max, step)",
    )  # type: ignore
    
    background_line_style: bpy.props.StringProperty(
        name="Background Style",
        default="{}",
        description="JSON configuration for background lines",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Plane")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "x_range")
        layout.prop(self, "y_range")
        layout.prop(self, "background_line_style")
    
    def draw_label(self):
        return self.bl_label

# Graph Function Node
class ManimFunctionGraphNode(Node, ManimNode):
    bl_idname = 'ManimFunctionGraphNodeType'
    bl_label = 'Function Graph'
    bl_icon = 'IPO_EASE_IN_OUT'
    
    function_text: bpy.props.StringProperty(
        name="Function",
        default="lambda x: x**2",
        description="Python function to graph (lambda x: ...)",
    )  # type: ignore
    
    x_range: bpy.props.FloatVectorProperty(
        name="X Range",
        subtype='XYZ',
        default=(-10.0, 10.0, 0.01),
        size=3,
        description="Range for X values (min, max, step)",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 0.5, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Graph color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Axes")
        self.outputs.new('ManimNodeSocket', "Graph")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "x_range")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

# Text Nodes
class ManimParagraphNode(Node, ManimNode):
    bl_idname = 'ManimParagraphNodeType'
    bl_label = 'Paragraph'
    bl_icon = 'ALIGN_LEFT'
    
    text: bpy.props.StringProperty(
        name="Text",
        default="This is a paragraph\nwith multiple lines\nof text.",
        description="Paragraph text content",
    )  # type: ignore
    
    alignment: bpy.props.EnumProperty(
        name="Alignment",
        items=[
            ('LEFT', "Left", "Left aligned text"),
            ('CENTER', "Center", "Center aligned text"),
            ('RIGHT', "Right", "Right aligned text"),
        ],
        default='LEFT',
        description="Text alignment",
    )  # type: ignore
    
    font: bpy.props.StringProperty(
        name="Font",
        default="",
        description="Font name (leave empty for default)",
    )  # type: ignore
    
    font_size: bpy.props.FloatProperty(
        name="Font Size",
        default=24.0,
        min=1.0,
        description="Font size",
    )  # type: ignore
    
    line_spacing: bpy.props.FloatProperty(
        name="Line Spacing",
        default=1.0,
        min=0.1,
        description="Spacing between lines",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Text color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Paragraph")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "text")
        layout.prop(self, "alignment")
        layout.prop(self, "font")
        layout.prop(self, "font_size")
        layout.prop(self, "line_spacing")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label


class ManimMarkupTextNode(Node, ManimNode):
    bl_idname = 'ManimMarkupTextNodeType'
    bl_label = 'Markup Text'
    bl_icon = 'COLOR_RED'
    
    text: bpy.props.StringProperty(
        name="Markup Text",
        default='<span foreground="red">Red</span> and <span foreground="blue">Blue</span> text',
        description="Text with markup",
    )  # type: ignore
    
    font_size: bpy.props.FloatProperty(
        name="Font Size",
        default=24.0,
        min=1.0,
        description="Font size",
    )  # type: ignore
    
    line_spacing: bpy.props.FloatProperty(
        name="Line Spacing",
        default=1.0,
        min=0.1,
        description="Spacing between lines",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Text")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "text")
        layout.prop(self, "font_size")
        layout.prop(self, "line_spacing")
        layout.label(text="Use Pango markup syntax")
    
    def draw_label(self):
        return self.bl_label



# 3D Axes Node
class Manim3DAxesNode(Node, ManimNode):
    bl_idname = 'Manim3DAxesNodeType'
    bl_label = '3D Axes'
    bl_icon = 'ORIENTATION_GLOBAL'
    
    x_range: bpy.props.FloatVectorProperty(
        name="X Range",
        subtype='XYZ',
        default=(-5.0, 5.0, 1.0),
        size=3,
        description="Range for X axis (min, max, step)",
    )  # type: ignore
    
    y_range: bpy.props.FloatVectorProperty(
        name="Y Range",
        subtype='XYZ',
        default=(-5.0, 5.0, 1.0),
        size=3,
        description="Range for Y axis (min, max, step)",
    )  # type: ignore
    
    z_range: bpy.props.FloatVectorProperty(
        name="Z Range",
        subtype='XYZ',
        default=(-5.0, 5.0, 1.0),
        size=3,
        description="Range for Z axis (min, max, step)",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "3D Scene")
        self.outputs.new('ManimNodeSocket', "3D Axes")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "x_range")
        layout.prop(self, "y_range")
        layout.prop(self, "z_range")
    
    def draw_label(self):
        return self.bl_label

# Surface Node - for 3D surfaces in Manim
class ManimSurfaceNode(Node, ManimNode):
    bl_idname = 'ManimSurfaceNodeType'
    bl_label = 'Surface'
    bl_icon = 'SURFACE_NSURFACE'
    
    function_text: bpy.props.StringProperty(
        name="Function",
        default="lambda x, y: np.sin(x) * np.cos(y)",
        description="Function for surface (lambda x, y: ...)",
    )  # type: ignore
    
    u_range: bpy.props.FloatVectorProperty(
        name="U Range",
        subtype='XYZ',
        default=(-3.0, 3.0, 0.5),
        size=3,
        description="Range for U parameter (min, max, step)",
    )  # type: ignore
    
    v_range: bpy.props.FloatVectorProperty(
        name="V Range",
        subtype='XYZ',
        default=(-3.0, 3.0, 0.5),
        size=3,
        description="Range for V parameter (min, max, step)",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.2, 0.5, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Surface color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "3D Scene")
        self.outputs.new('ManimNodeSocket', "Surface")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "u_range")
        layout.prop(self, "v_range")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

# Sphere Node
class ManimSphereNode(Node, ManimNode):
    bl_idname = 'ManimSphereNodeType'
    bl_label = 'Sphere'
    bl_icon = 'MESH_UVSPHERE'
    
    radius: bpy.props.FloatProperty(
        name="Radius",
        default=1.0,
        min=0.1,
        description="Radius of the sphere",
    )  # type: ignore
    
    resolution: bpy.props.IntProperty(
        name="Resolution",
        default=20,
        min=4,
        description="Resolution of the sphere",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 0.5, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Sphere color",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "3D Scene")
        self.outputs.new('ManimNodeSocket', "Sphere")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "radius")
        layout.prop(self, "resolution")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label



# Value Tracker Nodes
class ManimValueTrackerNode(Node, ManimNode):
    bl_idname = 'ManimValueTrackerNodeType'
    bl_label = 'Value Tracker'
    bl_icon = 'DRIVER'
    
    value: bpy.props.FloatProperty(
        name="Value",
        default=0.0,
        description="Initial value",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Tracker")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "value")
    
    def draw_label(self):
        return self.bl_label

class ManimComplexValueTrackerNode(Node, ManimNode):
    bl_idname = 'ManimComplexValueTrackerNodeType'
    bl_label = 'Complex Value Tracker'
    bl_icon = 'IPO_BEZIER'
    
    real: bpy.props.FloatProperty(
        name="Real Part",
        default=1.0,
        description="Real part of complex value",
    )  # type: ignore
    
    imag: bpy.props.FloatProperty(
        name="Imaginary Part",
        default=0.0,
        description="Imaginary part of complex value",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Complex Tracker")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "real")
        layout.prop(self, "imag")
    
    def draw_label(self):
        return self.bl_label



# Additional Geometry Nodes
class ManimDotNode(Node, ManimNode):
    bl_idname = 'ManimDotNodeType'
    bl_label = 'Dot'
    bl_icon = 'KEYTYPE_JITTER_VEC'
    
    point: bpy.props.FloatVectorProperty(
        name="Point",
        subtype='XYZ',
        default=(0.0, 0.0, 0.0),
        size=3,
        description="Position of the dot",
    )  # type: ignore
    
    radius: bpy.props.FloatProperty(
        name="Radius",
        default=0.08,
        min=0.01,
        description="Radius of the dot",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the dot",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Dot")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "point")
        layout.prop(self, "radius")
        layout.prop(self, "color")
    
    def draw_label(self):
        return self.bl_label

class ManimRectangleNode(Node, ManimNode):
    bl_idname = 'ManimRectangleNodeType'
    bl_label = 'Rectangle'
    bl_icon = 'MESH_PLANE'
    
    width: bpy.props.FloatProperty(
        name="Width",
        default=4.0,
        min=0.01,
        description="Width of the rectangle",
    )  # type: ignore
    
    height: bpy.props.FloatProperty(
        name="Height",
        default=2.0,
        min=0.01,
        description="Height of the rectangle",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 0.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the rectangle",
    )  # type: ignore 
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Fill opacity of the rectangle",
    )  # type: ignore

    grid_xstep: bpy.props.FloatProperty(
        name="Grid X Step",
        default=1.0,
        description="Step size for the grid in the X direction",
    )  # type: ignore

    grid_ystep: bpy.props.FloatProperty(
        name="Grid Y Step",
        default=1.0,
        description="Step size for the grid in the Y direction",
    )  # type: ignore

    mark_paths_closed: bpy.props.BoolProperty(
        name="Mark Paths Closed",
        default=True,
        description="Mark the paths as closed",
    )  # type: ignore

    close_new_points: bpy.props.BoolProperty(
        name="Close New Points",
        default=True,
        description="Close the new points",
    )  # type: ignore    
    
    def init(self, context):
        self.outputs.new('ManimObjectSocket', "Rectangle")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "width")
        layout.prop(self, "height")
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "grid_xstep")
        layout.prop(self, "grid_ystep")
        layout.prop(self, "mark_paths_closed")
        layout.prop(self, "close_new_points")

    def draw_label(self):
        return self.bl_label

class ManimSquareNode(Node, ManimNode):
    bl_idname = 'ManimSquareNodeType'
    bl_label = 'Square'
    bl_icon = 'MESH_PLANE'
    
    side_length: bpy.props.FloatProperty(
        name="Side Length",
        default=2.0,
        min=0.01,
        description="Length of each side",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 0.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the square",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Fill opacity of the square",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Square")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "side_length")
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

class ManimEllipseNode(Node, ManimNode):
    bl_idname = 'ManimEllipseNodeType'
    bl_label = 'Ellipse'
    bl_icon = 'MESH_CIRCLE'
    
    width: bpy.props.FloatProperty(
        name="Width",
        default=4.0,
        min=0.01,
        description="Width of the ellipse",
    )  # type: ignore
    
    height: bpy.props.FloatProperty(
        name="Height",
        default=2.0,
        min=0.01,
        description="Height of the ellipse",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the ellipse",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Fill opacity of the ellipse",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Ellipse")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "width")
        layout.prop(self, "height")
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

class ManimTriangleNode(Node, ManimNode):
    bl_idname = 'ManimTriangleNodeType'
    bl_label = 'Triangle'
    bl_icon = 'MESH_CONE'
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 0.5, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the triangle",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Fill opacity of the triangle",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Triangle")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

class ManimStarNode(Node, ManimNode):
    bl_idname = 'ManimStarNodeType'
    bl_label = 'Star'
    bl_icon = 'LIGHT_SUN'
    
    n_points: bpy.props.IntProperty(
        name="Number of Points",
        default=5,
        min=3,
        description="Number of points on the star",
    )  # type: ignore
    
    outer_radius: bpy.props.FloatProperty(
        name="Outer Radius",
        default=1.0,
        min=0.1,
        description="Outer radius of the star",
    )  # type: ignore
    
    inner_radius: bpy.props.FloatProperty(
        name="Inner Radius",
        default=0.5,
        min=0.01,
        description="Inner radius of the star",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the star",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=1.0,
        min=0.0,
        max=1.0,
        description="Fill opacity of the star",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Star")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "n_points")
        layout.prop(self, "outer_radius")
        layout.prop(self, "inner_radius")
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

class ManimRegularPolygonNode(Node, ManimNode):
    bl_idname = 'ManimRegularPolygonNodeType'
    bl_label = 'Regular Polygon'
    bl_icon = 'MOD_BEVEL'
    
    n_sides: bpy.props.IntProperty(
        name="Number of Sides",
        default=6,
        min=3,
        description="Number of sides",
    )  # type: ignore
    
    radius: bpy.props.FloatProperty(
        name="Radius",
        default=1.0,
        min=0.01,
        description="Radius of the polygon",
    )  # type: ignore
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.5, 0.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the polygon",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Fill opacity of the polygon",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "RegularPolygon")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "n_sides")
        layout.prop(self, "radius")
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

# Shape Matcher Nodes
class ManimSurroundingRectangleNode(Node, ManimNode):
    bl_idname = 'ManimSurroundingRectangleNodeType'
    bl_label = 'Surrounding Rectangle'
    bl_icon = 'MOD_SOLIDIFY'
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Rectangle color",
    )  # type: ignore
    
    buff: bpy.props.FloatProperty(
        name="Buffer",
        default=0.15,
        min=0.0,
        description="Buffer distance from the target",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=2.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    corner_radius: bpy.props.FloatProperty(
        name="Corner Radius",
        default=0.0,
        min=0.0,
        description="Radius for rounded corners",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Rectangle")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "buff")
        layout.prop(self, "stroke_width")
        layout.prop(self, "corner_radius")
    
    def draw_label(self):
        return self.bl_label

class ManimUnderlineNode(Node, ManimNode):
    bl_idname = 'ManimUnderlineNodeType'
    bl_label = 'Underline'
    bl_icon = 'UNDERLINE'
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Underline color",
    )  # type: ignore
    
    buff: bpy.props.FloatProperty(
        name="Buffer",
        default=0.1,
        min=0.0,
        description="Buffer distance below the target",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=2.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Underline")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "buff")
        layout.prop(self, "stroke_width")
    
    def draw_label(self):
        return self.bl_label

class ManimCrossNode(Node, ManimNode):
    bl_idname = 'ManimCrossNodeType'
    bl_label = 'Cross'
    bl_icon = 'X'
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Cross color",
    )  # type: ignore
    
    stroke_width: bpy.props.FloatProperty(
        name="Stroke Width",
        default=6.0,
        min=0.0,
        description="Width of the stroke",
    )  # type: ignore
    
    scale_factor: bpy.props.FloatProperty(
        name="Scale Factor",
        default=1.0,
        min=0.1,
        description="How large to make the cross relative to the target",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Cross")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "stroke_width")
        layout.prop(self, "scale_factor")
    
    def draw_label(self):
        return self.bl_label

class ManimBackgroundRectangleNode(Node, ManimNode):
    bl_idname = 'ManimBackgroundRectangleNodeType'
    bl_label = 'Background Rectangle'
    bl_icon = 'NODE_MATERIAL'
    
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Background color",
    )  # type: ignore
    
    fill_opacity: bpy.props.FloatProperty(
        name="Fill Opacity",
        default=0.75,
        min=0.0,
        max=1.0,
        description="Fill opacity of the background",
    )  # type: ignore
    
    buff: bpy.props.FloatProperty(
        name="Buffer",
        default=0.2,
        min=0.0,
        description="Buffer distance around the target",
    )  # type: ignore
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Background")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "fill_opacity")
        layout.prop(self, "buff")
    
    def draw_label(self):
        return self.bl_label


node_classes = [
    ManimValueTrackerNode,
    ManimComplexValueTrackerNode,
    ManimDotNode,
    ManimRectangleNode,

    ManimArcNode,
    ManimBooleanOpsNode,
    ManimLabeledNode,
    ManimShapeMatchersNode,
    ManimTipsNode,
    ManimTextNode,
    ManimMathTexNode,
    ManimFunctionGraphNode,
    ManimParagraphNode,
    ManimSurfaceNode,
    ManimSphereNode,
    
]