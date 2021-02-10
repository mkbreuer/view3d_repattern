import bpy
from bpy.props import EnumProperty


# RP: RENDER #   
class PropsGroup_Render(bpy.types.PropertyGroup):
 
    render_presets : EnumProperty(
      items = [("reso_a", "32x32px",     "32x32px"),
               ("reso_b", "64x64px",     "64x64px"),
               ("reso_c", "128x128px",   "128x128px"), 
               ("reso_d", "256x256px",   "256x256px"), 
               ("reso_e", "512x512px",   "512x512px"), 
               ("reso_f", "1024x1024px", "1024x1024px"), 
               ("reso_g", "2048x2048px", "2048x2048px"), 
               ("reso_h", "4096x4096px", "4096x4096px")], 
               name = "Render Presets",
               default = "reso_e",
               description="render presets")
