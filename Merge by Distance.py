import bpy

context = bpy.context
current_mesh = 0
total_meshes = 0
total_vertices = 0
total_removed_vertices = 0
current_vertices_start = 0
current_vertices_end = 0
current_removed_vertices = 0

# Merge by Distance threshold in meters
threshold = 0.00001


# First pass to gather mesh and vertex count for analytics purposes
for o in context.selected_objects:
    if o.type == 'MESH':
        total_meshes += 1
        total_vertices += len(o.data.vertices)


print("Total meshes: " + str(total_meshes))
print("Total vertex count: " + str(total_vertices) + "\n")


# Second pass to do the Merge by Distance operation
for o in context.selected_objects:
    if o.type == 'MESH':
        current_mesh += 1
        current_vertices_start = len(o.data.vertices)
        print("Mesh Number: " + str(current_mesh) + " / " + str(total_meshes))
        print("Mesh vertex count: " + str(current_vertices_start))
        context.view_layer.objects.active = o
        o.select_set(True)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.mesh.remove_doubles(threshold)
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        o.select_set(False)
        current_vertices_end = len(o.data.vertices)
        current_removed_vertices = current_vertices_start - current_vertices_end
        total_removed_vertices += current_removed_vertices
        print(str(current_removed_vertices) + " vertices removed.\n")

print(str(total_removed_vertices) + " vertices removed.")
print("Final vertex count: " + str(total_vertices - total_removed_vertices))
        
        