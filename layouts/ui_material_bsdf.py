import bpy
from ..utilities.utils import get_prefs
from bpy_extras.node_utils import find_node_input

import nodeitems_utils
from bpy.types import Header, Menu, Panel
from bpy.app.translations import pgettext_iface as iface_
from bpy.app.translations import contexts as i18n_contexts
from bl_ui.utils import PresetPanel
from bl_ui.properties_grease_pencil_common import (
    AnnotationDataPanel,
)
from bl_ui.space_toolsystem_common import (
    ToolActivePanelHelper,
)
from bl_ui.properties_material import (
    EEVEE_MATERIAL_PT_settings,
    MATERIAL_PT_viewport
)
from bl_ui.properties_world import (
    WORLD_PT_viewport_display
)
from bl_ui.properties_data_light import (
    DATA_PT_light,
    DATA_PT_EEVEE_light,
)


def panel_node_draw(layout, ntree, _output_type, input_name):
    node = ntree.get_output_node('EEVEE')

    if node:
        input = find_node_input(node, input_name)
        if input:
            layout.template_node_view(ntree, node, input)
        else:
            layout.label(text="Incompatible output node")
    else:
        layout.label(text="No output node")


def show_socket_input(self, socket):
    return hasattr(socket, 'draw') and socket.enabled and not socket.is_linked


def mat_props_shader(self, box, layout):
     

    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    mat_prefs = prefs.mat_type
  
    layout.scale_y = panel_prefs.ui_scale_y
     
    mat = bpy.context.object.active_material
    if mat:
        if mat.use_nodes:
 
            box.separator()

            row = box.row(align=True)   
            row.prop(bpy.context.active_object.active_material.node_tree.nodes.active, "name", icon='NODE')
            row.operator('node.find_node', text="", icon='VIS_SEL_11')   

            box.separator()  
            box.separator()  

            active_nodes = bpy.context.active_object.active_material.node_tree
            if active_nodes:  

                if mat_prefs.mat_all_props == True:
                
                    active_out = bpy.context.active_object.active_material.node_tree#.nodes.active.type                
                    if active_out in ['OUTPUT_MATERIAL']:  

                            row = box.row(align=True)
                            
                            if active_out in ['OUTPUT_MATERIAL', "Surface"]:
                                panel_node_draw(box, mat.node_tree, 'OUTPUT_MATERIAL', "Surface")
                                
                                box.separator() 
                            
                            if active_out in ['OUTPUT_MATERIAL', "Volume"]:
                                panel_node_draw(box, mat.node_tree, 'OUTPUT_MATERIAL', "Volume")

                            if bpy.context.scene.render.engine == 'CYCLES':

                                if active_out in ['OUTPUT_MATERIAL', "Displacement"]:                                
                                    box.separator() 
                                    panel_node_draw(box, mat.node_tree, 'OUTPUT_MATERIAL', "Displacement")

                            box.separator() 

                    else:
                        active_shader = bpy.context.active_object.active_material.node_tree.nodes.active
                    
                        # set "node" context pointer for the panel layout
                        row = box.row(align=True)
                        node = bpy.context.active_object.active_material.node_tree.nodes.active
                        row.context_pointer_set("node", node)

                        if hasattr(node, "draw_buttons_ext"):
                            node.draw_buttons_ext(bpy.context, box)

                        elif hasattr(node, "draw_buttons"):
                            node.draw_buttons(bpy.context, box)

                        # xxx this could be filtered further to exclude socket types
                        # which don't have meaningful input values (e.g. cycles shader)
                        value_inputs = [socket for socket in node.inputs if show_socket_input(self, socket)]
                        if value_inputs:
                            box.separator()
                            
                            row = box.row(align=True)
                            row.label(text="Inputs:")
                            
                            for socket in value_inputs:
                                box.separator()
                                row = box.row()
                                socket.draw(bpy.context, row, node, iface_(socket.label if socket.label else socket.name, socket.bl_rna.translation_context))

            else:
                row.label(text='Nodes not Found!')  

        else:
            box.separator()  

            row = box.column(align=True)  
            row.use_property_split = True
            row.prop(mat, "diffuse_color", text="Base Color")                                        
            row.prop(mat, "metallic")
            row.prop(mat, "specular_intensity", text="Specular")
            row.prop(mat, "roughness")

            box.separator() 