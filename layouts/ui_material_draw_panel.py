import bpy
from ..utilities.utils import get_prefs

def mat_props_draw_panel(layout, box): 
    view_layer = bpy.context.view_layer 
    
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    mat_prefs = prefs.mat_type

    rp_props = bpy.context.window_manager.rp_props_repattern 

    layout.scale_y = panel_prefs.ui_scale_y

    box.separator() 

    rd = bpy.context.scene.render
    if rd.engine == 'CYCLES':    
       
        row = box.row(align=True)
        row.label(text="Override: Materials")  
        row.prop(view_layer, "material_override", text='')
       
        box.separator()         
      
        row = box.row(align=True)
        row.label(text="Override: Samples")  
        row.prop(view_layer, "samples", text='')        
     
        box.separator()   
        box.separator()    

    row = box.row(align=True) 
    row.label(text='Object ID:', icon='DOT') 
    sub = row.row(align=True)
    sub.scale_x = 0.75 
    obj = bpy.context.object
    if obj is not None:
        sub.label(text=obj.name, icon='EDITMODE_HLT') 
    else:
        sub.label(text='No Selection!')                
    if rp_props.mat_use_objname == True:  
        icon_object = 'CHECKBOX_HLT'
    else:
        icon_object = 'CHECKBOX_DEHLT'                
    row.prop(rp_props, 'mat_use_objname', text='', icon=icon_object)  

    box.separator() 

    row = box.row(align=True) 
    row.label(text='Separator:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75      
    sub.prop(rp_props, 'mat_separator', text='') 
    if rp_props.mat_use_id == True:  
        icon_index = 'CHECKBOX_HLT'
    else:
        icon_index = 'CHECKBOX_DEHLT'                
    row.prop(rp_props, 'mat_use_id', text='', icon=icon_index)      

    box.separator() 

    row = box.row(align=True)                  
    row.label(text='Custom ID:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75    
    sub.prop(rp_props, 'mat_numbered', text='') 
    if rp_props.mat_use_id == True:  
        icon_index = 'CHECKBOX_HLT'
    else:
        icon_index = 'CHECKBOX_DEHLT'                
    row.prop(rp_props, 'mat_use_id', text='', icon=icon_index)                
    
    box.separator()               
    
    row = box.row(align=True)                  
    row.label(text='Hex ID:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75
    sub.active = mat_prefs.fake_props  
    sub.label(text='#RRGGBB')
    if rp_props.mat_use_hexname == True:  
        icon_hexid = 'CHECKBOX_HLT'
    else:
        icon_hexid = 'CHECKBOX_DEHLT'                
    row.prop(rp_props, 'mat_use_hexname', text='', icon=icon_hexid)                    

    box.separator() 
    
    mat = bpy.context.active_object.active_material
    if mat:
        row = box.row(align=True)                
        row.label(text='Pass ID:', icon='DOT')
        sub = row.row(align=True)
        sub.scale_x = 0.75  
        sub.prop(mat, "pass_index", text='')
        
        if view_layer.use_pass_material_index == True:  
            icon_pass = 'CHECKBOX_HLT'
        else:
            icon_pass = 'CHECKBOX_DEHLT'   
        row.prop(view_layer, "use_pass_material_index", text='', icon=icon_pass)

        box.separator()  

