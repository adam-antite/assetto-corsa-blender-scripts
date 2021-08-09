# Assetto Corsa Blender Scripts
This is just a collection of assorted Blender Python scripts to aid in the track modding process for Assetto Corsa.

# How to Use
Download or clone this repository and then open the .py scripts inside of Blender's text editor.

## Alpha_Blend to Opaque
Sometimes when importing tracks from other games, Blender will change the material blend method to Alpha Blend, causing objects to appear transparent and have an x-ray effect. This script automatically changed the blend method of the selected objects to opaque.

## Delete Loose Vertices
Self-explanatory; deletes all the loose vertices for each selected object.

## Merge by Distance
Automatically applies the Merge by Distance operation for each selected object. Threshold can be changed by altering the ```threshold``` variable in the script.

## Scale Selected Objects to 1,1,1
Sets scale of selected objects to (1,1,1). Useful for fixing improperly scaled meshes from FBX imports.

## Specular and Metallic to 0
Blender usually sets Specular and Metallic for imported object materials to 1, which doesn't look good. This script sets the Specular and Metallic nodes of all the selected objects to 0.