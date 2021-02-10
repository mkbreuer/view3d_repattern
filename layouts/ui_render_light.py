import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def find_node(material, nodetype):
    if material and material.node_tree:
        ntree = material.node_tree

        active_output_node = None
        for node in ntree.nodes:
            if getattr(node, "type", None) == nodetype:
                if getattr(node, "is_active_output", True):
                    return node
                if not active_output_node:
                    active_output_node = node
        return active_output_node

    return None

def find_node_input(node, name):
    for input in node.inputs:
        if input.name == name:
            return input

    return None

def panel_node_draw(layout, id_data, output_type, input_name):
    if not id_data.use_nodes:
        layout.operator("cycles.use_shading_nodes", icon='NODETREE')
        return False

    ntree = id_data.node_tree

    node = find_node(id_data, output_type)
    if not node:
        layout.label(text="No output node")
    else:
        input = find_node_input(node, input_name)        
        
        col = layout.column()  
        col.separator()
        col.template_node_view(ntree, node, input)

    return True



def draw_light_ui(self, context):
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_DEFAULT'

    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    light_prefs = prefs.light_type

    scene = context.scene
    
    box = layout.box().column(align=True)
    box.separator()
    
    row = box.row(align=True)                
    row.scale_y = 1.3 
    row.label(text="Add Light:")
    row.operator("rts_ot.repattern_add_light", text="", icon='CHECKMARK')
  
    box.separator()

    row = box.row(align=True)    
    row.scale_y = 1.3 
    row.prop_search(data = context.scene, property = 'collection_rp_select_list_lights', search_data = bpy.data, search_property = 'lights',  text="") 
    
    box.separator()    
  
    row = box.row(align=True)                
    row.scale_y = 1.3 
    row.label(text="Select List Light:") 
    row.operator("rts_ot.repattern_light_jump", text="", icon='VIS_SEL_11') 

    box.separator()
    row.scale_y = 1.3 
    row = box.row(align=True)                
    row.label(text="Remove List Light:") 
    row.operator("rts_ot.repattern_light_remove", text="", icon='PANEL_CLOSE')

    box.separator()


    obj = context.active_object
    if obj:
        obj_type = obj.type

        if obj_type in {'LIGHT'}:    

            light = context.object.data
            if light.type in {'POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'}:                          

                box.separator()
                
                row = box.row(align=True)
                row.prop(light, "type", expand=True)

                box.separator()
            
            row = box.row(align=True)  
            row.label(text="Light Properties")                                             
            row.prop(panel_prefs, "display_rp_light", text="", icon='SETTINGS', emboss=False)                                     


            box.separator()            

            light = context.object.data
            if light.type in {'POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'}:                          

                if panel_prefs.display_rp_light:                         
                  
                    if bpy.context.scene.render.engine == 'CYCLES':
                    
                        light = context.object.data
                        clamp = light.cycles
                     
                        row = box.row(align=True)
                        row.label(text='Type')   
                        row.use_property_split = True
                        row.row().prop(light, "type")

                        box.separator()  
                     
                        row = box.row(align=True)
                        row.label(text='Color')  
                        row.prop(light, "color", text="")

                        box.separator()                                
                       
                        row = box.row(align=True)
                        row.label(text='Energy') 
                        row.prop(light, "energy", text="")

                        box.separator()    

                        if light.type in {'POINT', 'SPOT'}:
                            row = box.row(align=True)
                            row.label(text='Size') 
                            row.prop(light, "shadow_soft_size", text="")
                       
                        elif light.type == 'SUN':
                            row = box.row(align=True)
                            row.label(text='Angle') 
                            row.prop(light, "angle", text="")
                      
                        elif light.type == 'AREA':
                            row = box.row(align=True)
                            row.label(text='Shape')
                            row.prop(light, "shape", text="")

                            if light.shape in {'SQUARE', 'DISK'}:
                                box.separator()                                    
                                
                                row = box.row(align=True)
                                row.label(text='Size')                                   
                                row.prop(light, "size", text="")
                          
                         
                            elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
                                
                                box.separator()

                                row = box.row(align=True)
                                row.label(text='Size X')  
                                row.prop(light, "size", text="")
                                
                                box.separator()

                                row = box.row(align=True)
                                row.label(text='Size Y')                                 
                                row.prop(light, "size_y", text="")


                        if not (light.type == 'AREA' and clamp.is_portal):
                            box.separator() 

                            row = box.row(align=True)
                            row.label(text='Samples')
                            row.prop(clamp, "samples", text="")

                            box.separator() 

                            row = box.row(align=True)
                            row.label(text='Max Bounces')
                            row.prop(clamp, "max_bounces", text="")

                       
                        box.separator() 

                        row = box.row(align=True)
                        row.label(text='Cast Shadow')
                        sub = row.column()                  
                        sub.active = not (light.type == 'AREA' and clamp.is_portal)
                        sub.prop(clamp, "cast_shadow", text="")

                        box.separator() 

                        row = box.row(align=True)
                        row.label(text='Multiple Importance')
                        row.prop(clamp, "use_multiple_importance_sampling", text="")

                        if light.type == 'AREA':
                            box.separator() 

                            row = box.row(align=True)
                            row.label(text='Portal')                                                          
                            row.prop(clamp, "is_portal", text="")
                   
                    else:
                        
                        light = context.object.data

                        row = box.row(align=True)
                        row.label(text='Type')   
                        row.use_property_split = True
                        row.row().prop(light, "type", text="")

                        box.separator()  
                     
                        row = box.row(align=True)
                        row.label(text='Color')  
                        row.prop(light, "color", text="")

                        box.separator()                                
                       
                        row = box.row(align=True)
                        row.label(text='Energy') 
                        row.prop(light, "energy", text="")

                        box.separator()                                
                       
                        row = box.row(align=True)
                        row.label(text='Specular') 
                        row.prop(light, "specular_factor", text="")

                        box.separator()

                        if light.type in {'POINT', 'SPOT'}:
                            row = box.row(align=True)
                            row.label(text='Radius')  
                            row.prop(light, "shadow_soft_size", text="")
                       
                        elif light.type == 'SUN':
                            row = box.row(align=True)
                            row.label(text='Angle')   
                            row.prop(light, "angle", text="")
                       
                        elif light.type == 'AREA':
                            row = box.row(align=True)
                            row.label(text='Shape')   
                            row.prop(light, "shape", text="")

                            if light.shape in {'SQUARE', 'DISK'}:
                                
                                box.separator()                                
                               
                                row = box.row(align=True)
                                row.label(text='Size')                                                                  
                                row.prop(light, "size", text="")
                          
                           
                            elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
                                
                                box.separator()

                                row = box.row(align=True)
                                row.label(text='Size X')  
                                row.prop(light, "size", text="")
                                
                                box.separator()

                                row = box.row(align=True)
                                row.label(text='Size Y')                                 
                                row.prop(light, "size_y", text="")
                                
                        box.separator()        

            row = box.row(align=True)  
            row.label(text="Shadow Properties")                                             
            row.prop(light_prefs, "light_shadow", text="", icon='SETTINGS', emboss=False)  
    
            if light_prefs.light_shadow == True:
                
                box = layout.box().column(align=True) 
                box.prop(light, "use_shadow", text="Use Shadows")
                box.active = light.use_shadow
                
                if light.type != 'SUN':
                    row = box.row(align=True)
                    row.label(text="Clip:")
                    row.prop(light, "shadow_buffer_clip_start", text="Start")

                row = box.row(align=True)
                row.label(text="Bias:")
                row.prop(light, "shadow_buffer_bias", text="")

                if light.type == 'SUN' and light.use_shadow:

                    row = box.row(align=True)  
                    row.label(text="Sun Shadow Settings")                                             
                    row.prop(light_prefs, "light_cascade", text="", icon='SETTINGS', emboss=False) 

                    if light_prefs.light_cascade == True:

                        row = box.row(align=True)
                        row.label(text="Cascade Count:")                
                        row.prop(light, "shadow_cascade_count", text="")
                        
                        row = box.row(align=True)
                        row.label(text="Fade:")                 
                        row.prop(light, "shadow_cascade_fade", text="")

                        row = box.row(align=True)
                        row.label(text="Max Distance:")      
                        row.prop(light, "shadow_cascade_max_distance", text="")
                        
                        row = box.row(align=True)
                        row.label(text="Distribution:")                  
                        row.prop(light, "shadow_cascade_exponent", text="")

                        box.separator()

                box = layout.box().column(align=True)           
                row = box.row(align=True)
                row.prop(light, "use_contact_shadow", text="Use Contact Shadows")

                if light.use_shadow and light.use_contact_shadow:
                    
                    row = box.row(align=True)
                    row.label(text="Distance:")  
                    row.prop(light, "contact_shadow_distance", text="")
                    
                    row = box.row(align=True)
                    row.label(text="Bias:")          
                    row.prop(light, "contact_shadow_bias", text="")
                    
                    row = box.row(align=True)
                    row.label(text="Thickness:")          
                    row.prop(light, "contact_shadow_thickness", text="")

                    box.separator()





    if bpy.context.scene.render.engine == 'CYCLES':
        box.separator()
       
        row = box.row(align=True)                                              
        row.operator('rts_ot.emission_use_node' , text='" Use Nodes "', icon='NODETREE')  
        row.operator('rts_ot.open_editor', text="", icon='NODE_MATERIAL').mode = "shader, lights"


    box = layout.box().column(align=True)  
    box.separator()
    
    row = box.row(align=True)  
    row.label(text="Add Volume Light")
    row.operator('rts_ot.repattern_light_back', text="", icon='OUTLINER_DATA_LIGHTPROBE')

    box.separator()  

    row = box.row(align=True)                   
    row.popover(panel="RENDER_PT_eevee_indirect_lighting", text="Bake Light")   
    row.label(text="")
    row.operator("scene.light_cache_bake", text="", icon='RENDER_STILL')

    box.separator() 

    if obj:
        obj_type = obj.type
        if obj_type in {'LIGHT'}: 
                 
            light = bpy.data.lights
            if light:
           
                probe = bpy.context.object.data
                if probe.type in {'GRID', 'PLANAR', 'CUBEMAP'} :
                    
                    box.use_property_split = True
                    
                    box = layout.box().column(align=True) 
                    box.separator()  
                
                    if probe.type == 'GRID':

                        col = box.column(align=True) 
                        col.prop(probe, "influence_distance", text="Distance")
                        col.prop(probe, "falloff", text="Falloff")
                        col.prop(probe, "intensity", text="Intensity")
                    
                        box.separator()  
                        
                        col = box.column(align=True) 
                        col.prop(probe, "grid_resolution_x", text="Resolution X")
                        col.prop(probe, "grid_resolution_y", text="Resolution Y")
                        col.prop(probe, "grid_resolution_z", text="Resolution Z")

                        box.separator() 

                    elif probe.type == 'PLANAR':
                        
                        col = box.column(align=True)
                        col.prop(probe, "influence_distance", text="Distance")
                        col.prop(probe, "falloff")
                    
                    else:
                        col = box.column(align=True)
                        col.prop(probe, "influence_type")
                        
                        box.separator() 

                        col = box.column(align=True)   

                        if probe.influence_type == 'ELIPSOID':
                            col.prop(probe, "influence_distance", text="Radius")
                        else:
                            col.prop(probe, "influence_distance", text="Size")

                        col.prop(probe, "falloff")
                        col.prop(probe, "intensity")
                    
                    box.separator() 
                    
                    col = box.column(align=True)
                    if probe.type != 'PLANAR':
                        col.prop(probe, "clip_start", text="Clip Start")
                    else:
                        col.prop(probe, "clip_start", text="Clip Offset")

                    if probe.type != 'PLANAR':
                        col.prop(probe, "clip_end", text="End") 

                    box.separator()        

                    if probe.type == 'GRID':

                        col = box.column(align=True)   
                        col.prop(probe, "visibility_buffer_bias", text="Bias")
                        col.prop(probe, "visibility_bleed_bias", text="Bleed Bias")
                        col.prop(probe, "visibility_blur", text="Blur")
                        
                        box.separator() 

                        col = box.row(align=True)            
                        col.prop(probe, "visibility_collection")
                        col.prop(probe, "invert_visibility_collection", text="", icon='ARROW_LEFTRIGHT')

                        box.separator() 
