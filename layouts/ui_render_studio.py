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
        layout.template_node_view(ntree, node, input)

    return True



def draw_render_ui(self, context):
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_DEFAULT'
    
    prefs = get_prefs()
    panel_prefs = prefs.panel_type       
    render_type = prefs.render_type       

    scene = context.scene
    
    box = layout.box().column(align=True)
  
    scene = bpy.context.scene
    rd = scene.render
    cycles = scene.cycles
    image_settings = rd.image_settings    

    if rd.has_multiple_engines:
        box.separator() 
        row = box.row(align=True)
        row.label(text="Engine")        
        row.prop(rd, "engine", text="")   
        row.label(text="", icon='SCENE')  
   
    box.separator()   
    
    row = box.row(align=True)               
    row.label(text="Image Size")               
    sub = row.row(align=True)
    sub.scale_x = 1
    sub.prop(render_type, "render_presets", text="")
    row.operator("rts_ot.repattern_render_presets", text="", icon='CHECKMARK')
    
    box.separator()       
    
    row = box.row(align=True)  
    row.label(text="Render HDRI View")
    if scene.use_preview_for_render == True:  
        icon_hdri = 'CHECKBOX_HLT'
    else:
        icon_hdri = 'CHECKBOX_DEHLT'           
    row.prop(scene,"use_preview_for_render", text="", icon=icon_hdri)


    if bpy.context.scene.render.engine != 'BLENDER_EEVEE':        
        box.separator()  
        
        row = box.row(align=True)
        row.label(text="Use Transparent")
        if scene.render.film_transparent == True:  
            icon_film = 'CHECKBOX_HLT'
        else:
            icon_film = 'CHECKBOX_DEHLT'        
        row.prop(scene.render,"film_transparent", text="", icon=icon_film)         
       
          
        if bpy.context.scene.render.film_transparent == True:
            box.separator()   
            
            row = box.row(align=True)
            row.label(text="Use Glass Rough")
            if scene.cycles.film_transparent_glass == True:  
                icon_glass = 'CHECKBOX_HLT'
            else:
                icon_glass = 'CHECKBOX_DEHLT'              

            sub = row.row(align=True)
            sub.scale_x = 0.75  
            sub.active = bpy.context.scene.render.film_transparent and scene.cycles.film_transparent_glass
            sub.prop(scene.cycles, "film_transparent_roughness", text="")                
            row.prop(scene.cycles,"film_transparent_glass", text="", icon=icon_glass)   
          


    else:
        box.separator()  
        
        row = box.row(align=True)
        row.label(text="Use Transparent")
        if scene.render.film_transparent == True:  
            icon_film = 'CHECKBOX_HLT'
        else:
            icon_film = 'CHECKBOX_DEHLT'
        row.prop(scene.render,"film_transparent", text="", icon=icon_film)         
       

    box.separator()       
    
    row = box.row(align=True) 
    row.label(text="Open Render Result")       
    row.operator('render.view_show',text="", icon='IMAGE')

    box.separator()
    box.separator()

    row = box.row(align=True)               
    row.scale_y = 1
    props = row.operator("render.render", text="Animation#")
    props.animation=True  
    props.use_viewport=True
  
    row.operator("render.opengl", text="Animation#").animation=True

    row = box.row(align=True)               
    row.scale_y = 3
    row.operator("render.render", text="Render#")
    row.operator("render.opengl", text="OpenGL#")           

    box.separator()
    
    row = box.row(align=True)                                               
    row.prop(panel_prefs, "display_rp_render", text="Setting")                                                  
    row.prop(panel_prefs, "display_rp_opengl", text="Setting")                             

    box.separator()
        
    if panel_prefs.display_rp_opengl:
         
        
        box.separator() 

        prefs = context.preferences
        system = prefs.system

        row = box.row(align=True)
        row.prop(system, "use_studio_light_edit", toggle=True)

        sub = row.row(align=True)
        sub.operator("preferences.studiolight_new", text="Save Preset", icon='FILE_TICK')
        sub.operator("preferences.studiolight_show", text="", icon='PREFERENCES')

        box.separator()

        def opengl_light_buttons(column, light):

            col = box.column()
            col.active = light.use

            col.prop(light, "use", text="Use Light")
            col.prop(light, "diffuse_color", text="Diffuse")
            col.prop(light, "specular_color", text="Specular")
            col.prop(light, "smooth")
            col.prop(light, "direction")

            box.separator()   
        

        box.use_property_split = True
        column = box.split()
        column.active = system.use_studio_light_edit

        light = system.solid_lights[0]
        colsplit = column.split(factor=0.85)
        opengl_light_buttons(colsplit, light)

        box.separator()  

        light = system.solid_lights[1]
        colsplit = column.split(factor=0.85)
        opengl_light_buttons(colsplit, light)

        box.separator()  

        light = system.solid_lights[2]
        colsplit = column.split(factor=0.85)
        opengl_light_buttons(colsplit, light)

        box.separator()  

        light = system.solid_lights[3]
        opengl_light_buttons(column, light)

        box.separator()

        box.prop(system, "light_ambient")

        box.separator() 



    if panel_prefs.display_rp_render: 

        scene = bpy.context.scene
        rd = scene.render
        cycles = scene.cycles
        image_settings = rd.image_settings          
        
        box.separator()  

        row = box.row()
        row.label(text="Device", icon='TOOL_SETTINGS')
        row.prop(cycles, "device", text="")
        box.separator()  
        
        row = box.row()
        row.label(text="Feature", icon='MOD_OCEAN')
        row.prop(cycles, "feature_set", text="")
        box.separator()  

        row = box.row(align=True)
        row.label(text="X Size:")        
        row.prop(rd, "resolution_x", text="")
        
        row = box.row(align=True)
        row.label(text="Y Size:")  
        row.prop(rd, "resolution_y", text="")
       
        box.separator()  
       
        row = box.row(align=True)
        row.label(text="Resolution:", icon='IMAGE')
        row.prop(rd, "resolution_percentage", text="")

        box.separator()  

        if bpy.context.scene.render.engine != 'BLENDER_EEVEE': 

            box.separator() 
          
            #if not use_optix(context):
            row = box.row(align=True)
            row.label(text="Integrator:", icon='RENDERLAYERS')
            row.prop(context.scene.cycles, "progressive", text="")
           
            box.separator() 


            if context.scene.cycles.progressive == 'PATH' or use_branched_path(context) is False:
                row = box.row(align=True)
                row.label(text="Samples:")
                row.prop(context.scene.cycles, "samples", text="")

                row = box.row(align=True)
                row.label(text="Viewport:")
                row.prop(context.scene.cycles, "preview_samples", text="")
             
            else:
                row = box.row(align=True)
                row.label(text="Samples:")
                row.prop(context.scene.cycles, "aa_samples", text="")

                row = box.row(align=True)
                row.label(text="Viewport:")
                row.prop(context.scene.cycles, "preview_aa_samples", text="") 

        else: 
       
            box.separator()  

            row = box.row(align=True)
            row.label(text="Samples:", icon='RENDERLAYERS')
            row.prop(context.scene.eevee, "taa_render_samples", text="")
          
            row = box.row(align=True)
            row.label(text="Viewport:")
            row.prop(context.scene.eevee, "taa_samples", text="")
          
            box.separator()  
          
            row = box.row()
            row.label(text="Use Denoising:", icon='STICKY_UVS_DISABLE')
            row.prop(context.scene.eevee, "use_taa_reprojection", text="")


        box.separator()  
       
        row = box.row()
        row.label(text="Format:", icon='IMAGE_DATA')
        row.prop(image_settings,"file_format", text="")
      
        box.separator()  
       
        row = box.row()
        row.prop(rd, "filepath", text="")
      
        box.separator()  
 
