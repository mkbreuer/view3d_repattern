import bpy
from bpy.props import BoolProperty, FloatVectorProperty


class PropsGroup_Insert(bpy.types.PropertyGroup):

    add_mat : BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    add_random : BoolProperty(name="Add Random",  description="add random materials", default=False, options={'SKIP_SAVE'})    
    add_color : FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor : FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])



