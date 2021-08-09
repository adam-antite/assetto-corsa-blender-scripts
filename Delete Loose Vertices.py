import bpy

context = bpy.context
total_meshes = 0
current_mesh = 0
total_vertices = 0
total_removed_vertices = 0
current_vertices_start = 0
current_vertices_end = 0
current_removed_vertices = 0


for o in context.selected_objects:
    if o.type == 'MESH':
        total_meshes += 1
	total_vertices += len(o.data.vertices)


print("Total meshes: " + str(total_meshes) + + "\n")
print("Total vertex count: " + str(total_vertices) + "\n")


for o in context.selected_objects:
    if o.type == 'MESH':
        current_mesh += 1
	current_vertices_start = len(o.data.vertices)
        context.view_layer.objects.active = o
        o.select_set(True)
        print("Current mesh: " + str(current_mesh) + " / " + str(total_meshes))
	print("Mesh vertex count: " + str(current_vertices_start))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_loose()
        bpy.ops.mesh.delete(type='VERT')
	current_vertices_end = len(o.data.vertices)
	current_removed_vertices = current_vertices_start - current_vertices_end
	total_removed_vertices += current_removed_vertices
	print(str(current_removed_vertices) + " vertices removed.\n")
        bpy.ops.object.mode_set(mode='OBJECT')
        o.select_set(False)
        
print(str(total_removed_vertices) + " vertices removed.")
print("Final vertex count: " + str(total_vertices - total_removed_vertices))
        
        