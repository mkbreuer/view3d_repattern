import bpy
from bpy import *
from bpy.props import *
import random

class RTS_OT_RePattern_Curve_Toggle_Bevel(bpy.types.Operator):
    """toggle curve bevel extrusion"""
    bl_idname = "rts_ot.toggle_curve_bevel"
    bl_label = "CurveBevel"
    bl_options = {'REGISTER', 'UNDO'}

    depth : FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring : IntProperty(name="Ring",  description=" ", min=0, max=100, default=12) 
    nring : IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop : IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 

    offset : FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height : FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    wire : bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})   


    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(align=True)                     
       
        row = box.row(align=True)                                                                                                                                                                                                                    
        row.operator("rts_ot.dynamic_normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(self, 'depth')
 
        if self.wire == True:
            row.prop(self, 'wire', text="", icon = 'MESH_PLANE')              
        else:                       
           row.prop(self, 'wire', text="", icon = 'MESH_GRID') 
                    
        row = box.row(align=True)
        row.prop(self, 'ring')  
        row.prop(self, 'loop')

        row = box.row(align=True)
        row.prop(self, 'offset')  
        row.prop(self, 'height')
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(align=True)
            row.prop(self, 'nring')
     
        box.separator()


    def execute(self, context):
         
        active_bevel = bpy.context.object.data.bevel_depth
      
        if active_bevel == 0.0:              
            
            show = bpy.context.object.data.dimensions
            if show == '3D':                            
                bpy.context.object.data.fill_mode = 'FULL'
            else:
                bpy.context.object.data.fill_mode = 'BOTH'

            bpy.context.object.data.bevel_resolution = self.loop

            bpy.context.object.data.bevel_depth = self.depth
            bpy.context.object.data.offset = self.offset
            bpy.context.object.data.extrude = self.height 

            if context.object.data.splines.active.type == 'NURBS':            
                bpy.context.object.data.splines[0].order_u = self.nring            
            else:
                bpy.context.object.data.resolution_u = self.ring

        else:                   

            show = bpy.context.object.data.dimensions
            if show == '3D':                            
                bpy.context.object.data.fill_mode = 'HALF'
            else:
                bpy.context.object.data.fill_mode = 'NONE'
            
            #bpy.context.object.data.bevel_resolution = 0
            #bpy.context.object.data.resolution_u = 0
            bpy.context.object.data.bevel_depth = 0.0
            bpy.context.object.data.extrude = 0
            bpy.context.object.data.offset = 0


        if self.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False 

        self.report({'INFO'}, 'Curve Bevel!')
        return {'FINISHED'}

