import bpy
from ..utilities.utils import get_prefs


def mat_utils_tools(self, box, layout): 
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    #mat_prefs = prefs.mat_type
  
    layout.scale_y = panel_prefs.ui_scale_y

    if bpy.context.object.mode == 'EDIT':

        row = box.row(align=True)
        row.operator("object.material_slot_assign", text="Assign")
        row.operator("object.material_slot_select", text="Select")
        row.operator("object.material_slot_deselect", text="Deselect")   

        row = box.row(align=True)
        row.operator('object.material_slot_copy', text='Transfer')    
        row.operator('rts_ot.matutils_replace_material', text='Replace')
        row.operator('rts_ot.matutils_fake_user_set', text='FakeUser') 

        box.separator() 
    
    else:
        row = box.row(align=True)
        row.operator("rts_ot.mat_shader_assign_color", text="Assign")
        row.operator("rts_ot.select_obj_with_active_material", text="Select")
        row.operator("rts_ot.select_obj_with_active_material", text="Deselect")   

        row = box.row(align=True)
        row.operator('rts_ot.matutils_merge_base_names', text='Merge')      
        row.operator('rts_ot.matutils_join_objects', text='Join')   
        row.operator('rts_ot.matutils_change_material_link', text='Change')   

        row = box.row(align=True)
        row.operator('object.material_slot_copy', text='Transfer')    
        row.operator('rts_ot.matutils_replace_material', text='Replace')
        row.operator('rts_ot.matutils_fake_user_set', text='FakeUser')        

        box.separator() 