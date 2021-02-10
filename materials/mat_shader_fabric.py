import bpy
from bpy.props import *
from ..utilities.utils import get_prefs
from ..utilities.cache import settings_load, settings_write
from ..layouts.ui_material_draw_panel import mat_props_draw_panel


class RTS_OT_Repattern_Shader_Fabric(bpy.types.Operator):
    """material shader"""
    bl_idname = "rts_ot.repattern_shader_fabric"
    bl_label = "Fabric Shader"
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

            # CONTRAST COLORS #
            if 'Black' in self.mode:
                fabric_id='Black'

            if 'Gray20' in self.mode:
                fabric_id='Gray20'
    
            if 'Gray40' in self.mode:
                fabric_id='Gray40'
                                                                                                        
            if 'Gray50' in self.mode:
                fabric_id='Gray50'                                          
                                                        
            if 'Gray60' in self.mode:
                fabric_id='Gray60'
                                                                                                            
            if 'Gray80' in self.mode:
                fabric_id='Gray80'
                                                                                                                
            if 'White' in self.mode:
                fabric_id='White'
                                                
                                                        
            # GREEN COLORS #     
            if 'Darkgreen' in self.mode:
                fabric_id='Darkgreen'
                                                                                
            if 'Hunter' in self.mode:
                fabric_id='Hunter'
                                                                                
            if 'Thyme' in self.mode:
                fabric_id='Thyme'
                                                                                
            if 'Grass_1' in self.mode:
                fabric_id='Grass_1'
                                                                                
            if 'Lightgreen' in self.mode:
                fabric_id='Lightgreen'
                                                        
            if 'Ino_1' in self.mode:
                fabric_id='Ino_1'
                                    
            if 'Ino_2' in self.mode:
                fabric_id='Ino_2'
                                                                                                            
            if 'Grass_2' in self.mode:
                fabric_id='Grass_2'
                                                                                        
            if 'Salvia' in self.mode:
                    fabric_id='Salvia'
                                                                                    
            if 'Pistachio' in self.mode:
                fabric_id='Pistachio'
                                                                                        
            if 'Limette' in self.mode:
                fabric_id='Limette'
                                                                                    
            if 'Lemon' in self.mode:
                fabric_id='Lemon'
                                                
                                                        
            # BLUE COLORS # 
            if 'Bluedark' in self.mode:
                fabric_id='Bluedark'
                                                                                
            if 'Darknavy' in self.mode:
                fabric_id='Darknavy'
                                                                                        
            if 'Darkroyal_blue_2' in self.mode:
                fabric_id='Darkroyal_blue_2'
                                                                                    
            if 'Royal_blue' in self.mode:
                fabric_id='Royal_blue'
                                                                                    
            if 'Darkroyal_blue_1' in self.mode:
                fabric_id='Darkroyal_blue_1'
                                                                                    
            if 'Blue' in self.mode:
                fabric_id='Blue'
                                        
            if 'Ice' in self.mode:
                fabric_id='Ice'
                                                                                        
            if 'Mint' in self.mode:
                fabric_id='Lightblue'
                                
            if 'Lightblue' in self.mode:
                fabric_id='Lightblue'
                                    
            if 'Grapes' in self.mode:
                fabric_id='Grapes'
                                
            if 'Lightplum' in self.mode:
                fabric_id='Lightplum'
                                                                                                            
            if 'Lilac' in self.mode:
                fabric_id='Lilac'
                                                
                                                        
            # BROWN COLORS #       
            if 'Chocolate' in self.mode:
                fabric_id='Chocolate'
                                                                                                            
            if 'Basalt' in self.mode:
                fabric_id='Basalt'                                                 
                                                        
            if 'Morel' in self.mode:
                fabric_id='Morel'
                                                                                                            
            if 'Brown' in self.mode:
                fabric_id='Brown'
                                                                                                        
            if 'Noisette' in self.mode:
                fabric_id='Noisette'                                                 
                                                        
            if 'Hazelnunt' in self.mode:
                fabric_id='Hazelnunt'
                                                                                        
            if 'Beige' in self.mode:                                                         
                fabric_id='Beige'                                                   
                                                    
            if 'Champanger' in self.mode:  
                fabric_id='Champanger'
                                        
            if 'Ivory' in self.mode:
                fabric_id='Ivory'
                                                                                                
            if 'Burgund' in self.mode:
                fabric_id='Burgund'
                                    
            if 'Chestnut' in self.mode:
                fabric_id='Chestnut'
                                    
            if 'Caramell' in self.mode:
                fabric_id='Caramell'
                                                
                                            
            # RED COLORS #
            if 'Red' in self.mode:
                fabric_id='Red'
                                                                                        
            if 'Scarlet' in self.mode:
                fabric_id='Scarlet'
                                                                                                            
            if 'Raspberry' in self.mode:
                fabric_id='Raspberry'
                                                                                        
            if 'Fuchsia' in self.mode:
                fabric_id='Fuchsia'
                                    
            if 'Watermelone' in self.mode:
                fabric_id='Watermelone'
                                
            if 'Orange' in self.mode:
                fabric_id='Orange'
                                                                                                            
            if 'Orangered' in self.mode:
                fabric_id='Orangered'
                                    
            if 'Cayenne' in self.mode:
                fabric_id='Cayenne'
                                
            if 'Peach' in self.mode:
                fabric_id='Peach'
                                                                                        
            if 'Rose' in self.mode:
                fabric_id='Rose'
                                                                                        
            if 'Blossom' in self.mode:
                fabric_id='Blossom'
                                                                                        
            if 'Perlrosa' in self.mode:
                fabric_id='Perlrosa'
                                                
                                                    
            # YELLOW COLORS #   
            if 'Mustard' in self.mode:
                fabric_id='Mustard'
                                                                                            
            if 'Gold' in self.mode:
                fabric_id='Gold'
                                        
            if 'Yelloworange' in self.mode:
                fabric_id='Yelloworange'
                                                                                        
            if 'Corn' in self.mode:
                fabric_id='Corn'
                                                                                    
            if 'Bumblebee' in self.mode:
                fabric_id='Bumblebee'
                                                                                        
            if 'Sungold' in self.mode:
                fabric_id='Sungold'
                                                                                    
            if 'Daffoldil' in self.mode:
                fabric_id='Daffoldil'
                                                                                    
            if 'Canary' in self.mode:
                fabric_id='Canary'
                                
            if 'Lemongrass' in self.mode:
                fabric_id='Lemongrass'
                                
            if 'Banana' in self.mode:
                fabric_id='Banana'
                                    
            if 'Vanille' in self.mode:
                fabric_id='Vanille'
                                
            if 'Creme' in self.mode:
                fabric_id='Creme'
                                    
                                                
            bpy.ops.rts.OT_shader_material( circle_type=rp_props.circle_type, fabric_type=fabric_id, pencil_type=rp_props.pencil_type, wood_type=rp_props.wood_type, 
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


