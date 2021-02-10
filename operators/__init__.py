import bpy
from bpy.app.handlers import persistent
from bpy.props import *


from .ot_array_mods import *                       
from .ot_array import *                                         
from .ot_camera import * 
from .ot_cleanup import *  
from .ot_cloning import *
from .ot_collection import *
from .ot_curve_2d import *
from .ot_curve_add import *
from .ot_curve_bevel import *
from .ot_curve_overlay import *
from .ot_delets import *
from .ot_display import *
from .ot_editor import * 
from .ot_fake import * 
from .ot_grid import *  
from .ot_hdri_render import *
from .ot_instance import *
from .ot_lights import *  
from .ot_lock import *
from .ot_message import *
from .ot_normals import *
from .ot_origin import *  
from .ot_render import *   
from .ot_reset import *
from .ot_select import *
from .ot_units import *


classes = (
    RTS_OT_RePattern_Modifier_XYZ_Array,
    RTS_OT_RePattern_Modifier_Apply_Array,
    RTS_OT_RePattern_Modifier_Remove_Array,
    RTS_OT_RePattern_Modifier_Remove_All_Array, 
    RTS_OT_RePattern_Modifier_Arrays,
    RTS_OT_RePattern_Modifier_Scale,
    RTS_OT_RePattern_Modifier_Offset,
    RTS_OT_RePattern_Camera,
    RTS_OT_RePattern_Camera_Jump,
    RTS_OT_RePattern_Camera_Align,
    RTS_OT_RePattern_Camera_Remove,
    RTS_OT_RePattern_CleanUp_Outside,
    RTS_OT_RePattern_Cutout_Center,
    RTS_OT_RePattern_Cloning,
    RTS_OT_RePattern_Coll_Collapse,  
    RTS_OT_RePattern_Coll_Selection,   
    RTS_OT_RePattern_Curve_Extrude_2d,
    RTS_OT_RePattern_Curve_Beveled,
    RTS_OT_RePattern_Curve_Wire,
    RTS_OT_RePattern_Curve_Bevel,
    RTS_OT_RePattern_Curve_Purge,
    RTS_OT_RePattern_Curve_Enable_Bevel,
    RTS_OT_RePattern_Curve_Quader,
    RTS_OT_RePattern_Curve_Half_Circle,
    RTS_OT_RePattern_Curve_Convert_to_Mesh,
    RTS_OT_RePattern_Curve_Lathe,
    RTS_OT_RePattern_Curve_Origin_Start,
    RTS_OT_RePattern_Curve_Extrude,
    RTS_OT_RePattern_Curve_Toggle_Bevel,
    RTS_OT_RePattern_Curve_Display_Point,
    RTS_OT_RePattern_Purge_Groups,
    RTS_OT_RePattern_Set_Shading,
    RTS_OT_RePattern_Set_Wire,
    RTS_OT_RePattern_Open_Editor,
    RTS_OT_RePattern_FakeOps,
    RTS_OT_RePattern_Grid_Reference,
    RTS_OT_RePattern_Grid_Sub,
    RTS_OT_RePattern_Instances,
    RTS_OT_RePattern_Instances_Merge,
    RTS_OT_RePattern_Instances_Separate,
    RTS_OT_RePattern_Instances_Draw_Type,
    RTS_OT_RePattern_Light_Add,
    RTS_OT_RePattern_Light_Jump,
    RTS_OT_RePattern_Light_Remove,
    RTS_OT_RePattern_Light_Selection,
    RTS_OT_RePattern_Light_Constraints,
    RTS_OT_RePattern_Light_Restrict,
    RTS_OT_RePattern_Light_Bake,
    RTS_OT_RePattern_Transform_Lock, 
    RTS_OT_RePattern_Normals,  
    RTS_OT_RePattern_Origin_BBox,
    RTS_OT_RePattern_Origin_Cursor_Align,
    RTS_OT_RePattern_Render_Presets,  
    RTS_OT_RePattern_Freeze,
    RTS_OT_RePattern_Unfreeze,
    RTS_OT_RePattern_Units_Metric,
    RTS_OT_RePattern_Report,
    RTS_OT_RePattern_Reset_3D_View,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.collection_rp_select_list = bpy.props.StringProperty(name="List", default="RePattern")    
    bpy.types.Scene.collection_rp_select_list_lights = bpy.props.StringProperty(name="List", default="RP_Light_Top")    
    bpy.types.Scene.collection_rp_select_list_cameras = bpy.props.StringProperty(name="List", default="RP_Camera_Top")    
    bpy.types.Scene.use_preview_for_render = bpy.props.BoolProperty(default=False, name="Render Viewport HDRI", description="If checked, the preview HDRI will be used for rendering")

    bpy.app.handlers.render_init.append(setup_hdri_for_render)
    bpy.app.handlers.render_post.append(remove_hdri_after_render)

    bpy.types.CYCLES_WORLD_PT_surface.append(draw_option)
    bpy.types.EEVEE_WORLD_PT_surface.append(draw_option) 

def unregister_operators():
    del bpy.types.Scene.collection_rp_select_list
    del bpy.types.Scene.collection_rp_select_list_lights
    del bpy.types.Scene.collection_rp_select_list_cameras
    del bpy.types.Scene.use_preview_for_render

    bpy.app.handlers.render_init.remove(setup_hdri_for_render)
    bpy.app.handlers.render_post.remove(remove_hdri_after_render)

    bpy.types.CYCLES_WORLD_PT_surface.remove(draw_option)
    bpy.types.EEVEE_WORLD_PT_surface.remove(draw_option)

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
