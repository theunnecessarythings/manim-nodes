import bpy
from bpy.types import NodeTree, NodeSocket, Menu
from bpy.props import FloatProperty, StringProperty, BoolProperty
from .sockets import ManimNodeSocket, ManimSequenceSocket, ManimAnimationSocket, ManimObjectSocket
from .compiler import NODE_OT_compile_nodetree

class ManimNodeTree(NodeTree):
    '''Manim node editor for creating mathematical animations'''
    bl_idname = 'ManimNodeTree'
    bl_label = 'Manim Node Editor'
    bl_icon = 'NODETREE'
    
    def update(self):
        bpy.app.timers.register(self._validate_links)

    def _validate_links(self):
        for link in list(self.links):
            from_sock = link.from_socket
            to_sock   = link.to_socket

            if type(from_sock) is not type(to_sock):
                link.is_valid = False
                # remove the link
                self.links.remove(link)
        return None

class MANIM_MT_sequence_menu(Menu):
    bl_idname = "MANIM_MT_sequence_menu"
    bl_label = "Sequence"
    
    def draw(self, context):
        if self.layout is None:
            return
        layout = self.layout
        op = layout.operator("node.add_node", text="Start Sequence")
        op.type = "ManimStartSequenceNodeType"
        op = layout.operator("node.add_node", text="End Sequence")
        op.type = "ManimEndSequenceNodeType"
        op = layout.operator("node.add_node", text="Add To Sequence")
        op.type = "ManimAddNodeType"
        op = layout.operator("node.add_node", text="Play Sequence")
        op.type = "ManimPlayNodeType"
        op = layout.operator("node.add_node", text="Wait Sequence")
        op.type = "ManimWaitNodeType"
       
class MANIM_MT_animation_menu(Menu):
    bl_idname = "MANIM_MT_animation_menu"
    bl_label = "Animations"
    
    def draw(self, context):
        if self.layout is None:
            return
        layout = self.layout
        layout.menu("MANIM_MT_animation_animation_menu", text="Animation")
        layout.menu("MANIM_MT_animation_changing_menu", text="Changing")
        layout.menu("MANIM_MT_animation_composition_menu", text="Composition")
        layout.menu("MANIM_MT_animation_creation_menu", text="Creation")
        layout.menu("MANIM_MT_animation_fading_menu", text="Fading")
        layout.menu("MANIM_MT_animation_growing_menu", text="Growing")
        layout.menu("MANIM_MT_animation_indication_menu", text="Indication")
        layout.menu("MANIM_MT_animation_movement_menu", text="Movement")
        layout.menu("MANIM_MT_animation_numbers_menu", text="Numbers")
        layout.menu("MANIM_MT_animation_rotation_menu", text="Rotation")
        layout.menu("MANIM_MT_animation_specialized_menu", text="Specialized")
        layout.menu("MANIM_MT_animation_speedmodifier_menu", text="Speed Modifier")
        layout.menu("MANIM_MT_animation_transform_menu", text="Transform")
        layout.menu("MANIM_MT_animation_transform_matching_parts_menu", text="Transform Matching Parts")
        layout.menu("MANIM_MT_animation_updaters_menu", text="Updaters")

# Animation submenu classes
class MANIM_MT_animation_animation_menu(Menu):
    bl_idname = "MANIM_MT_animation_animation_menu"
    bl_label = "Animation"
    
    def draw(self, context):
        if self.layout is None:
            return
        layout = self.layout
        props = layout.operator("node.add_node", text="Wait")
        props.type = "ManimWaitNodeType"
        props.use_transform = True

class MANIM_MT_animation_changing_menu(Menu):
    bl_idname = "MANIM_MT_animation_changing_menu"
    bl_label = "Changing"
    
    def draw(self, context):
        if self.layout is None:
            return
        layout = self.layout
        props = layout.operator("node.add_node", text="Animated Boundary")
        props.type = "ManimAnimatedBoundaryNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Traced Path")
        props.type = "ManimTracedPathNodeType"
        props.use_transform = True

class MANIM_MT_animation_composition_menu(Menu):
    bl_idname = "MANIM_MT_animation_composition_menu"
    bl_label = "Composition"
    
    def draw(self, context):
        if self.layout is None:
            return
        layout = self.layout
        props = layout.operator("node.add_node", text="Animation Group")
        props.type = "ManimAnimationGroupNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Lagged Start")
        props.type = "ManimLaggedStartNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Lagged Start Map")
        props.type = "ManimLaggedStartMapNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Succession")
        props.type = "ManimSuccessionNodeType"
        props.use_transform = True

class MANIM_MT_animation_creation_menu(Menu):
    bl_idname = "MANIM_MT_animation_creation_menu"
    bl_label = "Creation"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Create")
        props.type = "ManimCreateNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Add Text Letter By Letter")
        props.type = "ManimAddTextLetterByLetterNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Add Text Word By Word")
        props.type = "ManimAddTextWordByWordNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Draw Border Then Fill")
        props.type = "ManimDrawBorderThenFillNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Show Increasing Subsets")
        props.type = "ManimShowIncreasingSubsetsNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Uncreate")
        props.type = "ManimUncreateNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Write")
        props.type = "ManimWriteNodeType"
        props.use_transform = True

class MANIM_MT_animation_fading_menu(Menu):
    bl_idname = "MANIM_MT_animation_fading_menu"
    bl_label = "Fading"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Fade In")
        props.type = "ManimFadeInNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Fade Out")
        props.type = "ManimFadeOutNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Fade To Color")
        props.type = "ManimFadeToColorNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Fade Transform")
        props.type = "ManimFadeTransformNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Fade Transform Pieces")
        props.type = "ManimFadeTransformPiecesNodeType"
        props.use_transform = True

class MANIM_MT_animation_growing_menu(Menu):
    bl_idname = "MANIM_MT_animation_growing_menu"
    bl_label = "Growing"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Grow Arrow")
        props.type = "ManimGrowArrowNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Grow From Center")
        props.type = "ManimGrowFromCenterNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Grow From Point")
        props.type = "ManimGrowFromPointNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Spin In From Nothing")
        props.type = "ManimSpinInFromNothingNodeType"
        props.use_transform = True

class MANIM_MT_animation_indication_menu(Menu):
    bl_idname = "MANIM_MT_animation_indication_menu"
    bl_label = "Indication"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Apply Wave")
        props.type = "ManimApplyWaveNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Circumscribe")
        props.type = "ManimCircumscribeNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Flash")
        props.type = "ManimFlashNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Focus On")
        props.type = "ManimFocusOnNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Indicate")
        props.type = "ManimIndicateNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Show Passing Flash")
        props.type = "ManimShowPassingFlashNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Wiggle")
        props.type = "ManimWiggleNodeType"
        props.use_transform = True

class MANIM_MT_animation_movement_menu(Menu):
    bl_idname = "MANIM_MT_animation_movement_menu"
    bl_label = "Movement"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Move Along Path")
        props.type = "ManimMoveAlongPathNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Homotopy")
        props.type = "ManimHomotopyNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Complex Homotopy")
        props.type = "ManimComplexHomotopyNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Phase Flow")
        props.type = "ManimPhaseFlowNodeType"
        props.use_transform = True

class MANIM_MT_animation_numbers_menu(Menu):
    bl_idname = "MANIM_MT_animation_numbers_menu"
    bl_label = "Numbers"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Changing Decimal")
        props.type = "ManimChangingDecimalNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Change Decimal To Value")
        props.type = "ManimChangeDecimalToValueNodeType"
        props.use_transform = True

class MANIM_MT_animation_rotation_menu(Menu):
    bl_idname = "MANIM_MT_animation_rotation_menu"
    bl_label = "Rotation"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Rotate")
        props.type = "ManimRotateNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Rotating")
        props.type = "ManimRotatingNodeType"
        props.use_transform = True

class MANIM_MT_animation_specialized_menu(Menu):
    bl_idname = "MANIM_MT_animation_specialized_menu"
    bl_label = "Specialized"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Broadcast")
        props.type = "ManimBroadcastNodeType"
        props.use_transform = True

class MANIM_MT_animation_speedmodifier_menu(Menu):
    bl_idname = "MANIM_MT_animation_speedmodifier_menu"
    bl_label = "Speed Modifier"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_animation_transform_menu(Menu):
    bl_idname = "MANIM_MT_animation_transform_menu"
    bl_label = "Transform"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Transform")
        props.type = "ManimTransformNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Apply Function")
        props.type = "ManimApplyFunctionNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Apply Matrix")
        props.type = "ManimApplyMatrixNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Cyclic Replace")
        props.type = "ManimCyclicReplaceNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Move To Target")
        props.type = "ManimMoveToTargetNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Replacement Transform")
        props.type = "ManimReplacementTransformNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Scale In Place")
        props.type = "ManimScaleInPlaceNodeType"
        props.use_transform = True

class MANIM_MT_animation_transform_matching_parts_menu(Menu):
    bl_idname = "MANIM_MT_animation_transform_matching_parts_menu"
    bl_label = "Transform Matching Parts"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_animation_updaters_menu(Menu):
    bl_idname = "MANIM_MT_animation_updaters_menu"
    bl_label = "Updaters"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

# 2. Camera Menu Structure
class MANIM_MT_camera_menu(Menu):
    bl_idname = "MANIM_MT_camera_menu"
    bl_label = "Cameras"
    
    def draw(self, context):
        layout = self.layout
        layout.menu("MANIM_MT_camera_camera_menu", text="Camera")
        layout.menu("MANIM_MT_camera_mapping_camera_menu", text="Mapping Camera")
        layout.menu("MANIM_MT_camera_moving_camera_menu", text="Moving Camera")
        layout.menu("MANIM_MT_camera_multi_camera_menu", text="Multi Camera")
        layout.menu("MANIM_MT_camera_three_d_camera_menu", text="3D Camera")

# Camera submenu classes
class MANIM_MT_camera_camera_menu(Menu):
    bl_idname = "MANIM_MT_camera_camera_menu"
    bl_label = "Camera"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Camera")
        props.type = "ManimCameraNodeType"
        props.use_transform = True

class MANIM_MT_camera_mapping_camera_menu(Menu):
    bl_idname = "MANIM_MT_camera_mapping_camera_menu"
    bl_label = "Mapping Camera"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_camera_moving_camera_menu(Menu):
    bl_idname = "MANIM_MT_camera_moving_camera_menu"
    bl_label = "Moving Camera"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Moving Camera")
        props.type = "ManimMovingCameraNodeType"
        props.use_transform = True

class MANIM_MT_camera_multi_camera_menu(Menu):
    bl_idname = "MANIM_MT_camera_multi_camera_menu"
    bl_label = "Multi Camera"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_camera_three_d_camera_menu(Menu):
    bl_idname = "MANIM_MT_camera_three_d_camera_menu"
    bl_label = "3D Camera"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="3D Camera")
        props.type = "ManimThreeDCameraNodeType"
        props.use_transform = True

# 3. Objects Menu Structure
class MANIM_MT_object_menu(Menu):
    bl_idname = "MANIM_MT_object_menu"
    bl_label = "Objects"
    
    def draw(self, context):
        layout = self.layout
        layout.menu("MANIM_MT_object_frame_menu", text="Frame")
        layout.menu("MANIM_MT_object_geometry_menu", text="Geometry")
        layout.menu("MANIM_MT_object_graph_menu", text="Graph")
        layout.menu("MANIM_MT_object_graphing_menu", text="Graphing")
        layout.menu("MANIM_MT_object_logo_menu", text="Logo")
        layout.menu("MANIM_MT_object_matrix_menu", text="Matrix")
        layout.menu("MANIM_MT_object_mobject_menu", text="Mobject")
        layout.menu("MANIM_MT_object_svg_menu", text="SVG")
        layout.menu("MANIM_MT_object_table_menu", text="Table")
        layout.menu("MANIM_MT_object_text_menu", text="Text")
        layout.menu("MANIM_MT_object_three_d_menu", text="3D")
        layout.menu("MANIM_MT_object_types_menu", text="Types")
        layout.menu("MANIM_MT_object_utils_menu", text="Utils")
        layout.menu("MANIM_MT_object_value_tracker_menu", text="Value Tracker")
        layout.menu("MANIM_MT_object_vector_field_menu", text="Vector Field")

# Object submenu classes
class MANIM_MT_object_frame_menu(Menu):
    bl_idname = "MANIM_MT_object_frame_menu"
    bl_label = "Frame"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_geometry_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_menu"
    bl_label = "Geometry"
    
    def draw(self, context):
        layout = self.layout
        
        layout.menu("MANIM_MT_object_geometry_arc_menu", text="Arc")
        layout.menu("MANIM_MT_object_geometry_boolean_ops_menu", text="Boolean Operations")
        layout.menu("MANIM_MT_object_geometry_circle_menu", text="Circle")
        layout.menu("MANIM_MT_object_geometry_labeled_menu", text="Labeled")
        layout.menu("MANIM_MT_object_geometry_line_menu", text="Line")
        layout.menu("MANIM_MT_object_geometry_polygram_menu", text="Polygram")
        layout.menu("MANIM_MT_object_geometry_shape_matchers_menu", text="Shape Matchers")
        layout.menu("MANIM_MT_object_geometry_tips_menu", text="Tips")

# Geometry submenu classes
class MANIM_MT_object_geometry_arc_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_arc_menu"
    bl_label = "Arc"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Arc")
        props.type = "ManimArcNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_boolean_ops_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_boolean_ops_menu"
    bl_label = "Boolean Operations"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Boolean Operations")
        props.type = "ManimBooleanOpsNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_circle_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_circle_menu"
    bl_label = "Circle"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Circle")
        props.type = "ManimCircleNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Ellipse")
        props.type = "ManimEllipseNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Dot")
        props.type = "ManimDotNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_labeled_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_labeled_menu"
    bl_label = "Labeled"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Labeled")
        props.type = "ManimLabeledNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_line_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_line_menu"
    bl_label = "Line"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Line")
        props.type = "ManimLineNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_polygram_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_polygram_menu"
    bl_label = "Polygram"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Polygram")
        props.type = "ManimPolygramNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Rectangle")
        props.type = "ManimRectangleNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Square")
        props.type = "ManimSquareNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Triangle")
        props.type = "ManimTriangleNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Star")
        props.type = "ManimStarNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Regular Polygon")
        props.type = "ManimRegularPolygonNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_shape_matchers_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_shape_matchers_menu"
    bl_label = "Shape Matchers"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Shape Matchers")
        props.type = "ManimShapeMatchersNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Surrounding Rectangle")
        props.type = "ManimSurroundingRectangleNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Underline")
        props.type = "ManimUnderlineNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Cross")
        props.type = "ManimCrossNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Background Rectangle")
        props.type = "ManimBackgroundRectangleNodeType"
        props.use_transform = True

class MANIM_MT_object_geometry_tips_menu(Menu):
    bl_idname = "MANIM_MT_object_geometry_tips_menu"
    bl_label = "Tips"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Tips")
        props.type = "ManimTipsNodeType"
        props.use_transform = True

class MANIM_MT_object_graph_menu(Menu):
    bl_idname = "MANIM_MT_object_graph_menu"
    bl_label = "Graph"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_graphing_menu(Menu):
    bl_idname = "MANIM_MT_object_graphing_menu"
    bl_label = "Graphing"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Axes")
        props.type = "ManimAxesNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Number Plane")
        props.type = "ManimNumberPlaneNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Function Graph")
        props.type = "ManimFunctionGraphNodeType"
        props.use_transform = True

class MANIM_MT_object_logo_menu(Menu):
    bl_idname = "MANIM_MT_object_logo_menu"
    bl_label = "Logo"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_matrix_menu(Menu):
    bl_idname = "MANIM_MT_object_matrix_menu"
    bl_label = "Matrix"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_mobject_menu(Menu):
    bl_idname = "MANIM_MT_object_mobject_menu"
    bl_label = "Mobject"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_svg_menu(Menu):
    bl_idname = "MANIM_MT_object_svg_menu"
    bl_label = "SVG"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_table_menu(Menu):
    bl_idname = "MANIM_MT_object_table_menu"
    bl_label = "Table"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_text_menu(Menu):
    bl_idname = "MANIM_MT_object_text_menu"
    bl_label = "Text"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Text")
        props.type = "ManimTextNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="MathTex")
        props.type = "ManimMathTexNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Paragraph")
        props.type = "ManimParagraphNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Markup Text")
        props.type = "ManimMarkupTextNodeType"
        props.use_transform = True

class MANIM_MT_object_three_d_menu(Menu):
    bl_idname = "MANIM_MT_object_three_d_menu"
    bl_label = "3D"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="3D Axes")
        props.type = "Manim3DAxesNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Surface")
        props.type = "ManimSurfaceNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Sphere")
        props.type = "ManimSphereNodeType"
        props.use_transform = True

class MANIM_MT_object_types_menu(Menu):
    bl_idname = "MANIM_MT_object_types_menu"
    bl_label = "Types"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_utils_menu(Menu):
    bl_idname = "MANIM_MT_object_utils_menu"
    bl_label = "Utils"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_object_value_tracker_menu(Menu):
    bl_idname = "MANIM_MT_object_value_tracker_menu"
    bl_label = "Value Tracker"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Value Tracker")
        props.type = "ManimValueTrackerNodeType"
        props.use_transform = True
        
        props = layout.operator("node.add_node", text="Complex Value Tracker")
        props.type = "ManimComplexValueTrackerNodeType"
        props.use_transform = True

class MANIM_MT_object_vector_field_menu(Menu):
    bl_idname = "MANIM_MT_object_vector_field_menu"
    bl_label = "Vector Field"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

# 4. Scene Menu Structure
class MANIM_MT_scene_menu(Menu):
    bl_idname = "MANIM_MT_scene_menu"
    bl_label = "Scenes"
    
    def draw(self, context):
        layout = self.layout
        layout.menu("MANIM_MT_scene_moving_camera_scene_menu", text="Moving Camera Scene")
        layout.menu("MANIM_MT_scene_section_menu", text="Section")
        layout.menu("MANIM_MT_scene_scene_menu", text="Scene")
        layout.menu("MANIM_MT_scene_scene_file_writer_menu", text="Scene File Writer")
        layout.menu("MANIM_MT_scene_three_d_scene_menu", text="3D Scene")
        layout.menu("MANIM_MT_scene_vector_space_scene_menu", text="Vector Space Scene")
        layout.menu("MANIM_MT_scene_zoomed_scene_menu", text="Zoomed Scene")

# Scene submenu classes
class MANIM_MT_scene_moving_camera_scene_menu(Menu):
    bl_idname = "MANIM_MT_scene_moving_camera_scene_menu"
    bl_label = "Moving Camera Scene"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_scene_section_menu(Menu):
    bl_idname = "MANIM_MT_scene_section_menu"
    bl_label = "Section"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_scene_scene_menu(Menu):
    bl_idname = "MANIM_MT_scene_scene_menu"
    bl_label = "Scene"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Scene")
        props.type = "ManimSceneNodeType"
        props.use_transform = True

class MANIM_MT_scene_scene_file_writer_menu(Menu):
    bl_idname = "MANIM_MT_scene_scene_file_writer_menu"
    bl_label = "Scene File Writer"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_scene_three_d_scene_menu(Menu):
    bl_idname = "MANIM_MT_scene_three_d_scene_menu"
    bl_label = "3D Scene"
    
    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="3D Scene")
        props.type = "Manim3DSceneNodeType"
        props.use_transform = True

class MANIM_MT_scene_vector_space_scene_menu(Menu):
    bl_idname = "MANIM_MT_scene_vector_space_scene_menu"
    bl_label = "Vector Space Scene"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

class MANIM_MT_scene_zoomed_scene_menu(Menu):
    bl_idname = "MANIM_MT_scene_zoomed_scene_menu"
    bl_label = "Zoomed Scene"
    
    def draw(self, context):
        layout = self.layout
        # Will be populated with nodes as they are created

# Registration
classes = (
    ManimNodeSocket,
    ManimSequenceSocket,
    ManimAnimationSocket,
    ManimObjectSocket,

    ManimNodeTree,

    NODE_OT_compile_nodetree,

    MANIM_MT_sequence_menu,
    
    # Animation menus
    MANIM_MT_animation_menu,
    MANIM_MT_animation_animation_menu,
    MANIM_MT_animation_changing_menu,
    MANIM_MT_animation_composition_menu,
    MANIM_MT_animation_creation_menu,
    MANIM_MT_animation_fading_menu,
    MANIM_MT_animation_growing_menu,
    MANIM_MT_animation_indication_menu,
    MANIM_MT_animation_movement_menu,
    MANIM_MT_animation_numbers_menu,
    MANIM_MT_animation_rotation_menu,
    MANIM_MT_animation_specialized_menu,
    MANIM_MT_animation_speedmodifier_menu,
    MANIM_MT_animation_transform_menu,
    MANIM_MT_animation_transform_matching_parts_menu,
    MANIM_MT_animation_updaters_menu,
    # Camera menus
    MANIM_MT_camera_menu,
    MANIM_MT_camera_camera_menu,
    MANIM_MT_camera_mapping_camera_menu,
    MANIM_MT_camera_moving_camera_menu,
    MANIM_MT_camera_multi_camera_menu,
    MANIM_MT_camera_three_d_camera_menu,
    # Object menus
    MANIM_MT_object_menu,
    MANIM_MT_object_frame_menu,
    MANIM_MT_object_geometry_menu,
    # Geometry submenus
    MANIM_MT_object_geometry_arc_menu,
    MANIM_MT_object_geometry_boolean_ops_menu,
    MANIM_MT_object_geometry_circle_menu,
    MANIM_MT_object_geometry_labeled_menu,
    MANIM_MT_object_geometry_line_menu,
    MANIM_MT_object_geometry_polygram_menu,
    MANIM_MT_object_geometry_shape_matchers_menu,
    MANIM_MT_object_geometry_tips_menu,
    MANIM_MT_object_graph_menu,
    MANIM_MT_object_graphing_menu,
    MANIM_MT_object_logo_menu,
    MANIM_MT_object_matrix_menu,
    MANIM_MT_object_mobject_menu,
    MANIM_MT_object_svg_menu,
    MANIM_MT_object_table_menu,
    MANIM_MT_object_text_menu,
    MANIM_MT_object_three_d_menu,
    MANIM_MT_object_types_menu,
    MANIM_MT_object_utils_menu,
    MANIM_MT_object_value_tracker_menu,
    MANIM_MT_object_vector_field_menu,
    # Scene menus
    MANIM_MT_scene_menu,
    MANIM_MT_scene_moving_camera_scene_menu,
    MANIM_MT_scene_section_menu,
    MANIM_MT_scene_scene_menu,
    MANIM_MT_scene_scene_file_writer_menu,
    MANIM_MT_scene_three_d_scene_menu,
    MANIM_MT_scene_vector_space_scene_menu,
    MANIM_MT_scene_zoomed_scene_menu,
)

def draw_compile_button(self, context):
    layout = self.layout
    space = context.space_data
    if getattr(space, 'tree_type', None) == 'ManimNodeTree':
        layout.operator('node.compile_nodetree', text='Compile Scene', icon='TEXT')


def register():
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except Exception as e:
            print(f"Error registering class {cls.__name__}: {e}")
    
    bpy.types.NODE_MT_add.append(add_manim_menu)
    bpy.types.NODE_HT_header.append(draw_compile_button)

def add_manim_menu(self, context):
    if context.space_data.tree_type == 'ManimNodeTree':
        layout = self.layout
        layout.menu("MANIM_MT_animation_menu")
        layout.menu("MANIM_MT_camera_menu")
        layout.menu("MANIM_MT_object_menu")
        layout.menu("MANIM_MT_scene_menu")
        layout.menu("MANIM_MT_sequence_menu")

def unregister():
    bpy.types.NODE_MT_add.remove(add_manim_menu)
    bpy.types.NODE_HT_header.remove(draw_compile_button)
    
    # Unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except Exception as e:
            print(f"Error unregistering class {cls.__name__}: {e}") 
