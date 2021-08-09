import bpy

context = bpy.context

for o in context.selected_objects:
    if o.type == 'MESH':
        o.scale = (1, 1, 1)