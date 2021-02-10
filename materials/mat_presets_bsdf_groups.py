import bpy
from ..utilities.utils import get_prefs
from..materials.mat_node_groups.mat_grp_atmo import*
from..materials.mat_node_groups.mat_grp_blood import*
from..materials.mat_node_groups.mat_grp_cloud import*
from..materials.mat_node_groups.mat_grp_curtain import*
from..materials.mat_node_groups.mat_grp_light import*
from..materials.mat_node_groups.mat_grp_ocean import*
from..materials.mat_node_groups.mat_grp_particles import*
from..materials.mat_node_groups.mat_grp_pbrd import*
from..materials.mat_node_groups.mat_grp_pbre import*
from..materials.mat_node_groups.mat_grp_pbrm import*
from..materials.mat_node_groups.mat_grp_skin import*
from..materials.mat_node_groups.mat_grp_snow import*
from..materials.mat_node_groups.mat_grp_transparent import*
from..materials.mat_node_groups.mat_grp_wax import*


# set material property presets  
def mat_presets_group_bsdf(self, mat): 
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    rp_props = bpy.context.window_manager.rp_props_repattern 

    # GET MATERIAL
    node_tree0 = mat.node_tree

    # NODES
    mat_out_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
    if hasattr(mat_out_0, 'color'):
        mat_out_0.color = (0.61, 0.61, 0.61)
    if hasattr(mat_out_0, 'hide'):
        mat_out_0.hide = False
    if hasattr(mat_out_0, 'is_active_output'):
        mat_out_0.is_active_output = True
    if hasattr(mat_out_0, 'location'):
        mat_out_0.location = (300.0, 0.0)
    if hasattr(mat_out_0, 'mute'):
        mat_out_0.mute = False
    if hasattr(mat_out_0, 'name'):
        mat_out_0.name = 'Material Output'
    if hasattr(mat_out_0, 'target'):
        mat_out_0.target = 'ALL'
    if hasattr(mat_out_0, 'use_custom_color'):
        mat_out_0.use_custom_color = False
    if hasattr(mat_out_0, 'width'):
        mat_out_0.width = 140.0

    mat_out_0.inputs[2].default_value = (0.0, 0.0, 0.0)
   
    if rp_props.mat_presets_type_bsdf == 'Atmosphere':   
        mat_presets_group_atmo(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'Blood':   
        mat_presets_group_blood(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'Cloud':
        mat_presets_group_cloud(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'Curtain':
        mat_presets_group_curtain(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'Light':
        mat_presets_group_light(node_tree0, mat_out_0)
        node_name = 'Emission'        

    if rp_props.mat_presets_type_bsdf == 'Ocean':
        mat_presets_group_ocean(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'Particles':
        mat_presets_group_particles(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'PBRD':
        mat_presets_group_pbrd(node_tree0, mat_out_0)
        node_name = 'PBR Displace' 
        self.report({'WARNING'}, "Missing Textures in Shader Editor!")  

    if rp_props.mat_presets_type_bsdf == 'PBRE':
        mat_presets_group_pbre(node_tree0, mat_out_0)
        node_name = 'PBR Emission' 
        self.report({'WARNING'}, "Missing Textures in Shader Editor!")  

    if rp_props.mat_presets_type_bsdf == 'PBRM':
        mat_presets_group_pbrm(node_tree0, mat_out_0)
        node_name = 'PBR Metallic' 
        self.report({'WARNING'}, "Missing Textures in Shader Editor!")                  

    if rp_props.mat_presets_type_bsdf == 'Skin':
        mat_presets_group_skin(node_tree0, mat_out_0)
        node_name = 'Skin'

    if rp_props.mat_presets_type_bsdf == 'Snow':
        mat_presets_group_snow(node_tree0, mat_out_0)
        node_name = 'Snow'        

    if rp_props.mat_presets_type_bsdf == 'Transparent':
        mat_presets_group_transparent(node_tree0, mat_out_0)

    if rp_props.mat_presets_type_bsdf == 'Wax':
        mat_presets_group_wax(node_tree0, mat_out_0)
        node_name = 'Wax'


    mat = bpy.context.object.active_material
    if mat.node_tree:
        nodes = mat.node_tree.nodes 
        node_groups = {'Light', 'PBRD', 'PBRE', 'PBRM', 'Skin', 'Snow', 'Wax'}
        if self.mat_presets_type_bsdf in node_groups:
            node_shader = nodes.get(node_name)                                                                                                                             
            node_shader.select = True
            nodes.active = node_shader   
        else:                                  
            node_shader = nodes.get('Group')                                                                                                                             
            node_shader.select = True
            nodes.active = node_shader   