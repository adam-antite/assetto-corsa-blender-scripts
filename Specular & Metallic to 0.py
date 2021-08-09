import bpy


def fix_node(node: bpy.types.Node, node_tree: bpy.types.NodeTree):
    """Adjust the properties if the node is a Principled BSDF"""
    if node.type == 'BSDF_PRINCIPLED':
        node.inputs['Specular'].default_value = 0.0
        node.inputs['Metallic'].default_value = 0.0



def fix_material(material: bpy.types.Material):
    """Fix the nodes of the given material"""
    for node in material.node_tree.nodes:
        fix_node(node, material.node_tree)


def fix_selected():
    """Fix the materials of the selected objects"""
    for object in bpy.context.selected_objects:
        for material_slot in object.material_slots:
            fix_material(material_slot.material)


if __name__ == "__main__":
    fix_selected()