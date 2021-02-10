import bpy
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty

# RP: CAMERA # 
class PropsGroup_Origin(bpy.types.PropertyGroup):

    box_level : EnumProperty(
        items=[("top"     ,"Top"     ,"constraint XY-Axis / plus Z-Axis"),
               ("middle"  ,"Middle"  ,"constraint XY-Axis / zero Z-Axis"),
               ("bottom"  ,"Bottom"  ,"constraint XY-Axis / minus Z-Axis")],
               name = " ",
               default = "middle")

    origin_location : EnumProperty( 
        items = [("center",         "center",  "center",    "BLANK1", 0),
                ("minus_y",         "--y",     "--y",       "BLANK1", 1), 
                ("minus_y_minus_x", "--y--x",  "--y--x",    "BLANK1", 2), 
                ("minus_x",         "--x",     "--x",       "BLANK1", 3), 
                ("plus_y_minus_x",  "+y--x",   "+y--x",     "BLANK1", 4), 
                ("plus_y",          "+y",      "+y",        "BLANK1", 5), 
                ("plus_y_plus_x",   "+y+x",    "+y+x",      "BLANK1", 6), 
                ("plus_x",          "+x",      "+x",        "BLANK1", 7),
                ("minus_y_plus_x",  "--x",     "--x",       "BLANK1", 8)],
                name = "bbox origin",  
                default = "center",  
                description=" ")     


    loc_x : BoolProperty (name = "Align to X axis", default= False, description= "Enable X axis alignment")
    loc_y : BoolProperty (name = "Align to Y axis", default= False, description= "Enable Y axis alignment")                               
    loc_z : BoolProperty (name = "Align to Z axis", default= False, description= "Enable Z axis alignment")

    loc_offset : FloatVectorProperty(name="Location Offset", description="Offset for location align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)       
