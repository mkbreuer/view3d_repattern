import bpy
from bpy.props import BoolProperty


# RP: TRANSFORM # 
class PropsGroup_Transform(bpy.types.PropertyGroup):

    # TRANSFORM LOCATION: ALIGN / APPLY / LOCK #
    location_x_axis : BoolProperty (name = "Align to X axis", default=False, description= "enable X axis location alignment")
    location_y_axis : BoolProperty (name = "Align to Y axis", default=False, description= "enable Y axis location alignment")                               
    location_z_axis : BoolProperty (name = "Align to Z axis", default=False, description= "enable Z axis location alignment")
    apply_loc : BoolProperty (name = "Apply Location", default=False, description= "apply location transform")
    lock_location_x : BoolProperty (name = "Lock X Location", default=True, description= "lock location transform on x axis")
    lock_location_y : BoolProperty (name = "Lock Y Location", default=True, description= "lock location transform on y axis")                               
    lock_location_z : BoolProperty (name = "Lock Z Location", default=True, description= "lock location transform on z axis")
  
    # TRANSFORM ROTATION: ALIGN / APPLY / LOCK #
    rotation_x : BoolProperty (name = "Align Rotation to X axis", default=False, description= "enable X axis rotation alignment")
    rotation_y : BoolProperty (name = "Align Rotation to Y axis", default=False, description= "enable Y axis rotation alignment")
    rotation_z : BoolProperty (name = "Align Rotation to Z axis", default=False, description= "enable Z axis rotation alignment")
    apply_rot : BoolProperty (name = "Apply Rotation", default=False, description= "apply rotation transform")
    lock_rotation_x : BoolProperty (name = "Lock X Rotation", default=True, description= "lock rotation transform on x axis")
    lock_rotation_y : BoolProperty (name = "Lock Y Rotation", default=True, description= "lock rotation transform on y axis")                               
    lock_rotation_z : BoolProperty (name = "Lock Z Rotation", default=True, description= "lock rotation transform on z axis")
  
    # TRANSFORM SCALE: ALIGN / APPLY / LOCK #
    scale_x : BoolProperty (name = "Match Scale to X axis", default=False, description= "enable X axis scale alignment")
    scale_y : BoolProperty (name = "Match Scale to Y axis", default=False, description= "enable Y axis scale alignment")
    scale_z : BoolProperty (name = "match Scale to Z axis", default=False, description= "enable Z axis scale alignment")
    apply_scale : BoolProperty (name = "Apply Scale", default=False, description= "apply scale transform")  
    lock_scale_x : BoolProperty (name = "Lock X Scale", default=True, description= "lock scale transform on x axis")
    lock_scale_y : BoolProperty (name = "Lock Y Scale", default=True, description= "lock scale transform on y axis")                               
    lock_scale_z : BoolProperty (name = "Lock Z Scale", default=True, description= "lock scale transform on z axis")

    axis_x : BoolProperty (name = "X-Axis", default=True, description= "enable X axis")
    axis_y : BoolProperty (name = "Y-Axis", default=False, description= "enable Y axis")                               
    axis_z : BoolProperty (name = "Z-Axis", default=False, description= "enable Z axis")