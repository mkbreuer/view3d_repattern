import bpy
from ..utilities.utils import get_prefs
from ..icons.contrast import get_icon_id_contrast
from ..icons.palette import load_icons

from .ui_material_circle import *
from .ui_material_fabric import *
from .ui_material_metal import *
from .ui_material_object import *
from .ui_material_pencil import *
from .ui_material_wood import *
from .ui_material_hex import *
from .ui_material_draw_panel import *
from .ui_material_bsdf import *
from .ui_material_preview import *
from .ui_material_utils import *

def draw_mat_ui(self, context):       
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_REGION_WIN'   
       
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    mat_prefs = prefs.mat_type
    rp_props = bpy.context.window_manager.rp_props_repattern 

    layout.scale_y = panel_prefs.ui_scale_y

    view_layer = bpy.context.view_layer
    selected = bpy.context.selected_objects         

    obj = context.object       
    if obj:
        obj_type = obj.type
        if obj_type:         
            is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
            is_wire = (obj_type in {'CAMERA', 'EMPTY'})
            is_empty_image = (obj_type == 'EMPTY' and obj.empty_display_type == 'IMAGE')
            is_dupli = (obj.instance_type != 'NONE')
            is_gpencil = (obj_type == 'GPENCIL')
            
            col = layout.row(align=True) 
            #col.prop(mat_prefs, "mat_switch", expand=True)
            col.prop_enum(mat_prefs, "mat_switch", 'material', text="Shader")
            col.prop_enum(mat_prefs, "mat_switch", 'object', text="Object")       

            if mat_prefs.mat_switch != 'object':
                if bpy.data.materials:
                    layout.separator()  
                    col = layout.row(align=True)    
                    col.menu("rts_mt.material_list", text="Material List", icon="COLLAPSEMENU")
                    col.menu("RTS_MT_RePattern_MAT_Delete", text="", icon ="ORPHAN_DATA")   

            box = layout.box().column(align=True) 
            box.separator()  


            if mat_prefs.mat_switch == 'object':

                row = box.row(align=True)                                           
                row.label(text='Shading Color', icon='DOT')      

                if is_geometry or is_dupli or is_empty_image or is_gpencil:
                    sub = row.row(align=True)
                    sub.scale_x = 0.75                       
                    sub.prop(obj, "color", text='')    
                
                if bpy.context.space_data.shading.color_type == 'OBJECT':           
                    row.prop_enum(context.space_data.shading, "color_type", 'MATERIAL', text="", icon='CHECKBOX_HLT')   
                else:            
                    row.prop_enum(context.space_data.shading, "color_type", 'OBJECT', text="", icon='CHECKBOX_DEHLT')

                box.separator() 

                row = box.row(align=True)                                           
                row.label(text='Random Color', icon='DOT')      
                if mat_prefs.mat_random_object == True:           
                    icon_rand='CHECKBOX_HLT'
                    row.prop(mat_prefs, 'mat_random_value', text='') 
                    row.operator("rts_ot.repattern_shader_object", text="", icon='ADD')   
                else:            
                    icon_rand='CHECKBOX_DEHLT'
                
                row.prop(mat_prefs, 'mat_random_object', text='', icon=icon_rand) 

                box.separator()   

                if mat_prefs.mat_random_object == False:
                    draw_id_object_ui(layout, box)


            if mat_prefs.mat_switch == 'material':

                rd = bpy.context.scene.render
                if rd.has_multiple_engines:
                    row = box.row(align=True)
                    row.label(text="Engine", icon='DOT') 
                    sub = row.row(align=True)
                    sub.scale_x = 0.75                            
                    sub.prop(rd, "engine", text="")    
                    
                row.operator('rts_ot.reset_shader_props', text="", icon='RECOVER_LAST')     
                
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
                if rp_props.mat_active_only == True:  
                    icon_act = 'CHECKBOX_HLT'
                else:
                    icon_act = 'CHECKBOX_DEHLT'             
                row.prop(rp_props, 'mat_active_only', text='', icon=icon_act) 

                box.separator()

                row = box.row(align=True) 
                row.label(text='Prefix ID:', icon='DOT')
                sub = row.row(align=True)
                sub.scale_x = 0.75     
                sub.prop(rp_props, 'mat_to_assign', text='')
                if rp_props.mat_use_preset_prefix == True:  
                    icon_prefix = 'CHECKBOX_HLT'
                else:
                    icon_prefix = 'CHECKBOX_DEHLT'                
                row.prop(rp_props, 'mat_use_preset_prefix', text='', icon=icon_prefix)                
              
                box.separator() 
               
                row = box.row(align=True)                                           
                row.label(text='Diffuse Color', icon='DOT')      
                sub = row.row(align=True)
                sub.scale_x = 0.75               
                
                mat = bpy.context.object.active_material
                if mat:                
                    if mat.use_nodes:
                        #if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
                        
                        active_nodes = mat.node_tree.nodes
                        if active_nodes: 
                            
                            active_shader = mat.node_tree.nodes.active             
                            if active_shader:

                                mat_base = bpy.context.active_object.active_material.node_tree.nodes.active                               
                                if mat_base:
                                    
                                    sub = row.row(align=True)
                                    sub.scale_x = 0.5495

                                    mat_base_node = mat_base.inputs[0]
                                    sub.prop(mat_base_node,'default_value', text='')                            
                                
                                sub.prop(rp_props, "mat_color", text="")                            
                        
                            else:    
                                row.operator('rts_ot.select_bsdf_node', text="Get BSDF", icon='NODE')

                        else:
                            row.label(text='Nodes not Found!')  

                    else:                    
                        sub = row.row(align=True)
                        sub.scale_x = 0.5495 
                        sub.prop(mat, "diffuse_color", text="")
                        sub.prop(rp_props, "mat_color", text="") 

                else:
                    sub.prop(rp_props, "mat_color", text="")          

                #row.operator("rts_ot.shader_material", text="", icon='ADD')    
                row.operator("rts_ot.repattern_shader_custom", text="", icon='ADD')    

                box.separator()    
                
                row = box.row(align=True)                                           
                row.label(text='Multi Random:', icon='DOT')   
                sub = row.row(align=True)
                sub.scale_x = 0.75
                sub.prop(rp_props, 'mat_random_amount', text="")#, expand=True) 
                if rp_props.mat_random_multi == True:   
                    icon_multi ='CHECKBOX_HLT'
                else:
                    icon_multi ='CHECKBOX_DEHLT'                
                row.prop(rp_props, 'mat_random_multi', text='', icon=icon_multi)

                box.separator()                   

                if rp_props.mat_random_multi == False:

                    row = box.row(align=True)                                           
                    row.label(text='Material Slot', icon='DOT')   
                    sub = row.row(align=True)
                    sub.scale_x = 0.75
                    sub.prop(rp_props, 'mat_replace_slot', text='')
                    row.prop(rp_props, 'mat_use_nodes', text='', icon='NODETREE')
                    
                    box.separator()

                row = box.row(align=True)                                           
                row.label(text='Shader Presets', icon='DOT')   
                sub = row.row(align=True)
                sub.scale_x = 0.75
                if mat_prefs.mat_color_palette =='id_metal':
                    sub.prop(rp_props, 'mat_presets_metal', text="")
                else:
                    if rp_props.mat_use_nodes == True:
                        sub.prop(rp_props, 'mat_presets_type_bsdf', text="")
                    else:
                        sub.prop(rp_props, 'mat_presets_type', text="")
                if rp_props.mat_use_preset_suffix == True:  
                    icon_suffix = 'CHECKBOX_HLT'
                else:
                    icon_suffix = 'CHECKBOX_DEHLT'                
                row.prop(rp_props, 'mat_use_preset_suffix', text='', icon=icon_suffix)     
                
                box.separator()   

                row = box.row(align=True)                                           
                row.label(text='ID Category', icon='DOT')   
                sub = row.row(align=True)
                sub.scale_x = 0.75
                sub.prop(rp_props, 'mat_id_category', text="")
                row.label(text='', icon='LONGDISPLAY')  
                
                box.separator()                     
                
                if rp_props.mat_id_category !='None':
                   
                    row = box.row(align=True)                                           
                    row.label(text='ID Presets', icon='DOT')   
                    sub = row.row(align=True)
                    sub.scale_x = 0.75
                    
                    if rp_props.mat_id_category == 'Natur':
                        sub.prop(rp_props, 'cat_nature', text="")
                    
                    if rp_props.mat_id_category == 'Fabric':
                        sub.prop(rp_props, 'cat_fabric', text="")
                    
                    if rp_props.mat_id_category == 'Glass':
                        sub.prop(rp_props, 'cat_glass', text="")
                    
                    if rp_props.mat_id_category == 'Gemstone':
                        sub.prop(rp_props, 'cat_gems', text="")
                    
                    if rp_props.mat_id_category == 'Human':
                        sub.prop(rp_props, 'cat_human', text="")
                    
                    if rp_props.mat_id_category == 'Light':
                        sub.prop(rp_props, 'cat_light', text="")
                    
                    if rp_props.mat_id_category == 'Metal':
                        sub.prop(rp_props, 'cat_metal', text="")
                    
                    if rp_props.mat_id_category == 'Painted':
                        sub.prop(rp_props, 'cat_painted', text="")
                    
                    if rp_props.mat_id_category == 'Plastic':
                        sub.prop(rp_props, 'cat_plastic', text="")
                    
                    if rp_props.mat_id_category == 'Rubber':
                        sub.prop(rp_props, 'cat_rubber', text="")
                    
                    if rp_props.mat_id_category == 'Soil':
                        sub.prop(rp_props, 'cat_soil', text="")
                    
                    if rp_props.mat_id_category == 'Street':
                        sub.prop(rp_props, 'cat_street', text="")
                    
                    if rp_props.mat_id_category == 'Stone':
                        sub.prop(rp_props, 'cat_stone', text="")
                    
                    if rp_props.mat_id_category == 'Water':
                        sub.prop(rp_props, 'cat_water', text="")
                    
                    if rp_props.mat_id_category == 'Wood':
                        sub.prop(rp_props, 'cat_wood', text="")

                    row.label(text='', icon='SHORTDISPLAY')
                    
                    box.separator()                     

                else:
                    pass

                row = box.row(align=True)           
                sub = row.row(align=True)
                sub.alignment = 'CENTER'
                sub.scale_x = 1.2  
                sub.scale_y = 0.75
                sub.prop_enum(mat_prefs, "mat_color_palette", 'id_off', text ='', icon='RESTRICT_COLOR_OFF') 
                sub.prop_enum(mat_prefs, "mat_color_palette", 'id_circle') 
                sub.prop_enum(mat_prefs, "mat_color_palette", 'id_pencil')                                  
                sub.prop_enum(mat_prefs, "mat_color_palette", 'id_hex')      
                sub.prop(mat_prefs, 'id_presets', text ='', icon='OPTIONS')      

                box.separator()  
                
                if mat_prefs.id_presets == True:
                    mat_props_draw_panel(layout, box)

                if mat_prefs.mat_color_palette == 'id_off':
                    pass

                if mat_prefs.mat_color_palette == 'id_circle':
                    draw_id_circle_ui(layout, box) 

                if mat_prefs.mat_color_palette == 'id_pencil':
                    
                    box.separator()  

                    row = box.row(align=True)           
                    row.alignment = 'CENTER'
                    row.scale_x = 1.2  
                    row.scale_y = 0.8 
                    row.label(text="", icon='COLLAPSEMENU')
                    row.prop(mat_prefs, "display_palette_pencil",  text="")

                    box.separator()  

                    if mat_prefs.display_palette_pencil == 'Wood':
                        draw_id_wood_ui(layout, box)  
                    
                    elif mat_prefs.display_palette_pencil == 'Metal':
                        draw_id_metal_ui(layout, box)
                    
                    elif mat_prefs.display_palette_pencil == 'Fabric':
                        draw_id_fabric_ui(layout, box)
                   
                    else:
                        draw_id_pencil_ui(layout, box)  

                if mat_prefs.mat_color_palette == 'id_hex':            
                    draw_id_hex_ui(layout, box) 


                if len(bpy.context.object.material_slots): 

                    box = layout.box().column(align=True) 
                    box.separator()

                    row = box.row(align=True)   
                    mat = bpy.context.object.active_material
                    if mat:
                        if mat.use_nodes:
                            text_value='" Nodes activated! "'
                        else:
                            text_value='" Node deactivated! "'                                                     
                        row.operator('rts_ot.bsdf_use_node' , text=text_value, icon='NODETREE')  

                        if mat.use_nodes:
                            row.prop(mat_prefs,'mat_all_props', text ='', icon='PRESET')  
                            row.operator('rts_ot.open_editor',text="", icon='NODE_MATERIAL').mode = "shader, object"   

                    box.separator()

                    # SHADER PREVIEW
                    mat_preview_shader(self, box, layout)

                    # SHADER PROPERTIES
                    mat_props_shader(self, box, layout)
                        

    else:
        box = layout.box().column(align=True) 
        box.separator()  

        row = box.row(align=True)                                           
        row.label(text='No Selection!', icon='ERROR')             

        box.separator()   
