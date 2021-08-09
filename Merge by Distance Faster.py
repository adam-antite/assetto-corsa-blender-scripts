import bpy
import bmesh

context = bpy.context
current_mesh = 0
total_meshes = 0
total_vertices = 0
total_removed_vertices = 0
current_vertices_start = 0
current_vertices_end = 0


# Merge by Distance threshold in meters
merge_threshold = 0.00001


print("Beginning Merge by Distance script.")

# First pass to gather mesh and vertex count for analytics purposes
for o in context.selected_objects:
    if o.type == 'MESH':
        total_meshes += 1
        total_vertices += len(o.data.vertices)

print("Total meshes: " + str(total_meshes))
print("Total vertex count: " + str(total_vertices) + "\n")


if True:
    meshes = set(o.data for o in context.selected_objects if o.type == 'MESH')
    bm = bmesh.new()
    for m in meshes:
        current_mesh += 1
        print("Current mesh: " + str(current_mesh) + " / " + str(total_meshes))
        bm.from_mesh(m)
        current_vertices_start = len(bm.verts)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=merge_threshold)
        current_vertices_end = len(bm.verts)
        current_removed_vertices = current_vertices_start - current_vertices_end
        total_removed_vertices += current_removed_vertices
        print("Removed vertices: " + str(current_removed_vertices) + "\n")
        bm.to_mesh(m)
        m.update()
        bm.clear()
    bm.free()

    
print(str(total_removed_vertices) + " vertices removed.")
print("Final vertex count: " + str(total_vertices - total_removed_vertices))
