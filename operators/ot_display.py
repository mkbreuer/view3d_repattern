# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


class RTS_OT_RePattern_Set_Shading(bpy.types.Operator):
    """Toggle object shading: smooth or flat"""
    bl_idname = "rts_ot.display_set_shading"
    bl_label = "Set Shading"
    bl_options = {'REGISTER', 'UNDO'}
     
    def execute(self, context):
        print(self)      
        return {'FINISHED'}

    event = None
    def invoke(self, context, event):
        ev = []    

        current_mode = bpy.context.object.mode

        if bpy.context.object.data.polygons[0].use_smooth:                
           
            ev.append("Shade Flat!") 

            if context.mode == 'EDIT_MESH':
                #bpy.ops.mesh.select_all(action='SELECT')                
                bpy.ops.mesh.faces_shade_flat()
            else:
                bpy.ops.object.mode_set(mode='OBJECT')                
                bpy.ops.object.shade_flat()

        else: 
            ev.append("Shade Smooth!") 
            
            if context.mode == 'EDIT_MESH':
                #bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.faces_shade_smooth()              
            else:
                bpy.ops.object.mode_set(mode='OBJECT')    
                bpy.ops.object.shade_smooth()


        bpy.ops.object.mode_set (mode=current_mode)

        #ev.append("Shade")
        self.report({'INFO'}, "".join(ev))        
        return {'FINISHED'}



class RTS_OT_RePattern_Set_Wire(bpy.types.Operator):
    """Default [LMB]: toggle object wire // [LMB+CTRL} toggle wire overlay for all objects"""
    bl_idname = "rts_ot.display_set_wire"
    bl_label = "Set Wire"
    bl_options = {'REGISTER', 'UNDO'}
     
    def execute(self, context):
        print(self)      
        return {'FINISHED'}

    event = None
    def invoke(self, context, event):    
        ev = []    
        if event.ctrl:                     
            if bpy.context.space_data.overlay.show_wireframes == True:
                ev.append("Wire Overlay disabled!") 
                bpy.context.space_data.overlay.show_wireframes = False
            else:
                ev.append("Wire Overlay enabled!") 
                bpy.context.space_data.overlay.show_wireframes = True
        
        else:            
            if bpy.context.object.show_wire == True:                
                ev.append("Wire Object disabled!") 
                bpy.context.object.show_wire = False
                bpy.context.object.show_all_edges = False
                       
            else: # snap
                ev.append("Wire Object enabled!") 
                bpy.context.object.show_wire = True
                bpy.context.object.show_all_edges = True
              
        #ev.append("Wire")
        self.report({'INFO'}, "".join(ev))        
        return {'FINISHED'}


