import bpy
import os
import math
import string

from ..properties.props_material import *
from ..utilities.utils import get_prefs


# HEX COLORS #
def draw_id_hex_ui(layout, box):        
   
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    rp_props = bpy.context.window_manager.rp_props_repattern 
  
    box.separator()  
    
    row = box.row(align=True) 
    row.label(text="MAT Count:")        
    row.prop(mat_prefs, "color_ID_count", text="", expand=False)
   
    box.separator()  
    
    row = box.row(align=True) 
    row.label(text="MAT Templates:")    
    row.prop(mat_prefs, "color_ID_templates", text="")
   
    box.separator()  
    
    row = box.row(align=True) 
    row.label(text="Hex Export:")  
    sub = row.row(align=True)
    sub.scale_x = 1
    sub.active = mat_prefs.fake_props  
    sub.label(text='#RRGGBB, #RRGGBB...')
    row.operator("rts_ot.textools_hex_export", text="", icon = 'EXPORT')
      
    box.separator()  
     
    row = box.row(align=True) 
    row.label(text="Hex Import:")
    sub = row.row(align=True)
    sub.scale_x = 1
    sub.active = mat_prefs.fake_props  
    sub.label(text='#RRGGBB, #RRGGBB...')        
    row.operator("rts_ot.textools_hex_import", text="", icon = 'IMPORT')
   
    box.separator()  
    
    row = box.row(align=True) 
    row.label(text="Remove all:")        
    row.operator("rts_ot.textools_color_clear", text="", icon = 'X')

    max_columns = 5
    if mat_prefs.color_ID_count < max_columns:
        max_columns = mat_prefs.color_ID_count

    count = math.ceil(mat_prefs.color_ID_count / max_columns)*max_columns

    for i in range(count):

        if i%max_columns == 0:
            box.separator()  
            row = box.row(align=True)

        col = row.column(align=True)
        #col = box.row(align=True)
        if i < mat_prefs.color_ID_count:
            col.prop(mat_prefs, "color_ID_color_{}".format(i), text="")
            col.operator("rts_ot.textools_color_assign", text="", icon = "FILE_TICK").index = i
           
            #view_layer = bpy.context.view_layer
            active = bpy.context.active_object
            selected = bpy.context.selected_objects    
           
            if active:
                if active in selected:
                    if len(selected) == 1:
                        if active.type == 'MESH':
                            col.operator("rts_ot.textools_color_select", text="", icon = "RESTRICT_SELECT_OFF").index = i
        else:
            col.label(text=" ")

