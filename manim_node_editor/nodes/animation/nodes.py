import bpy
from bpy.types import Node
from manim_node_editor.nodes import ManimNode

# Animation Node - for basic animations
class ManimFadeInNode(Node, ManimNode):
    bl_idname = 'ManimFadeInNodeType'
    bl_label = 'Fade In'
    bl_icon = 'TRIA_RIGHT'
    
    duration = bpy.props.FloatProperty(
        name="Duration",
        default=1.0,
        min=0.1,
        description="Duration of the animation in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "duration")
    
    def draw_label(self):
        return self.bl_label


# Animation nodes
class ManimWaitNode(Node, ManimNode):
    bl_idname = 'ManimWaitNodeType'
    bl_label = 'Wait'
    bl_icon = 'PAUSE'
    
    duration = bpy.props.FloatProperty(
        name="Duration",
        default=1.0,
        min=0.1,
        description="Duration to wait in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "duration")
    
    def draw_label(self):
        return self.bl_label

class ManimTransformNode(Node, ManimNode):
    bl_idname = 'ManimTransformNodeType'
    bl_label = 'Transform'
    bl_icon = 'MOD_MESHDEFORM'
    
    path_arc = bpy.props.FloatProperty(
        name="Path Arc",
        default=0.0,
        description="Arc angle for the path of the transform",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Duration of the animation in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.inputs.new('ManimNodeSocket', "Target From")
        self.inputs.new('ManimNodeSocket', "Target To")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "path_arc")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Create Node
class ManimCreateNode(Node, ManimNode):
    bl_idname = 'ManimCreateNodeType'
    bl_label = 'Create'
    bl_icon = 'ADD'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Duration of the animation in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.inputs.new('ManimNodeSocket', "Target")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# FadeOut Node
class ManimFadeOutNode(Node, ManimNode):
    bl_idname = 'ManimFadeOutNodeType'
    bl_label = 'Fade Out'
    bl_icon = 'TRIA_LEFT'
    
    duration = bpy.props.FloatProperty(
        name="Duration",
        default=1.0,
        min=0.1,
        description="Duration of the animation in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "duration")
    
    def draw_label(self):
        return self.bl_label

# Rotate Node - for rotation animations
class ManimRotateNode(Node, ManimNode):
    bl_idname = 'ManimRotateNodeType'
    bl_label = 'Rotate'
    bl_icon = 'DRIVER_ROTATIONAL_DIFFERENCE'
    
    angle = bpy.props.FloatProperty(
        name="Angle",
        default=3.14159,
        description="Rotation angle in radians",
    )
    
    axis = bpy.props.FloatVectorProperty(
        name="Axis",
        subtype='XYZ',
        default=(0.0, 0.0, 1.0),
        size=3,
        description="Rotation axis",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Duration of the animation in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "angle")
        layout.prop(self, "axis")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Animation Changing Nodes
class ManimAnimatedBoundaryNode(Node, ManimNode):
    bl_idname = 'ManimAnimatedBoundaryNodeType'
    bl_label = 'Animated Boundary'
    bl_icon = 'FORCE_FORCE'
    
    colors = bpy.props.StringProperty(
        name="Colors",
        default="['#FFC200', '#FC6255', '#7676F5']",
        description="List of colors for boundary (as JSON array of hex values)",
    )
    
    cycle_rate = bpy.props.FloatProperty(
        name="Cycle Rate",
        default=0.5,
        min=0.0,
        description="Rate at which colors cycle",
    )
    
    max_stroke_width = bpy.props.FloatProperty(
        name="Max Stroke Width",
        default=3.0,
        min=0.0,
        description="Maximum stroke width",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Boundary")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "colors")
        layout.prop(self, "cycle_rate")
        layout.prop(self, "max_stroke_width")
    
    def draw_label(self):
        return self.bl_label

class ManimTracedPathNode(Node, ManimNode):
    bl_idname = 'ManimTracedPathNodeType'
    bl_label = 'Traced Path'
    bl_icon = 'CURVE_PATH'
    
    stroke_width = bpy.props.FloatProperty(
        name="Stroke Width",
        default=2.0,
        min=0.0,
        description="Width of the traced path",
    )
    
    stroke_color = bpy.props.FloatVectorProperty(
        name="Stroke Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the traced path",
    )
    
    min_distance_to_new_point = bpy.props.FloatProperty(
        name="Min Distance",
        default=0.1,
        min=0.0,
        description="Minimum distance to add a new point",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Path")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "stroke_width")
        layout.prop(self, "stroke_color")
        layout.prop(self, "min_distance_to_new_point")
    
    def draw_label(self):
        return self.bl_label

# Animation Composition Nodes
class ManimAnimationGroupNode(Node, ManimNode):
    bl_idname = 'ManimAnimationGroupNodeType'
    bl_label = 'Animation Group'
    bl_icon = 'GROUP'
    
    group_type = bpy.props.EnumProperty(
        name="Group Type",
        items=[
            ('SIMULTANEOUS', "Simultaneous", "All animations play together"),
            ('SEQUENTIAL', "Sequential", "Animations play one after another"),
        ],
        default='SIMULTANEOUS',
        description="How to organize animations in the group",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Duration of the animation in seconds",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Animation 1")
        self.inputs.new('ManimNodeSocket', "Animation 2")
        self.outputs.new('ManimNodeSocket', "Group")
        
        # Add button for adding more animation inputs
        self.use_custom_color = True
        self.color = (0.3, 0.6, 0.9)
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "group_type")
        layout.prop(self, "run_time")
        
        # Add button to add more animation inputs
        row = layout.row()
        op = row.operator("node.manim_add_animation_input", text="Add Animation Input")
        op.node_name = self.name
    
    def draw_label(self):
        return self.bl_label

class ManimLaggedStartNode(Node, ManimNode):
    bl_idname = 'ManimLaggedStartNodeType'
    bl_label = 'Lagged Start'
    bl_icon = 'NLA_PUSHDOWN'
    
    lag_ratio = bpy.props.FloatProperty(
        name="Lag Ratio",
        default=0.2,
        min=0.0,
        max=1.0,
        description="Ratio of lag between animations",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Duration of the entire lagged animation",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Animation 1")
        self.inputs.new('ManimNodeSocket', "Animation 2")
        self.outputs.new('ManimNodeSocket', "Lagged Group")
        
        # Add button for adding more animation inputs
        self.use_custom_color = True
        self.color = (0.3, 0.7, 0.7)
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "lag_ratio")
        layout.prop(self, "run_time")
        
        # Add button to add more animation inputs
        row = layout.row()
        op = row.operator("node.manim_add_animation_input", text="Add Animation Input")
        op.node_name = self.name
    
    def draw_label(self):
        return self.bl_label

class ManimLaggedStartMapNode(Node, ManimNode):
    bl_idname = 'ManimLaggedStartMapNodeType'
    bl_label = 'Lagged Start Map'
    bl_icon = 'NLA_PUSHDOWN'
    
    animation_type = bpy.props.EnumProperty(
        name="Animation Type",
        items=[
            ('FADE_IN', "Fade In", "Fade in animation"),
            ('FADE_OUT', "Fade Out", "Fade out animation"),
            ('SCALE', "Scale", "Scale animation"),
            ('ROTATE', "Rotate", "Rotate animation"),
        ],
        default='FADE_IN',
        description="Type of animation to apply to each submobject",
    )
    
    lag_ratio = bpy.props.FloatProperty(
        name="Lag Ratio",
        default=0.2,
        min=0.0,
        max=1.0,
        description="Ratio of lag between animations",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Duration of the entire lagged animation",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobjects")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "animation_type")
        layout.prop(self, "lag_ratio")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimSuccessionNode(Node, ManimNode):
    bl_idname = 'ManimSuccessionNodeType'
    bl_label = 'Succession'
    bl_icon = 'DECORATE_ANIMATE'
    
    run_time = bpy.props.FloatProperty(
        name="Total Run Time",
        default=5.0,
        min=0.1,
        description="Total duration of all animations",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Animation 1")
        self.inputs.new('ManimNodeSocket', "Animation 2")
        self.outputs.new('ManimNodeSocket', "Succession")
        
        # Add button for adding more animation inputs
        self.use_custom_color = True
        self.color = (0.5, 0.5, 0.9)
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        
        # Add button to add more animation inputs
        row = layout.row()
        op = row.operator("node.manim_add_animation_input", text="Add Animation Input")
        op.node_name = self.name
    
    def draw_label(self):
        return self.bl_label

# Animation Creation Nodes
class ManimAddTextLetterByLetterNode(Node, ManimNode):
    bl_idname = 'ManimAddTextLetterByLetterNodeType'
    bl_label = 'Add Text Letter By Letter'
    bl_icon = 'SEQUENCE'
    
    time_per_char = bpy.props.FloatProperty(
        name="Time Per Character",
        default=0.1,
        min=0.01,
        description="Time to display each character",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Total animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Text Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "time_per_char")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimAddTextWordByWordNode(Node, ManimNode):
    bl_idname = 'ManimAddTextWordByWordNodeType'
    bl_label = 'Add Text Word By Word'
    bl_icon = 'SEQUENCE'
    
    time_per_word = bpy.props.FloatProperty(
        name="Time Per Word",
        default=0.3,
        min=0.01,
        description="Time to display each word",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Total animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Text Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "time_per_word")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimDrawBorderThenFillNode(Node, ManimNode):
    bl_idname = 'ManimDrawBorderThenFillNodeType'
    bl_label = 'Draw Border Then Fill'
    bl_icon = 'STROKE'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Total animation duration",
    )
    
    stroke_width = bpy.props.FloatProperty(
        name="Stroke Width",
        default=4.0,
        min=0.1,
        description="Width of the border stroke",
    )
    
    stroke_color = bpy.props.FloatVectorProperty(
        name="Stroke Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the border stroke",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "stroke_width")
        layout.prop(self, "stroke_color")
    
    def draw_label(self):
        return self.bl_label

class ManimUncreateNode(Node, ManimNode):
    bl_idname = 'ManimUncreateNodeType'
    bl_label = 'Uncreate'
    bl_icon = 'X'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimShowIncreasingSubsetsNode(Node, ManimNode):
    bl_idname = 'ManimShowIncreasingSubsetsNodeType'
    bl_label = 'Show Increasing Subsets'
    bl_icon = 'SORTSIZE'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    suspend_mobject_updating = bpy.props.BoolProperty(
        name="Suspend Updating",
        default=True,
        description="Suspend updating for better performance",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Group Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "suspend_mobject_updating")
    
    def draw_label(self):
        return self.bl_label

class ManimWriteNode(Node, ManimNode):
    bl_idname = 'ManimWriteNodeType'
    bl_label = 'Write'
    bl_icon = 'OUTLINER_DATA_FONT'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    lag_ratio = bpy.props.FloatProperty(
        name="Lag Ratio",
        default=0.05,
        min=0.0,
        max=1.0,
        description="Lag between components",
    )
    
    rate_func = bpy.props.EnumProperty(
        name="Rate Function",
        items=[
            ('LINEAR', "Linear", "Linear rate function"),
            ('SMOOTH', "Smooth", "Smooth rate function"),
            ('RUSH_INTO', "Rush Into", "Speed up at the beginning"),
            ('RUSH_FROM', "Rush From", "Speed up at the end"),
        ],
        default='SMOOTH',
        description="How the animation progresses over time",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Text Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "lag_ratio")
        layout.prop(self, "rate_func")
    
    def draw_label(self):
        return self.bl_label

# Animation Fading Nodes
class ManimFadeToColorNode(Node, ManimNode):
    bl_idname = 'ManimFadeToColorNodeType'
    bl_label = 'Fade To Color'
    bl_icon = 'COLOR'
    
    target_color = bpy.props.FloatVectorProperty(
        name="Target Color",
        subtype='COLOR',
        default=(1.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Target color to fade to",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "target_color")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimFadeTransformNode(Node, ManimNode):
    bl_idname = 'ManimFadeTransformNodeType'
    bl_label = 'Fade Transform'
    bl_icon = 'MOD_MASK'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.5,
        min=0.1,
        description="Animation duration",
    )
    
    shift = bpy.props.BoolProperty(
        name="Shift",
        default=True,
        description="Whether to shift during transform",
    )
    
    stretch = bpy.props.BoolProperty(
        name="Stretch",
        default=False,
        description="Whether to stretch during transform",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "From Mobject")
        self.inputs.new('ManimNodeSocket', "To Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "shift")
        layout.prop(self, "stretch")
    
    def draw_label(self):
        return self.bl_label

class ManimFadeTransformPiecesNode(Node, ManimNode):
    bl_idname = 'ManimFadeTransformPiecesNodeType'
    bl_label = 'Fade Transform Pieces'
    bl_icon = 'MOD_MESHDEFORM'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.5,
        min=0.1,
        description="Animation duration",
    )
    
    lag_ratio = bpy.props.FloatProperty(
        name="Lag Ratio",
        default=0.1,
        min=0.0,
        max=1.0,
        description="Lag between pieces",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "From VMobject")
        self.inputs.new('ManimNodeSocket', "To VMobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "lag_ratio")
    
    def draw_label(self):
        return self.bl_label

# Animation Growing Nodes
class ManimGrowArrowNode(Node, ManimNode):
    bl_idname = 'ManimGrowArrowNodeType'
    bl_label = 'Grow Arrow'
    bl_icon = 'FORWARD'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Arrow")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimGrowFromCenterNode(Node, ManimNode):
    bl_idname = 'ManimGrowFromCenterNodeType'
    bl_label = 'Grow From Center'
    bl_icon = 'FULLSCREEN_ENTER'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    point_color = bpy.props.FloatVectorProperty(
        name="Point Color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the starting point",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "point_color")
    
    def draw_label(self):
        return self.bl_label

class ManimGrowFromPointNode(Node, ManimNode):
    bl_idname = 'ManimGrowFromPointNodeType'
    bl_label = 'Grow From Point'
    bl_icon = 'FULLSCREEN_ENTER'
    
    point = bpy.props.FloatVectorProperty(
        name="Point",
        subtype='XYZ',
        default=(0.0, 0.0, 0.0),
        size=3,
        description="Point to grow from",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "point")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimSpinInFromNothingNode(Node, ManimNode):
    bl_idname = 'ManimSpinInFromNothingNodeType'
    bl_label = 'Spin In From Nothing'
    bl_icon = 'MOD_SCREW'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Animation Indication Nodes
class ManimApplyWaveNode(Node, ManimNode):
    bl_idname = 'ManimApplyWaveNodeType'
    bl_label = 'Apply Wave'
    bl_icon = 'MOD_WAVE'
    
    direction = bpy.props.FloatVectorProperty(
        name="Direction",
        subtype='XYZ',
        default=(0.0, 1.0, 0.0),
        size=3,
        description="Direction of the wave",
    )
    
    amplitude = bpy.props.FloatProperty(
        name="Amplitude",
        default=0.2,
        description="Amplitude of the wave",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "direction")
        layout.prop(self, "amplitude")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimCircumscribeNode(Node, ManimNode):
    bl_idname = 'ManimCircumscribeNodeType'
    bl_label = 'Circumscribe'
    bl_icon = 'MESH_CIRCLE'
    
    shape = bpy.props.EnumProperty(
        name="Shape",
        items=[
            ('CIRCLE', "Circle", "Circular shape"),
            ('RECTANGLE', "Rectangle", "Rectangular shape"),
        ],
        default='CIRCLE',
        description="Shape to circumscribe with",
    )
    
    color = bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the shape",
    )
    
    fade_in = bpy.props.BoolProperty(
        name="Fade In",
        default=True,
        description="Whether to fade in the shape",
    )
    
    fade_out = bpy.props.BoolProperty(
        name="Fade Out",
        default=True,
        description="Whether to fade out the shape",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "shape")
        layout.prop(self, "color")
        layout.prop(self, "fade_in")
        layout.prop(self, "fade_out")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimFlashNode(Node, ManimNode):
    bl_idname = 'ManimFlashNodeType'
    bl_label = 'Flash'
    bl_icon = 'LIGHT_SUN'
    
    color = bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the flash",
    )
    
    line_length = bpy.props.FloatProperty(
        name="Line Length",
        default=0.5,
        min=0.0,
        description="Length of the flash lines",
    )
    
    num_lines = bpy.props.IntProperty(
        name="Number of Lines",
        default=12,
        min=4,
        description="Number of lines in the flash",
    )
    
    flash_radius = bpy.props.FloatProperty(
        name="Flash Radius",
        default=0.3,
        min=0.0,
        description="Radius of the flash",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Point")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "line_length")
        layout.prop(self, "num_lines")
        layout.prop(self, "flash_radius")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimFocusOnNode(Node, ManimNode):
    bl_idname = 'ManimFocusOnNodeType'
    bl_label = 'Focus On'
    bl_icon = 'ZOOM_IN'
    
    color = bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the focus circle",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Point")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimIndicateNode(Node, ManimNode):
    bl_idname = 'ManimIndicateNodeType'
    bl_label = 'Indicate'
    # bl_icon = 'HARDPAINT'
    
    color = bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the indication",
    )
    
    scale_factor = bpy.props.FloatProperty(
        name="Scale Factor",
        default=1.2,
        min=1.0,
        description="How much to scale by",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=0.5,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "color")
        layout.prop(self, "scale_factor")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimShowPassingFlashNode(Node, ManimNode):
    bl_idname = 'ManimShowPassingFlashNodeType'
    bl_label = 'Show Passing Flash'
    bl_icon = 'FORCE_CURVE'
    
    time_width = bpy.props.FloatProperty(
        name="Time Width",
        default=0.1,
        min=0.01,
        description="Width of the flash in time",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "VMobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "time_width")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimWiggleNode(Node, ManimNode):
    bl_idname = 'ManimWiggleNodeType'
    bl_label = 'Wiggle'
    bl_icon = 'MOD_NOISE'
    
    scale_value = bpy.props.FloatProperty(
        name="Scale Value",
        default=1.2,
        min=1.0,
        description="How much to scale by",
    )
    
    rotation_angle = bpy.props.FloatProperty(
        name="Rotation Angle",
        default=0.05,
        description="How much to rotate by (radians)",
    )
    
    n_wiggles = bpy.props.IntProperty(
        name="Number of Wiggles",
        default=6,
        min=1,
        description="Number of wiggles",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Target Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "scale_value")
        layout.prop(self, "rotation_angle")
        layout.prop(self, "n_wiggles")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Animation Movement Nodes
class ManimMoveAlongPathNode(Node, ManimNode):
    bl_idname = 'ManimMoveAlongPathNodeType'
    bl_label = 'Move Along Path'
    bl_icon = 'CURVE_PATH'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=3.0,
        min=0.1,
        description="Animation duration",
    )
    
    loop = bpy.props.BoolProperty(
        name="Loop",
        default=False,
        description="Whether to loop the movement",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.inputs.new('ManimNodeSocket', "Path")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "loop")
    
    def draw_label(self):
        return self.bl_label

class ManimHomotopyNode(Node, ManimNode):
    bl_idname = 'ManimHomotopyNodeType'
    bl_label = 'Homotopy'
    bl_icon = 'MOD_WARP'
    
    function_text = bpy.props.StringProperty(
        name="Homotopy Function",
        default="lambda x, y, z, t: (x, y, z)",
        description="Function (x,y,z,t) -> (x',y',z')",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=3.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimComplexHomotopyNode(Node, ManimNode):
    bl_idname = 'ManimComplexHomotopyNodeType'
    bl_label = 'Complex Homotopy'
    bl_icon = 'MOD_WARP'
    
    function_text = bpy.props.StringProperty(
        name="Complex Function",
        default="lambda z, t: z",
        description="Function (z,t) -> z'",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=3.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimPhaseFlowNode(Node, ManimNode):
    bl_idname = 'ManimPhaseFlowNodeType'
    bl_label = 'Phase Flow'
    bl_icon = 'FORCE_VORTEX'
    
    function_text = bpy.props.StringProperty(
        name="Vector Field Function",
        default="lambda p, t: p + 0.1",
        description="Function (point,t) -> vector",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Animation Numbers Nodes
class ManimChangingDecimalNode(Node, ManimNode):
    bl_idname = 'ManimChangingDecimalNodeType'
    bl_label = 'Changing Decimal'
    bl_icon = 'SETTINGS'
    
    function_text = bpy.props.StringProperty(
        name="Number Function",
        default="lambda t: t",
        description="Function t -> number",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "DecimalNumber")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimChangeDecimalToValueNode(Node, ManimNode):
    bl_idname = 'ManimChangeDecimalToValueNodeType'
    bl_label = 'Change Decimal To Value'
    bl_icon = 'SETTINGS'
    
    target_value = bpy.props.FloatProperty(
        name="Target Value",
        default=10.0,
        description="Target value to change to",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "DecimalNumber")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "target_value")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Animation Rotation Nodes
class ManimRotatingNode(Node, ManimNode):
    bl_idname = 'ManimRotatingNodeType'
    bl_label = 'Rotating'
    bl_icon = 'FORCE_VORTEX'
    
    axis = bpy.props.FloatVectorProperty(
        name="Axis",
        subtype='XYZ',
        default=(0.0, 0.0, 1.0),
        size=3,
        description="Axis of rotation",
    )
    
    radians = bpy.props.FloatProperty(
        name="Radians",
        default=3.14159,
        description="Angle of rotation in radians",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=2.0,
        min=0.1,
        description="Animation duration",
    )
    
    rate_func = bpy.props.EnumProperty(
        name="Rate Function",
        items=[
            ('LINEAR', "Linear", "Linear rate function"),
            ('SMOOTH', "Smooth", "Smooth rate function"),
            ('RUSH_INTO', "Rush Into", "Speed up at the beginning"),
            ('RUSH_FROM', "Rush From", "Speed up at the end"),
        ],
        default='LINEAR',
        description="How the animation progresses over time",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "axis")
        layout.prop(self, "radians")
        layout.prop(self, "run_time")
        layout.prop(self, "rate_func")
    
    def draw_label(self):
        return self.bl_label

# Animation Specialized Nodes
class ManimBroadcastNode(Node, ManimNode):
    bl_idname = 'ManimBroadcastNodeType'
    bl_label = 'Broadcast'
    bl_icon = 'RADIOBUT_ON'
    
    focal_point = bpy.props.FloatVectorProperty(
        name="Focal Point",
        subtype='XYZ',
        default=(0.0, 0.0, 0.0),
        size=3,
        description="Focal point of the broadcast",
    )
    
    n_circles = bpy.props.IntProperty(
        name="Number of Circles",
        default=5,
        min=1,
        description="Number of circles in the broadcast",
    )
    
    initial_radius = bpy.props.FloatProperty(
        name="Initial Radius",
        default=0.1,
        min=0.0,
        description="Initial radius of the broadcast",
    )
    
    stroke_width = bpy.props.FloatProperty(
        name="Stroke Width",
        default=2.0,
        min=0.0,
        description="Stroke width of the circles",
    )
    
    color = bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        description="Color of the circles",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=3.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Scene")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "focal_point")
        layout.prop(self, "n_circles")
        layout.prop(self, "initial_radius")
        layout.prop(self, "stroke_width")
        layout.prop(self, "color")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

# Additional Transform Nodes
class ManimApplyFunctionNode(Node, ManimNode):
    bl_idname = 'ManimApplyFunctionNodeType'
    bl_label = 'Apply Function'
    bl_icon = 'DRIVER'
    
    function_text = bpy.props.StringProperty(
        name="Function",
        default="lambda p: p + 0.2*UP",
        description="Function to apply to points",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "function_text")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimApplyMatrixNode(Node, ManimNode):
    bl_idname = 'ManimApplyMatrixNodeType'
    bl_label = 'Apply Matrix'
    bl_icon = 'OUTLINER_DATA_LATTICE'
    
    matrix_text = bpy.props.StringProperty(
        name="Matrix",
        default="[[1, 0.5], [0, 1]]",
        description="Matrix to apply (as a Python list)",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "matrix_text")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimScaleInPlaceNode(Node, ManimNode):
    bl_idname = 'ManimScaleInPlaceNodeType'
    bl_label = 'Scale In Place'
    bl_icon = 'ARROW_LEFTRIGHT'
    
    scale_factor = bpy.props.FloatProperty(
        name="Scale Factor",
        default=1.5,
        min=0.01,
        description="Factor to scale by",
    )
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "scale_factor")
        layout.prop(self, "run_time")
    
    def draw_label(self):
        return self.bl_label

class ManimReplacementTransformNode(Node, ManimNode):
    bl_idname = 'ManimReplacementTransformNodeType'
    bl_label = 'Replacement Transform'
    bl_icon = 'MOD_INSTANCE'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    replace_mobject = bpy.props.BoolProperty(
        name="Replace Mobject",
        default=True,
        description="Whether to replace the mobject in the scene",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject From")
        self.inputs.new('ManimNodeSocket', "Mobject To")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.prop(self, "replace_mobject")
    
    def draw_label(self):
        return self.bl_label

class ManimCyclicReplaceNode(Node, ManimNode):
    bl_idname = 'ManimCyclicReplaceNodeType'
    bl_label = 'Cyclic Replace'
    bl_icon = 'FILE_REFRESH'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject 1")
        self.inputs.new('ManimNodeSocket', "Mobject 2")
        self.inputs.new('ManimNodeSocket', "Mobject 3")
        self.outputs.new('ManimNodeSocket', "Animation")
        
        # Add button for adding more mobject inputs
        self.use_custom_color = True
        self.color = (0.3, 0.5, 0.7)
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        
        # Add button to add more mobject inputs
        row = layout.row()
        op = row.operator("node.manim_add_mobject_input", text="Add Mobject Input")
        op.node_name = self.name
    
    def draw_label(self):
        return self.bl_label

class ManimMoveToTargetNode(Node, ManimNode):
    bl_idname = 'ManimMoveToTargetNodeType'
    bl_label = 'Move To Target'
    bl_icon = 'TRACKER'
    
    run_time = bpy.props.FloatProperty(
        name="Run Time",
        default=1.0,
        min=0.1,
        description="Animation duration",
    )
    
    def init(self, context):
        self.inputs.new('ManimNodeSocket', "Mobject")
        self.outputs.new('ManimNodeSocket', "Animation")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "run_time")
        layout.label(text="Mobject must have .target set")
    
    def draw_label(self):
        return self.bl_label


node_classes = [
    ManimMoveAlongPathNode,
    ManimHomotopyNode,
    ManimComplexHomotopyNode,
    ManimPhaseFlowNode,
    ManimChangingDecimalNode,
    ManimChangeDecimalToValueNode,
    ManimBroadcastNode,
    ManimApplyFunctionNode,
    ManimApplyMatrixNode,
    ManimScaleInPlaceNode,
    ManimReplacementTransformNode,
    ManimCyclicReplaceNode,
    ManimMoveToTargetNode,
    ManimFadeInNode,
    ManimTransformNode,
    ManimCreateNode,
    ManimRotateNode,
    ManimAnimationGroupNode,
    ManimLaggedStartNode,
    ManimLaggedStartMapNode,
    ManimSuccessionNode,
    ManimAddTextLetterByLetterNode,
    ManimAddTextWordByWordNode,
    ManimUncreateNode,
    ManimFadeToColorNode,
    ManimGrowArrowNode,
    ManimGrowFromPointNode,
    ManimSpinInFromNothingNode,
    ManimApplyWaveNode,
    ManimCircumscribeNode,
    ManimFlashNode,
    ManimFocusOnNode,
    ManimIndicateNode,
    ManimShowPassingFlashNode,
    ManimWiggleNode,
]