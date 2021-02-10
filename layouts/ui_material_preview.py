import bpy
from ..utilities.utils import get_prefs

from ..materials.mat_utils import *
from ..layouts.ui_material_utils import mat_utils_tools

def mat_preview_shader(self, box, layout):
    layout.operator_context = 'INVOKE_REGION_WIN'
    
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    mat_prefs = prefs.mat_type
  
    layout.scale_y = panel_prefs.ui_scale_y
    
    box.separator()   

    view_layer = bpy.context.view_layer        
    obj = view_layer.objects.active                              
       
    row = box.row(align=True)                   
    row.prop(mat_prefs, 'switch_matlib_preview', text="", icon="FILE_REFRESH")  
    row.menu("rts_mt.material_list", text="Material List", icon="COLLAPSEMENU")   
    if bpy.context.object.mode != 'EDIT':
        row.operator('rts_ot.matutils_auto_smooth_angle', text='', icon="AUTO")    
    row.menu("MATERIAL_MT_context_menu", icon='DOWNARROW_HLT', text="")         
    
    box.separator()               
                
    row = box.row()                              
    if mat_prefs.switch_matlib_preview == False:                      
        row.template_list("MATERIAL_UL_matslots", "", obj, "material_slots", obj, "active_material_index", rows=4)                                 
    else:
        row.template_list("RTS_UL_RePattern_Material_Preview", "compact", obj, "material_slots",  obj, "active_material_index", type='GRID', rows=4, columns=6)                 
     
    col = row.column(align=True)                            
    col.operator("object.material_slot_add", icon='ADD', text="") 
    col.operator("rts_ot.remove_all_material", icon='REMOVE', text="").mode='mat_slots_single'
    col.operator("object.material_slot_move", icon='TRIA_UP', text="").direction = 'UP'
    col.operator("object.material_slot_move", icon='TRIA_DOWN', text="").direction = 'DOWN'      
    col.menu("RTS_MT_RePattern_MAT_Delete", text="", icon ="ORPHAN_DATA")
    
    box.separator()  
   
    mat_utils_tools(self, box, layout)
    
    row = box.row(align=True)
    row.operator('rts_ot.select_bsdf_node', text="", icon='NODE')
    row.template_ID(obj, "active_material", new="material.new")

    box.separator()  
