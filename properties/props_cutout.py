import bpy
from bpy.props import BoolProperty, FloatProperty, EnumProperty


# RP: CUTOUT #
class PropsGroup_Cutout(bpy.types.PropertyGroup):

        cutout_reso : EnumProperty( 
        items = [("32px",   "0.313m", "32px/26dpi/0.313m",  "", 1),
                ("64px",    "0.625m", "64px/26dpi/0.625m",  "", 2), 
                ("128px",   "0.125m", "128px/26dpi/0.125m", "", 3), 
                ("256px",   "0.25m",  "256px/26dpi/0.25m",  "", 4), 
                ("512px",   "0.5m",   "512px/26dpi/0.5m",   "", 5), 
                ("1024px",  "1m",     "1024px/26dpi/1m",    "", 6), 
                ("2048px",  "2m",     "2048px/26dpi/2m",    "", 7), 
                ("4096px",  "4m",     "4096px/26dpi/4m",    "", 8),
                ("custom",  "Custom", "custom",             "", 9)],
                name = "CutOut Size",  
                default = "1024px",  
                description=" ")  

        custom_cutout : FloatProperty(name="Custom Value",  description="use custom value = radius of subgrid / default 1k", default=50, min=0.0, max=1000)
        cutout_edit : BoolProperty(name="Editmode",  description="toggle to editmode", default=False, options={'SKIP_SAVE'})  

