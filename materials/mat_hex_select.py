import bpy
import bmesh

from bpy.props import *
from ..materials.mat_utils import *
from ..utilities.utils import get_prefs

class RTS_OT_RePattern_Tex_Color_Select(bpy.types.Operator):
    bl_description = "Select faces by this color"    
    bl_idname = "rts_ot.textools_color_select"
    bl_label = "Select Color"
    bl_options = {'REGISTER', 'UNDO'}
    
    index : IntProperty(description="Color Index", default=0)

    @classmethod
    def poll(cls, context):
        if not bpy.context.active_object:
            return False

        if bpy.context.active_object not in bpy.context.selected_objects:
            return False

        # allow only 1 object selected
        if len(bpy.context.selected_objects) != 1:
            return False

        if bpy.context.active_object.type != 'MESH':
            return False

        return True

    
    def execute(self, context):

        view_layer = bpy.context.view_layer        
        obj = view_layer.objects.active 
        #obj = bpy.context.active_object
        
        # check for missing slots, materials,..
        if self.index >= len(obj.material_slots):
            self.report({'ERROR_INVALID_INPUT'}, "No material slot for color '{}' found".format(self.index))
            return

        if not obj.material_slots[self.index].material:
            self.report({'ERROR_INVALID_INPUT'}, "No material found for material slot '{}'".format(self.index))
            return      

        if bpy.context.active_object.mode != 'EDIT':
            bpy.ops.object.mode_set(mode='EDIT')

        # select faces
        bm = bmesh.from_edit_mesh(bpy.context.active_object.data);
        bpy.ops.mesh.select_all(action='DESELECT')
        for face in bm.faces:
            if face.material_index == self.index:
                face.select = True

        return {'FINISHED'}            

