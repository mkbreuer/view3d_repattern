import bpy
from bpy.props import StringProperty, EnumProperty, BoolProperty, IntProperty, FloatProperty

# RP: GRID / SUBGRID #  
class PropsGroup_Grid(bpy.types.PropertyGroup):

    # UNITS # 
    unit_typ : EnumProperty( 
        items = [("metric", "Metric", "1m = 1BU = 1024px"),
                 ("none",   "None",   "1BU = 1m = 1024px")],
                 name = "Unit Sytem",  
                 default = "metric",  
                 description="unit system for interface controls")  

    u_lenght : EnumProperty( 
        items = [("meters", "Meters",      ""),
                 ("centi",  "Centimeters", "")],
                 name = "Unit Length",  
                 default = "meters",  
                 description="unit system for interface controls")  
  
  
    collapse_toggle : BoolProperty(name="Close Collections", description="close all collections", default=False)   
    collapse_parent : BoolProperty(name="Parent Collections", description="parent to scene or under child collections", default=False)   
   
    # GRID # 
    grid : IntProperty(name="Div XY",  description=" ", min=0, max=40, default=3)                                 
    lock_grid : BoolProperty(name="NoSelect",  description="restrict viewport selection", default=True, options={'SKIP_SAVE'})   
    render_grid : BoolProperty(name="NoRender",  description="restrict rendering", default=True, options={'SKIP_SAVE'})  
    pock_grid : BoolProperty(name="Pock",  description="add a triangulate wired grid", default=False, options={'SKIP_SAVE'})  
    grid_snappoints : BoolProperty(name="Snap",  description="add vertices as snap points to the grid", default=False, options={'SKIP_SAVE'})  
    grid_div : IntProperty(name="Div",  description="subdivide wired grid", min=1, max=10, default=1) 
    grid_z_offset : BoolProperty(name="Z Offset", description="set z offset / bottom to xy", default=False, options={'SKIP_SAVE'})    
    custom_grid : FloatProperty(name="Custom Value",  description="use custom value / default for 1k", default=150, min=0.0, max=1000)

    grid_result : EnumProperty( 
       items = [("32px",   "0.313m", "32px/26dpi/0.313m",  "", 1),
                ("64px",   "0.625m", "64px/26dpi/0.625m",  "", 2), 
                ("128px",  "0.125m", "128px/26dpi/0.125m", "", 3), 
                ("256px",  "0.25m",  "256px/26dpi/0.25m",  "", 4), 
                ("512px",  "0.5m",   "512px/26dpi/0.5m",   "", 5), 
                ("1024px", "1m",     "1024px/26dpi/1m",    "", 6), 
                ("2048px", "2m",     "2048px/26dpi/2m",    "", 7), 
                ("4096px", "4m",     "4096px/26dpi/4m",    "", 8),
                ("custom", "Custom", "custom",             "", 9)],
                name = "Size",  
                default = "1024px",  
                description=" ")  


    axis_rota : EnumProperty( 
        items = [("rota_axis_xy", "xy", "xy horizontal"),
                 ("rota_axis_yz", "yz", "yz vertical"  ), 
                 ("rota_axis_xz", "xz", "xz vertical"  )],
                 name = "Axis Rotation",  
                 default = "rota_axis_xy",  
                 description=" ")  

    add_axis : BoolProperty(name="Merge", description="add axis", default=False, options={'SKIP_SAVE'})   
    set_axis_xy : BoolProperty(name="XY", description="xy horizontal", default=True, options={'SKIP_SAVE'})   
    set_axis_yz : BoolProperty(name="YZ", description="yz vertical", default=False, options={'SKIP_SAVE'})   
    set_axis_xz : BoolProperty(name="XZ", description="xz vertical", default=False, options={'SKIP_SAVE'})   
    set_axis_xy : BoolProperty(name="XY", description="xy horizontal", default=True, options={'SKIP_SAVE'})   
    set_axis_wall : BoolProperty(name="Wall", description="shift to canvas", default=False, options={'SKIP_SAVE'})   
    set_axis_cube : BoolProperty(name="Cube", description="create canvas cube", default=False, options={'SKIP_SAVE'})   

    # COLLECTION #    
    rb_collection_name_grid : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_grid : StringProperty(name="Parent", description="create custom group name", default="")


    # SUBGRID #
    subgrid_x : IntProperty(name="Div X",  description="loops on x axis", min=0, max=40, default=3)                                 
    subgrid_y : IntProperty(name="Div Y",  description="loops on y axis", min=0, max=40, default=3)                                 
    lock_subgrid : BoolProperty(name="NoSelect",  description="restrict viewport selection", default=True, options={'SKIP_SAVE'})  
    render_subgrid : BoolProperty(name="NoRender",  description="restrict rendering", default=True, options={'SKIP_SAVE'})  
    pock_subgrid : BoolProperty(name="Pock",  description="add a triangulate wired grid", default=False, options={'SKIP_SAVE'})  
    subgrid_snappoints : BoolProperty(name="Snap",  description="add vertices as snap points to the grid", default=False, options={'SKIP_SAVE'})  
    subgrid_div : IntProperty(name="Div",  description="subdivide wired grid", min=1, max=10, default=1) 
    subgrid_z_offset : BoolProperty(name="Z Offset", description="set z offset / bottom to xy", default=False, options={'SKIP_SAVE'})   

    custom_subgrid : FloatProperty(name="Custom Value",  description="use custom value / default 1k", default=50, min=0.0, max=1000)
 
    grid_result : EnumProperty( 
        items = [("32px",   "0.313m", "subgrid for 0.313m", "", 1),
                ("64px",    "0.625m", "subgrid for 0.625m", "", 2), 
                ("128px",   "0.125m", "subgrid for 0.125m", "", 3), 
                ("256px",   "0.25m",  "subgrid for 0.25m",  "", 4), 
                ("512px",   "0.5m",   "subgrid for 0.5m",   "", 5), 
                ("1024px",  "1m",     "subgrid for 1m",     "", 6), 
                ("2048px",  "2m",     "subgrid for 2m",     "", 7), 
                ("4096px",  "4m",     "subgrid for 4m",     "", 8),
                ("custom",  "Custom", "custom",             "", 9)],
                name = "SubGrid",  
                default = "1024px",  
                description=" ")  

    axis_rota : EnumProperty( 
        items = [("rota_axis_xy", "xy", "xy horizontal"),
                 ("rota_axis_yz", "yz", "yz vertical"  ), 
                 ("rota_axis_xz", "xz", "xz vertical"  )],
                 name = "Axis Rotation",  
                 default = "rota_axis_xy",  
                 description=" ")  

    add_axis : BoolProperty(name="Merge", description="add axis", default=False, options={'SKIP_SAVE'})   
    set_axis_xy : BoolProperty(name="XY", description="xy horizontal", default=True, options={'SKIP_SAVE'})   
    set_axis_yz : BoolProperty(name="YZ", description="yz vertical", default=False, options={'SKIP_SAVE'})   
    set_axis_xz : BoolProperty(name="XZ", description="xz vertical", default=False, options={'SKIP_SAVE'})   
    set_axis_xy : BoolProperty(name="XY", description="xy horizontal", default=True, options={'SKIP_SAVE'})   
    set_axis_wall : BoolProperty(name="Wall", description="shift to canvas", default=False, options={'SKIP_SAVE'})   
    set_axis_cube : BoolProperty(name="Cube", description="create canvas cube", default=False, options={'SKIP_SAVE'})   

    # COLLECTION #    
    rb_collection_name_subgrid : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_subgrid : StringProperty(name="Parent", description="create custom group name", default="")

