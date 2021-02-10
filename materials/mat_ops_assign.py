import bpy
import bmesh
from bpy.props import *
from ..utilities.utils import get_prefs



class RTS_OT_RePattern_Shader_Assign_Color(bpy.types.Operator):
    bl_idname = "rts_ot.mat_shader_assign_color"
    bl_label = "RTS Shader Assign Color"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        prefs = get_prefs()
        mat_prefs = prefs.mat_type

        # store active
        c = bpy.context
        src = c.active_object
        vly = c.view_layer
        act = vly.objects.active
        sct = bpy.context.selected_editable_objects
        selected = bpy.context.selected_editable_objects 
        mat = bpy.context.object.active_material 

        obj_list = [obj for obj in sct]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}    
        else:   
            mat_name = mat.name    
            mat_get = bpy.data.materials.get(mat_name)
            if mat_get is not None:

                for obj in sct:  
                    vly.objects.active = obj

                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='TOGGLE')         
                    bpy.ops.mesh.select_all(action='SELECT')         
                    bpy.ops.object.material_slot_assign()   
                    bpy.ops.object.editmode_toggle()

        # reload active #     
        vly.objects.active = act
        return {'FINISHED'}




class RTS_OT_RePattern_Shader_Assign(bpy.types.Operator):
    '''assign material to selected objects'''
    bl_idname = "rts_ot.mat_shader_assign"
    bl_label = "RTS MAT Shader Assign"
    bl_options = {'REGISTER', 'UNDO'}
    
    mat_string : StringProperty(default="", name='')

    def execute(self, context):
        prefs = get_prefs()
        mat_prefs = prefs.mat_type
        rp_props = bpy.context.window_manager.rp_props_repattern 

        # store active # 
        c = bpy.context
        src = c.active_object
        vly = c.view_layer
        act = vly.objects.active
        sct = bpy.context.selected_editable_objects
        selected = bpy.context.selected_objects 
        mat_act = bpy.context.object.active_material 

        obj_list = [obj for obj in sct]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}    
        else:   

            for obj in sct:  
                vly.objects.active = obj


                if bpy.context.object.mode == 'OBJECT':
        
                    obj_list = [obj.name for obj in bpy.context.selected_objects]
        
                    for obj in obj_list:
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.data.objects[obj].select_set(state=True)               
                        vly.objects.active = bpy.data.objects[obj]
        
                        if self.mat_string == bpy.data.materials:
                            bpy.context.active_object.active_material = bpy.data.materials[mat_name]
                        else:
                            if not len(bpy.context.object.material_slots):
                                bpy.ops.object.material_slot_add()
        
                            bpy.context.active_object.active_material = bpy.data.materials[self.mat_string]
        
                    for obj in obj_list:
                        bpy.data.objects[obj].select_set(state=True)
         
                
                elif bpy.context.mode == 'EDIT_MESH':

                    mat_name = [mat.name for mat in bpy.context.object.material_slots if len(bpy.context.object.material_slots)]
        
                    if self.mat_string in mat_name:
                        context.object.active_material_index = mat_name.index(self.mat_string) 
                        bpy.ops.object.material_slot_assign() 
                    else: 
                        bpy.ops.object.material_slot_add()
                        bpy.context.object.active_material = bpy.data.materials[self.mat_string] 
                        bpy.ops.object.material_slot_assign() 

                else:                          
                    bpy.ops.object.material_slot_add()
                    bpy.context.object.active_material = bpy.data.materials[self.mat_string] 
                    bpy.ops.object.material_slot_assign() 


        # reload active #     
        vly.objects.active = act

        self.report({'INFO'}, 'Assign MAT from List!') 
        return {'FINISHED'}



                

class RTS_MT_RePattern_Material_List(bpy.types.Menu): 
    """apply material to object or mesh"""
    bl_idname = "rts_mt.material_list"
    bl_label = "RTS Material List"

    def draw(self, context):
        layout = self.layout

        for mat in bpy.data.materials:  
            name = mat.name
            try:
                icon_val = layout.icon(mat)
            except:
                icon_val = 1
                #print ("WARNING [Mat Panel]: Could not get icon value for %s" % name)
            ops = layout.operator("rts_ot.mat_shader_assign", text=name, icon_value=icon_val)
            ops.mat_string = name


