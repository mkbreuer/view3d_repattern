import bpy
from bpy import*
from bpy.props import *

from ..utilities.utils import get_prefs


def modif_array_x(self, obj):
    mod = bpy.data.objects[obj.name].modifiers.new(name='Array_X', type='ARRAY')
    mod.count = 5
    mod.relative_offset_displace[0] = 1
    mod.relative_offset_displace[1] = 0
    mod.relative_offset_displace[2] = 0

def modif_array_y(self, obj):
    mod = bpy.data.objects[obj.name].modifiers.new(name='Array_Y', type='ARRAY')
    mod.count = 5
    mod.relative_offset_displace[0] = 0
    mod.relative_offset_displace[1] = 1
    mod.relative_offset_displace[2] = 0

def modif_array_z(self, obj):
    mod = bpy.data.objects[obj.name].modifiers.new(name='Array_Z', type='ARRAY')
    mod.count = 5
    mod.relative_offset_displace[0] = 0
    mod.relative_offset_displace[1] = 0
    mod.relative_offset_displace[2] = 1


class RTS_OT_RePattern_Modifier_XYZ_Array(bpy.types.Operator):
    bl_label = 'XYZ Array'
    bl_idname = 'rts_ot.mods_xyz_array'
    bl_options = {'REGISTER', 'UNDO'}

    array_x : BoolProperty(name="X-Array", description="add x array modifier", default = True)
    array_y : BoolProperty(name="Y-Array", description="add y array modifier", default = False)
    array_z : BoolProperty(name="Z-Array", description="add z array modifier", default = False)

    def draw(self, context):
        layout = self.layout

        box = layout.box().column(align=True)

        row = box.row()
        row.prop(self, 'array_x')
        row.prop(self, 'array_y')
        row.prop(self, 'array_z')
        
        box.separator() 
 
    def execute(self, context):
  
        view_layer = bpy.context.view_layer  
        selected = bpy.context.selected_objects 

        for obj in selected: 
            view_layer.objects.active = obj

            if self.array_x == True and self.array_y == False and self.array_z == False:         
                modif_array_x(self, obj)

            if self.array_x == False and self.array_y == True and self.array_z == False:               
                modif_array_y(self, obj)

            if self.array_x == False and self.array_y == False and self.array_z == True:  
                modif_array_z(self, obj)

            if self.array_x == True and self.array_y == True and self.array_z == False:         
                modif_array_x(self, obj)
                modif_array_y(self, obj)

            if self.array_x == True and self.array_y == False and self.array_z == True:               
                modif_array_x(self, obj)
                modif_array_z(self, obj)

            if self.array_x == False and self.array_y == True and self.array_z == True:  
                modif_array_y(self, obj)
                modif_array_z(self, obj)
           
            if self.array_x == True and self.array_y == True and self.array_z == True:  
                modif_array_x(self, obj)
                modif_array_y(self, obj)
                modif_array_z(self, obj)

        return {'FINISHED'}





EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class RTS_OT_RePattern_Modifier_Apply_Array(bpy.types.Operator):
    """apply modifier array"""
    bl_idname = "rts_ot.mods_apply_array"
    bl_label = "Apply Array"
    bl_options = {'REGISTER', 'UNDO'}

    array_x : BoolProperty(name="X", description="Apply x array modifier", default = True)
    array_y : BoolProperty(name="Y", description="Apply y array modifier", default = True)
    array_z : BoolProperty(name="Z", description="Apply z array modifier", default = True)

    def draw(self, context):      
        layout = self.layout

        box = layout.box().column(align=True)
        row = box.row()
        row.prop(self, 'array_x')
        row.prop(self, 'array_y')
        row.prop(self, 'array_z')
        box.separator()

    def execute(self, context):
        prefs = get_prefs()
        modif_prefs = prefs.modif_type   
 
        is_select, is_mod = False, False
        message_a = ""

        selected = bpy.context.selected_objects 
        
        for obj in selected:
            is_select = True
 
            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()    
               
                for modifier in obj.modifiers:                   
                    if (modifier.type == 'ARRAY'):
                        is_mod = True     
                                        
                        if self.array_x == True and self.array_y == False and self.array_z == False:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                        
                        if self.array_x == False and self.array_y == True and self.array_z == False:  
                            bpy.ops.object.modifier_apply(modifier="Array_Y")
                      
                        if self.array_x == False and self.array_y == False and self.array_z == True:   
                            bpy.ops.object.modifier_apply(modifier="Array_Z")

                        if self.array_x == True and self.array_y == True and self.array_z == False:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                            bpy.ops.object.modifier_apply(modifier="Array_Y")

                        if self.array_x == True and self.array_y == False and self.array_z == True:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                            bpy.ops.object.modifier_apply(modifier="Array_Z")

                        if self.array_x == False and self.array_y == True and self.array_z == True:  
                            bpy.ops.object.modifier_apply(modifier="Array_Y")
                            bpy.ops.object.modifier_apply(modifier="Array_Z")

                        if self.array_x == True and self.array_y == True and self.array_z == True:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                            bpy.ops.object.modifier_apply(modifier="Array_Y")
                            bpy.ops.object.modifier_apply(modifier="Array_Z")
                              
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode
                bpy.ops.object.mode_set(mode='OBJECT')   
                                  
                for modifier in obj.modifiers:                   
                    if (modifier.type == 'ARRAY'):
                        is_mod = True     

                        if self.array_x == True and self.array_y == False and self.array_z == False:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                        
                        if self.array_x == False and self.array_y == True and self.array_z == False:  
                            bpy.ops.object.modifier_apply(modifier="Array_Y")
                      
                        if self.array_x == False and self.array_y == False and self.array_z == True:   
                            bpy.ops.object.modifier_apply(modifier="Array_Z")

                        if self.array_x == True and self.array_y == True and self.array_z == False:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                            bpy.ops.object.modifier_apply(modifier="Array_Y")

                        if self.array_x == True and self.array_y == False and self.array_z == True:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                            bpy.ops.object.modifier_apply(modifier="Array_Z")

                        if self.array_x == False and self.array_y == True and self.array_z == True:  
                            bpy.ops.object.modifier_apply(modifier="Array_Y")
                            bpy.ops.object.modifier_apply(modifier="Array_Z")

                        if self.array_x == True and self.array_y == True and self.array_z == True:  
                            bpy.ops.object.modifier_apply(modifier="Array_X")
                            bpy.ops.object.modifier_apply(modifier="Array_Y")
                            bpy.ops.object.modifier_apply(modifier="Array_Z")
 
                bpy.ops.object.mode_set(mode=oldmode)      
            

        if is_select:
            if is_mod:
                message_a = "Removed Array!"
            else:
                message_a = "NOPE: no Array available!"
        else:
            self.report(type={"INFO"}, message="NOPE: No Selection. No apply!")
        return {'CANCELLED'}

        self.report(type={"INFO"}, message=message_a)

        return {'FINISHED'} 

    def invoke(self, context, event):
        dpi_value = bpy.context.preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2)#, height=300)




class RTS_OT_RePattern_Modifier_Remove_Array(bpy.types.Operator):
    """remove xyz array modifier"""
    bl_idname = "rts_ot.mods_remove_array"
    bl_label = "Remove Array"
    bl_options = {'REGISTER', 'UNDO'}

    array_x : BoolProperty(name="X", description="Apply x array modifier", default = True)
    array_y : BoolProperty(name="Y", description="Apply y array modifier", default = True)
    array_z : BoolProperty(name="Z", description="Apply z array modifier", default = True)

    def draw(self, context):      
        layout = self.layout

        box = layout.box().column(align=True)
        row = box.row()
        row.prop(self, 'array_x')
        row.prop(self, 'array_y')
        row.prop(self, 'array_z')
        box.separator()


    def execute(self, context):         
        prefs = get_prefs()
        modif_prefs = prefs.modif_type 

        selected = bpy.context.selected_objects 
       
        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for obj in selected:            
            for modifier in obj.modifiers:    
                if (modifier.type == 'ARRAY'):

                    if self.array_x == True and self.array_y == False and self.array_z == False:  
                        bpy.ops.object.modifier_remove(modifier="Array_X")
                    
                    if self.array_x == False and self.array_y == True and self.array_z == False:  
                        bpy.ops.object.modifier_remove(modifier="Array_Y")
                    
                    if self.array_x == False and self.array_y == False and self.array_z == True:   
                        bpy.ops.object.modifier_remove(modifier="Array_Z")

                    if self.array_x == True and self.array_y == True and self.array_z == False:  
                        bpy.ops.object.modifier_remove(modifier="Array_X")
                        bpy.ops.object.modifier_remove(modifier="Array_Y")

                    if self.array_x == True and self.array_y == False and self.array_z == True:  
                        bpy.ops.object.modifier_remove(modifier="Array_X")
                        bpy.ops.object.modifier_remove(modifier="Array_Z")

                    if self.array_x == False and self.array_y == True and self.array_z == True:  
                        bpy.ops.object.modifier_remove(modifier="Array_Y")
                        bpy.ops.object.modifier_remove(modifier="Array_Z")

                    if self.array_x == True and self.array_y == True and self.array_z == True:  
                        #bpy.ops.object.modifier_remove(modifier="Array_X")
                        #bpy.ops.object.modifier_remove(modifier="Array_Y")
                        #bpy.ops.object.modifier_remove(modifier="Array_Z")     
                        bpy.ops.rts.OT_mods_remove_all_array()

        bpy.ops.object.mode_set(mode=oldmode)
        return {'FINISHED'}

    def invoke(self, context, event):
        dpi_value = bpy.context.preferences.system.dpi        
        return bpy.context.window_manager.invoke_props_dialog(self, width=dpi_value*2)#, height=300)



class RTS_OT_RePattern_Modifier_Remove_All_Array(bpy.types.Operator):
    """remove all array modifier"""
    bl_idname = "rts_ot.mods_remove_all_array"
    bl_label = "Remove All Array"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        view_layer = bpy.context.view_layer        
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = view_layer.objects.active                    
                for modifier in obj.modifiers: 
                    if (modifier.type == 'ARRAY'):
                        obj.modifiers.remove(modifier)
        else:
            for obj in selected:                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'ARRAY'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}

