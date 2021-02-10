import bpy
from bpy.props import BoolProperty, StringProperty


class PropsGroup_Collection(bpy.types.PropertyGroup):

    rp_hide_select : BoolProperty(name="",  description="toggle selection", default=False) 
    rp_hide_view : BoolProperty(name="",  description="toggle hide", default=False) 
    rp_hide_viewport : BoolProperty(name="",  description="toggle viewport", default=False) 
    rp_hide_render : BoolProperty(name="",  description="toggle hide render", default=False) 
    rp_holdout : BoolProperty(name="",  description="toggle holdout", default=False) 
    rp_indirect_only : BoolProperty(name="",  description="toggle indirect only", default=False) 
    delete_coll : BoolProperty(name="",  description="delete collection from outliner", default=False) 

    rp_hide_select_obj : BoolProperty(name="",  description="toggle selection", default=False) 
    rp_hide_view_obj : BoolProperty(name="",  description="toggle hide", default=False) 
    rp_hide_viewport_obj : BoolProperty(name="",  description="toggle viewport", default=False) 
    rp_hide_render_obj : BoolProperty(name="",  description="toggle hide render", default=False) 
    delete_selected : BoolProperty(name="",  description="delete object from scene", default=False) 

    purge_data : BoolProperty(name="",  description="purge unused data after deleting object from scene", default=True) 

    collection_rp_select_list = StringProperty(name="List", default="Collection")    
    collection_rp_select : StringProperty(name="Name", default="*name*", description="select all objects in a collection and make one active")

    rb_collection_name_source : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_source : StringProperty(name="Parent", description="create custom group name", default="")

    collapse_toggle : BoolProperty(name="Close Collections", description="close all collections", default=False)   
    collapse_parent : BoolProperty(name="Parent Collections", description="parent to scene or under child collections", default=False)   

