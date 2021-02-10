import bpy


from .mat_utils import *
from .mat_hex_assign import *
from .mat_hex_clear import *
from .mat_hex_io import *
from .mat_hex_select import *
from .mat_ops_assign import *
from .mat_ops_delete import *
from .mat_ops_selection import *
from .mat_ops_nodes import *
from .mat_shader import *
from .mat_shader_custom import *
from .mat_shader_circle import *
from .mat_shader_fabric import *
from .mat_shader_metal import *
from .mat_shader_object import *
from .mat_shader_pencil import *
from .mat_shader_wood import *
from .mat_shader_reset import *
from .matu_functions import *
from .matu_operators import *
#from .temp import *


# REGISTRY
classes = (
    RTS_OT_RePattern_Material_Delete,
    RTS_OT_RePattern_Material_Dots_Stroke,    
    RTS_OT_RePattern_Material_Select,
    RTS_OT_RePattern_Material_Select_BSDF,
    RTS_OT_RePattern_Shader_Material,
    RTS_OT_RePattern_Shader_Assign,
    RTS_OT_RePattern_Shader_Assign_Color,
    RTS_OT_RePattern_BSDF_Use_Nodes,
    RTS_OT_RePattern_Emission_Use_Nodes,
    RTS_OT_RePattern_Hex_Color_Assign,
    RTS_OT_RePattern_Hex_Color_Clear,
    RTS_OT_RePattern_Hex_Export,
    RTS_OT_RePattern_Hex_Import,
    RTS_OT_RePattern_Tex_Color_Select, 
    RTS_OT_Repattern_Shader_Custom,
    RTS_OT_Repattern_Shader_Circle,
    RTS_OT_Repattern_Shader_Fabric,
    RTS_OT_Repattern_Shader_Metal, 
    RTS_OT_Repattern_Shader_Object, 
    RTS_OT_Repattern_Shader_Pencil, 
    RTS_OT_Repattern_Shader_Wood,    
    RTS_OT_RePattern_Shader_Reset_Props,
    RTS_MT_RePattern_Material_List, 
    RTS_UL_RePattern_Material_Preview, 

    RTS_OT_MATUTILS_assign_material_edit,
    RTS_OT_MATUTILS_assign_material_object,
    RTS_OT_MATUTILS_select_by_material_name,
    RTS_OT_MATUTILS_copy_material_to_others,
    RTS_OT_MATUTILS_clean_material_slots,
    RTS_OT_MATUTILS_remove_material_slot,
    RTS_OT_MATUTILS_remove_all_material_slots,
    RTS_OT_MATUTILS_replace_material,
    RTS_OT_MATUTILS_fake_user_set,
    RTS_OT_MATUTILS_change_material_link,
    RTS_OT_MATUTILS_merge_base_names,
    RTS_OT_MATUTILS_material_slot_move,
    RTS_OT_MATUTILS_join_objects,
    RTS_OT_MATUTILS_auto_smooth_angle,    
)


def register_material():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_material():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

