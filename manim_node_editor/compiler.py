import bpy

def get_varname(name):
    return name.lower().replace(".", "_")

def compile_node(node: bpy.types.Node, var_map: dict, var_name: str, lines: list):
    """Compile a single node to Python code."""
    if node.bl_idname == 'ManimRectangleNodeType':
        inputs = [var_map.get(link.from_node.name) for inp in node.inputs for link in inp.links if inp.__class__.__name__ != 'ManimSequenceSocket']
        if inputs:
            rect = f"Rectangle({', '.join(inputs)})"
            var_map[var_name] = rect
            lines.append(f"        {var_name} = {rect}")
        else:
            lines.append(f"        {var_name} = Rectangle()")
    elif node.bl_idname == 'ManimAddNodeType':
        objects = node.inputs[1].links
        objects = [get_varname(inp.from_node.name) for inp in objects]
        lines.append(f"        self.add({', '.join(objects)})")
    elif node.bl_idname == 'ManimWaitNodeType':
        seconds = node.inputs[1].default_value
        lines.append(f"        self.wait({seconds})")


class NODE_OT_compile_nodetree(bpy.types.Operator):
    bl_idname = "node.compile_nodetree"
    bl_label = "Compile NodeTree to Python"
    bl_description = "Traverse current node tree and generate Manim Python code"
    
    def execute(self, context):
        tree = context.space_data.node_tree
        if not tree:
            self.report({'ERROR'}, "No node tree found")
            return {'CANCELLED'}

        # Helper: find the Start node
        start_nodes = [n for n in tree.nodes if n.bl_idname == 'ManimStartSequenceNodeType']
        if not start_nodes:
            self.report({'ERROR'}, "Start node not found")
            return {'CANCELLED'}
        start = start_nodes[0]

        # Traverse sequence: follow the first sequence socket link from each node
        sequence_path = []
        current = start
        while True:
            sequence_path.append(current)
            # find outgoing link on the sequence output socket
            seq_out = next((s for s in current.outputs if s.__class__.__name__ == 'ManimSequenceSocket'), None)
            if not seq_out or not seq_out.links:
                break
            next_link = seq_out.links[0]
            current = next_link.to_node
            if current.bl_idname == 'ManimEndSequenceNodeType':
                sequence_path.append(current)
                break
        print(f"Sequence path: {[n.bl_idname for n in sequence_path]}")

        lines = ["from manim import *", "", "class GeneratedScene(Scene):", "    def construct(self):"]
        var_map = {}
        counter = {}

        def collect_deps(node, deps, visited):
            # recursively collect non-sequence inputs
            if node in visited:
                return
            visited.add(node)
            for inp in node.inputs:
                # skip sequence socket
                print(f"Checking input: {inp.__class__.__name__}")
                if inp.__class__.__name__ == 'ManimSequenceSocket':
                    continue
                for link in inp.links:
                    src = link.from_node
                    collect_deps(src, deps, visited)
                    deps.append(src)

        for node in sequence_path:
            if node.bl_idname in ('ManimStartSequenceNodeType', 'ManimEndSequenceNodeType'):
                continue

            # gather and sort dependencies for this node
            deps = []
            collect_deps(node, deps, set())
            print(f"Dependencies for {node.bl_idname}: {[d.bl_idname for d in deps]}")
            # remove duplicates while preserving order
            seen = set()
            ordered_deps = [d for d in deps if not (d in seen or seen.add(d))]

            # compile dependencies first
            for dep in ordered_deps:
                var_name = get_varname(dep.name)
                if var_name in var_map and not getattr(dep, 'force_recalc', False):
                    continue
                compile_node(dep, var_map, var_name, lines)
            var_name = node.name.lower().replace(".", "_")
            compile_node(node, var_map, var_name, lines)

        # write the code to a new text block
        text_name = "generated_scene.py"
        if text_name in bpy.data.texts:
            txt = bpy.data.texts[text_name]
            txt.clear()
        else:
            txt = bpy.data.texts.new(text_name)
        for ln in lines:
            txt.write(ln + "\n")
        print(f"Generated code:\n")
        for ln in lines:
            print(ln)

        self.report({'INFO'}, f"Generated code in Text Editor: {text_name}")
        return {'FINISHED'}

