import bpy
from ..utilities.utils import get_prefs
from ..icons.pencils import get_icon_id_pencils


# PANEL
def draw_id_pencil_ui(layout, box):  
    prefs = get_prefs()
    mat_prefs = prefs.mat_type 

    if mat_prefs.display_palette_pencil == 'Autumn':
        draw_pen_autumn_ui(layout, box)   

    if mat_prefs.display_palette_pencil == 'Graphit':
        draw_pen_graphit_ui(layout, box)   

    if mat_prefs.display_palette_pencil == 'Charcoal':
        draw_pen_charcoal_ui(layout, box)   

    if mat_prefs.display_palette_pencil == 'Water':
        draw_pen_water_ui(layout, box)   

    if mat_prefs.display_palette_pencil == 'Inktense':
        draw_pen_inktense_ui(layout, box)   



# AUTUMN COLORS #
def draw_pen_autumn_ui(layout, box):        

    box.separator()  

    #row = box.column_flow(columns=2, align=True)                          
    
    row = box.row(align=True)
    row.alignment = 'CENTER' 
    row.scale_x = 1.2    
    row.scale_y = 1.2        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_light_sienna")).mode = 'Light_Sienna'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_solway_blue")).mode = 'Solway_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_ink_blue")).mode = 'Ink_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_smoke_blue")).mode = 'Smoke_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_pale_cedar")).mode = 'Pale_Cedar'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_green_shadow")).mode = 'Green_Shadow'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                           
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_crag_green")).mode = 'Crag_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_olive_earth")).mode = 'Olive_Earth'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_warm_earth")).mode = 'Warm_Earth'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_brown_ochre")).mode = 'Brown_Ochre'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_wheat")).mode = 'Wheat'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_yellow_ochre")).mode = 'Yellow_Ochre'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                           
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_sepia_red")).mode = 'Sepia_Red'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_mars_orange")).mode = 'Mars_Orange'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_sanguine")).mode = 'Sanguine'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_venetian_red")).mode = 'Venetian_Red'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_terracotta")).mode = 'Terracotta'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_mars_violet")).mode = 'Mars_Violet'   

    row = box.row(align=True) 
    row.alignment = 'CENTER'                           
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_ruby_earth")).mode = 'Ruby_Earth'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_chocolate")).mode = 'Chocolate'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_ivory_black")).mode = 'Ivory_Black'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_warm_gray")).mode = 'Warm_Gray'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_terracotta")).mode = 'Terracotta'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_autumn_cool_gray")).mode = 'Cool_Gray'  

    box.separator()  



# GRAPHITINT COLORS #
def draw_pen_graphit_ui(layout, box):        

    box.separator()  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_port")).mode = 'Port'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_juniper")).mode = 'Juniper'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_aubergine")).mode = 'Aubergine'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_dark_indigo")).mode = 'Dark_Indigo'         
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_cool_gray")).mode = 'Cool_Gray'   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_shadow")).mode = 'Shadow'            
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_steel_blue")).mode = 'Steel_Blue'         
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_ocean_blue")).mode = 'Ocean_Blue'         
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_slate_green")).mode = 'Slate_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_meadow")).mode = 'Meadow' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_ivy")).mode = 'Ivy'                   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_sage")).mode = 'Sage'       
        
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_chestnut")).mode = 'Chestnut'          
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_autumn_brown")).mode = 'Autumn_Brown'               
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_cocoa")).mode = 'Cocoa'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_russet")).mode = 'Russet'           
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_cool_brown")).mode = 'Cool_Brown'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_storm")).mode = 'Storm'       


    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_midnight_black")).mode = 'Midnight_Black'             
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_warm_gray")).mode = 'Warm_Gray'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_mountain_gray")).mode = 'Mountain_Gray'                     
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_graphit_cloud_gray")).mode = 'Cloud_Gray' 
    
    box.separator()  



# TINTED CHARCOAL COLORS # 
def draw_pen_charcoal_ui(layout, box):        

    box.separator()  
                         
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_sand")).mode = 'Sand'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_burnt_orange")).mode = 'Burnt_Orange'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_sunset_pink")).mode = 'Sunset_Pink'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_glowing_embers")).mode = 'Glowing_Embers'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_heather_mist")).mode = 'Heather_Mist'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_burnt_embers")).mode = 'Burnt_Embers'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_lavender")).mode = 'Lavender' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_thistle")).mode = 'Thistle'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_bilberry")).mode = 'Bilberry'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_elderberry")).mode = 'Elderberry'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_slate")).mode = 'Burnt_Earth'    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_ocean_deep")).mode = 'Ocean_Deep'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_slate")).mode = 'Slate' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_mountain_blue")).mode = 'Mountain_Blue'   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_forest_pine")).mode = 'Natural'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_forest_pine")).mode = 'Forest_Pine'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_green_moss")).mode = 'Green_Moss'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_dark_moss")).mode = 'Dark_Moss'      
    
  
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_green_moss")).mode = 'Charcoal_Light'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_dark_moss")).mode = 'Charcoal_Medium'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_peat")).mode = 'Peat'         
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_driftwood")).mode = 'Driftwood'
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_dark")).mode = 'Charcoal_Dark'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_charcoal_black")).mode = 'Charcoal_Black' 

    box.separator()  




# WATER COLORS #
def draw_pen_water_ui(layout, box):        

    box.separator()  
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_zinc_yellow")).mode = 'Zinc_Yellow'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_lemon_cadmium")).mode = 'Lemon_Cadmium'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_gold")).mode = 'Gold'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_primrose_yellow")).mode = 'Primrose_Yellow'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_straw_yellow")).mode = 'Straw_Yellow'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_deep_cadmium")).mode = 'Deep_Cadmium'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_naples_yellow")).mode = 'Naples_Yellow'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_middle_chrome")).mode = 'Middle_Chrome'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_deep_chrome")).mode = 'Deep_Chrome'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_orange_chrome")).mode = 'Orange_Chrome'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_spectrum_orange")).mode = 'Spectrum_Orange'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_scarlet_lake")).mode = 'Scarlet_Lake'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_pale_vermilion")).mode = 'Pale_Vermilion'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_geranium_lake")).mode = 'Geranium_Lake'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_flesh_pink")).mode = 'Flesh_Pink'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_pink_madder_lake")).mode = 'Pink_Madder_Lake'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_rose_pink")).mode = 'Rose_Pink'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_madder_carmine")).mode = 'Madder_Carmine'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_crimson_lake")).mode = 'Crimson_Lake'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_rose_madder_lake")).mode = 'Rose_Madder_Lake'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_magenta")).mode = 'Magenta'           
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_red_violet_lake")).mode = 'Red_Violet_Lake'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_imperial_purple")).mode = 'Imperial_Purple'    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_dark_violet")).mode = 'Dark_Violet'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_light_violet")).mode = 'Light_Violet'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_blue_violet_lake")).mode = 'Blue_Violet_Lake'                  
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_smalt_blue")).mode = 'Smalt_Blue'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_spectrum_blue")).mode = 'Spectrum_Blue'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_light_blue")).mode = 'Light_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_kingfisher")).mode = 'Kingfisher'

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_sky_blue")).mode = 'Sky_Blue'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_turquoise_blue")).mode = 'Turquoise_Blue'            
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_oriental_blue")).mode = 'Oriental_Blue'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_cobald_blue")).mode = 'Cobald_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_ultramarine")).mode = 'Ultramarine'     
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_delft_blue")).mode = 'Delft_Blue'     


    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_indigo")).mode = 'Indigo'         
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_prussian_blue")).mode = 'Prussian_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_blue_gray")).mode = 'Blue_Gray'
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_gun_metal")).mode = 'Gun_Metal'   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_french_gray")).mode = 'French_Gray' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_silver_gray")).mode = 'Silver_Gray'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_water_green")).mode = 'Water_Green'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_turquoise_green")).mode = 'Turquoise_Green'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_jade_green")).mode = 'Jade_Green'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_juniper_green")).mode = 'Juniper_Green'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_bottle_green")).mode = 'Bottle_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_mineral_green")).mode = 'Mineral_Green'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_emerald_green")).mode = 'Emerald_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_grass_green")).mode = 'Grass_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_may_green")).mode = 'May_Green'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_sap_green")).mode = 'Sap_Green'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_cedar_green")).mode = 'Cedar_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_olive_green")).mode = 'Olive_Green' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_bronze")).mode = 'Bronze'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_sepia")).mode = 'Sepia'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_vandyke_brown")).mode = 'Vandyke_Brown'          
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_raw_umber")).mode = 'Raw_Umber'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_brown_ochre")).mode = 'Brown_Ochre'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_raw_sienna")).mode = 'Raw_Sienna' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_golden_brown")).mode = 'Golden_Brown'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_burnt_yellow_ochre")).mode = 'Burnt_Yellow_Ochre'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_burnt_sienna")).mode = 'Burnt_Sienna'    
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_burnt_carmine")).mode = 'Burnt_Carmine'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_terracotta")).mode = 'Terracotta'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_venetia_red")).mode = 'Venetia_Red'   

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_copper_beach")).mode = 'Copper_Beach'          
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_burnt_umber")).mode = 'Burnt_Umber'     
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_chocolate")).mode = 'Chocolate'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_water_ivory_black")).mode = 'Ivory_Black'      
      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2  
       

    box.separator()  



# INKTENSE COLORS # 
def draw_pen_inktense_ui(layout, box):        

    box.separator()  
                         
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_sherbert_lemon")).mode = 'Sherbert_Lemon'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_sun_yellow")).mode = 'Sun_Yellow'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_cadmium_yellow")).mode = 'Cadmium_Yellow'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_silician_yellow")).mode = 'Silician_Yellow'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_golden_yellow")).mode = 'Golden_Yellow'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_sienna_gold")).mode = 'Sienna_Gold'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_cadmium_orange")).mode = 'Cadmium_Orange' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_burnt_orange")).mode = 'Burnt_Orange'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_tangerine")).mode = 'Tangerine'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_mid_vermilion")).mode = 'Mid_Vermilion'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_scarlet_pink")).mode = 'Scarlet_Pink'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_poppy_red")).mode = 'Poppy_Red'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_hot_red")).mode = 'Hot_Red' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_chilli_red")).mode = 'Chilli_Red'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_cherry")).mode = 'Cherry'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_carmine_pink")).mode = 'Carmine_Pink'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_crimson")).mode = 'Crimson'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_shiraz")).mode = 'Shiraz'   
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_red_violet")).mode = 'Red_Violet' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_fuchsia")).mode = 'Fuchsia'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_deep_rose")).mode = 'Deep_Rose'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_thistle")).mode = 'Thistle'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_dusky_purple")).mode = 'Dusky_Purple'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_mauve")).mode = 'Mauve' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_dark_purple")).mode = 'Dark_Purple'  
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_deep_violet")).mode = 'Deep_Violet'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_violet")).mode = 'Violet'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_lagoon")).mode = 'Lagoon'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_peacock_blue")).mode = 'Peacock_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_navy_blue")).mode = 'Navy_Blue' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_iron_blue")).mode = 'Iron_Blue' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_deep_blue")).mode = 'Deep_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_iris_blue")).mode = 'Iris_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_bright_blue")).mode = 'Bright_Blue'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_deep_indigo")).mode = 'Deep_Indigo'   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_dark_aquamarine")).mode = 'Dark_Aquamarine' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_turquoise")).mode = 'Turquoise'                   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_green_aquamarine")).mode = 'Green_Aquamarine'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_mallard_green")).mode = 'Mallard_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_teal_green")).mode = 'Teal_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_iron_green")).mode = 'Iron_Green' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_ionian_green")).mode = 'Ionian_Green'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_vivid_green")).mode = 'Vivid_Green'     
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_apple_green")).mode = 'Apple_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_field_green")).mode = 'Field_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_beech_green")).mode = 'Beech_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_hookers_green")).mode = 'Hookers_Green' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_felt_green")).mode = 'Felt_Green'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_light_olive")).mode = 'Light_Olive'         
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_spring_green")).mode = 'Spring_Green'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_fern")).mode = 'Fern'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_leaf_green")).mode = 'Leaf_Green'   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_mustard")).mode = 'Mustard' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_amber")).mode = 'Amber'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_tan")).mode = 'Tan'           
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_oak")).mode = 'Oak'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_saddle_brown")).mode = 'Saddle_Brown'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_baked_earth")).mode = 'Baked_Earth' 
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_bark")).mode = 'Bark'   
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_willow")).mode = 'Willow'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_oxide_red")).mode = 'Oxide_Red'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_madder_brown")).mode = 'Madder_Brown'       
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_dark_chocolate")).mode = 'Dark_Chocolate'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_sepia_ink")).mode = 'Sepia_Ink'  
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_indian_ink")).mode = 'Indian_Ink'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_Chinese_ink")).mode = 'Chinese_Ink'

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_ink_black")).mode = 'Ink_Black'        
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_charcoal_gray")).mode = 'Charcoal_Gray'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_paynes_gray")).mode = 'Paynes_Gray'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_ink_black")).mode = 'Neutral_Gray'          
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_dark_slate")).mode = 'Dark_Slate'      
    row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_blacken")).mode = 'Blacken'       
    #row.operator("rts_ot.repattern_shader_pencil", text="", icon_value=get_icon_id_pencils("pen_inktense_silver")).mode = 'Silver'          

    box.separator()  
