
import bpy

class RTS_OT_RePattern_Shader_Reset_Props(bpy.types.Operator):
    bl_description = "Resets the 3D view to the blender defaults"
    bl_idname = "rts_ot.reset_shader_props"
    bl_label = "Reset 3D View"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self,context):

        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_active_only=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_to_assign="RP_MAT" 
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_separator="_"
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_use_objname=False 
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_use_id=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_numbered="1"
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_pass_index=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_assign_single=False 
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_random_multi=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_use_nodes=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_expand_props=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_color=(0.9, 0.9, 0.9, 1)
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_subsurface=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_subsurface_rd1=1
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_subsurface_rd2=0.2
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_subsurface_rd3=0.1
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_subsurface_color=(0.9, 0.9, 0.9, 1)
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_metallic=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_specular=0.5
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_specular_tint=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_roughness=0.5
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_anisotropic=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_anisotropic_rotation=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_sheen=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_sheen_tint=0.5
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_clearcoat=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_clearcoat_roughness=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_ior=1.45
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_transmission=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_transmission_roughness=0
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_emission_color=(0, 0, 0, 1)
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_alpha=1
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_distribution='MULTI_GGX'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_subsurface_method='BURLEY'
        bpy.data.window_managers["WinMan"].rp_props_repattern.circle_type='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.fabric_type='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.pencil_type='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.wood_type='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_presets_type='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_presets_type_bsdf='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.metal_type='Custom'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_ior_values='ior000'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_replace_slot='Replace'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_random_amount=1
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_presets_metal='Standard'
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_use_hexname=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_use_preset_suffix=False
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_use_preset_prefix=True
        bpy.data.window_managers["WinMan"].rp_props_repattern.mat_id_category='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_nature='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_water='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_wood='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_painted='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_light='None' 
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_glass='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_gems='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_human='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_fabric='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_street='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_stone='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_plastic='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_rubber='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_metal='None'
        bpy.data.window_managers["WinMan"].rp_props_repattern.cat_contrast='None'

        return {"FINISHED"}


