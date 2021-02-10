import bpy
from bpy.props import BoolProperty, EnumProperty


# RP: MODIFIER ARRAY #
class PropsGroup_Modifier(bpy.types.PropertyGroup):

    display_array : BoolProperty(name="Open", description="Open", default=False)   
    display_subsurf : BoolProperty(name="Open", description="Open", default=False)   
    display_array_curve : BoolProperty(name="Open", description="Open", default=False)   

    half_scale : BoolProperty(name="Scale 0.5",  description="down scale for array", default=True)       
    origin_minus_xy : BoolProperty(name="Origin -XY",  description="set origin to minus xy", default=False)       

    xy_array : EnumProperty( 
        items = [("32px",  "0.313m", "32px/26dpi/0.313m",  "BLANK1", 1),
                ("64px",   "0.625m", "64px/26dpi/0.625m",  "BLANK1", 2), 
                ("128px",  "0.125m", "128px/26dpi/0.125m", "BLANK1", 3), 
                ("256px",  "0.25m",  "256px/26dpi/0.25m",  "BLANK1", 4), 
                ("512px",  "0.5m",   "512px/26dpi/0.5m",   "BLANK1", 5), 
                ("1024px", "1m",     "1024px/26dpi/1m",    "BLANK1", 6), 
                ("2048px", "2m",     "2048px/26dpi/2m",    "BLANK1", 7), 
                ("4096px", "4m",     "4096px/26dpi/4m",    "BLANK1", 8)],
                name = "Array Size",  
                default = "1024px",  
                description=" ")  

    scale_uncut : BoolProperty(name="Array Uncut",  description="expand array density for uncured instances", default=False)    

    array_x : BoolProperty(name="X-Array", description="add x array modifier", default = True)
    array_y : BoolProperty(name="Y-Array", description="add y array modifier", default = False)
    array_z : BoolProperty(name="Z-Array", description="add z array modifier", default = False)
   
    array_axis : EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"All"  ,"04")],
               name = "Apply Array",
               default = "tp_a",    
               description = "apply modifier array")

    array_scale : EnumProperty( 
        items = [("32px",  "0.313m", "32px/26dpi/0.313m",  "BLANK1", 1),
                ("64px",   "0.625m", "64px/26dpi/0.625m",  "BLANK1", 2), 
                ("128px",  "0.125m", "128px/26dpi/0.125m", "BLANK1", 3), 
                ("256px",  "0.25m",  "256px/26dpi/0.25m",  "BLANK1", 4), 
                ("512px",  "0.5m",   "512px/26dpi/0.5m",   "BLANK1", 5), 
                ("1024px", "1m",     "1024px/26dpi/1m",    "BLANK1", 6), 
                ("2048px", "2m",     "2048px/26dpi/2m",    "BLANK1", 7), 
                ("4096px", "4m",     "4096px/26dpi/4m",    "BLANK1", 8)],
                name = "Xy Scale",  
                default = "1024px",  
                description=" ")  
 
  
    tp_verts_offset : EnumProperty(
        items=[("tp_verts_x"    ,"X Axis"   ,"X Axis"),
               ("tp_verts_y"    ,"Y Axis"   ,"Y Axis"),
               ("tp_verts_xy"   ,"XY Axis"  ,"XY Axis")],
               name = "Offset",
               default = "tp_verts_xy",    
               description = "Add single vertices to correct array offset")

    verts_offset : EnumProperty( 
        items = [("32px",  "0.313m", "32px/26dpi/0.313m",  "BLANK1", 1),
                ("64px",   "0.625m", "64px/26dpi/0.625m",  "BLANK1", 2), 
                ("128px",  "0.125m", "128px/26dpi/0.125m", "BLANK1", 3), 
                ("256px",  "0.25m",  "256px/26dpi/0.25m",  "BLANK1", 4), 
                ("512px",  "0.5m",   "512px/26dpi/0.5m",   "BLANK1", 5), 
                ("1024px", "1m",     "1024px/26dpi/1m",    "BLANK1", 6), 
                ("2048px", "2m",     "2048px/26dpi/2m",    "BLANK1", 7), 
                ("4096px", "4m",     "4096px/26dpi/4m",    "BLANK1", 8)],
                name = "Size",  
                default = "1024px",  
                description=" ")                                

    array_divide : EnumProperty( 
        items = [("two",  "2 Array",  "use for 2 array",  "BLANK1", 1),
                ("three", "3 Array",  "use for 3 array",  "BLANK1", 2), 
                ("four",  "4 Array",  "use for 4 array",  "BLANK1", 3), 
                ("five",  "5 Array",  "use for 5 array",  "BLANK1", 4), 
                ("six",   "6 Array",  "use for 6 array",  "BLANK1", 5), 
                ("seven", "7 Array",  "use for 7 array",  "BLANK1", 6), 
                ("eight", "8 Array",  "use for 8 array",  "BLANK1", 7), 
                ("nine",  "9 Array",  "use for 9 array",  "BLANK1", 8),
                ("ten",   "10 Array", "use for 10 array",  "BLANK1", 9)],
                name = "Div",  
                default = "two",  
                description=" ")   


      