import bpy

context = bpy.context

for obj in context.selected_objects:
    if len(obj.children) == 0:
        if obj.type != 'MESH':
            continue
        if len(obj.data.materials) >= 1:
            if obj.active_material.blend_method == 'BLEND':
                obj.active_material.blend_method = 'OPAQUE'