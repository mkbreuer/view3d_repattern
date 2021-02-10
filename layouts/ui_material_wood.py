import bpy
from ..utilities.utils import get_prefs
from ..icons.wood import get_icon_id_wood

# PANEL
def draw_id_wood_ui(layout, box):  

    box.separator()  

    # CONTRAST # 
    #row = box.column(align=True) 
    #row = box.column_flow(columns=2, align=False)   
    row = box.grid_flow(row_major=False, columns=2, even_columns=False, even_rows=False, align=False)   
    row.scale_x = 1.1    
    row.scale_y = 1.1
    row.operator("rts_ot.repattern_shader_wood", text="Acacia Steamed",  icon_value=get_icon_id_wood("wood_acacia_steamed")).mode="Acacia_steamed"
    row.operator("rts_ot.repattern_shader_wood", text="Apple India",     icon_value=get_icon_id_wood("wood_apple_india")).mode="Apple_india" 
    row.operator("rts_ot.repattern_shader_wood", text="Ash",             icon_value=get_icon_id_wood("wood_ash")).mode="Ash"            
    row.operator("rts_ot.repattern_shader_wood", text="Bamboo Steamed",  icon_value=get_icon_id_wood("wood_bamboo_steamed")).mode="Bamboo_steamed"                  
    row.operator("rts_ot.repattern_shader_wood", text="Bangkirai",       icon_value=get_icon_id_wood("wood_bangkirai")).mode="Bangkirai"                  
    row.operator("rts_ot.repattern_shader_wood", text="Beech Steamed",   icon_value=get_icon_id_wood("wood_beech_steamed")).mode="Beech_steamed"                  
    row.operator("rts_ot.repattern_shader_wood", text="Cherry_amer",     icon_value=get_icon_id_wood("wood_cherry_amer")).mode="Cherry_amer"                  
    row.operator("rts_ot.repattern_shader_wood", text="Cherry_eur",      icon_value=get_icon_id_wood("wood_cherry_eur")).mode="Cherry_eur"                  
    row.operator("rts_ot.repattern_shader_wood", text="Cumaru",          icon_value=get_icon_id_wood("wood_cumaru")).mode="Cumaru"    
    row.operator("rts_ot.repattern_shader_wood", text="Doussie",         icon_value=get_icon_id_wood("wood_doussie")).mode="Doussie"
    row.operator("rts_ot.repattern_shader_wood", text="Garapa",          icon_value=get_icon_id_wood("wood_garapa")).mode="Garapa"
    row.operator("rts_ot.repattern_shader_wood", text="Ipe",             icon_value=get_icon_id_wood("wood_ipe")).mode="Ipe"                
    row.operator("rts_ot.repattern_shader_wood", text="Iroko Kambala",   icon_value=get_icon_id_wood("wood_iroko_kambala")).mode="Iroko_kambala"                  
    row.operator("rts_ot.repattern_shader_wood", text="Jacaranda",       icon_value=get_icon_id_wood("wood_jacaranda")).mode="Jacaranda"                     
    row.operator("rts_ot.repattern_shader_wood", text="Jatoba",          icon_value=get_icon_id_wood("wood_jatoba")).mode="Jatoba"                  
    row.operator("rts_ot.repattern_shader_wood", text="Kempas",          icon_value=get_icon_id_wood("wood_kempas")).mode="Kempas"                  
    row.operator("rts_ot.repattern_shader_wood", text="Larch",           icon_value=get_icon_id_wood("wood_larch")).mode="Larch"                  
    row.operator("rts_ot.repattern_shader_wood", text="Macassar",        icon_value=get_icon_id_wood("wood_macassar")).mode="Macassar"    
    row.operator("rts_ot.repattern_shader_wood", text="Maple can.",      icon_value=get_icon_id_wood("wood_maple_can")).mode="Maple_can"
    row.operator("rts_ot.repattern_shader_wood", text="Maple eur.",      icon_value=get_icon_id_wood("wood_maple_eur")).mode="Maple_eur"
    row.operator("rts_ot.repattern_shader_wood", text="Massaranduba",    icon_value=get_icon_id_wood("wood_massaranduba")).mode="Massaranduba"                
    row.operator("rts_ot.repattern_shader_wood", text="Merbau",          icon_value=get_icon_id_wood("wood_merbau")).mode="Merbau"                  
    row.operator("rts_ot.repattern_shader_wood", text="Oak",             icon_value=get_icon_id_wood("wood_oak")).mode="Oak"                     
    row.operator("rts_ot.repattern_shader_wood", text="Oak Darkbrown",   icon_value=get_icon_id_wood("wood_oak_darkbrown")).mode="Oak_darkbrown"                  
    row.operator("rts_ot.repattern_shader_wood", text="Oak Middlebraun", icon_value=get_icon_id_wood("wood_oak_middlebraun")).mode ="Oak_middlebraun"                  
    row.operator("rts_ot.repattern_shader_wood", text="Oak Redbrown",    icon_value=get_icon_id_wood("wood_oak_redbrown")).mode="Oak_redbrown"                  
    row.operator("rts_ot.repattern_shader_wood", text="Oak Smoked",      icon_value=get_icon_id_wood("wood_oak_smoked_core")).mode="Oak_smoked_core"    
    row.operator("rts_ot.repattern_shader_wood", text="Oak_white",       icon_value=get_icon_id_wood("wood_oak_white")).mode="Oak_white"
    row.operator("rts_ot.repattern_shader_wood", text="Olive",           icon_value=get_icon_id_wood("wood_olive")).mode="Olive"
    row.operator("rts_ot.repattern_shader_wood", text="Panga Panga",     icon_value=get_icon_id_wood("wood_panga_panga")).mode="Panga_panga"                 
    row.operator("rts_ot.repattern_shader_wood", text="Pear",            icon_value=get_icon_id_wood("wood_pear")).mode="Pear"                  
    row.operator("rts_ot.repattern_shader_wood", text="Teak",            icon_value=get_icon_id_wood("wood_teak")).mode="Teak"                  
    row.operator("rts_ot.repattern_shader_wood", text="Walnut amer.",    icon_value=get_icon_id_wood("wood_walnut_amer")).mode="Walnut_amer"                  
    row.operator("rts_ot.repattern_shader_wood", text="Walnut eur.",     icon_value=get_icon_id_wood("wood_walnut_eur")).mode="Walnut_eur"                  
    row.operator("rts_ot.repattern_shader_wood", text="Wenge",           icon_value=get_icon_id_wood("wood_wenge")).mode="Wenge"                  
    row.operator("rts_ot.repattern_shader_wood", text="Willow",          icon_value=get_icon_id_wood("wood_willow")).mode="Willow"    
    row.operator("rts_ot.repattern_shader_wood", text="Zebrano",         icon_value=get_icon_id_wood("wood_zebrano")).mode="Zebrano"    

    box.separator()  
