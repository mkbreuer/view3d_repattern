import bpy
from bpy.props import *

from ..utilities.utils import get_prefs

class RTS_OT_RePattern_Units_Metric(bpy.types.Operator):
    """set default blender units or metric units"""
    bl_idname = "rts_ot.units_metric"
    bl_label = "Scene Units"
    bl_options = {'REGISTER', 'UNDO'}


    def draw(self, context):  
        layout = self.layout.column(align=True)       
        
        prefs = get_prefs()
        grid_prefs = prefs.grid_type  

        row = layout.row(align=True)
        row.label(text="Set System", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.8         
        sub.prop(grid_prefs, 'unit_typ', text='')  

    def execute(self, context):
        
        prefs = get_prefs()
        grid_prefs = prefs.grid_type    

        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.length_unit = 'METERS'
        bpy.context.scene.unit_settings.scale_length = 1.0
        
        bpy.context.space_data.overlay.grid_scale = 0.05
        bpy.context.space_data.overlay.grid_lines = 10
        bpy.context.space_data.overlay.grid_subdivisions = 10
        bpy.context.space_data.clip_end = 1000

        self.report({'INFO'}, "Metrics: Meters!") 
        return {'FINISHED'}

