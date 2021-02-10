import bpy
import bmesh
from bpy.props import *
from ..materials.mat_utils import *
from ..utilities.utils import get_prefs
from ..utilities.cache import settings_load, settings_write

class RTS_OT_RePattern_Hex_Color_Assign(bpy.types.Operator):
    bl_description = "Assign color to selected objects or faces in edit mode."    
    bl_idname = "rts_ot.textools_color_assign"
    bl_label = "Assign Color"
    bl_options = {'REGISTER', 'UNDO'}
    
    index : IntProperty(description="Color Index", default=0)

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
        assign_color(self, context, self.index)
        return {'FINISHED'}


def assign_color(self, context, index):
        
    selected_obj = bpy.context.selected_objects.copy()

    previous_mode = 'OBJECT'
    if len(selected_obj) == 1:
        previous_mode = bpy.context.active_object.mode

    for obj in selected_obj:
        # select object
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(state=True, view_layer=None)
        bpy.context.view_layer.objects.active = obj

        # enter Edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        bm = bmesh.from_edit_mesh(obj.data);
        faces = []

        # assign to all or just selected faces?
        if previous_mode == 'EDIT':
            faces = [face for face in bm.faces if face.select]
        else:
            faces = [face for face in bm.faces]     

        if previous_mode == 'OBJECT':
            bpy.ops.mesh.select_all(action='SELECT')
        

        # verify material slots
        for i in range(index+1):
            if index >= len(obj.material_slots):
                bpy.ops.object.material_slot_add()

        assign_slot(obj, index)

        # assign to selection
        obj.active_material_index = index
        bpy.ops.object.material_slot_assign()


    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    for obj in selected_obj:
        obj.select_set(state=True, view_layer=None)
    
    # restore mode
    bpy.ops.object.mode_set(mode=previous_mode)

