import bpy
from bpy.props import *

from ..utilities.utils import get_prefs

class RTS_OT_RePattern_Units_Metric(bpy.types.Operator):
    """set units to nelnder units or metrics"""
    bl_idname = "rts_ot.units_metric_cm"
    bl_label = "Scene Units"
    bl_options = {'REGISTER', 'UNDO'}


    def draw(self, context):  
        layout = self.layout.column(align=True)       
        
        prefs = get_prefs()
        grid_prefs = prefs.grid_type  

        row = layout.row(align=True)
        row.prop(grid_prefs, 'unit_typ')  

        layout.separator() 

        if grid_prefs.unit_typ == 'metric': 

            row = layout.row(align=True)
            row.prop(grid_prefs, 'u_lenght')  
        
            layout.separator()  


    def execute(self, context):
        
        prefs = get_prefs()
        grid_prefs = prefs.grid_type      

        if grid_prefs.unit_typ == 'metric':     
            bpy.context.scene.unit_settings.system = 'METRIC'
            
            if grid_prefs.u_lenght == 'meters':
                bpy.context.scene.unit_settings.length_unit = 'METERS'
                bpy.context.space_data.overlay.grid_scale = 1
                self.report({'INFO'}, "Metrics: Meters!")                 
            else:
                bpy.context.scene.unit_settings.length_unit = 'CENTIMETERS'       
                bpy.context.space_data.overlay.grid_scale = 0.01
                self.report({'INFO'}, "Metrics: Centimeters!") 

            bpy.context.space_data.overlay.grid_subdivisions = 10
            bpy.context.space_data.clip_end = 1000
            
        else:
            bpy.context.scene.unit_settings.system = 'NONE'
            bpy.context.space_data.overlay.grid_scale = 0.1
            bpy.context.space_data.overlay.grid_subdivisions = 10
            bpy.context.space_data.clip_end = 1000
            bpy.context.scene.unit_settings.use_separate = False        
            self.report({'INFO'}, "Blender Units!") 

        return {'FINISHED'}

