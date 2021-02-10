import bpy
from bpy.props import StringProperty, EnumProperty

# RP: CAMERA # 
class PropsGroup_Camera(bpy.types.PropertyGroup):

    rb_collection_name_camera : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_camera : StringProperty(name="Parent", description="parent under collection", default="")

    cam_reso : EnumProperty( 
        items = [("32px",   "0.313m", "32px/26dpi/0.313m",  "", 1),
                    ("64px",   "0.625m", "64px/26dpi/0.625m",  "", 2), 
                    ("128px",  "0.125m", "128px/26dpi/0.125m", "", 3), 
                    ("256px",  "0.25m",  "256px/26dpi/0.25m",  "", 4), 
                    ("512px",  "0.5m",   "512px/26dpi/0.5m",   "", 5), 
                    ("1024px", "1m",     "1024px/26dpi/1m",    "", 6), 
                    ("2048px", "2m",     "2048px/26dpi/2m",    "", 7), 
                    ("4096px", "4m",     "4096px/26dpi/4m",    "", 8)],
                    name = "Size",  
                    default = "1024px",  
                    description=" ")  

    cam_lens : EnumProperty( 
        items = [("ortho", "Orthographic", "", 1 ),
                    ("persp",  "Perspective", "", 2)],
                    name = "Lens",  
                    default = "ortho",  
                    description="change camera lens")  

    cam_set : EnumProperty(
        items = [("rp_camera", "Camera",    "", "", 1),
                    ("rp_light",  "Light",     "", "", 2),
                    ("rp_world",  "World",     "", "", 3),
                    ("rp_object", "Objects",   "", "", 4),
                    ("rp_visual", "Visual",    "", "", 5),
                    ("rp_render", "Render",    "", "", 6)],
                    name = "CamLight",  
                    default = "rp_camera",   
                    description="options for camera, light and world")  

    cam_render : EnumProperty(
        items = [("rp_image", "Render Set",  "", "", 1),
                ("rp_opengl", "OpenGl Set", "", "", 2)], 
                name = "Render Settings",
                default = "rp_image",
                description="render settings")