import bpy
from ..utilities.utils import get_prefs

def mat_props_draw_ops(self, layout): 
    prefs = get_prefs()
    mat_prefs = prefs.mat_type

    scene = bpy.context.scene
    rd = scene.render
    cycles = scene.cycles
    image_settings = rd.image_settings   

    box = layout.box().column(align=True) 
    if rd.has_multiple_engines:
        box.separator() 
        row = box.row(align=True)
        row.label(text="Render Engine")        
        row.prop(rd, "engine", text="")    
         
    box.separator() 
    
    if bpy.context.scene.render.engine == 'CYCLES':
        view_layer = bpy.context.view_layer        
       
        row = box.row(align=True)
        row.label(text="Override: Materials")  
        row.prop(view_layer, "material_override", text='')
       
        box.separator()         
      
        row = box.row(align=True)
        row.label(text="Override: Samples")  
        row.prop(view_layer, "samples", text='')        
     
        box.separator()  

    row = layout.row(align=True)
    row.operator('rts_ot.reset_shader_props', text="Reset Panel Properties", icon='RECOVER_LAST')       
    
    box = layout.box().column(align=True)        
    box.separator()    

    row = box.row(align=True)
    row.label(text='Active only:', icon='DOT')  
    row.prop(self, 'mat_active_only', text='') 
    
    box.separator()
    box = layout.box().column(align=True)  
    box.separator()  

    row = box.row(align=True) 
    row.label(text='Active:', icon='DOT') 
    sub = row.row(align=True)
    sub.scale_x = 0.75 
    obj = bpy.context.object
    if obj is not None:
        sub.template_ID(bpy.context.view_layer.objects, "active", filter='AVAILABLE')
    else:
        sub.label(text='No Selection!')                
    if self.mat_use_objname == True:  
        icon_object = 'CHECKBOX_HLT'
    else:
        icon_object = 'CHECKBOX_DEHLT'                
    row.prop(self, 'mat_use_objname', text='', icon=icon_object)  

    box.separator()

    row = box.row(align=True) 
    row.label(text='Prefix:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75      
    sub.prop(self, 'mat_to_assign', text='')
    row.label(text='', icon='LOCKED')  

    row = box.row(align=True) 
    row.label(text='Separator:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75      
    sub.prop(self, 'mat_separator', text='') 
    if self.mat_use_id == True:  
        icon_index = 'CHECKBOX_HLT'
    else:
        icon_index = 'CHECKBOX_DEHLT'                
    row.prop(self, 'mat_use_id', text='', icon=icon_index)      
    
    row = box.row(align=True)                  
    row.label(text='Custom ID:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75    
    sub.prop(self, 'mat_numbered', text='') 
    if self.mat_use_id == True:  
        icon_index = 'CHECKBOX_HLT'
    else:
        icon_index = 'CHECKBOX_DEHLT'                
    row.prop(self, 'mat_use_id', text='', icon=icon_index)                
    
    box.separator()               

    row = box.row(align=True)                  
    row.label(text='Hex ID:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75
    sub.active = mat_prefs.fake_props  
    sub.label(text='#00000')
    if self.mat_use_hexname == True:  
        icon_hexid = 'CHECKBOX_HLT'
    else:
        icon_hexid = 'CHECKBOX_DEHLT'                
    row.prop(self, 'mat_use_hexname', text='', icon=icon_hexid)                    

    box.separator()  

    row = box.row(align=True)                  
    row.label(text='Prefix ID:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75
    sub.active = mat_prefs.fake_props  
    sub.label(text='#Shader')
    if self.mat_use_preset_prefix == True:  
        icon_prefix = 'CHECKBOX_HLT'
    else:
        icon_prefix = 'CHECKBOX_DEHLT'                
    row.prop(self, 'mat_use_preset_prefix', text='', icon=icon_prefix)                    

    box.separator() 

    row = box.row(align=True)                  
    row.label(text='Suffix ID:', icon='DOT')
    sub = row.row(align=True)
    sub.scale_x = 0.75
    sub.active = mat_prefs.fake_props  
    sub.label(text='#Presets')
    if self.mat_use_preset_suffix == True:  
        icon_suffix = 'CHECKBOX_HLT'
    else:
        icon_suffix = 'CHECKBOX_DEHLT'                
    row.prop(self, 'mat_use_preset_suffix', text='', icon=icon_suffix)                    

    box.separator() 

    
    if self.fabric_type != 'Custom' or self.pencil_type != 'Custom' or self.wood_type != 'Custom' or self.metal_type != 'Custom':
    
        box = layout.box().column(align=True)  
        box.separator()     

        row = box.row(align=True) 
        row.label(text='Used Color Swat:')

        row = box.row(align=True) 
        row.prop(self, 'fabric_type', text='') 
        row.prop(self, 'pencil_type', text='') 

        row = box.row(align=True) 
        row.prop(self, 'wood_type', text='') 
        row.prop(self, 'metal_type', text='') 

        box.separator()

