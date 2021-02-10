import bpy
from bpy.props import *
from ..utilities.utils import get_prefs
from ..utilities.cache import settings_load, settings_write
from ..layouts.ui_material_draw_panel import mat_props_draw_panel


class RTS_OT_Repattern_Shader_Metal(bpy.types.Operator):
    """material shader"""
    bl_idname = "rts_ot.repattern_shader_metal"
    bl_label = "Metal Shader"
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

            # METAL COLORS #
            if 'Aluminium' in self.mode:
                metal_id='Aluminium'

            if 'Beryllium' in self.mode:
                metal_id='Beryllium'
    
            if 'Bismuth' in self.mode:
                metal_id='Bismuth'
                                                                                                        
            if 'Brass' in self.mode:
                metal_id='Brass'                                          
                                                        
            if 'Bronze' in self.mode:
                metal_id='Bronze'
                                                                                                            
            if 'Chromium' in self.mode:
                metal_id='Chromium'
                                                                                                                
            if 'Cobalt' in self.mode:
                metal_id='Cobalt'
                                                    
            if 'Copper' in self.mode:
                metal_id='Copper'
                                                                                
            if 'Gallium' in self.mode:
                metal_id='Gallium'
                                                                                
            if 'Germanium' in self.mode:
                metal_id='Germanium'
                                                                                
            if 'Gold' in self.mode:
                metal_id='Gold'
                                                                                
            if 'Iridium' in self.mode:
                metal_id='Iridium'
                                                        
            if 'Iron' in self.mode:
                metal_id='Iron'
                                    
            if 'Lead' in self.mode:
                metal_id='Lead'
                                                                                                            
            if 'Lithium' in self.mode:
                metal_id='Lithium'
                                                                                        
            if 'Mercury' in self.mode:
                metal_id='Mercury'
                                                                                    
            if 'Molybdenum' in self.mode:
                metal_id='Molybdenum'
                                                                                        
            if 'Nickel' in self.mode:
                metal_id='Nickel'
                                                                                    
            if 'Palladium' in self.mode:
                metal_id='Palladium'
                                                    
            if 'Platinum' in self.mode:
                metal_id='Platinum'
                                                                                
            if 'Silver' in self.mode:
                metal_id='Silver'
                                                                                        
            if 'Titanium' in self.mode:
                metal_id='Titanium'
                                                                                    
            if 'Zinc' in self.mode:
                metal_id='Zinc'
                                                                                    
            if 'Zirconium' in self.mode:
                metal_id='Zirconium'
                                                                                    

            bpy.ops.rts.OT_shader_material( circle_type=rp_props.circle_type, fabric_type=rp_props.fabric_type, pencil_type=rp_props.pencil_type, wood_type=rp_props.wood_type, 
                                            metal_type=metal_id, mat_presets_metal=rp_props.mat_presets_metal, mat_use_preset_suffix=rp_props.mat_use_preset_suffix,
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


