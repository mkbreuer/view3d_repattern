import bpy
from bpy.props import StringProperty, EnumProperty, BoolProperty, FloatProperty

# RP: LIGHT #  
class PropsGroup_Light(bpy.types.PropertyGroup):

    light_mode : StringProperty(default="")

    light_reso : EnumProperty( 
        items = [
                ("1024px", "1m",     "1024px/26dpi/1m",    "", 1), 
                ("2048px", "2m",     "2048px/26dpi/2m",    "", 2), 
                ("4096px", "4m",     "4096px/26dpi/4m",    "", 3),
                ("custom", "Custom", "custom",             "", 4)],
                name = "Size",  
                default = "1024px",  
                description=" ",
                options={'SKIP_SAVE'})  


    custom_value : FloatProperty(name="Custom Value",  description="use custom value", default=100, min=0.0, max=10000)
    custom_grid : FloatProperty(name="Custom Value",  description="use custom value", default=400, min=0.0, max=10000)
    
    light_radius : FloatProperty(name="Radius",  description="use custom radius", default=300, min=0.0, max=10000)
    light_rotation : BoolProperty(name="Rotation",  description=" ", default=False, options={'SKIP_SAVE'})    

    light_rotation_type : EnumProperty( 
       items = [("45",      "45°",    "", 0),
                ("custom",  "custom", "", 1)],
                name = "Rotation",  
                default = "45",  
                description=" ",
                options={'SKIP_SAVE'})  

    custom_rotation : FloatProperty(name="Custom Value",  description="use custom value", default=400, min=0.0, max=10000)
    custom_switch : BoolProperty(name="single / separated",  description="use custom values", default=False, options={'SKIP_SAVE'})        
    custom_grid : FloatProperty(name="Custom XYZ",  description="use custom value", default=100, min=0.0, max=10000)

    custom_grid_top_x : FloatProperty(name="Top X",  description="use custom value", default= 0, min=-10000, max=10000)                             
    custom_grid_top_y : FloatProperty(name="Top Y",  description="use custom value", default= 0, min=-10000, max=10000)                 
    custom_grid_top_z : FloatProperty(name="Top Z",  description="use custom value", default= 200, min=-10000, max=10000)                    

    custom_vgrid_x : FloatProperty(name="X",  description="use custom value", default= 10, min=-10000, max=10000)                             
    custom_vgrid_y : FloatProperty(name="Y",  description="use custom value", default= 10, min=-10000, max=10000)                 
    custom_vgrid_z : FloatProperty(name="Z",  description="use custom value", default= 10, min=-10000, max=10000)  
    light_vradius : FloatProperty(name="Radius",  description="use custom radius", default=50, min=0.0, max=10000)
    
    # COLLECTION #    
    rb_collection_name_lights : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_lights : StringProperty(name="Parent", description="create custom group name", default="")


    light_shadow : BoolProperty(name="Shadow",  description=" ", default=False, options={'SKIP_SAVE'})    
    light_cascade : BoolProperty(name="Cascade Shadow Map",  description=" ", default=False, options={'SKIP_SAVE'})    
