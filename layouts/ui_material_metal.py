import bpy
from ..utilities.utils import get_prefs
from ..icons.metal import get_icon_id_metal



# METAL COLORS #
def draw_id_metal_ui(layout, box):        

    box.separator()  

    row = box.column_flow(columns=2, align=False) 
    row.scale_x = 1.2    
    row.scale_y = 1.2        
    row.operator("rts_ot.repattern_shader_metal", text="Aluminium", icon_value=get_icon_id_metal("metal_aluminium")).mode = 'Aluminium' 
    row.operator("rts_ot.repattern_shader_metal", text="Beryllium", icon_value=get_icon_id_metal("metal_beryllium")).mode = 'Beryllium'      
    row.operator("rts_ot.repattern_shader_metal", text="Bismuth", icon_value=get_icon_id_metal("metal_bismuth")).mode = 'Bismuth'      
    row.operator("rts_ot.repattern_shader_metal", text="Brass", icon_value=get_icon_id_metal("metal_brass")).mode = 'Brass'      
    row.operator("rts_ot.repattern_shader_metal", text="Bronze", icon_value=get_icon_id_metal("metal_bronze")).mode = 'Bronze'           
    row.operator("rts_ot.repattern_shader_metal", text="Chromium", icon_value=get_icon_id_metal("metal_chromium")).mode = 'Chromium'         
    row.operator("rts_ot.repattern_shader_metal", text="Cobalt", icon_value=get_icon_id_metal("metal_cobalt")).mode = 'Cobalt'      
    row.operator("rts_ot.repattern_shader_metal", text="Copper", icon_value=get_icon_id_metal("metal_copper")).mode = 'Copper'       
    row.operator("rts_ot.repattern_shader_metal", text="Gallium", icon_value=get_icon_id_metal("metal_gallium")).mode = 'Gallium'       
    row.operator("rts_ot.repattern_shader_metal", text="Germanium", icon_value=get_icon_id_metal("metal_germanium")).mode = 'Germanium'       
    row.operator("rts_ot.repattern_shader_metal", text="Gold", icon_value=get_icon_id_metal("metal_gold")).mode = 'Gold'      
    row.operator("rts_ot.repattern_shader_metal", text="Iridium", icon_value=get_icon_id_metal("metal_iridium")).mode = 'Iridium'           
    row.operator("rts_ot.repattern_shader_metal", text="Iron", icon_value=get_icon_id_metal("metal_iron")).mode = 'Iron' 
    row.operator("rts_ot.repattern_shader_metal", text="Lead", icon_value=get_icon_id_metal("metal_lead")).mode = 'Lead'      
    row.operator("rts_ot.repattern_shader_metal", text="Lithium", icon_value=get_icon_id_metal("metal_lithium")).mode = 'Lithium'       
    row.operator("rts_ot.repattern_shader_metal", text="Mercury", icon_value=get_icon_id_metal("metal_mercury")).mode = 'Mercury'      
    row.operator("rts_ot.repattern_shader_metal", text="Molybdenum", icon_value=get_icon_id_metal("metal_molybdenum")).mode = 'Molybdenum'      
    row.operator("rts_ot.repattern_shader_metal", text="Nickel", icon_value=get_icon_id_metal("metal_nickel")).mode = 'Nickel'         
    row.operator("rts_ot.repattern_shader_metal", text="Palladium", icon_value=get_icon_id_metal("metal_palladium")).mode = 'Palladium'      
    row.operator("rts_ot.repattern_shader_metal", text="Platinum", icon_value=get_icon_id_metal("metal_platinum")).mode = 'Platinum'        
    row.operator("rts_ot.repattern_shader_metal", text="Silver", icon_value=get_icon_id_metal("metal_silver")).mode = 'Silver'       
    row.operator("rts_ot.repattern_shader_metal", text="Titanium", icon_value=get_icon_id_metal("metal_titanium")).mode = 'Titanium'      
    row.operator("rts_ot.repattern_shader_metal", text="Zinc", icon_value=get_icon_id_metal("metal_zinc")).mode = 'Zinc'            
    row.operator("rts_ot.repattern_shader_metal", text="Zirconium", icon_value=get_icon_id_metal("metal_zirconium")).mode = 'Zirconium'      

    box.separator()  

