import bpy
import bmesh

from ..materials.mat_utils import *
from ..utilities.utils import get_prefs


class RTS_OT_RePattern_Hex_Color_Clear(bpy.types.Operator):
    bl_description = "remove materials on selected ones"
    bl_idname = "rts_ot.textools_color_clear"
    bl_label = "Clear Colors"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if not bpy.context.active_object:
            return False

        if bpy.context.active_object not in bpy.context.selected_objects:
            return False

        if bpy.context.active_object.type != 'MESH':
            return False

        return True
    
    def execute(self, context):
              
        prefs = get_prefs()
        mat_prefs = prefs.mat_type

        view_layer = bpy.context.view_layer
        selected = bpy.context.selected_objects
        for obj in selected:
            view_layer.objects.active = obj

            # store mode
            current_mode = bpy.context.active_object.mode
            
            if bpy.context.active_object.mode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')

            bm = bmesh.from_edit_mesh(bpy.context.active_object.data);

            # Set all faces
            for face in bm.faces:
                face.material_index = 0

            # Clear material slots
            bpy.ops.object.mode_set(mode='OBJECT')
            count = len(obj.material_slots)
            for i in range(count):
                bpy.ops.object.material_slot_remove()

            # Delete materials if not used
            for material in bpy.data.materials:
                if mat_prefs.mat_to_assign in material.name:
                    if material.users == 0:
                        material.user_clear()
                        bpy.data.materials.remove(material)

            # restore mode
            bpy.ops.object.mode_set(mode=current_mode)

            for area in bpy.context.screen.areas:
                #print("area: {}".format(area.type))
                if area.type == 'PROPERTIES':
                    for space in area.spaces:
                        if space.type == 'PROPERTIES':
                            # space.shading.type = 'MATERIAL'
                            space.context = 'MATERIAL'

            # Show Material Tab
            for area in bpy.context.screen.areas:
                if area.type == 'PROPERTIES':
                    for space in area.spaces:
                        if space.type == 'PROPERTIES':
                            space.context = 'MATERIAL'

            # Switch Solid shading
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.shading.type = 'SOLID'

        return {'FINISHED'}
