import bpy
from ..utilities.utils import get_prefs
from ..icons.fabric import get_icon_id_fabric


# PANEL
def draw_id_fabric_ui(layout, box):    

    box.separator() 

    row = box.row(align=True)
    row.alignment = 'CENTER' 
    row.scale_x = 1.2    
    row.scale_y = 1.2        
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_darkgreen")).mode = 'Darkgreen' 
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_hunter")).mode = 'Hunter'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_thyme")).mode = 'Thyme'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_grass_1")).mode = 'Grass_1'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_lightgreen")).mode = 'Lightgreen'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_ino_1")).mode = 'Ino_1'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                           
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_ino_2")).mode = 'Ino_2'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_grass_2")).mode = 'Grass_2'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_salvia")).mode = 'Salvia'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_pistachio")).mode = 'Pistachio'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_limette")).mode = 'Limette'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_lemon")).mode = 'Lemon'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_bluedark")).mode = 'Bluedark'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_darknavy")).mode = 'Darknavy'        
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_darkroyal_blue_2")).mode = 'Darkroyal_blue_2'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_royal_blue")).mode = 'Royal_blue'         
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_darkroyal_blue_1")).mode = 'Darkroyal_blue_1'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_blue")).mode = 'Blue'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_ice")).mode = 'Ice'         
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_mint")).mode = 'Mint'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_lightblue")).mode = 'Lightblue'        
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_grapes")).mode = 'Grapes'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_lightplum")).mode = 'Lightplum'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_lilac")).mode = 'Lilac'      
                
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_Chocolate")).mode = 'Chocolate'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_basalt")).mode = 'Basalt'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_morel")).mode = 'Morel'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_brown")).mode = 'Brown'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_noisette")).mode = 'Noisette'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_hazelnunt")).mode = 'Hazelnunt'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_beige")).mode = 'Beige' 
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_champanger")).mode = 'Champanger'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_ivory")).mode = 'Ivory'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_burgund")).mode = 'Burgund'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_Chestnut")).mode = 'Chestnut'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_caramell")).mode = 'Caramell'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_red")).mode = 'Red'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_scarlet")).mode = 'Scarlet'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_raspberry")).mode = 'Raspberry'        
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_fuchsia")).mode = 'Fuchsia'        
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_watermelone")).mode = 'Watermelone'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_orange")).mode = 'Orange'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_orangered")).mode = 'Orangered'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_cayenne")).mode = 'Cayenne'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_peach")).mode = 'Peach'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_rose")).mode = 'Rose'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_blossom")).mode = 'Blossom'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_perlrosa")).mode = 'Perlrosa'       

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_mustard")).mode = 'Mustard'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_gold")).mode = 'Gold'             
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_yelloworange")).mode = 'Yelloworange'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_corn")).mode = 'Corn'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_blumblebee")).mode = 'Bumblebee'        
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_sungold")).mode = 'Sungold'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_daffoldil")).mode = 'Daffoldil'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_canary")).mode = 'Canary'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_lemongrass")).mode = 'Lemongrass'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_banana")).mode = 'Banana'       
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_vanille")).mode = 'Vanille'      
    row.operator("rts_ot.repattern_shader_fabric", text="", icon_value=get_icon_id_fabric("fabric_creme")).mode = 'Creme'      

    box.separator()  
