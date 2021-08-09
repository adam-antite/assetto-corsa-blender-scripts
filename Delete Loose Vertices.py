import bpy

context = bpy.context
total_meshes = 0
current_mesh = 0

for o in context.selected_objects:
    if o.type == 'MESH':
        total_meshes += 1

print("Total meshes: " + str(total_meshes) + + "\n")

for o in context.selected_objects:
    if o.type == 'MESH':
        current_mesh += 1
        context.view_layer.objects.active = o
        o.select_set(True)
        print("Current mesh: " + str(current_mesh) + " / " + str(total_meshes))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_loose()
        bpy.ops.mesh.delete(type='VERT')
        print("Loose vertices deleted.\n")
        bpy.ops.object.mode_set(mode='OBJECT')
        o.select_set(False)
        
print("Finished.\n\n")
        
        