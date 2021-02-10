import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty


# MIFT CLONING #
class PropsGroup_Clone(bpy.types.PropertyGroup):
    
    rb_collection_name_clone : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_clone : StringProperty(name="Parent", description="parent under collection", default="")

    create_clones : IntProperty(default=8, min=2, max=300)
    create_last_clone : BoolProperty(name="Create Last Clone", description="create last clone...", default=False)
    radial_clones_angle : FloatProperty(default=360.0, min=-360.0, max=360.0)
    make_single : BoolProperty(name="Unlink", description="unlink instances", default=False)
    object_join : BoolProperty(name="Join", description="join instances", default=False)
 
    radial_clones_axis : EnumProperty(
        items=(('X', 'X', ''),
               ('Y', 'Y', ''),
               ('Z', 'Z', '')),
               default = 'Z')

    radial_clones_axis_type : EnumProperty(
        items=(('Global', 'Global', ''),
               ('Local', 'Local', '')),
               default = 'Global')

    lock_clones : BoolProperty(name="NoSelect",  description="restrict viewport selection for instances", default=True)   
    make_single : BoolProperty(name="Unlink", description="unlink instances", default=False)
    object_join : BoolProperty(name="Join", description="join instances", default=False)
    editmode_toggle_clones : BoolProperty(name="Editmode", description="toggle to editmode", default=True)   
    wired_clones : BoolProperty(name="Wired",  description="set display draw type: wire", default=False)   
    parent_clones : BoolProperty(name="Parent",  description="parent clones to selected", default=False)  
    collapse_toggle : BoolProperty(name="Close Collections", description="close all collections", default=False)   
    collapse_parent : BoolProperty(name="Parent Collections", description="parent to scene or under child collections", default=False)   
    purge_data : BoolProperty(name="",  description="purge unused after deleting objects from collection", default=True) 