import bpy


class RTS_OT_RePattern_Units_Metric(bpy.types.Operator):
    """set units: metric 0.01 cm"""
    bl_idname = "rts_ot.units_metric_cm"
    bl_label = "Metric 0.01"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.scale_length = 0.01
        bpy.context.scene.unit_settings.length_unit = 'CENTIMETERS'
        bpy.context.space_data.overlay.grid_lines = 10
        bpy.context.space_data.overlay.grid_scale = 0.01
        bpy.context.space_data.overlay.grid_subdivisions = 10
        bpy.context.space_data.clip_end = 10000
        
        self.report({'INFO'}, "Units: Metric 0.01cm!") 
        return {'FINISHED'}

