import bpy
import bmesh
from bpy.props import *


class RTS_OT_RePattern_Normals(bpy.types.Operator):
    bl_description = "recalculate normals for all selected"
    bl_idname = "rts_ot.recalculate_normals"
    bl_label = "Recalculate Normals"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        view_layer = bpy.context.view_layer
        selected = bpy.context.selected_objects           

        current_mode = bpy.context.object.mode

        obj_list = [obj for obj in selected] 
        if not obj_list:
            self.report({'INFO'}, "Nothing Selected!")              
            return {'CANCELLED'}
        else:

            for obj in selected:
                view_layer.objects.active = obj
           
                if obj.type == 'MESH':
                    obj.select_set(True)
                    
                    bpy.ops.object.mode_set(mode='EDIT')   
                    bpy.ops.mesh.select_mode(type="VERT")    

                    me = context.object.data
                    bm = bmesh.from_edit_mesh(me)
                    verts_sel = ([v for v in bm.verts if v.select])
                    #verts_sel = [v.select for v in bm.verts]
                    
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent(inside=False)
                    bpy.ops.mesh.select_all(action='DESELECT')

                    for v in verts_sel:
                        v.select = True
                else:
                    obj.select_set(False)
                    self.report({'INFO'}, "Mesh object required!")              
                    return {'CANCELLED'}
        
        bpy.ops.object.mode_set(mode=current_mode)

        return {"FINISHED"}

