import bpy
from ..utilities.utils import get_prefs
from ..icons.circle import get_icon_id_circle


# PANEL
def draw_id_object_ui(layout, box):    
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    mat_prefs = prefs.mat_type
    
    layout.scale_y = panel_prefs.ui_scale_y

    box.separator()  

    row = box.row(align=True)           
    sub = row.row(align=True)
    sub.alignment = 'CENTER'
    sub.scale_x = 1.2  
    sub.scale_y = 0.75 
    sub.prop_enum(mat_prefs, "display_palette_circle", 'contrast', text="")
    sub.prop_enum(mat_prefs, "display_palette_circle", 'red',      text="")
    sub.prop_enum(mat_prefs, "display_palette_circle", 'blue',     text="")
    sub.prop_enum(mat_prefs, "display_palette_circle", 'green',    text="")
    sub.prop_enum(mat_prefs, "display_palette_circle", 'brown',    text="")
    sub.prop_enum(mat_prefs, "display_palette_circle", 'all',    text="")
    #row.prop(panel_prefs, "display_color_palette", text=" ", expand=True)

    box.separator()  
    box.separator()  
    
    if mat_prefs.display_palette_circle == 'contrast':
        draw_contrast_ui(layout, box) 

    if mat_prefs.display_palette_circle == 'red':                  
        draw_red_ui(layout, box) 

    if mat_prefs.display_palette_circle == 'blue':                   
        draw_blue_ui(layout, box) 
     
    if mat_prefs.display_palette_circle == 'green':                  
        draw_green_ui(layout, box) 

    if mat_prefs.display_palette_circle == 'brown':                   
        draw_brown_ui(layout, box)        

    if mat_prefs.display_palette_circle == 'all':                   
        draw_all_ui(layout, box)    


# CONTRAST COLORS # 
     
def draw_contrast_ui(layout, box):        
     
    box.separator()  

    row = box.row(align=True) 
    row.alignment = 'CENTER'     
    row.scale_x = 1.2    
    row.scale_y = 1.2                 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_00")).mode = 'gray_00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_20")).mode = 'gray_20'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_40")).mode = 'gray_40'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_50")).mode = 'gray_50'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_60")).mode = 'gray_60'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_80")).mode = 'gray_80'                
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_10")).mode = 'gray_10'     

    box.separator()  



# RED COLORS #
def draw_red_ui(layout, box):        

    box.separator()  
                 
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("601600")).mode = '0x601600'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("861900")).mode = '0x861900'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b41b00")).mode = '0xb41b00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d21c00")).mode = '0xd21c00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ef1f00")).mode = '0xef1f00'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ee3d1a")).mode = '0xee3d1a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f05d42")).mode = '0xf05d42'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f1826a")).mode = '0xf1826a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f4aa97")).mode = '0xf4aa97'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8d4c2")).mode = '0xf8d4c2'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("600000")).mode = '0x600000'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("870000")).mode = '0x870000'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b20000")).mode = '0xb20000'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cf0000")).mode = '0xcf0000'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ec0000")).mode = '0xec0000'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ee1a1f")).mode = '0xee1a1f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ef3e44")).mode = '0xef3e44'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f0686f")).mode = '0xf0686f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ef9394")).mode = '0xef9394'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f7c8cb")).mode = '0xf7c8cb'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("550020")).mode = '0x550020'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("750027")).mode = '0x750027'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("9a002e")).mode = '0x9a002e'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b30033")).mode = '0xb30033'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ce003b")).mode = '0xce003b'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d51252")).mode = '0xd51252'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("dc3670")).mode = '0xdc3670'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e05d8e")).mode = '0xe05d8e'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("de91af")).mode = '0xde91af'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("efc2d3")).mode = '0xefc2d3'      
        
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("490031")).mode = '0x490031'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("640040")).mode = '0x640040'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("83004f")).mode = '0x83004f'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("970056")).mode = '0x970056'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ac0069")).mode = '0xac0069'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b51380")).mode = '0xb51380'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c02e93")).mode = '0xc02e93'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cf57ac")).mode = '0xcf57ac'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("db85c6")).mode = '0xdb85c6'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ecbbdc")).mode = '0xecbbdc'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("410048")).mode = '0x410048'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("580061")).mode = '0x580061'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("70007f")).mode = '0x70007f'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("830093")).mode = '0x830093'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("9500a7")).mode = '0x9500a7'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("a600ae")).mode = '0xa600ae'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b42cc2")).mode = '0xb42cc2'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c450d1")).mode = '0xc450d1'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d481e4")).mode = '0xd481e4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ecb5f8")).mode = '0xecb5f8'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("250041")).mode = '0x250041'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("300056")).mode = '0x300056'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3d0070")).mode = '0x3d0070'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("430082")).mode = '0x430082'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("490090")).mode = '0x490090'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5d00a6")).mode = '0x5d00a6'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("752baf")).mode = '0x752baf'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8c52c6")).mode = '0x8c52c6'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ad7dd7")).mode = '0xad7dd7'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d4b5f0")).mode = '0xd4b5f0'      

    box.separator()  



# 0x COLORS #   
def draw_blue_ui(layout, box):        

    box.separator()  
                         
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("160042")).mode = '0x160042'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1b005a")).mode = '0x1b005a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1e0075")).mode = '0x1e0075'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("200084")).mode = '0x200084'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("220098")).mode = '0x220098'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3300a4")).mode = '0x3300a4'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4c2bbb")).mode = '0x4c2bbb'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6d51ca")).mode = '0x6d51ca'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("957fd9")).mode = '0x957fd9'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c7b9f1")).mode = '0xc7b9f1'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("060642")).mode = '0x060642' 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0B0058")).mode = '0x0B0058'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0B0072")).mode = '0x0B0072'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0b0088")).mode = '0x0b0088'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0c009a")).mode = '0x0c009a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1d1dad")).mode = '0x1d1dad'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("373bbb")).mode = '0x373bbb'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5b5ccd")).mode = '0x5b5ccd'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8286df")).mode = '0x8286df'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b9c0f0")).mode = '0xb9c0f0'      
       
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0d1944")).mode = '0x0d1944'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("111d60")).mode = '0x111d60'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("11227a")).mode = '0x11227a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("14268d")).mode = '0x14268d'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1729a6")).mode = '0x1729a6'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("233dae")).mode = '0x233dae'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3c57bd")).mode = '0x3c57bd'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5b76cb")).mode = '0x5b76cb'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("899dda")).mode = '0x899dda'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b5cbf4")).mode = '0xb5cbf4'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("112649")).mode = '0x112649' 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("153063")).mode = '0x153063'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("193b80")).mode = '0x193b80'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1c438f")).mode = '0x1c438f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1d4ba4")).mode = '0x1d4ba4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2b5faf")).mode = '0x2b5faf'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4176c2")).mode = '0x4176c2'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5e91d9")).mode = '0x5e91d9'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8bb3e3")).mode = '0x8bb3e3'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c1d3ef")).mode = '0xc1d3ef'      
   
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("162f4a")).mode = '0x162f4a'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("193e66")).mode = '0x193e66'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("204f86")).mode = '0x204f86'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("205c96")).mode = '0x205c96'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("226aac")).mode = '0x226aac'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("327bbd")).mode = '0x327bbd'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4690c8")).mode = '0x4690c8'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("65aad1")).mode = '0x65aad1'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("90c0e2")).mode = '0x90c0e2'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c2def5")).mode = '0xc2def5'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("193d4e")).mode = '0x193d4e' 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("21546c")).mode = '0x21546c'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("266c8b")).mode = '0x266c8b'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2a7da4")).mode = '0x2a7da4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2e8bb7")).mode = '0x2e8bb7'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3b9fc4")).mode = '0x3b9fc4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4dadce")).mode = '0x4dadce'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6bc0de")).mode = '0x6bc0de'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("93d0e7")).mode = '0x93d0e7'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c2edf0")).mode = '0xc2edf0'      
    
    box.separator()  




# GREEN COLORS #
def draw_green_ui(layout, box):        

    box.separator()  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1c4927")).mode = '0x1c4927'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("246533")).mode = '0x246533'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2c8240")).mode = '0x2c8240'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("319845")).mode = '0x319845'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("36aa4e")).mode = '0x36aa4e'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3fbb61")).mode = '0x3fbb61'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("53c47e")).mode = '0x53c47e'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6dd598")).mode = '0x6dd598'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("93e2b5")).mode = '0x93e2b5'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c2efd8")).mode = '0xc2efd8'  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1c4500")).mode = '0x1c4500'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("225d00")).mode = '0x225d00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2a7900")).mode = '0x2a7900'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("308e00")).mode = '0x308e00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("359f00")).mode = '0x359f00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("40ae00")).mode = '0x40ae00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("54bf2a")).mode = '0x54bf2a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6ed252")).mode = '0x6ed252'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("98da8a")).mode = '0x98da8a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c0efbb")).mode = '0xc0efbb'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("264a00")).mode = '0x264a00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("336600")).mode = '0x336600'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3e8400")).mode = '0x3e8400'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("479800")).mode = '0x479800'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4eaf00")).mode = '0x4eaf00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5fbd00")).mode = '0x5fbd00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("78c62a")).mode = '0x78c62a'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("95d45c")).mode = '0x95d45c'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b4e27e")).mode = '0xb4e27e'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d4efc0")).mode = '0xd4efc0'  
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3a5000")).mode = '0x3a5000'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4e6f00")).mode = '0x4e6f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("629100")).mode = '0x629100'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("71a600")).mode = '0x71a600'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("80bf00")).mode = '0x80bf00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("91cd00")).mode = '0x91cd00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("a4d32d")).mode = '0xa4d32d'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b5da56")).mode = '0xb5da56'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cdee82")).mode = '0xcdee82'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e2f7b3")).mode = '0xe2f7b3'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5e6b00")).mode = '0x5e6b00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("788600")).mode = '0x788600'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("9eb000")).mode = '0x9eb000'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("bdd400")).mode = '0xbdd400'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d1ed00")).mode = '0xd1ed00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e1f400")).mode = '0xe1f400'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("def22d")).mode = '0xdef22d'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e5f65a")).mode = '0xe5f65a'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("eef98b")).mode = '0xeef98b'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6fdc6")).mode = '0xf6fdc6'  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("676800")).mode = '0x676800'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("939300")).mode = '0x939300'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c0c200")).mode = '0xc0c200'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("eaee00")).mode = '0xeaee00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ffff00")).mode = '0xffff00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fffe00")).mode = '0xfffe00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fefe30")).mode = '0xfefe30'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fefe5a")).mode = '0xfefe5a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fffe8d")).mode = '0xfffe8d'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fefdc9")).mode = '0xfefdc9'      
    
    box.separator()  
    




# 0x COLORS #
def draw_brown_ui(layout, box):        

    box.separator()  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("685f00")).mode = '0x685f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("938700")).mode = '0x938700'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("bdb200")).mode = '0xbdb200'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f1e200")).mode = '0xf1e200'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fcec00")).mode = '0xfcec00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fcf022")).mode = '0xfcf022'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdf133")).mode = '0xfdf133'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fef870")).mode = '0xfef870'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fef78f")).mode = '0xfef78f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdfcc2")).mode = '0xfdfcc2'     

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("655100")).mode = '0x655100'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8f7000")).mode = '0x8f7000'             
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("bd9100")).mode = '0xbd9100'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d9a400")).mode = '0xd9a400'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f7bd00")).mode = '0xf7bd00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8ca00")).mode = '0xf8ca00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9d338")).mode = '0xf9d338'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8de64")).mode = '0xf8de64'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fde791")).mode = '0xfde791'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdf4c8")).mode = '0xfdf4c8'      
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("614400")).mode = '0x614400'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8a5c00")).mode = '0x8a5c00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b57800")).mode = '0xb57800'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d68a00")).mode = '0xd68a00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f59a00")).mode = '0xf59a00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f4ad00")).mode = '0xf4ad00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8bf38")).mode = '0xf8bf38'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9cb63")).mode = '0xf9cb63'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9da9a")).mode = '0xf9da9a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdebc7")).mode = '0xfdebc7'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("633900")).mode = '0x633900'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8c4c00")).mode = '0x8c4c00'             
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b76100")).mode = '0xb76100'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cf7000")).mode = '0xcf7000'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f17900")).mode = '0xf17900'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f48e00")).mode = '0xf48e00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f5a637")).mode = '0xf5a637'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f7bb67")).mode = '0xf7bb67'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9d19a")).mode = '0xf9d19a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fde7c9")).mode = '0xfde7c9'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("602f00")).mode = '0x602f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("873e00")).mode = '0x873e00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b24f00")).mode = '0xb24f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d45800")).mode = '0xd45800'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f06300")).mode = '0xf06300'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f47a19")).mode = '0xf47a19'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6943a")).mode = '0xf6943a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f1ad65")).mode = '0xf1ad65'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6c798")).mode = '0xf6c798'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fae3c4")).mode = '0xfae3c4'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("612700")).mode = '0x612700'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("883000")).mode = '0x883000'             
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b53c00")).mode = '0xb53c00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d14500")).mode = '0xd14500'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f04c00")).mode = '0xf04c00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f16618")).mode = '0xf16618'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f0803c")).mode = '0xf0803c'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f29c6f")).mode = '0xf29c6f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6bd94")).mode = '0xf6bd94'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fee3d0")).mode = '0xfee3d0'  

    box.separator() 



def draw_all_ui(layout, box):   
     
    box.separator()  

    row = box.row(align=True) 
    row.alignment = 'CENTER'     
    row.scale_x = 1.2    
    row.scale_y = 1.2                 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_00")).mode = 'gray_00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_20")).mode = 'gray_20'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_40")).mode = 'gray_40'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_50")).mode = 'gray_50'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_60")).mode = 'gray_60'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_80")).mode = 'gray_80'                
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("gray_10")).mode = 'gray_10'     

    box.separator()  


# RED COLORS #
                 
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("601600")).mode = '0x601600'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("861900")).mode = '0x861900'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b41b00")).mode = '0xb41b00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d21c00")).mode = '0xd21c00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ef1f00")).mode = '0xef1f00'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ee3d1a")).mode = '0xee3d1a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f05d42")).mode = '0xf05d42'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f1826a")).mode = '0xf1826a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f4aa97")).mode = '0xf4aa97'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8d4c2")).mode = '0xf8d4c2'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("600000")).mode = '0x600000'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("870000")).mode = '0x870000'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b20000")).mode = '0xb20000'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cf0000")).mode = '0xcf0000'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ec0000")).mode = '0xec0000'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ee1a1f")).mode = '0xee1a1f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ef3e44")).mode = '0xef3e44'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f0686f")).mode = '0xf0686f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ef9394")).mode = '0xef9394'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f7c8cb")).mode = '0xf7c8cb'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("550020")).mode = '0x550020'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("750027")).mode = '0x750027'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("9a002e")).mode = '0x9a002e'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b30033")).mode = '0xb30033'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ce003b")).mode = '0xce003b'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d51252")).mode = '0xd51252'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("dc3670")).mode = '0xdc3670'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e05d8e")).mode = '0xe05d8e'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("de91af")).mode = '0xde91af'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("efc2d3")).mode = '0xefc2d3'      
        
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("490031")).mode = '0x"490031'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("640040")).mode = '0x"640040'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("83004f")).mode = '0x"83004f'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("970056")).mode = '0x"970056'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ac0069")).mode = '0x"ac0069'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b51380")).mode = '0x"b51380'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c02e93")).mode = '0x"c02e93'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cf57ac")).mode = '0x"cf57ac'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("db85c6")).mode = '0x"db85c6'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ecbbdc")).mode = '0x"ecbbdc'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("410048")).mode = '0x410048'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("580061")).mode = '0x580061'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("70007f")).mode = '0x70007f'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("830093")).mode = '0x830093'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("9500a7")).mode = '0x9500a7'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("a600ae")).mode = '0xa600ae'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b42cc2")).mode = '0xb42cc2'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c450d1")).mode = '0xc450d1'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d481e4")).mode = '0xd481e4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ecb5f8")).mode = '0xecb5f8'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("250041")).mode = '0x250041'         
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("300056")).mode = '0x300056'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3d0070")).mode = '0x3d0070'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("430082")).mode = '0x430082'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("490090")).mode = '0x490090'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5d00a6")).mode = '0x5d00a6'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("752baf")).mode = '0x752baf'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8c52c6")).mode = '0x8c52c6'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ad7dd7")).mode = '0xad7dd7'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d4b5f0")).mode = '0xd4b5f0'      


# BLUE COLORS #   
   
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("160042")).mode = '0x160042'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1b005a")).mode = '0x1b005a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1e0075")).mode = '0x1e0075'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("200084")).mode = '0x200084'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("220098")).mode = '0x220098'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3300a4")).mode = '0x3300a4'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4c2bbb")).mode = '0x4c2bbb'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6d51ca")).mode = '0x6d51ca'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("957fd9")).mode = '0x957fd9'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c7b9f1")).mode = '0xc7b9f1'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("060642")).mode = '0x666642' 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0B0058")).mode = '0x0B0058'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0B0072")).mode = '0x0b0072'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0b0088")).mode = '0x0b0088'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0c009a")).mode = '0x0c009a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1d1dad")).mode = '0x1d1dad'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("373bbb")).mode = '0x373bbb'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5b5ccd")).mode = '0x5b5ccd'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8286df")).mode = '0x8286df'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b9c0f0")).mode = '0xb9c0f0'      
     
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("0d1944")).mode = '0x0d1944'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("111d60")).mode = '0x111d60'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("11227a")).mode = '0x11227a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("14268d")).mode = '0x14268d'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1729a6")).mode = '0x1729a6'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("233dae")).mode = '0x233dae'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3c57bd")).mode = '0x3c57bd'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5b76cb")).mode = '0x5b76cb'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("899dda")).mode = '0x899dda'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b5cbf4")).mode = '0xb5cbf4'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("112649")).mode = '0x112649' 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("153063")).mode = '0x153063'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("193b80")).mode = '0x193b80'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1c438f")).mode = '0x1c438f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1d4ba4")).mode = '0x1d4ba4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2b5faf")).mode = '0x2b5faf'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4176c2")).mode = '0x4176c2'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5e91d9")).mode = '0x5e91d9'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8bb3e3")).mode = '0x8bb3e3'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c1d3ef")).mode = '0xc1d3ef'      
   
    row = box.row(align=True) 
    row.alignment = 'CENTER'                         
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("162f4a")).mode = '0x162f4a'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("193e66")).mode = '0x193e66'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("204f86")).mode = '0x204f86'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("205c96")).mode = '0x205c96'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("226aac")).mode = '0x226aac'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("327bbd")).mode = '0x327bbd'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4690c8")).mode = '0x4690c8'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("65aad1")).mode = '0x65aad1'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("90c0e2")).mode = '0x90c0e2'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c2def5")).mode = '0xc2def5'       
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("193d4e")).mode = '0x193d4e' 
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("21546c")).mode = '0x21546c'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("266c8b")).mode = '0x266c8b'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2a7da4")).mode = '0x2a7da4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2e8bb7")).mode = '0x2e8bb7'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3b9fc4")).mode = '0x3b9fc4'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4dadce")).mode = '0x4dadce'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6bc0de")).mode = '0x6bc0de'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("93d0e7")).mode = '0x93d0e7'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c2edf0")).mode = '0xc2edf0'      


# GREEN COLORS #

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1c4927")).mode = '0x1c4927'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("246533")).mode = '0x246533'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2c8240")).mode = '0x2c8240'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("319845")).mode = '0x319845'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("36aa4e")).mode = '0x36aa4e'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3fbb61")).mode = '0x3fbb61'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("53c47e")).mode = '0x53c47e'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6dd598")).mode = '0x6dd598'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("93e2b5")).mode = '0x93e2b5'  
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c2efd8")).mode = '0xc2efd8'  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("1c4500")).mode = '0x1c4500'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("225d00")).mode = '0x225d00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("2a7900")).mode = '0x2a7900'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("308e00")).mode = '0x308e00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("359f00")).mode = '0x359f00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("40ae00")).mode = '0x40ae00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("54bf2a")).mode = '0x54bf2a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("6ed252")).mode = '0x6ed252'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("98da8a")).mode = '0x98da8a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c0efbb")).mode = '0xc0efbb'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("264a00")).mode = '0x264a00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("336600")).mode = '0x336600'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3e8400")).mode = '0x3e8400'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("479800")).mode = '0x479800'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4eaf00")).mode = '0x4eaf00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5fbd00")).mode = '0x5fbd00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("78c62a")).mode = '0x78c62a'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("95d45c")).mode = '0x95d45c'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b4e27e")).mode = '0xb4e27e'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d4efc0")).mode = '0xd4efc0'  
    
    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("3a5000")).mode = '0x3a5000'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("4e6f00")).mode = '0x4e6f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("629100")).mode = '0x629100'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("71a600")).mode = '0x71a600'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("80bf00")).mode = '0x80bf00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("91cd00")).mode = '0x91cd00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("a4d32d")).mode = '0xa4d32d'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b5da56")).mode = '0xb5da56'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cdee82")).mode = '0xcdee82'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e2f7b3")).mode = '0xe2f7b3'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("5e6b00")).mode = '0x5e6b00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("788600")).mode = '0x788600'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("9eb000")).mode = '0x9eb000'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("bdd400")).mode = '0xbdd400'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d1ed00")).mode = '0xd1ed00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e1f400")).mode = '0xe1f400'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("def22d")).mode = '0xdef22d'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("e5f65a")).mode = '0xe5f65a'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("eef98b")).mode = '0xeef98b'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6fdc6")).mode = '0xf6fdc6'  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                          
    row.scale_x = 1.2    
    row.scale_y = 1.2    
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("676800")).mode = '0x676800'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("939300")).mode = '0x939300'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("c0c200")).mode = '0xc0c200'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("eaee00")).mode = '0xeaee00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("ffff00")).mode = '0xffff00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fffe00")).mode = '0xfffe00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fefe30")).mode = '0xfefe30'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fefe5a")).mode = '0xfefe5a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fffe8d")).mode = '0xfffe8d'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fefdc9")).mode = '0xfefdc9'      


# BROWN COLORS #

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("685f00")).mode = '0x685f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("938700")).mode = '0x938700'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("bdb200")).mode = '0xbdb200'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f1e200")).mode = '0xf1e200'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fcec00")).mode = '0xfcec00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fcf022")).mode = '0xfcf022'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdf133")).mode = '0xfdf133'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fef870")).mode = '0xfef870'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fef78f")).mode = '0xfef78f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdfcc2")).mode = '0xfdfcc2'      

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("655100")).mode = '0x655100'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8f7000")).mode = '0x8f7000'             
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("bd9100")).mode = '0xbd9100'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d9a400")).mode = '0xd9a400'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f7bd00")).mode = '0xf7bd00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8ca00")).mode = '0xf8ca00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9d338")).mode = '0xf9d338'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8de64")).mode = '0xf8de64'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fde791")).mode = '0xfde791'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdf4c8")).mode = '0xfdf4c8' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("614400")).mode = '0x614400'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8a5c00")).mode = '0x8a5c00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b57800")).mode = '0xb57800'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d68a00")).mode = '0xd68a00'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f59a00")).mode = '0xf59a00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f4ad00")).mode = '0xf4ad00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f8bf38")).mode = '0xf8bf38'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9cb63")).mode = '0xf9cb63'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9da9a")).mode = '0xf9da9a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fdebc7")).mode = '0xfdebc7' 

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("633900")).mode = '0x633900'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("8c4c00")).mode = '0x8c4c00'             
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b76100")).mode = '0xb76100'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("cf7000")).mode = '0xcf7000'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f17900")).mode = '0xf17900'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f48e00")).mode = '0xf48e00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f5a637")).mode = '0xf5a637'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f7bb67")).mode = '0xf7bb67'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f9d19a")).mode = '0xf9d19a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fde7c9")).mode = '0xfde7c9'  

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("602f00")).mode = '0x602f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("873e00")).mode = '0x873e00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b24f00")).mode = '0xb24f00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d45800")).mode = '0xd45800'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f06300")).mode = '0xf06300'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f47a19")).mode = '0xf47a19'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6943a")).mode = '0xf6943a'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f1ad65")).mode = '0xf1ad65'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6c798")).mode = '0xf6c798'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fae3c4")).mode = '0xfae3c4'

    row = box.row(align=True) 
    row.alignment = 'CENTER'                        
    row.scale_x = 1.2    
    row.scale_y = 1.2     
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("612700")).mode = '0x612700'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("883000")).mode = '0x883000'             
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("b53c00")).mode = '0xb53c00'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("d14500")).mode = '0xd14500'       
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f04c00")).mode = '0xf04c00'        
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f16618")).mode = '0xf16618'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f0803c")).mode = '0xf0803c'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f29c6f")).mode = '0xf29c6f'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("f6bd94")).mode = '0xf6bd94'      
    row.operator("rts_ot.repattern_shader_object", text="", icon_value=get_icon_id_circle("fee3d0")).mode = '0xfee3d0'  


    box.separator()  

