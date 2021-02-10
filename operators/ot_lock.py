import bpy
from bpy import *
from bpy.props import *

from ..utilities.utils import get_prefs

class RTS_OT_RePattern_Transform_Lock(bpy.types.Operator):
    """(un)lock transforms for selected objects"""
    bl_idname = "rts_ot.transform_lock"
    bl_label = "(Un-)Lock Transform"
    bl_options = {'REGISTER', 'UNDO'} 
        
    def draw(self, context):
        layout = self.layout
       
        prefs = get_prefs()
        transform_props = prefs.transform_type   

        box = layout.box().column(align=True)    
        box.separator() 
        
        if bpy.context.object.lock_location[0] == True:
            ico_x = 'LOCKED'
        else:
            ico_x = 'UNLOCKED'       

        if bpy.context.object.lock_location[1] == True:
            ico_y = 'LOCKED'
        else:
            ico_y = 'UNLOCKED'       
      
        if bpy.context.object.lock_location[2] == True:
            ico_z = 'LOCKED'
        else:
            ico_z = 'UNLOCKED'          
    
        row = box.row(align=True)         
        row.label(text="Location:")   
        
        row = box.row(align=False)              
        row.prop(transform_props, "lock_location_x", text="X", icon=ico_x) 
        row.prop(transform_props, "lock_location_y", text="y", icon=ico_y) 
        row.prop(transform_props, "lock_location_z", text="Z", icon=ico_z)             

        box.separator()  
       
        if bpy.context.object.lock_rotation[0] == True:
            ico_x = 'LOCKED'
        else:
            ico_x = 'UNLOCKED'       

        if bpy.context.object.lock_rotation[1] == True:
            ico_y = 'LOCKED'
        else:
            ico_y = 'UNLOCKED'       
      
        if bpy.context.object.lock_rotation[2] == True:
            ico_z = 'LOCKED'
        else:
            ico_z = 'UNLOCKED'       

        row = box.row(align=True) 
        row.label(text="Rotation:")   
        
        row = box.row(align=False)  
        row.prop(transform_props, "lock_rotation_x", text="X", icon=ico_x) 
        row.prop(transform_props, "lock_rotation_y", text="Y", icon=ico_y) 
        row.prop(transform_props, "lock_rotation_z", text="Z", icon=ico_z)            
        
        box.separator()  
       
        if bpy.context.object.lock_scale[0] == True:
            ico_x = 'LOCKED'
        else:
            ico_x = 'UNLOCKED'       

        if bpy.context.object.lock_scale[1] == True:
            ico_y = 'LOCKED'
        else:
            ico_y = 'UNLOCKED'       
      
        if bpy.context.object.lock_scale[2] == True:
            ico_z = 'LOCKED'
        else:
            ico_z = 'UNLOCKED'       
       
        row = box.row(align=True) 
        row.label(text="Scale:")  
        
        row = box.row(align=False)  
        row.prop(transform_props, "lock_scale_x", text="X", icon=ico_x)   
        row.prop(transform_props, "lock_scale_y", text="Y", icon=ico_y)  
        row.prop(transform_props, "lock_scale_z", text="Z", icon=ico_z)            

        box.separator()               

        return
 
    def execute(self, context):
        view_layer = bpy.context.view_layer  
      
        prefs = get_prefs()
        transform_props = prefs.transform_type     

        selected = bpy.context.selected_objects            
        obj_list = [obj for obj in selected]    
        if not obj_list:
            self.report({'INFO'}, "Nothing Selected!")              
            return {'CANCELLED'}
        else:
            ev = [] 
            for obj in selected:  
                view_layer.objects.active = obj

                ev.append("Transform")

                if obj.lock_location[0] == False or transform_props.lock_location_x == False:
                    obj.lock_location[0] = True
                else:
                    obj.lock_location[0] = False
               
                if obj.lock_location[1] == False or transform_props.lock_location_y == False:
                    obj.lock_location[1] = True
                else:
                    obj.lock_location[1] = False
                
                if obj.lock_location[2] == False or transform_props.lock_location_z == False:
                    obj.lock_location[2] = True
                else:
                    obj.lock_location[2] = False

                if obj.lock_rotation[0] == False or transform_props.lock_rotation_x == False:
                    obj.lock_rotation[0] = True
                else:
                    obj.lock_rotation[0] = False 
               
                if obj.lock_rotation[1] == False or transform_props.lock_rotation_y == False:
                    obj.lock_rotation[1] = True
                else:
                    obj.lock_rotation[1] = False
               
                if obj.lock_rotation[2] == False or transform_props.lock_rotation_z == False:
                    obj.lock_rotation[2] = True
                else:
                    obj.lock_rotation[2] = False
               
                if obj.lock_scale[0] == False or transform_props.lock_scale_x == False:
                    obj.lock_scale[0] = True
                else:
                    obj.lock_scale[0] = False
               
                if obj.lock_scale[1] == False or transform_props.lock_scale_y == False:
                    obj.lock_scale[1] = True
                else:
                    obj.lock_scale[1] = False
               
                if obj.lock_scale[2] == False or transform_props.lock_scale_z == False:
                    obj.lock_scale[2] = True
                else:
                    obj.lock_scale[2] = False

                if obj.lock_location[0] == True or obj.lock_location[1] == True or obj.lock_location[2] == True:
                    ev.append("+ Location")
                else:
                    ev.append("+ Location")

                if obj.lock_rotation[0] == True or obj.lock_rotation[1] == True or obj.lock_rotation[2] == True:
                    ev.append(" + Rotation")
                else:
                    ev.append(" + Rotation")
 
                if obj.lock_scale[0] == True or obj.lock_scale[1] == True or obj.lock_scale[2] == True:
                    ev.append(" + Scale")
                else:
                    ev.append(" + Scale")
              
              
                if obj.lock_location[0] == True or obj.lock_location[1] == True or obj.lock_location[2] == True or \
                obj.lock_rotation[0] == True or obj.lock_rotation[1] == True or obj.lock_rotation[2] == True or \
                obj.lock_scale[0] == True or obj.lock_scale[1] == True or obj.lock_scale[2] == True:
                    ev.append(" + Locked ")
                else:
                    ev.append(" + Unlocked ")


        self.report({'INFO'}, "".join(ev)) 
        return {'FINISHED'}


