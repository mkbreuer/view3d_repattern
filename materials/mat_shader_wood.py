import bpy
from bpy.props import *
from ..utilities.utils import get_prefs
from ..utilities.cache import settings_load, settings_write
from ..layouts.ui_material_draw_panel import mat_props_draw_panel


class RTS_OT_Repattern_Shader_Wood(bpy.types.Operator):
    """wood id / material shader """
    bl_idname = "rts_ot.repattern_shader_wood"
    bl_label = "Wood Shader"
    bl_options = {'REGISTER', 'UNDO'}         
    
    mode : StringProperty(default="", description="change if operation with a string", options={'HIDDEN'})  

    def draw(self, context):
        layout = self.layout.column(align=True)
        box = layout.box().column(align=True)          
        mat_props_draw_panel(layout, box)

    def execute(self, context):
        prefs = get_prefs()
        mat_prefs = prefs.mat_type
        rp_props = bpy.context.window_manager.rp_props_repattern 

        # store active # 
        view_layer = bpy.context.view_layer  
        target = view_layer.objects.active 

        selected = bpy.context.selected_objects             
        obj_list = [obj for obj in selected]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}    
        else:  

            if "Acacia_steamed"     in self.mode: wood_id = "Acacia_steamed" 
            if "Apple_india"        in self.mode: wood_id = "Apple_india"    
            if "Ash"                in self.mode: wood_id = "Ash"            
            if "Bamboo_steamed"     in self.mode: wood_id = "Bamboo_steamed" 
            if "Bangkirai"          in self.mode: wood_id = "Bangkirai"      
            if "Beech_steamed"  	in self.mode: wood_id = "Beech_steamed"  
            if "Cherry_amer"        in self.mode: wood_id = "Cherry_amer"    
            if "Cherry_eur"         in self.mode: wood_id = "Cherry_eur"     
            if "Cumaru"             in self.mode: wood_id = "Cumaru"         
            if "Doussie"            in self.mode: wood_id = "Doussie"        
            if "Garapa"             in self.mode: wood_id = "Garapa"         
            if "Ipe"                in self.mode: wood_id = "Ipe"            
            if "Iroko_kambala"      in self.mode: wood_id = "Iroko_kambala"  
            if "Jacaranda"          in self.mode: wood_id = "Jacaranda"      
            if "Jatoba"             in self.mode: wood_id = "Jatoba"         
            if "Kempas"             in self.mode: wood_id = "Kempas"         
            if "Larch"              in self.mode: wood_id = "Larch"          
            if "Macassar"           in self.mode: wood_id = "Macassar"       
            if "Maple_can"          in self.mode: wood_id = "Maple_can"      
            if "Maple_eur"          in self.mode: wood_id = "Maple_eur"      
            if "Massaranduba"       in self.mode: wood_id = "Massaranduba"   
            if "Merbau"             in self.mode: wood_id = "Merbau"         
            if "Oak"                in self.mode: wood_id = "Oak"            
            if "Oak_darkbrown"      in self.mode: wood_id = "Oak_darkbrown"  
            if "Oak_middlebraun"    in self.mode: wood_id = "Oak_middlebraun"
            if "Oak_redbrown"       in self.mode: wood_id = "Oak_redbrown"   
            if "Oak_smoked_core"    in self.mode: wood_id = "Oak_smoked_core"
            if "Oak_white"          in self.mode: wood_id = "Oak_white"      
            if "Olive"              in self.mode: wood_id = "Olive"          
            if "Panga_panga"        in self.mode: wood_id = "Panga_panga"    
            if "Pear"               in self.mode: wood_id = "Pear"           
            if "Teak"               in self.mode: wood_id = "Teak"           
            if "Walnut_amer"        in self.mode: wood_id = "Walnut_amer"    
            if "Walnut_eur"         in self.mode: wood_id = "Walnut_eur"     
            if "Wenge"              in self.mode: wood_id = "Wenge"          
            if "Willow"             in self.mode: wood_id = "Willow"         
            if "Zebrano"            in self.mode: wood_id = "Zebrano"        

            bpy.ops.rts.OT_shader_material( circle_type=rp_props.circle_type, fabric_type=rp_props.fabric_type, pencil_type=rp_props.pencil_type, wood_type=wood_id, 
                                            metal_type=rp_props.metal_type, mat_presets_metal=rp_props.mat_presets_metal, mat_use_preset_suffix=rp_props.mat_use_preset_suffix,
                                            mat_active_only=rp_props.mat_active_only, mat_to_assign=rp_props.mat_to_assign, mat_separator=rp_props.mat_separator, 
                                            mat_use_objname=rp_props.mat_use_objname, mat_use_id=rp_props.mat_use_id, mat_numbered=rp_props.mat_numbered, 
                                            mat_pass_index=rp_props.mat_pass_index, mat_assign_single=rp_props.mat_assign_single, mat_random_multi=rp_props.mat_random_multi, 
                                            mat_use_nodes=rp_props.mat_use_nodes, mat_expand_props=rp_props.mat_expand_props, mat_use_preset_prefix=rp_props.mat_use_preset_prefix,
                                            mat_color=rp_props.mat_color, mat_subsurface=rp_props.mat_subsurface, mat_subsurface_rd1=rp_props.mat_subsurface_rd1, 
                                            mat_subsurface_rd2=rp_props.mat_subsurface_rd2, mat_subsurface_rd3=rp_props.mat_subsurface_rd3, 
                                            mat_subsurface_color=rp_props.mat_subsurface_color, mat_metallic=rp_props.mat_metallic, mat_specular=rp_props.mat_specular, 
                                            mat_specular_tint=rp_props.mat_specular_tint, mat_roughness=rp_props.mat_roughness, 
                                            mat_anisotropic=rp_props.mat_anisotropic, mat_anisotropic_rotation=rp_props.mat_anisotropic_rotation, 
                                            mat_sheen=rp_props.mat_sheen, mat_sheen_tint=rp_props.mat_sheen_tint, mat_clearcoat=rp_props.mat_clearcoat, 
                                            mat_clearcoat_roughness=rp_props.mat_clearcoat_roughness, mat_ior=rp_props.mat_ior, mat_transmission=rp_props.mat_transmission, 
                                            mat_transmission_roughness=rp_props.mat_transmission_roughness, mat_emission_color=rp_props.mat_emission_color, 
                                            mat_alpha=rp_props.mat_alpha, mat_distribution=rp_props.mat_distribution, mat_subsurface_method=rp_props.mat_subsurface_method,  
                                            mat_presets_type=rp_props.mat_presets_type, mat_presets_type_bsdf=rp_props.mat_presets_type_bsdf, mat_ior_values=rp_props.mat_ior_values,
                                            mat_replace_slot=rp_props.mat_replace_slot, mat_random_amount=rp_props.mat_random_amount, mat_use_hexname=rp_props.mat_use_hexname,
                                            mat_color_palette=rp_props.mat_color_palette, mat_id_category=rp_props.mat_id_category, display_palette_circle=rp_props.display_palette_circle,
                                            cat_nature=rp_props.cat_nature, cat_water=rp_props.cat_water, cat_wood=rp_props.cat_wood, cat_painted=rp_props.cat_painted, cat_light=rp_props.cat_light, 
                                            cat_glass=rp_props.cat_glass, cat_gems=rp_props.cat_gems, cat_human=rp_props.cat_human, cat_fabric=rp_props.cat_fabric, cat_street=rp_props.cat_street, 
                                            cat_stone=rp_props.cat_stone, cat_plastic=rp_props.cat_plastic, cat_rubber=rp_props.cat_rubber, cat_metal=rp_props.cat_metal, cat_contrast=rp_props.cat_contrast,
                                            )  


            if rp_props.mat_active_only == False:
                n = len(selected)
                if n > 1:  
                    bpy.ops.object.material_slot_copy() 
                    self.report({'INFO'}, 'MAT to all Selected!') 
            else:
                self.report({'INFO'}, 'MAT to Active only!') 

            EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_METABALL"]  
            if bpy.context.mode in EDIT:          
                bpy.ops.object.material_slot_assign()   

        # reload active #     
        view_layer.objects.active = target
        return {'FINISHED'}   









































