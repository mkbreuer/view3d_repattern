import bpy
from bpy import *
from bpy.props import *
from random import random
from ..utilities.utils import get_prefs


def mat_slots_single(self):
    view_layer = bpy.context.view_layer                                       
    selected = bpy.context.selected_editable_objects                        
    
    if self.mat_active_only == False:
        for obj in selected:
            view_layer.objects.active = obj            
            bpy.ops.object.material_slot_remove()
    else:
        bpy.ops.object.material_slot_remove()


def mat_slots_all(self):
    view_layer = bpy.context.view_layer                                       
    selected = bpy.context.selected_editable_objects                        
    
    if self.mat_active_only == False:
        for obj in selected:
            view_layer.objects.active = obj            
            bpy.context.object.data.materials.clear()
    else:
        bpy.context.object.data.materials.clear()    


def mat_slots_unused(self):
    view_layer = bpy.context.view_layer                                   
    selected = bpy.context.selected_editable_objects                         
    
    if self.mat_active_only == False:
        for obj in selected:
            view_layer.objects.active = obj                       
            bpy.ops.object.material_slot_remove_unused()           
    else:
        bpy.ops.object.material_slot_remove_unused()   


def mat_slots_amount(self):
    view_layer = bpy.context.view_layer                                   
    selected = bpy.context.selected_editable_objects                       
    
    if self.mat_active_only == False:
        for obj in selected:
            view_layer.objects.active = obj

            for slot in obj.material_slots:  
                for i in range(0,len(obj.material_slots)):
                    obj.active_material_index = i 
                    bpy.ops.object.material_slot_move(direction='DOWN')  

            for i in range(self.mat_slots_amount):
                bpy.ops.object.material_slot_remove()
    else:
        obj = view_layer.objects.active
        for slot in obj.material_slots:  
            for i in range(0,len(obj.material_slots)):
                obj.active_material_index = i 
                bpy.ops.object.material_slot_move(direction='DOWN')  

        for i in range(self.mat_slots_amount):
            bpy.ops.object.material_slot_remove()  


def mat_purge_all(self):           
    temp_remove = eval("bpy.data.materials")
    for item in temp_remove:                                  
        if item.users == 0:
            temp_remove.remove(item)


def mat_purge_prefix(self):                  
    temp_remove = eval("bpy.data.materials") 
    prefix = self.mat_purge_prefix 
    if prefix != '':                                                      
        for key, item in bpy.data.materials.items():
            if key.startswith(prefix):                                                                                                                             
                temp_remove.remove(temp_remove[key], do_unlink=True, do_id_user=True, do_ui_user=True)


def mat_purge_slot(self): 
    view_layer = bpy.context.view_layer                                   
    selected = bpy.context.selected_editable_objects    
   
    if self.mat_active_only == False:
        for obj in selected:
            view_layer.objects.active = obj      
            mat_slots_all(self)      
    else:    
        mat_slots_all(self)

    mat_purge_all(self) 


class RTS_OT_RePattern_Material_Delete(bpy.types.Operator):
    """Remove all materials slots / Value Slider"""
    bl_idname = "rts_ot.remove_all_material"
    bl_label = "RTS Remove & Purge"
    bl_options = {'REGISTER', 'UNDO'}
    
    mode : StringProperty(default="") 
    mat_active_only : BoolProperty(name="Active Only", description="", default=False)   
    mat_slots_amount : IntProperty(name = "Remove Slots", description="remove material slot by value", default=1, min=0, max=1000, subtype='NONE') 
    mat_purge_prefix : StringProperty(name = "Prefix", default="RP_MAT")
   
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(align=True)   
                
        row = box.row(align=True)  
        row.prop(self,'mat_active_only')    

        box.separator()   
        
        if self.mode in 'mat_slots_amount':

            row = box.row(align=True)  
            row.prop(self,'mat_slots_amount')    

            box.separator()   

        if self.mode in 'mat_purge_prefix':

            row = box.row(align=True)  
            row.prop(self,'mat_purge_prefix')    

            box.separator()   

        
    def execute(self, context): 
        view_layer = bpy.context.view_layer  
        active = view_layer.objects.active
        current_mode = bpy.context.object.mode  
        
        selected = bpy.context.selected_objects             
        obj_list = [obj for obj in selected]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}    
        else:      
            if bpy.context.object.mode == 'EDIT':
                bpy.ops.object.editmode_toggle() 
                         
            if self.mode in 'mat_purge_slot':
                mat_purge_slot(self)
                self.report({'INFO'}, 'Removed Slots & Purged All!')    
            
            if self.mode in 'mat_slots_single':   
                mat_slots_single(self)
                self.report({'INFO'}, 'Removed Slot!') 

            if self.mode in 'mat_slots_all':   
                mat_slots_all(self)
                self.report({'INFO'}, 'Removed all Slots!') 
                                                         
            if self.mode in 'mat_slots_unused':   
                mat_slots_unused(self)
                self.report({'INFO'}, 'Removed all unused Slots!')                 
            
            if self.mode in 'mat_slots_amount': 
                mat_slots_amount(self)
                self.report({'INFO'}, 'Removed Slots:'+ self.mat_slots_amount)                
                
            if self.mode in 'mat_purge_all':  
                mat_purge_all(self)
                self.report({'INFO'}, 'Purged All Orphaned!') 

            if self.mode in 'mat_purge_prefix':
                mat_purge_prefix(self)
                self.report({'INFO'}, 'Purged Orphaned by Prefix!') 

        
        bpy.ops.object.mode_set (mode=current_mode)        
        bpy.context.view_layer.objects.active = active  
        return {'FINISHED'}



class RTS_OT_RePattern_Material_Dots_Stroke(bpy.types.Operator):
    """delete dots stroke material if not needed"""
    bl_idname = "rts_ot.remove_dots_stroke"
    bl_label = "RTS Remove Dots Stroke"
    bl_options = {'REGISTER', 'UNDO'}
    
   
    def execute(self, context): 

        temp_remove = eval("bpy.data.materials") 
        prefix = 'Dots Stroke'
        if prefix != '':                                                      
            for key, item in bpy.data.materials.items():
                if key.startswith(prefix):                                                                                                                             
                    temp_remove.remove(temp_remove[key], do_unlink=True, do_id_user=True, do_ui_user=True)

        return {'FINISHED'}

