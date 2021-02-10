import bpy
from bpy import *
from bpy.props import *

from ..utilities.utils import get_prefs


class RTS_OT_RePattern_Render_Presets(bpy.types.Operator):
    """set render resolution"""
    bl_idname = "rts_ot.repattern_render_presets"
    bl_label = "Render Presets"
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):  
        layout = self.layout.column(align=True)       
        
        prefs = get_prefs()
        render_props = prefs.render_type  

        box = col.box().column(align=True)          
        box.separator() 

        row = box.row(align=True)
        row.prop(render_props, 'render_presets', text="", icon ="RENDER_REGION")  

        box.separator()  

        row = box.row(align=True)
        row.operator("view3d.viewnumpad", text="CamView", icon ="OUTLINER_DATA_CAMERA").type='CAMERA'
        row.operator("render.render", text="Render", icon='RENDER_STILL')
      
        box.separator()  

       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):     
        prefs = get_prefs()
        render_props = prefs.render_type  

        scene = bpy.context.scene

        if render_props.render_presets == 'reso_a':
            scene.render.resolution_x = 32
            scene.render.resolution_y = 32

        if render_props.render_presets == 'reso_b':
            scene.render.resolution_x = 64
            scene.render.resolution_y = 64

        if render_props.render_presets == 'reso_c':
            scene.render.resolution_x = 128
            scene.render.resolution_y = 128

        if render_props.render_presets == 'reso_d':
            scene.render.resolution_x = 256
            scene.render.resolution_y = 256
            
        if render_props.render_presets == 'reso_e':
            scene.render.resolution_x = 512
            scene.render.resolution_y = 512

        if render_props.render_presets == 'reso_f':
            scene.render.resolution_x = 1024
            scene.render.resolution_y = 1024

        if render_props.render_presets == 'reso_g':
            scene.render.resolution_x = 2048
            scene.render.resolution_y = 2048
            
        if render_props.render_presets == 'reso_h':
            scene.render.resolution_x = 4096
            scene.render.resolution_y = 4096

        scene.render.resolution_percentage = 100  

        #print(self)
        self.report({'INFO'}, "Set Render Preset!")   
        return {'FINISHED'}
