from bpy.types import NodeSocket
from bpy.props import FloatProperty

class ManimNodeSocket(NodeSocket):
    '''Custom node socket type for Manim'''
    bl_idname = 'ManimNodeSocket'
    bl_label = 'Manim Node Socket'
    
    value_prop: FloatProperty(default=0.0) # type: ignore
    
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "value_prop", text=text)
    
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 1.0)


class ManimAnimationSocket(NodeSocket):
    '''Animation Socket'''
    bl_idname = 'ManimAnimationSocket'
    bl_label = 'Manim Animation Socket'
    
    value_prop: FloatProperty(default=0.0) # type: ignore

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "value_prop", text=text)

    def draw_color(self, context, node):
        return (0.0, 0.0, 0.8, 1.0)


class ManimObjectSocket(NodeSocket):
    '''Object Socket'''
    bl_idname = 'ManimObjectSocket'
    bl_label = 'Manim Object Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 1.0)
    

class ManimSequenceSocket(NodeSocket):
    '''Sequence Socket'''
    bl_idname = 'ManimSequenceSocket'
    bl_label = 'Manim Sequence Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0.0, 0.8, 0.0, 1.0)
