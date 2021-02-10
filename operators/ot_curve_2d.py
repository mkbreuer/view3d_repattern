import bpy
from bpy.props import FloatProperty, IntProperty, BoolProperty


class RTS_OT_RePattern_Curve_Extrude_2d(bpy.types.Operator):
    """create 2d bevel extrude on curve"""
    bl_idname = "rts_ot.curve_extrude_2d"
    bl_label = "Curve Extrude"
    bl_options = {"REGISTER", "UNDO"}

    depth : FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)
    ring : IntProperty(name="Ring",  description=" ", min=0, max=100, default=1) 
    nring : IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop : IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 
    offset : FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height : FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)
    wire : BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    
    convert : BoolProperty(name="Convert to Mesh",  description=" ", default=False, options={'SKIP_SAVE'})   

    def draw(self, context):      
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(align=True)             

        box.separator()        
       
        row = box.row(align=True)                                                                                                                                                                                                                    
        row.operator("rts_ot.dynamic_normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(self, 'depth')
 
        if self.wire == True:
            row.prop(self, 'wire', "", icon = 'MESH_PLANE')              
        else:                       
           row.prop(self, 'wire', "", icon = 'MESH_GRID') 
                    
        row = box.row(align=True)
        row.prop(self, 'ring')  
        row.prop(self, 'loop')

        row = box.row(align=True)
        row.prop(self, 'offset')  
        row.prop(self, 'height')
    
        box.separator()
                    
    def execute(self, context):
 
        # curve extrude    
        if bpy.context.object.mode == "OBJECT":               
            bpy.ops.object.mode_set(mode = 'EDIT')
        
        if bpy.context.object.data.splines.active.use_cyclic_u == True:         
            pass
        else:
            bpy.ops.curve.cyclic_toggle()

        bpy.context.object.data.dimensions = '2D'
        bpy.context.object.data.fill_mode = 'BOTH'
        bpy.context.object.data.bevel_depth = self.depth
        bpy.context.object.data.bevel_resolution = self.ring         
        bpy.context.object.data.resolution_u = self.loop
        bpy.context.object.data.offset = self.offset            
        bpy.context.object.data.extrude = self.height           
        
        # wire visibility
        if self.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False 
                  
        return {"FINISHED"}












