import bpy
from bpy.props import *
from ..utilities.utils import get_prefs
from ..utilities.cache import settings_load, settings_write
from ..layouts.ui_material_draw_panel import mat_props_draw_panel


class RTS_OT_Repattern_Shader_Pencil(bpy.types.Operator):
    """pencil id / material shader """
    bl_idname = "rts_ot.repattern_shader_pencil"
    bl_label = "Pencil Shader"
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
            if "Blacken" in self.mode: #1D1D1D
                pencil_id='Blacken'

            if "Dark_Slate" in self.mode: #363636
                pencil_id='Dark_Slate'

            if "Silver" in self.mode: #D0D0D0
                pencil_id='Silver'


            # AUTUMN COLORS #
            if "Light_Sienna" in self.mode: #FECD94       
                pencil_id='Light_Sienna'

            if "Solway_Blue" in self.mode: #CEE2DB 
                pencil_id='Solway_Blue'

            if "Ink_Blue" in self.mode: #5B8287 
                pencil_id='Ink_Blue'

            if "Smoke_Blue" in self.mode: #ADDAC6
                pencil_id='Smoke_Blue'        

            if "Pale_Cedar" in self.mode: #E1E0AA 
                pencil_id='Pale_Cedar'         

            if "Green_Shadow" in self.mode: #9CB490
                pencil_id='Green_Shadow'          

            if "Crag_Green" in self.mode: #B0C388
                pencil_id='Crag_Green'       
            
            if "Olive_Earth" in self.mode: #6C784D
                pencil_id='Olive_Earth'        
            
            if "Warm_Earth" in self.mode: #A48452 
                pencil_id='Warm_Earth'        
            
            if "Brown_Ochre" in self.mode: #DCAB58 
                pencil_id='Brown_Ochre'         
            
            if "Wheat" in self.mode: #FBF3C7  
                pencil_id='Wheat'           
            
            if "Yellow_Ochre" in self.mode: #FED86A 
                pencil_id='Yellow_Ochre'        

            if "Sepia_Red" in self.mode: #8B695B
                pencil_id='Sepia_Red'        

            if "Mars_Orange" in self.mode: #FC6636
                pencil_id='Mars_Orange'         

            if "Sanguine" in self.mode: #DB4529
                pencil_id='Sanguine'           

            if "Venetian_Red" in self.mode: #AC5B45
                pencil_id='Venetian_Red'      

            if "Terracotta" in self.mode: #C55E4B
                pencil_id='Terracotta'         

            if "Mars_Violet" in self.mode: #AA7C7F
                pencil_id='Mars_Violet'          

            if "Ruby_Earth" in self.mode: #9F514F
                pencil_id='Ruby_Earth'          

            if "Chocolate" in self.mode: #474441
                pencil_id='Chocolate'         

            if "Ivory_Black" in self.mode: #192223
                pencil_id='Ivory_Black'          

            if "Warm_Gray" in self.mode: #C9BD9A 
                pencil_id='Warm_Gray'          

            if "Cool_Gray" in self.mode: #BAC5AC
                pencil_id='Cool_Gray'           


            # GRAPHITINT COLORS #
            if "Port" in self.mode: #A95658
                pencil_id='Port'            

            if "Juniper" in self.mode: #946683
                pencil_id='Juniper'           

            if "Aubergine" in self.mode: #5F4877
                pencil_id='Aubergine'        

            if "Dark_Indigo" in self.mode: #2C3A4F
                pencil_id='Dark_Indigo'        

            if "Shadow" in self.mode: #23525F
                pencil_id='Shadow'         

            if "Steel_Blue" in self.mode: #325A60
                pencil_id='Steel_Blue'      

            if "Ocean_Blue" in self.mode: #1D4B73
                pencil_id='Ocean_Blue'     

            if "Slate_Green" in self.mode: #235E51
                pencil_id='Slate_Green'        

            if "Meadow" in self.mode: #3F4A2F
                pencil_id='Meadow'           

            if "Ivy" in self.mode: #5F6D30
                pencil_id='Ivy'

            if "Sage" in self.mode: #6A5228
                pencil_id='Sage'         

            if "Chestnut" in self.mode: #602A23
                pencil_id='Chestnut'        

            if "Russet" in self.mode: #613A26
                pencil_id='Russet'         

            if "Cool_Brown" in self.mode: #47472B
                pencil_id='Cool_Brown'        

            if "Cocoa" in self.mode: #633829
                pencil_id='Cocoa'           

            if "Autumn_Brown" in self.mode: #5D352C
                pencil_id='Autumn_Brown'         

            if "Storm" in self.mode: #332D26
                pencil_id='Storm'            

            if "Warm_Gray" in self.mode: #373635
                pencil_id='Warm_Gray'          

            if "Midnight_Black" in self.mode: #272B23
                pencil_id='Midnight_Black'         

            if "Mountain_Gray" in self.mode: #535249
                pencil_id='Mountain_Gray'        

            if "Mountain_Blue" in self.mode: #535249
                pencil_id='Mountain_Blue'        

            if "Cloud_Gray" in self.mode: #65726A
                pencil_id='Cloud_Gray'        

            if "Cool_Gray" in self.mode: #2B4648
                pencil_id='Cool_Gray'        


            # TINTED CHARCOAL COLORS #
            if "Sand" in self.mode: #E2B35B
                pencil_id='Sand'           

            if "Burnt_Orange" in self.mode: #D88135
                pencil_id='Burnt_Orange'          

            if "Sunset_Pink" in self.mode: #E39774
                pencil_id='Sunset_Pink'         

            if "Glowing_Embers" in self.mode: #6D5E4A
                pencil_id='Glowing_Embers'         

            if "Heather_Mist" in self.mode: #8A776A
                pencil_id='Heather_Mist'        

            if "Burnt_Embers" in self.mode: #6F645C
                pencil_id='Burnt_Embers'           

            if "Lavender" in self.mode: #57454A
                pencil_id='Lavender'            

            if "Thistle" in self.mode: #5D5859
                pencil_id='Thistle'            

            if "Bilberry" in self.mode: #455560
                pencil_id='Bilberry'            
            
            if "Elderberry" in self.mode: #425968             
                pencil_id='Elderberry'          
            
            if "Moutain_blue" in self.mode: #48635E
                pencil_id='Moutain_blue'         

            if "Ocean_Deep" in self.mode: #3B4444
                pencil_id='Ocean_Deep'          

            if "Slate" in self.mode: #415151
                pencil_id='Slate'           

            if "Forest_Pine" in self.mode: #4D6656
                pencil_id='Forest_Pine'           

            if "Green_Moss" in self.mode: #6E735A
                pencil_id='Green_Moss'           

            if "Dark_Moss" in self.mode: #63654A
                pencil_id='Dark_Moss'          

            if "Driftwood" in self.mode: #232518
                pencil_id='Driftwood'           

            if "Peat" in self.mode: #474332
                pencil_id='Peat'           

            if "Burnt_Earth" in self.mode: #363325
                pencil_id='Burnt_Earth'          

            if "Natural" in self.mode: #515446
                pencil_id='Natural'            

            if "Charcoal_Light" in self.mode: #45483B
                pencil_id='Charcoal_Light'         

            if "Charcoal_Medium" in self.mode: #2B2D23
                pencil_id='Charcoal_Medium'        

            if "Charcoal_Dark" in self.mode: #1E211B
                pencil_id='Charcoal_Dark'          

            if "Charcoal_Black" in self.mode: #1E211B
                pencil_id='Charcoal_Black'          


            # WATER COLORS #
            if "Zinc_Yellow" in self.mode: #F6EB81
                pencil_id='Zinc_Yellow'          

            if "Lemon_Cadmium" in self.mode: #F7EB82
                pencil_id='Lemon_Cadmium'          

            if "Gold" in self.mode: #FDDD59
                pencil_id='Gold'            

            if "Primrose_Yellow" in self.mode: #F7EFA2
                pencil_id='Primrose_Yellow'       

            if "Straw_Yellow" in self.mode: #F9ED90
                pencil_id='Straw_Yellow'            

            if "Deep_Cadmium" in self.mode: #FBE968
                pencil_id='Deep_Cadmium'           

            if "Naples_Yellow" in self.mode: #FDDA5A
                pencil_id='Naples_Yellow'         

            if "Middle_Chrome" in self.mode: #FFBD43
                pencil_id='Middle_Chrome'       

            if "Deep_Chrome" in self.mode: #FFB24E
                pencil_id='Deep_Chrome'            

            if "Orange_Chrome" in self.mode: #FF9D44
                pencil_id='Orange_Chrome'           

            if "Spectrum_Orange" in self.mode: #FF7C3D
                pencil_id='Spectrum_Orange'        

            if "Scarlet_Lake" in self.mode: #FF673A
                pencil_id='Scarlet_Lake'            

            if "Pale_Vermilion" in self.mode: #FF7E56
                pencil_id='Pale_Vermilion'           

            if "Geranium_Lake" in self.mode: #FF5E45
                pencil_id='Geranium_Lake'        

            if "Flesh_Pink" in self.mode: #FCF5D6
                pencil_id='Flesh_Pink'           

            if "Pink_Madder_Lake" in self.mode: #FE918B
                pencil_id='Pink_Madder_Lake'            

            if "Rose_Pink" in self.mode: #FCD6E4
                pencil_id='Rose_Pink'            
            
            if "Madder_Carmine" in self.mode: #F24234
                pencil_id='Madder_Carmine'         
            
            if "Crimson_Lake" in self.mode: #F53B2D
                pencil_id='Crimson_Lake'         

            if "Rose_Madder_Lake" in self.mode: #F7465F
                pencil_id='Rose_Madder_Lake'        

            if "Magenta" in self.mode: #C55DA9
                pencil_id='Magenta'            

            if "Imperial_Purple" in self.mode: #4D3178
                pencil_id='Imperial_Purple'           

            if "Red_Violet_Lake" in self.mode: #9674AA
                pencil_id='Red_Violet_Lake'         

            if "Dark_Violet" in self.mode: #323688
                pencil_id='Dark_Violet'       

            if "Light_Violet" in self.mode: #AAA6D2
                pencil_id='Light_Violet'       

            if "Blue_Violet_Lake" in self.mode: #6C94CC
                pencil_id='Blue_Violet_Lake'      

            if "Delft_Blue" in self.mode: #1F2E78
                pencil_id='Delft_Blue'         

            if "Ultramarine" in self.mode: #214DA4
                pencil_id='Ultramarine'         

            if "Smalt_Blue" in self.mode: #4FA5D8
                pencil_id='Smalt_Blue'          

            if "Cobald_Blue" in self.mode: #116AB7
                pencil_id='Cobald_Blue'       

            if "Spectrum_Blue" in self.mode: #337EC3
                pencil_id='Spectrum_Blue'         

            if "Light_Blue" in self.mode: #30B2E3
                pencil_id='Light_Blue'          

            if "Sky_Blue" in self.mode: #A1E3EA
                pencil_id='Sky_Blue'          

            if "Prussian_Blue" in self.mode: #173E93
                pencil_id='Prussian_Blue'         

            if "Indigo" in self.mode: #1F3459
                pencil_id='Indigo'             

            if "Oriental_Blue" in self.mode: #268ACB
                pencil_id='Oriental_Blue'           

            if "Kingfisher" in self.mode: #1AA9DD
                pencil_id='Kingfisher'         

            if "Turquoise_Blue" in self.mode: #97E0E5
                pencil_id='Turquoise_Blue'       

            if "Turquoise_Green" in self.mode: #96DDD6
                pencil_id='Turquoise_Green'        

            if "Jade_Green" in self.mode: #38C3B9
                pencil_id='Jade_Green'            

            if "Juniper_Green" in self.mode: #288A6D
                pencil_id='Juniper_Green'          

            if "Bottle_Green" in self.mode: #1D8B63
                pencil_id='Bottle_Green'          

            if "Water_Green" in self.mode: #B1E1BC
                pencil_id='Water_Green'         

            if "Mineral_Green" in self.mode: #1C8D49
                pencil_id='Mineral_Green'          

            if "Emerald_Green" in self.mode: #47BD69
                pencil_id='Emerald_Green'         

            if "Grass_Green" in self.mode: #82CB6B
                pencil_id='Grass_Green'            

            if "May_Green" in self.mode: #A1D265
                pencil_id='May_Green'          

            if "Sap_Green" in self.mode: #288747
                pencil_id='Sap_Green'          

            if "Cedar_Green" in self.mode: #3C703A
                pencil_id='Cedar_Green'           

            if "Olive_Green" in self.mode: #84993F
                pencil_id='Olive_Green'          

            if "Bronze" in self.mode: #836A30
                pencil_id='Bronze'           

            if "Sepia" in self.mode: #5C5232
                pencil_id='Sepia'          

            if "Burnt_Umber" in self.mode: #281E1B
                pencil_id='Burnt_Umber'           

            if "Vandyke_Brown" in self.mode: #7D5834
                pencil_id='Vandyke_Brown'        

            if "Raw_Umber" in self.mode: #CA8B34
                pencil_id='Raw_Umber'           

            if "Brown_Ochre" in self.mode: #D99E3B
                pencil_id='Brown_Ochre'       

            if "Raw_Sienna" in self.mode: #FEC44D
                pencil_id='Raw_Sienna'      

            if "Golden_Brown" in self.mode: #F39733
                pencil_id='Golden_Brown'       

            if "Burnt_Yellow_Ochre" in self.mode: #FD9D3A
                pencil_id='Burnt_Yellow_Ochre'         

            if "Copper_Beach" in self.mode: #89442C
                pencil_id='Copper_Beach'        

            if "Burnt_Sienna" in self.mode: #FE993C
                pencil_id='Burnt_Sienna'      

            if "Venetia_Red" in self.mode: #B14C2D
                pencil_id='Venetia_Red'         
            
            if "Terracotta" in self.mode: #F96733
                pencil_id='Terracotta'         
            
            if "Burnt_Carmine" in self.mode: #FE782E
                pencil_id='Burnt_Carmine'          

            if "Chocolate" in self.mode: #25201E
                pencil_id='Chocolate'           

            if "Ivory_Black" in self.mode: #171E1C
                pencil_id='Ivory_Black'          

            if "Blue_Gray" in self.mode: #17597B
                pencil_id='Gun_Metal'           

            if "Gun_Metal" in self.mode: #587484
                pencil_id='Gun_Metal'

            if "French_Gray" in self.mode: #A4A992
                pencil_id='French_Gray'          

            if "Silver_Gray" in self.mode: #C9E4E0
                pencil_id='Silver_Gray'         


            # INKTENSE COLORS #
            if "Sherbert_Lemon" in self.mode: #EBE982
                pencil_id='Sherbert_Lemon'           

            if "Sun_Yellow" in self.mode: #FEF083
                pencil_id='Sun_Yellow'           

            if "Cadmium_Yellow" in self.mode: #FDE47D
                pencil_id='Cadmium_Yellow'           

            if "Silician_Yellow" in self.mode: #F5CB8F
                pencil_id='Silician_Yellow'           

            if "Golden_Yellow" in self.mode: #F4AD6C
                pencil_id='Golden_Yellow'        

            if "Sienna_Gold" in self.mode: #E79167
                pencil_id='Sienna_Gold'           

            if "Cadmium_Orange" in self.mode: #F09062
                pencil_id='Cadmium_Orange'          

            if "Burnt_Orange" in self.mode: #B76D54
                pencil_id='Burnt_Orange'             

            if "Tangerine" in self.mode: #EA7C5C
                pencil_id='Tangerine'          

            if "Mid_Vermilion" in self.mode: #D97768
                pencil_id='Mid_Vermilion'            

            if "Scarlet_Pink" in self.mode: #E26956
                pencil_id='Scarlet_Pink'           

            if "Poppy_Red" in self.mode: #D85B4E
                pencil_id='Poppy_Red'            

            if "Hot_Red" in self.mode: #C8554D
                pencil_id='Hot_Red'            

            if "Chilli_Red" in self.mode: #A1524F
                pencil_id='Chilli_Red'          

            if "Cherry" in self.mode: #B05350
                pencil_id='Cherry'           

            if "Carmine_Pink" in self.mode: #B65658
                pencil_id='Carmine_Pink'          

            if "Crimson" in self.mode: #9C4E53
                pencil_id='Crimson'            

            if "Shiraz" in self.mode: #574749
                pencil_id='Shiraz'           

            if "Red_Violet" in self.mode: #814E5F
                pencil_id='Red_Violet'           

            if "Fuchsia" in self.mode: #B85A75
                pencil_id='Fuchsia'           

            if "Deep_Rose" in self.mode: #8F4B5E
                pencil_id='Deep_Rose'           

            if "Thistle" in self.mode: #855B7F
                pencil_id='Thistle'            

            if "Dusky_Purple" in self.mode: #3E424A
                pencil_id='Dusky_Purple'          

            if "Mauve" in self.mode: #514967
                pencil_id='Mauve'          

            if "Dark_Purple" in self.mode: #504966
                pencil_id='Dark_Purple'          

            if "Deep_Violet" in self.mode: #494F67
                pencil_id='Deep_Violet'            

            if "Violet" in self.mode: #4D5578
                pencil_id='Violet'            

            if "Lagoon" in self.mode: #414A71
                pencil_id='Lagoon'            

            if "Peacock_Blue" in self.mode: #3A4877
                pencil_id='Peacock_Blue'           

            if "Navy_Blue" in self.mode: #405067
                pencil_id='Navy_Blue'            

            if "Iron_Blue" in self.mode: #405067
                pencil_id='Iron_Blue'            

            if "Deep_Blue" in self.mode: #3C518E
                pencil_id='Deep_Blue'            

            if "Iris_Blue" in self.mode: #5E8CC8
                pencil_id='Iris_Blue'            

            if "Bright_Blue" in self.mode: #4D6AA7
                pencil_id='Bright_Blue'           

            if "Deep_Indigo" in self.mode: #3C4C5D
                pencil_id='Deep_Indigo'           

            if "Dark_Aquamarine" in self.mode: #34517F
                pencil_id='Dark_Aquamarine'             

            if "Turquoise" in self.mode: #51A1C2
                pencil_id='Turquoise'            

            if "Green_Aquamarine" in self.mode: #3E658A
                pencil_id='Green_Aquamarine'          

            if "Mallard_Green" in self.mode: #477E8F
                pencil_id='Mallard_Green'        

            if "Teal_Green" in self.mode: #478489
                pencil_id='Teal_Green'            

            if "Iron_Green" in self.mode: #374C59
                pencil_id='Iron_Green'           

            if "Ionian_Green" in self.mode: #3C5352
                pencil_id='Ionian_Green'            

            if "Vivid_Green" in self.mode: #518D77
                pencil_id='Vivid_Green'           

            if "Apple_Green" in self.mode: #7FBA69
                pencil_id='Apple_Green'           

            if "Field_Green" in self.mode: #496A56
                pencil_id='Field_Green'          

            if "Beech_Green" in self.mode: #3D5853
                pencil_id='Beech_Green'           

            if "Hookers_Green" in self.mode: #4E7B5D
                pencil_id='Hookers_Green'             

            if "Felt_Green" in self.mode: #496A56
                pencil_id='Felt_Green'            

            if "Light_Olive" in self.mode: #4D5B55
                pencil_id='Light_Olive'           

            if "Spring_Green" in self.mode: #6B8765
                pencil_id='Spring_Green'           

            if "Fern" in self.mode: #819065
                pencil_id='Fern'           

            if "Leaf_Green" in self.mode: #545D56
                pencil_id='Leaf_Green'           

            if "Mustard" in self.mode: #B69066
                pencil_id='Mustard'             

            if "Amber" in self.mode: #8C7560
                pencil_id='Amber'            

            if "Tan" in self.mode: #947A63
                pencil_id='Tan'           

            if "Oak" in self.mode: #5E625F
                pencil_id='Oak'            

            if "Saddle_Brown" in self.mode: #836C61
                pencil_id='Saddle_Brown'           

            if "Baked_Earth" in self.mode: #A36C58
                pencil_id='Baked_Earth'            

            if "Willow" in self.mode: #866556
                pencil_id='Willow'          

            if "Oxide_Red" in self.mode: #7A524E
                pencil_id='Oxide_Red'          

            if "Madder_Brown" in self.mode: #504A4B
                pencil_id='Madder_Brown'         

            if "Dark_Chocolate" in self.mode: #474C50
                pencil_id='Dark_Chocolate'         

            if "Bark" in self.mode: #A56E5A
                pencil_id='Bark'            

            if "Sepia_Ink" in self.mode: #434E50
                pencil_id='Sepia_Ink'           

            if "Indian_Ink" in self.mode: #454F54
                pencil_id='Indian_Ink'           

            if "Chinese_Ink" in self.mode: #344146
                pencil_id='Chinese_Ink'           

            if "Charcoal_Gray" in self.mode: #445157
                pencil_id='Charcoal_Gray'           

            if "Paynes_Gray" in self.mode: #414F5E
                pencil_id='Paynes_Gray'          

            if "Neutral_Gray" in self.mode: #3E4B50
                pencil_id='Neutral_Gray'            

            if "Ink_Black" in self.mode: #39454B
                pencil_id='Ink_Black'


            bpy.ops.rts.OT_shader_material( circle_type=rp_props.circle_type, fabric_type=rp_props.fabric_type, pencil_type=pencil_id, wood_type=rp_props.wood_type, 
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


