import bpy
import bmesh
from bpy import *
from bpy.props import *
from random import random

from . import *
from ..utilities.utils import get_prefs 
from ..icons.palette import load_icons
from ..utilities.cache import settings_load, settings_write
from ..properties.props_material import *
from ..layouts.ui_material_draw_ops import mat_props_draw_ops

from .mat_presets_default import *
from .mat_presets_bsdf import *
from .mat_presets_bsdf_default import *
from .mat_presets_bsdf_metal import *
from .mat_presets_circle import *
from .mat_presets_bsdf_circle import *
from .mat_presets_fabric import *
from .mat_presets_bsdf_fabric import *
from .mat_presets_pencil import *
from .mat_presets_bsdf_pencil import *
from .mat_presets_wood import *
from .mat_presets_bsdf_wood import *
from .mat_presets_metal import *
from .mat_presets_bsdf_metal import *
from .mat_presets_bsdf_groups import *

EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']


def mat_material_creation(self, mat_prefs, obj):

    #if mat exist?
    if self.mat_replace_slot == 'Replace':    
        mat_exist = bpy.context.object.active_material
        if mat_exist:
            if self.mat_random_multi == True:
                bpy.context.object.data.materials.clear()
            else:            
                bpy.ops.object.material_slot_remove()
            
    
    if self.mat_use_preset_suffix == True:
        
        if mat_prefs.display_palette_pencil == 'Metal':
            mat_preset_suffix = '_' + self.mat_presets_metal

        elif mat_prefs.display_palette_pencil == 'Wood':
            mat_preset_suffix = '_' + self.wood_type

        elif mat_prefs.display_palette_pencil == 'Fabric':
            mat_preset_suffix = '_' + self.fabric_type

        else: 
            if self.mat_use_nodes == True: 
                mat_preset_suffix = '_' + self.mat_presets_type_bsdf
            
            else:
                mat_preset_suffix = '_' + self.mat_presets_type
    else:
        mat_preset_suffix = ''



    if self.mat_id_category == 'None':
        mat_preset_prefix = self.mat_to_assign
        mat_id_temp = ''
        mat_sub_temp = ''

    else:
        
        if self.mat_use_preset_prefix == True:
            mat_preset_prefix = self.mat_to_assign + '_'
        else:
            mat_preset_prefix = ''


        if self.mat_id_category !='None':
            mat_id_temp = self.mat_id_category
        else:
            mat_id_temp = ''          
            

        if self.mat_id_category == 'Fabric':
            if self.cat_fabric !='None':
                mat_sub_temp = '_' + self.cat_fabric
            else:
                mat_sub_temp = ''   

        elif self.mat_id_category == 'Glass':
            if self.cat_glass !='None':
                mat_sub_temp = '_' + self.cat_glass
            else:
                mat_sub_temp = ''           

        elif self.mat_id_category == 'Gemstone':
            if self.cat_gems !='None':
                mat_sub_temp = '_' + self.cat_gems
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Human':
            if self.cat_human !='None':
                mat_sub_temp = '_' + self.cat_human
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Light':
            if self.cat_light !='None':
                mat_sub_temp = '_' + self.cat_light
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Metal':
            if self.cat_metal !='None':
                mat_sub_temp = '_' + self.cat_metal
            else:
                mat_sub_temp = ''           

        elif self.mat_id_category == 'Natur':
            if self.cat_nature !='None':
                mat_sub_temp = '_' + self.cat_nature
            else:
                mat_sub_temp = ''           

        elif self.mat_id_category == 'Painted':
            if self.cat_painted !='None':
                mat_sub_temp = '_' + self.cat_painted
            else:
                mat_sub_temp = ''           
                
        elif self.mat_id_category == 'Plastic':
            if self.cat_plastic !='None':
                mat_sub_temp = '_' + self.cat_plastic
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Rubber':
            if self.cat_rubber !='None':
                mat_sub_temp = '_' + self.cat_rubber
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Soil':
            if self.cat_soil !='None':
                mat_sub_temp = '_' + self.cat_soil
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Street':
            if self.cat_street !='None':
                mat_sub_temp = '_' + self.cat_street
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Stone':
            if self.cat_stone !='None':
                mat_sub_temp = '_' + self.cat_stone
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Water':
            if self.cat_water !='None':
                mat_sub_temp = '_' + self.cat_water
            else:
                mat_sub_temp = ''           
        
        elif self.mat_id_category == 'Wood':      
            if self.cat_wood !='None':
                mat_sub_temp = '_' + self.cat_wood
            else:
                mat_sub_temp = ''           

        else:
            mat_sub_temp = ''



    if mat_prefs.mat_color_palette == 'id_off':
        mat_preset_prefix = self.mat_to_assign
        mat_pencil_temp = ''

    else:        
        if self.mat_use_preset_prefix == True:
            mat_preset_prefix = self.mat_to_assign + '_'
        else:
            mat_preset_prefix = ''        
        
        if mat_prefs.mat_color_palette == 'id_pencil':
            if mat_prefs.display_palette_pencil == 'Metal':
                mat_pencil_temp = self.metal_type 
            elif mat_prefs.display_palette_pencil == 'Fabric':
                mat_pencil_temp = self.fabric_type 
            elif mat_prefs.display_palette_pencil == 'Wood':
                mat_pencil_temp = self.wood_type
            else:
                mat_pencil_temp = self.pencil_type 
                 
        else:
            mat_pencil_temp = ''


    if self.mat_use_objname == True:
        mat_object_id = bpy.context.object.name                                                
    else:
        mat_object_id = ''    


    mat_shader_type = mat_preset_prefix + mat_object_id + mat_pencil_temp + mat_id_temp + mat_sub_temp + mat_preset_suffix


    # create custom index
    if self.mat_numbered != '':
        id = int(self.mat_numbered)
        numberDigits = len(self.mat_numbered)    
    else:
        id = 0
        numberDigits = 3  

    if self.mat_use_id == True:
        #for slot in obj.material_slots:
        for mat in bpy.data.materials:  
            bpy.context.object.active_material_index = id
            id += 1  
    
        set_id = str(id)  
        mat_name = mat_shader_type + self.mat_separator + set_id 

    else:                                    
        mat_name = mat_shader_type   



    # create material
    if self.mat_random_multi == True: 

        for i in range(self.mat_random_amount):
            mat = bpy.data.materials.new(mat_name+"_%i" % i)
            obj.data.materials.append(mat)
            
    else:
        
        mat = bpy.data.materials.new(mat_name)
        
        if self.mat_replace_slot == 'Top':
            bpy.ops.object.material_slot_add()          
            if len(obj.data.materials):     
                obj.material_slots[obj.material_slots.__len__() - 1].material = mat
                bpy.context.object.active_material = mat
                                                
                for i in range(0, len(obj.material_slots)):
                    bpy.ops.object.material_slot_move(direction='UP')
                bpy.ops.object.material_slot_move(direction='UP')
            else:
                obj.data.materials.append(mat) # no slots

        elif self.mat_replace_slot == 'Bottom':
            bpy.ops.object.material_slot_add()
            if len(obj.data.materials):
                obj.material_slots[obj.material_slots.__len__() - 1].material = mat
            else:
                obj.data.materials.append(mat) # no slots
        else:
            if len(obj.data.materials):
                EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_METABALL"]  
                if bpy.context.mode in EDIT:   
                    idx = obj.active_material_index
                    obj.material_slots[idx].material = mat
                else:
                    #if obj.data.materials[i] is None:
                    if obj.material_slots is None:
                        obj.data.materials[0] = mat
                    else:
                        idx = obj.active_material_index
                        obj.material_slots[idx].material = mat  
            else:
                obj.data.materials.append(mat) # no slots



    # use nodes
    if self.mat_use_nodes == True:
        mat.use_nodes = True   

    node_groups = {'Atmosphere', 'Blood', 'Cloud', 'Curtain', 'Light', 'Ocean', 'Particles', 'PBRD', 'PBRE', 'PBRM', 'Skin', 'Snow', 'Transparent', 'Wax'}
    if self.mat_presets_type_bsdf in node_groups:
        node_tree = mat.node_tree
        for node in node_tree.nodes:
            node_tree.nodes.remove(node)
     
        mat_presets_group_bsdf(self, mat)


    else:

        # set random color
        if self.mat_random_multi == True:

            for i in range(0, len(obj.material_slots)):   
                obj.active_material_index = i 
                mat = obj.data.materials[i] 

                if mat.use_nodes == True:
                    nodes = mat.node_tree.nodes                                    
                    node_shader = nodes.get('Principled BSDF')                                                
                
                    if node_shader is None:               
                        node = mat.node_tree.nodes['Diffuse BSDF']   
                    else:
                        node_shader.select = True
                        nodes.active = node_shader                        
                        node = mat.node_tree.nodes['Principled BSDF']                                                   
                    
                    # set colour
                    for i in range(3):
                        if node_shader is None:         
                            node.inputs['Color'].default_value[i] *= random() 
                        else:                      
                            node.inputs['Base Color'].default_value[i] *= random()                    
                        
                        # set material property preset
                        mat_presets_custom_bsdf(self, node)

                        if self.mat_use_hexname ==True:
                            hexname = color_to_hex(node.inputs[0].default_value)
                            mat.name = mat_name + '_' + hexname  

                else:
                    for i in range(3):
                        mat.diffuse_color[i] *= random()                                              
                        
                        # set material property preset
                        mat_presets_diffuse(self, mat)            

                        if self.mat_use_hexname ==True:
                            hexname = color_to_hex(mat.diffuse_color)
                            mat.name = mat_name + '_' + hexname  


        else:
            if mat.node_tree:                                                 
                nodes = mat.node_tree.nodes                                    
                node_shader = nodes.get('Principled BSDF')                                                
            
                if node_shader is None:               
                    node = mat.node_tree.nodes['Diffuse BSDF']   
                else:
                    node_shader.select = True
                    nodes.active = node_shader                
                    node = mat.node_tree.nodes['Principled BSDF']                                                   
                

                # without nodes
                if self.mat_use_nodes == False:                                                                    
                    
                    # id color    
                    if mat_prefs.mat_color_palette =='id_circle':
                        mat_presets_circle(self, mat)       

                    elif mat_prefs.mat_color_palette =='id_pencil':
                        
                        if mat_prefs.display_palette_pencil =='Metal':
                            mat_presets_metal(self, mat)
                        
                        if mat_prefs.display_palette_pencil =='Wood':
                            mat_presets_wood(self, mat)
                        
                        if mat_prefs.display_palette_pencil =='Fabric':
                            mat_presets_fabric(self, mat)

                        else:
                            mat_presets_pencil(self, mat)

                    # custom colour
                    else:                 
                        add_color = self.mat_color
                        mat = (float(add_color[0]), float(add_color[1]), float(add_color[2]),1)      

                    # set colour
                    if node_shader is None:       
                        node.inputs['Color'].default_value = mat
                    else:                      
                        node.inputs['Base Color'].default_value = mat    

                    if self.mat_use_hexname ==True:
                        hexname = color_to_hex(node.inputs[0].default_value)
                        mat.name = mat_name + '_' + hexname    
            
                # use nodes
                else:

                    # set material id color 
                    if mat_prefs.mat_color_palette =='id_circle':
                        mat_presets_circle_bsdf(self, node)
                        mat_presets_shader_bsdf(self, node)        

                    elif mat_prefs.mat_color_palette =='id_pencil':
                        
                        if mat_prefs.display_palette_pencil =='Metal':
                            mat_presets_metal_bsdf(self, node)
                            mat_presets_metal_type_bsdf(self, node)
                        
                        elif mat_prefs.display_palette_pencil =='Wood':
                            mat_presets_wood_bsdf(self, node)
                            mat_presets_shader_bsdf(self, node) 
                        
                        elif mat_prefs.display_palette_pencil =='Fabric':
                            mat_presets_fabric_bsdf(self, node)
                            mat_presets_shader_bsdf(self, node)   
                        
                        else:
                            mat_presets_pencil_bsdf(self, node)
                            mat_presets_shader_bsdf(self, node) 

                    else:  
                        mat_presets_custom_bsdf(self, node)
                        mat_presets_shader_bsdf(self, node)    

                
                    if self.mat_use_hexname ==True:
                        hexname = color_to_hex(node.inputs[0].default_value)
                        mat.name = mat_name + '_' + hexname         

            # without nodes                                    
            else:           
            
                # id color               
                if mat_prefs.mat_color_palette =='id_circle':
                    mat_presets_circle(self, mat)         
                    mat_presets_diffuse(self, mat)

                elif mat_prefs.mat_color_palette =='id_pencil':
                    
                    if mat_prefs.display_palette_pencil =='Metal':
                        mat_presets_metal(self, mat)
                        mat_presets_metal_type(self, mat)                            
                    
                    if mat_prefs.display_palette_pencil =='Wood':
                        mat_presets_wood(self, mat)
                        mat_presets_diffuse(self, mat)                              
                    
                    if mat_prefs.display_palette_pencil =='Fabric':
                        mat_presets_fabric(self, mat)         
                        mat_presets_diffuse(self, mat)                       
                    
                    else:
                        mat_presets_pencil(self, mat)
                        mat_presets_diffuse(self, mat)
                
                else:            
                    mat.diffuse_color = self.mat_color
                    mat_presets_diffuse(self, mat)
                                

                if self.mat_use_hexname ==True:
                    hexname = color_to_hex(mat.diffuse_color)
                    mat.name = mat_name + '_' + hexname          
      
 
    # bpy.context.object.active_material.pass_index = self.mat_pass_index
        


class RTS_OT_RePattern_Shader_Material(bpy.types.Operator):
    bl_description = "create material shader"
    bl_idname="rts_ot.shader_material"
    bl_label = "RP Shader"
    #bl_options = {'REGISTER', 'UNDO', 'PRESET'} 
    bl_options = {'INTERNAL'} 

    # MATERIAL #
    mat_replace_slot : EnumProperty(
            items=[ ('Replace',  "Replace"  ,"replace shader at first slot" ,'' ,0),
                    ('Top',      "Top"      ,"prepend shader to top"        ,'' ,1),
                    ('Bottom',   "Bottom"   ,"append shader to bottom"      ,'' ,2),
                    ],
                    default='Replace',
                    name="Replace",
                    description="replace first slot / prepend to top / append to bottom")
    
    mat_active_only : BoolProperty(name="Active Only", description="", default=False)   
    mat_use_custom_name : BoolProperty(name="Custom", description = "use custom name instead of color palette name", default = False)
    mat_to_assign : StringProperty(name="Prefix", default="RP_MAT")   
    mat_separator : StringProperty(name="Separator", default="_", description="separator for index number") 
    mat_use_objname : BoolProperty(name="Object Name", description = "add object name to the material description", default = False)
    mat_use_hexname : BoolProperty(name="Hex Name", description = "add hexadezimal name to the material description", default = False)
    mat_use_preset_prefix : BoolProperty(name="", description="add preset prefix", default=True) 
    mat_use_preset_suffix : BoolProperty(name="", description="add preset suffix", default=False) 

    mat_use_id : BoolProperty(name="Custom IDs", description = "add continious id number to material", default = False)#
    mat_numbered : StringProperty(name="Start Number", default="1", description="create number order")# 

    mat_pass_index : IntProperty(name="MAT Pass ID", description="create new material pass index", default=0, min=0, max=10000) 

    mat_assign_single : BoolProperty(name="Single MAT", description = "assign single material to all selected", default = False)
    mat_random_multi : BoolProperty(name="Random MAT", description = "random material", default = False)
    mat_random_amount : IntProperty(name="Random MAT Amount",  description="random material amount", min=0, max=100, default=1) 
   
    mat_use_nodes : BoolProperty(name="Use Nodes", description = "use shader node to render the materials", default = False)

    # BSDF NODE #
    mat_expand_props : BoolProperty(name="Show all Properties", description="", default=False)   

    mat_color : FloatVectorProperty(name='Base Color', description='Index 0', default=(0.9, 0.9, 0.9, 1), min=0, max=1, step=1, precision=4, subtype='COLOR', size=4)
    mat_subsurface : FloatProperty(name="SubSurface", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_subsurface_rd1 : FloatProperty(name="SubSurface Radius", description = "", default = 1.000, min = 0.000, max = 100.000) 
    mat_subsurface_rd2 : FloatProperty(name="SubSurface Radius", description = "", default = 0.200, min = 0.000, max = 100.000) 
    mat_subsurface_rd3 : FloatProperty(name="SubSurface Radius", description = "", default = 0.100, min = 0.000, max = 100.000) 
    mat_subsurface_color : FloatVectorProperty(name='SubSurface Color', description='', default=(0.9, 0.9, 0.9, 1), min=0, max=1, step=1, precision=4, subtype='COLOR', size=4)
    mat_metallic : FloatProperty(name="Metallic", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_specular : FloatProperty(name="Specular", description = "", default = 0.500, min = 0.000, max = 1.000) 
    mat_specular_tint : FloatProperty(name="Specular Tint", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_roughness : FloatProperty(name="Roughness",description = "", default = 0.500, min = 0.000, max = 1.000) 
    mat_anisotropic : FloatProperty(name="Anisotropic", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_anisotropic_rotation : FloatProperty(name="Anisotropic Rotation", description = "", default = 0.000, min = 0.000, max = 1.000)  
    mat_sheen : FloatProperty(name="Sheen", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_sheen_tint : FloatProperty(name="Sheen Tint", description = "", default = 0.500, min = 0.000, max = 1.000) 
    mat_clearcoat : FloatProperty(name="Clearcoat", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_clearcoat_roughness : FloatProperty(name="Clearcoat Roughness", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_ior : FloatProperty(name="IOR", description = "", default = 1.450, min = 0.000, max = 1000.000)  
    mat_transmission : FloatProperty(name="Transmission", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_transmission_roughness : FloatProperty(name="Transmission Roughness", description = "", default = 0.000, min = 0.000, max = 1.000) 
    mat_emission_color : FloatVectorProperty(name='Emission', description='Emission', default=(0.000, 0.000, 0.000, 1.000), min=0, max=1, step=1, precision=4, subtype='COLOR_GAMMA', size=4)
    mat_alpha : FloatProperty(name="Alpha", description = "", default = 1.000, min = 0.000, max = 1.000) 
    
    mat_distribution : EnumProperty(
    name="",
    description="Distribution",
    items=[('GGX',       "GGX"              ,""),
            ('MULTI_GGX', "Multiscatter GGX" ,"")],
            default='MULTI_GGX')

    mat_subsurface_method : EnumProperty(
    name="",
    description="Subsurface Method",
    items=[('BURLEY',      "Christensen-Burley" ,""),
            ('RANDOM_WALK', "Random Walk"        ,"")],
            default='BURLEY')


    mat_color_palette : EnumProperty(
            items = [("id_off"     ," Off"     ,"off"),                       
                    ("id_circle"  ," Circle"  ,"colorcircle"),                       
                    ("id_pencil"  ," Charts"  ,"colorcharts"),                                                                     
                    ("id_hex"     ," HexID"   ,"use hexadzimal values"),    
                    ],             
                    name="",
                    default = "id_off",
                    description="color swats and ids for materials")


    # DEFAULT ID SWAT
    icons = load_icons()
    palette_circle = [("contrast" ,""  ,"Contrast"    ,icons["icon_black"].icon_id    ,1),
                        ("red"      ,""  ,"Red"         ,icons["icon_red"].icon_id      ,2),                         
                        ("blue"     ,""  ,"Blue"        ,icons["icon_blue"].icon_id     ,3),
                        ("green"    ,""  ,"Green"       ,icons["icon_green"].icon_id    ,4),
                        ("brown"    ,""  ,"Brown"       ,icons["icon_brown"].icon_id    ,5),
                        ("all"      ,""  ,"All"         ,icons["icon_all"].icon_id      ,6)]
    display_palette_circle : EnumProperty(name=" ", default = "contrast", items = palette_circle)    


    # FABRIC ID SWAT          
    fabric_type : EnumProperty(
            items=[ ("Custom"           ,"Custom"           ,""),

                    # GREEN COLORS #
                    ("Darkgreen"        ,"Darkgreen"        ,""),                               
                    ("Hunter"           ,"Hunter"           ,""),                               
                    ("Thyme"            ,"Thyme"            ,""),                               
                    ("Grass_1"          ,"Grass 1"          ,""),                               
                    ("Lightgreen"       ,"Lightgreen"       ,""),                               
                    ("Ino_1"            ,"Ino 1"            ,""),                               
                    ("Ino_2"            ,"Ino 2"            ,""),                               
                    ("Grass_2"          ,"Grass 2"          ,""),                               
                    ("Salvia"           ,"Salvia"           ,""),                               
                    ("Pistachio"        ,"Pistachio"        ,""),                               
                    ("Limette"          ,"Limette"          ,""),                               
                    ("Lemon"            ,"Lemon"            ,""),                               
                    
                    # BLUE COLORS #
                    ("Bluedark"         ,"Bluedark"         ,""),                               
                    ("Darknavy"         ,"Darknavy"         ,""),                               
                    ("Darkroyal_blue_2" ,"Darkroyal blue 2" ,""),                               
                    ("Darkroyal_blue_1" ,"Darkroyal blue 1" ,""),                               
                    ("Royal_blue"       ,"Royal_blue"       ,""),                               
                    ("Blue"             ,"Blue"             ,""),                               
                    ("Ice"              ,"Ice"              ,""),                               
                    ("Mint"             ,"Mint"             ,""),                               
                    ("Lightblue"        ,"Lightblue"        ,""),                               
                    ("Grapes"           ,"Grapes"           ,""),                               
                    ("Lightplum"        ,"Lightplum"        ,""),                               
                    ("Lilac"            ,"Lilac"            ,""),                               
                    
                    # BROWN COLORS # 
                    ("Chocolate"        ,"Chocolate"        ,""),                               
                    ("Basalt"           ,"Basalt"           ,""),                               
                    ("Morel"            ,"Morel"            ,""),                               
                    ("Brown"            ,"Brown"            ,""),                               
                    ("Noisette"         ,"Noisette"         ,""),                               
                    ("Hazelnunt"        ,"Hazelnunt"        ,""),                               
                    ("Beige"            ,"Beige"            ,""),                               
                    ("Champanger"       ,"Champanger"       ,""),                               
                    ("Ivory"            ,"Ivory"            ,""),                               
                    ("Burgund"          ,"Burgund"          ,""),                               
                    ("Chestnut"         ,"Chestnut"         ,""),                               
                    ("Caramell"         ,"Caramell"         ,""),                               
                    
                    # RED COLORS #
                    ("Red"              ,"Red"              ,""),                               
                    ("Scarlet"          ,"Scarlet"          ,""),                               
                    ("Raspberry"        ,"Raspberry"        ,""),                               
                    ("Fuchsia"          ,"Fuchsia"          ,""),                               
                    ("Watermelone"      ,"Watermelone"      ,""),                               
                    ("Orange"           ,"Orange"           ,""),                               
                    ("Orangered"        ,"Orangered"        ,""),                               
                    ("Cayenne"          ,"Cayenne"          ,""),                               
                    ("Peach"            ,"Peach"            ,""),                               
                    ("Rose"             ,"Rose"             ,""),                               
                    ("Blossom"          ,"Blossom"          ,""),                               
                    ("Perlrosa"         ,"Perlrosa"         ,""),                               
                    
                    # YELLOW COLORS #
                    ("Mustard"          ,"Mustard"          ,""),                               
                    ("Gold"             ,"Gold"             ,""),                               
                    ("Yelloworange"     ,"Yelloworange"     ,""),                               
                    ("Corn"             ,"Corn"             ,""),                               
                    ("Bumblebee"        ,"Bumblebee"        ,""),                               
                    ("Sungold"          ,"Sungold"          ,""),                               
                    ("Daffoldil"        ,"Daffoldil"        ,""),                               
                    ("Canary"           ,"Canary"           ,""),                               
                    ("Lemongrass"       ,"Lemongrass"       ,""),                               
                    ("Banana"           ,"Banana"           ,""),                               
                    ("Vanille"          ,"Vanille"          ,""),                               
                    ("Creme"            ,"Creme"            ,""),                                                             
                    ("Slate"            ,"Slate"            ,""),                               
                    ("Silver"           ,"Silver"           ,""),
                    
                    # CONTRAST COLORS #
                    ("White"            ,"White"            ,""),
                    ("Gray80"           ,"Gray80"           ,""),
                    ("Gray60"           ,"Gray60"           ,""),
                    ("Gray50"           ,"Gray50"           ,""),
                    ("Gray40"           ,"Gray40"           ,""),
                    ("Gray20"           ,"Gray20"           ,""),
                    ("Black"            ,"Black"            ,""),                 
                    
                    ],                                
                    name="",
                    default = "Custom",    
                    description="bsdf shader palette: fabric")    



    # PENCIL ID SWAT
    palette_pencil = [("Autumn"    ,"Autumn"    ,""),
                      ("Charcoal"  ,"Charcoal"  ,""),
                      ("Graphit"   ,"Graphit"   ,""),
                      ("Metal"     ,"Metal"     ,""),
                      ("Fabric"    ,"Fabric"    ,""),
                      ("Water"     ,"Water"     ,""),
                      ("Wood"      ,"Wood"      ,"")]                   
    display_palette_pencil : EnumProperty(name=" ", default = "Autumn", items = palette_pencil)   

    pencil_type : EnumProperty(
            items=[                                                
                    ("Custom"           ,"Custom"                   ,"custom value"),                   
                    
                    # AUTUMN COLORS #
                    ("Light_Sienna"         ,"Light_Sienna"         ,"autumn swat"),
                    ("Solway_Blue"          ,"Solway_Blue"          ,"autumn swat"),
                    ("Ink_Blue"             ,"Ink_Blue"             ,"autumn swat"),           
                    ("Smoke_Blue"           ,"Smoke_Blue"           ,"autumn swat"),
                    ("Pale_Cedar"           ,"Pale_Cedar"           ,"autumn swat"),
                    ("Green_Shadow"         ,"Green_Shadow"         ,"autumn swat"),
                    ("Crag_Green"           ,"Crag_Green"           ,"autumn swat"),           
                    ("Olive_Earth"          ,"Olive_Earth"          ,"autumn swat"),           
                    ("Warm_Earth"           ,"Warm_Earth"           ,"autumn swat"),           
                    ("Brown_Ochre"          ,"Brown_Ochre"          ,"autumn swat"),           
                    ("Wheat"                ,"Wheat"                ,"autumn swat"),           
                    ("Yellow_Ochre"         ,"Yellow_Ochre"         ,"autumn swat"),
                    ("Sepia_Red"            ,"Sepia_Red"            ,"autumn swat"),
                    ("Mars_Orange"          ,"Mars_Orange"          ,"autumn swat"),
                    ("Sanguine"             ,"Sanguine"             ,"autumn swat"),
                    ("Venetian_Red"         ,"Venetian_Red"         ,"autumn swat"),
                    ("Terracotta"           ,"Terracotta"           ,"autumn swat"),
                    ("Mars_Violet"          ,"Mars_Violet"          ,"autumn swat"),
                    ("Ruby_Earth"           ,"Ruby_Earth"           ,"autumn swat"),
                    ("Chocolate"            ,"Chocolate"            ,"autumn swat"),
                    ("Ivory_Black"          ,"Ivory_Black"          ,"autumn swat"),
                    ("Warm_Gray"            ,"Warm_Gray"            ,"autumn swat"),
                    ("Cool_Gray"            ,"Cool_Gray"            ,"autumn swat"),

                    # GRAPHITINT COLORS #
                    ("Port"                 ,"Port"                 ,"graphit-int swat"),
                    ("Juniper"              ,"Juniper"              ,"graphit-int swat"),
                    ("Aubergine"            ,"Aubergine"            ,"graphit-int swat"),
                    ("Dark_Indigo"          ,"Dark_Indigo"          ,"graphit-int swat"),
                    ("Shadow"               ,"shadow"               ,"graphit-int swat"),
                    ("Steel_Blue"           ,"Steel_Blue"           ,"graphit-int swat"),
                    ("Ocean_Blue"           ,"Ocean_Blue"           ,"graphit-int swat"),
                    ("Slate_Green"          ,"Slate_Green"          ,"graphit-int swat"),
                    ("Meadow"               ,"Meadow"               ,"graphit-int swat"),
                    ("Ivy"                  ,"Ivy"                  ,"graphit-int swat"),
                    ("Sage"                 ,"Sage"                 ,"graphit-int swat"),
                    ("Chestnut"             ,"Chestnut"             ,"graphit-int swat"),
                    ("Russet"               ,"Russet"               ,"graphit-int swat"),
                    ("Cool_Brown"           ,"Cool_Brown"           ,"graphit-int swat"),
                    ("Cocoa"                ,"Cocoa"                ,"graphit-int swat"),
                    ("Autumn_Brown"         ,"Autumn_Brown"         ,"graphit-int swat"),
                    ("Storm"                ,"Storm"                ,"graphit-int swat"),
                    ("Warm_Gray"            ,"Warm_Gray"            ,"graphit-int swat"),
                    ("Midnight_Black"       ,"Midnight_Black"       ,"graphit-int swat"),
                    ("Mountain_Gray"        ,"Mountain_Gray"        ,"graphit-int swat"),
                    ("Cloud_Gray"           ,"Cloud_Gray"           ,"graphit-int swat"),
                    ("Cool_Gray"            ,"Cool_Gray"            ,"graphit-int swat"),
    
                    # TINTED CHARCOAL COLORS #
                    ("Sand"                 ,"Sand"                 ,"tinted charcoal swat"),
                    ("Burnt_Orange"         ,"Burnt_Orange"         ,"tinted charcoal swat"),
                    ("Sunset_Pink"          ,"Sunset_Pink"          ,"tinted charcoal swat"),
                    ("Glowing_Embers"       ,"Glowing_Embers"       ,"tinted charcoal swat"),
                    ("Heather_Mist"         ,"Heather_Mist"         ,"tinted charcoal swat"),
                    ("Burnt_Embers"         ,"Burnt_Embers"         ,"tinted charcoal swat"),
                    ("Lavender"             ,"Lavender"             ,"tinted charcoal swat"),
                    ("Thistle"              ,"Thistle"              ,"tinted charcoal swat"),
                    ("Bilberry"             ,"Bilberry"             ,"tinted charcoal swat"),         
                    ("Elderberry"           ,"Elderberry"           ,"tinted charcoal swat"),           
                    ("Mountain_Blue"        ,"Mountain_Blue"        ,"tinted charcoal swat"),
                    ("Ocean_Deep"           ,"Ocean_Deep"           ,"tinted charcoal swat"),
                    ("Slate"                ,"Slate"                ,"tinted charcoal swat"),
                    ("Forest_Pine"          ,"Forest_Pine"          ,"tinted charcoal swat"),
                    ("Green_Moss"           ,"Green_Moss"           ,"tinted charcoal swat"),
                    ("Dark_Moss"            ,"Dark_Moss"            ,"tinted charcoal swat"),
                    ("Driftwood"            ,"Driftwood"            ,"tinted charcoal swat"),
                    ("Peat"                 ,"Peat"                 ,"tinted charcoal swat"),
                    ("Burnt_Earth"          ,"Burnt_Earth"          ,"tinted charcoal swat"),
                    ("Natural"              ,"Natural"              ,"tinted charcoal swat"),
                    ("Charcoal_Light"       ,"Charcoal_Light"       ,"tinted charcoal swat"),
                    ("Charcoal_Medium"      ,"Charcoal_Medium"      ,"tinted charcoal swat"),
                    ("Charcoal_Dark"        ,"Charcoal_Dark"        ,"tinted charcoal swat"),
                    ("Charcoal_Black"       ,"Charcoal_Black"       ,"tinted charcoal swat"),

                    # WATER COLORS #
                    ("Zinc_Yellow"          ,"Zinc_Yellow"          ,"water swat"),
                    ("Lemon_Cadmium"        ,"Lemon_Cadmium"        ,"water swat"),
                    ("Gold"                 ,"Gold"                 ,"water swat"),
                    ("Primrose_Yellow"      ,"Primrose_Yellow"      ,"water swat"),
                    ("Straw_Yellow"         ,"Straw_Yellow"         ,"water swat"),
                    ("Deep_Cadmium"         ,"Deep_Cadmium"         ,"water swat"),
                    ("Naples_Yellow"        ,"Naples_Yellow"        ,"water swat"),
                    ("Middle_Chrome"        ,"Middle_Chrome"        ,"water swat"),
                    ("Deep_Chrome"          ,"Deep_Chrome"          ,"water swat"),
                    ("Orange_Chrome"        ,"Orange_Chrome"        ,"water swat"),
                    ("Spectrum_Orange"      ,"Spectrum_Orange"      ,"water swat"),
                    ("Scarlet_Lake"         ,"Scarlet_Lake"         ,"water swat"),
                    ("Pale_Vermilion"       ,"Pale_Vermilion"       ,"water swat"),
                    ("Geranium_Lake"        ,"Geranium_Lake"        ,"water swat"),
                    ("Flesh_Pink"           ,"Flesh_Pink"           ,"water swat"),
                    ("Pink_Madder_Lake"     ,"Pink_Madder_Lake"     ,"water swat"),
                    ("Rose_Pink"            ,"Rose_Pink"            ,"water swat"),           
                    ("Madder_Carmine"       ,"Madder_Carmine"       ,"water swat"),         
                    ("Crimson_Lake"         ,"Crimson_Lake"         ,"water swat"),
                    ("Rose_Madder_Lake"     ,"Rose_Madder_Lake"     ,"water swat"),
                    ("Magenta"              ,"Magenta"              ,"water swat"),
                    ("Imperial_Purple"      ,"Imperial_Purple"      ,"water swat"),    
                    ("Red_Violet_Lake"      ,"Red_Violet_Lake"      ,"water swat"),
                    ("Dark_Violet"          ,"Dark_Violet"          ,"water swat"),
                    ("Light_Violet"         ,"Light_Violet"         ,"water swat"),
                    ("Blue_Violet_Lake"     ,"Blue_Violet_Lake"     ,"water swat"),
                    ("Delft_Blue"           ,"Delft_Blue"           ,"water swat"),
                    ("Ultramarine"          ,"Ultramarine"          ,"water swat"),
                    ("Smalt_Blue"           ,"Smalt_Blue"           ,"water swat"),
                    ("Cobald_Blue"          ,"Cobald_Blue"          ,"water swat"),
                    ("Spectrum_Blue"        ,"Spectrum_Blue"        ,"water swat"),
                    ("Light_Blue"           ,"Light_Blue"           ,"water swat"),
                    ("Sky_Blue"             ,"Sky_Blue"             ,"water swat"),
                    ("Prussian_Blue"        ,"Prussian_Blue"        ,"water swat"),
                    ("Indigo"               ,"Indigo"               ,"water swat"),
                    ("Oriental_Blue"        ,"Oriental_Blue"        ,"water swat"),
                    ("Kingfisher"           ,"Kingfisher"           ,"water swat"),
                    ("Turquoise_Blue"       ,"Turquoise_Blue"       ,"water swat"),
                    ("Turquoise_Green"      ,"Turquoise_Green"      ,"water swat"),
                    ("Jade_Green"           ,"Jade_Green"           ,"water swat"),
                    ("Juniper_Green"        ,"Juniper_Green"        ,"water swat"),
                    ("Bottle_Green"         ,"Bottle_Green"         ,"water swat"),
                    ("Water_Green"          ,"Water_Green"          ,"water swat"),
                    ("Mineral_Green"        ,"Mineral_Green"        ,"water swat"),
                    ("Emerald_Green"        ,"Emerald_Green"        ,"water swat"),
                    ("Grass_Green"          ,"Grass_Green"          ,"water swat"),
                    ("May_Green"            ,"May_Green"            ,"water swat"),
                    ("Sap_Green"            ,"Sap_Green"            ,"water swat"),
                    ("Cedar_Green"          ,"Cedar_Green"          ,"water swat"),
                    ("Olive_Green"          ,"Olive_Green"          ,"water swat"),
                    ("Bronze"               ,"Bronze"               ,"water swat"),
                    ("Sepia"                ,"Sepia"                ,"water swat"),
                    ("Burnt_Umber"          ,"Burnt_Umber"          ,"water swat"),
                    ("Vandyke_Brown"        ,"Vandyke_Brown"        ,"water swat"),
                    ("Raw_Umber"            ,"Raw_Umber"            ,"water swat"),
                    ("Brown_Ochre"          ,"Brown_Ochre"          ,"water swat"),
                    ("Raw_Sienna"           ,"Raw_Sienna"           ,"water swat"),
                    ("Golden_Brown"         ,"Golden_Brown"         ,"water swat"),
                    ("Burnt_Yellow_Ochre"   ,"Burnt_Yellow_Ochre"   ,"water swat"),
                    ("Copper_Beach"         ,"Copper_Beach"         ,"water swat"),
                    ("Burnt_Sienna"         ,"Burnt_Sienna"         ,"water swat"),
                    ("Venetia_Red"          ,"Venetia_Red"          ,"water swat"),          
                    ("Terracotta"           ,"Terracotta"           ,"water swat"),         
                    ("Burnt_Carmine"        ,"Burnt_Carmine"        ,"water swat"),
                    ("Chocolate"            ,"Chocolate"            ,"water swat"),
                    ("Ivory_Black"          ,"Ivory_Black"          ,"water swat"),
                    ("Blue_Gray"            ,"Blue_Gray"            ,"water swat"),
                    ("Gun_Metal"            ,"Gun_Metal"            ,"water swat"),
                    ("French_Gray"          ,"French_Gray"          ,"water swat"),
                    ("Silver_Gray"          ,"Silver_Gray"          ,"water swat"),

                    # INKTENSE COLORS #
                    ("Sherbert_Lemon"       ,"Sherbert_Lemon"       ,"inktense swat"),
                    ("Sun_Yellow"           ,"Sun_Yellow"           ,"inktense swat"),
                    ("Cadmium_Yellow"       ,"Cadmium_Yellow"       ,"inktense swat"),
                    ("Silician_Yellow"      ,"Silician_Yellow"      ,"inktense swat"),
                    ("Golden_Yellow"        ,"Golden_Yellow"        ,"inktense swat"),
                    ("Sienna_Gold"          ,"Sienna_Gold"          ,"inktense swat"),
                    ("Cadmium_Orange"       ,"Cadmium_Orange"       ,"inktense swat"),
                    ("Burnt_Orange"         ,"Burnt_Orange"         ,"inktense swat"),
                    ("Tangerine"            ,"Tangerine"            ,"inktense swat"),
                    ("Mid_Vermilion"       ,"Mid_Vermilion"         ,"inktense swat"),
                    ("Scarlet_Pink"         ,"Scarlet_Pink"         ,"inktense swat"),
                    ("Poppy_Red"            ,"Poppy_Red"            ,"inktense swat"),
                    ("Hot_Red"              ,"Hot_Red"              ,"inktense swat"),
                    ("Chilli_Red"           ,"Chilli_Red"           ,"inktense swat"),
                    ("Cherry"               ,"Cherry"               ,"inktense swat"),
                    ("Carmine_Pink"         ,"Carmine_Pink"         ,"inktense swat"),
                    ("Crimson"              ,"Crimson"              ,"inktense swat"),
                    ("Shiraz"               ,"Shiraz"               ,"inktense swat"),
                    ("Red_Violet"           ,"Red_Violet"           ,"inktense swat"),
                    ("Fuchsia"              ,"Fuchsia"              ,"inktense swat"),
                    ("Deep_Rose"            ,"Deep_Rose"            ,"inktense swat"),     
                    ("Thistle"              ,"Thistle"              ,"inktense swat"),
                    ("Dusky_Purple"         ,"Dusky_Purple"         ,"inktense swat"),
                    ("Mauve"                ,"Mauve"                ,"inktense swat"),
                    ("Dark_Purple"          ,"Dark_Purple"          ,"inktense swat"),
                    ("Deep_Violet"          ,"Deep_Violet"          ,"inktense swat"),
                    ("Violet"               ,"Violet"               ,"inktense swat"),
                    ("Lagoon"               ,"Lagoon"               ,"inktense swat"),
                    ("Peacock_Blue"         ,"Peacock_Blue"         ,"inktense swat"),
                    ("Navy_Blue"            ,"Navy_Blue"            ,"inktense swat"),
                    ("Iron_Blue"            ,"Iron_Blue"            ,"inktense swat"),
                    ("Deep_Blue"            ,"Deep_Blue"            ,"inktense swat"),
                    ("Iris_Blue"            ,"Iris_Blue"            ,"inktense swat"),
                    ("Bright_Blue"          ,"Bright_Blue"          ,"inktense swat"),
                    ("Deep_Indigo"          ,"Deep_Indigo"          ,"inktense swat"),  
                    ("Dark_Aquamarine"      ,"Dark_Aquamarine"      ,"inktense swat"),
                    ("Turquoise"            ,"Turquoise"            ,"inktense swat"),
                    ("Green_Aquamarine"     ,"Green_Aquamarine"     ,"inktense swat"),
                    ("Mallard_Green"        ,"Mallard_Green"        ,"inktense swat"),
                    ("Teal_Green"           ,"Teal_Green"           ,"inktense swat"),
                    ("Iron_Green"           ,"Iron_Green"           ,"inktense swat"),
                    ("Ionian_Green"         ,"Ionian_Green"         ,"inktense swat"),
                    ("Vivid_Green"          ,"Vivid_Green"          ,"inktense swat"),
                    ("Apple_Green"          ,"Apple_Green"          ,"inktense swat"),
                    ("Field_Green"          ,"Field_Green"          ,"inktense swat"),
                    ("Beech_Green"          ,"Beech_Green"          ,"inktense swat"),
                    ("Hookers_Green"        ,"Hookers_Green"        ,"inktense swat"),
                    ("Felt_Green"           ,"Felt_Green"           ,"inktense swat"),
                    ("Light_Olive"          ,"Light_Olive"          ,"inktense swat"),
                    ("Spring_Green"         ,"Spring_Green"         ,"inktense swat"),
                    ("Fern"                 ,"Fern"                 ,"inktense swat"),
                    ("Leaf_Green"           ,"Leaf_Green"           ,"inktense swat"),
                    ("Mustard"              ,"Mustard"              ,"inktense swat"),
                    ("Amber"                ,"Amber"                ,"inktense swat"),
                    ("Tan"                  ,"Tan"                  ,"inktense swat"),
                    ("Oak"                  ,"Oak"                  ,"inktense swat"),
                    ("Saddle_Brown"         ,"Saddle_Brown"         ,"inktense swat"),
                    ("Baked_Earth"          ,"Baked_Earth"          ,"inktense swat"),
                    ("Willow"               ,"Willow"               ,"inktense swat"),
                    ("Oxide_Red"            ,"Oxide_Red"            ,"inktense swat"),
                    ("Madder_Brown"         ,"Madder_Brown"         ,"inktense swat"),
                    ("Dark_Chocolate"       ,"Dark_Chocolate"       ,"inktense swat"),
                    ("Bark"                 ,"Bark"                 ,"inktense swat"),
                    ("Sepia_Ink"            ,"Sepia_Ink"            ,"inktense swat"),
                    ("Indian_Ink"           ,"Indian_Ink"           ,"inktense swat"),
                    ("Chinese_Ink"          ,"Chinese_Ink"          ,"inktense swat"),
                    ("Charcoal_Gray"        ,"Charcoal_Gray"        ,"inktense swat"),
                    ("Paynes_Gray"          ,"Paynes_Gray"          ,"inktense swat"),
                    ("Neutral_Gray"         ,"Neutral_Gray"         ,"inktense swat"),
                    ("Ink_Black"            ,"Ink_Black"            ,"inktense swat"),                            
                    ("Blacken"              ,"Blacken"              ,"inktense swat"),                            
                    ("Dark_Slate"           ,"Dark_Slate"           ,"inktense swat"),                            
                    ("Silver"               ,"Silver"               ,"inktense swat"),                        

                    # CONTRAST COLORS #
                    ("White"                ,"White"                ,"contrast swat"),
                    ("gray08"               ,"Gray80"               ,"contrast swat"),
                    ("gray06"               ,"Gray60"               ,"contrast swat"),
                    ("gray05"               ,"Gray50"               ,"contrast swat"),
                    ("gray04"               ,"Gray40"               ,"contrast swat"),
                    ("gray02"               ,"Gray20"               ,"contrast swat"),
                    ("Black"                ,"Black"                ,"contrast swat")],       
                                
                    name="",
                    default = "Custom",    
                    description="bsdf shader palette: pencil")    


    # WOOD ID SWAT
    wood_type : EnumProperty(
            items=[
            ("Custom",    "Custom",          ""), 
            ("Acacia_steamed" ,  "Acacia_steamed",  ""),
            ("Apple_india"    ,  "Apple_india",     ""),
            ("Ash"            ,  "Ash",             ""),
            ("Bamboo_steamed" ,  "Bamboo_steamed",  ""),
            ("Bangkirai"      ,  "Bangkirai",       ""),
            ("Beech_steamed"  ,  "Beech_steamed",   ""),
            ("Cherry_amer"    ,  "Cherry_amer",     ""),
            ("Cherry_eur"     ,  "Cherry_eur",      ""),
            ("Cumaru"         ,  "Cumaru",          ""),
            ("Doussie"        ,  "Doussie",         ""),
            ("Garapa"         ,  "Garapa",          ""),
            ("Ipe"            ,  "Ipe",             ""),
            ("Iroko_kambala"  ,  "Iroko_kambala",   ""),
            ("Jacaranda"      ,  "Jacaranda",       ""),
            ("Jatoba"         ,  "Jatoba",          ""),
            ("Kempas"         ,  "Kempas",          ""),
            ("Larch"          ,  "Larch",           ""),
            ("Macassar"       ,  "Macassar",        ""),
            ("Maple_can"      ,  "Maple_can",       ""),
            ("Maple_eur"      ,  "Maple_eur",       ""),
            ("Massaranduba"   ,  "Massaranduba",    ""),
            ("Merbau"         ,  "Merbau",          ""),
            ("Oak"            ,  "Oak",             ""),
            ("Oak_darkbrown"  ,  "Oak_darkbrown",   ""),
            ("Oak_middlebraun",  "Oak_middlebraun", ""),
            ("Oak_redbrown"   ,  "Oak_redbrown",    ""),
            ("Oak_smoked_core",  "Oak_smoked_core", ""),
            ("Oak_white"      ,  "Oak_white",       ""),
            ("Olive"          ,  "Olive",           ""),
            ("Panga_panga"    ,  "Panga_panga",     ""),
            ("Pear"           ,  "Pear",            ""),
            ("Teak"           ,  "Teak",            ""),
            ("Walnut_amer"    ,  "Walnut_amer",     ""),
            ("Walnut_eur"     ,  "Walnut_eur",      ""),
            ("Wenge"          ,  "Wenge",           ""),
            ("Willow"         ,  "Willow",          ""),
            ("Zebrano"        ,  "Zebrano",         ""),
            ],                                        
            name="",
            default = "Custom",    
            description="bsdf shader palette: colour id")   


    # TEMP ID 
    palette_ddo = [("None"     ,"None"     ,""),
                   ("Fabric"   ,"Fabric"   ,""), 
                   ("Glass"    ,"Glass"    ,""), 
                   ("Gemstone" ,"Gemstone" ,""), 
                   ("Human"    ,"Human"    ,""), 
                   ("Light"    ,"Light"    ,""), 
                   ("Metal"    ,"Metal"    ,""), 
                   ("Nature"   ,"Nature"   ,""), 
                   ("Painted"  ,"Painted"  ,""), 
                   ("Plastic"  ,"Plastic"  ,""),    
                   ("Rubber"   ,"Rubber"   ,""),    
                   ("Soil"     ,"Soil"     ,""), 
                   ("Street"   ,"Street"   ,""),
                   ("Stone"    ,"Stone"    ,""),
                   ("Water"    ,"Water"    ,""),
                   ("Wood"     ,"Wood"     ,"")]                  
    mat_id_category : EnumProperty(name=" ", default = "None", items = palette_ddo)    

    cat_nature : EnumProperty(
            items=[
            #NATURE
            ("None",  "None",             ""), 
            ("Soil",        "Soil",       ""),  
            ("Dirt",        "Dirt",       ""),
            ("Dust",        "Dust",       ""),
            ("Earth",       "Earth",      ""),
            ("Grass",       "Grass",      ""),
            ("Mud",         "Mud",        ""),
            ("Sand",        "Sand",       ""),             
            ("Sand_Dry",    "Sand_Dry",   ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for natur")    

    cat_water : EnumProperty(
            items=[
            # WATER COLORS #
            ("None",  "None",                       ""), 
            ("Water",           "Water",            ""),
            ("Ice",             "Ice",              ""),
            ("Ice_Cube",        "Ice_Cube",         ""),
            ("Ice_Ocean",       "Ice_Ocean",        ""),
            ("Liquid",          "Liquid",           ""),               
            ("Milk",            "Milk",             ""),  
            ("Snow",            "Snow",             ""), 
            ("Snow_Melting",    "Snow_Melting",     ""), 
            ],                                        
            name="",
            default = "None",    
            description="ids for liquids")                  
    
    cat_wood : EnumProperty(
            items=[
            # WOOD COLORS # 
            ("None",            "None",            ""),                                 
            ("Wood_Bare",       "Wood_Bare",       ""),                    
            ("Wood_Raw",        "Wood_Raw",        ""),
            ("Wood_Varnished",  "Wood_Varnished",  ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for wood")                                    
            
    cat_painted : EnumProperty(
            items=[              
            # PAINTED COLORS #
            ("None",      "None",     ""),    
            ("Acrylic",   "Acrylic",  ""),    
            ("Asphalt",   "Asphalt",  ""),     
            ("Concrete",  "Concrete", ""), 
            ("Metal",     "Metal",    ""), 
            ("Plastic",   "Plastic",  ""),
            ("Rubber",    "Rubber",   ""),
            ("Rust",      "Rust",     ""), 
            ("Stone",     "Stone",    ""),
            ("Wood",      "Wood",     ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for painted")                 

    cat_light : EnumProperty(
            items=[     
            # LIGHT COLORS #             
            ("None",       "None",       ""),
            ("Car",        "Car",        ""),
            ("Car_Orange", "Car_Orange", ""), 
            ("Head",       "Head",       ""), 
            ("Soot",       "Soot",       ""),
            ("Wax",        "Wax",        ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for light")                 

    cat_glass : EnumProperty(
            items=[   
            # GLASS COLORS #           
            ("None",    "None",     ""), 
            ("Glass",   "Colored",  ""), 
            ("Bottle",  "Bottle",   ""), 
            ("Plexi",   "Plexi",    ""),            
            ("Window",  "Window",   ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for glass")                

    cat_gems : EnumProperty(
            items=[   
            # GEMSTONE COLORS #  
            ("None",      "None",     ""),  
            ("Crystal",   "Crystal",  ""),
            ("Diamond",   "Diamond",  ""), 
            ("Ruby",      "Ruby",     ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for gemstone")                 

    cat_human : EnumProperty(
            items=[   
            # HUMAN COLORS #
            ("None",        "None",        ""),
            ("Bone",        "Bone",        ""),
            ("Eyeball",     "Eyeball",     ""),
            ("Fingernail",  "Fingernail",  ""),
            ("Hair",        "Hair",        ""),
            ("Iris",        "Iris",        ""),
            ("Lips",        "Lips",        ""),
            ("Pupil",       "Pupil",       ""),
            ("Skin",        "Skin",        ""), 
            ("Skin_Rough",  "Skin_Rough",  ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for human")                

    cat_fabric : EnumProperty(
            items=[   
            # FABRIC COLORS #  
            ("None",      "None",       ""),
            ("Carpet",    "Carpet",     ""),
            ("Cotton",    "Cotton",     ""),
            ("Denim",     "Denim",      ""),
            ("Leather",   "Leather",    ""),
            ("Nylon",     "Nylon",      ""),
            ("Silk",      "Silk",       ""),
            ("Synthetic", "Synthetic",  ""), 
            ("Velvet",    "Velvet",     ""),
            ("Velvetin",  "Velvetin",   ""),
            ("Wool",      "Wool",       ""),
            ("Yarn",      "Yarn",       ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for fabric")                



    cat_street : EnumProperty(
            items=[   
            # STREET COLORS # 
            ("None",           "None",          ""), 
            ("Asphalt",        "Asphalt",       ""), 
            ("Asphalt_Fresh",  "Asphalt_Fresh", ""),
            ("Asphalt_Tar",    "Asphalt_Tar",   ""),
            ("Asphalt_Worn",   "Asphalt_Worn",  ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for streets")                

    cat_stone : EnumProperty(
            items=[   
            # STONE COLORS #    
            ("None",            "None",             ""),
            ("Brick",           "Brick",            ""),
            ("Cement",          "Cement",           ""),
            ("Cement_Clean",    "Cement_Clean",     ""),
            ("Cement_White",    "Cement_White",     ""),
            ("Ceramic",         "Ceramic",          ""),
            ("Charcoal",        "Charcoal",         ""),
            ("Clay",            "Clay",             ""),
            ("Clay_Dry",        "Clay_Dry",         ""),
            ("Concrete",        "Concrete",         ""),
            ("Concrete_New",    "Concrete_New",     ""),
            ("Concrete_Old",    "Concrete_Old",     ""),         
            ("Concrete_Rough",  "Concrete_Rough",   ""),
            ("Graphite",        "Graphite",         ""),
            ("Gravel",          "Gravel",           ""), 
            ("Grout",           "Grout",            ""),
            ("Marble",          "Marble",           ""),
            ("Mortar",          "Mortar",           ""),
            ("Pearl",           "Pearl",            ""),
            ("Pebble",          "Pebble",           ""), 
            ("Porcelain",       "Porcelain",        ""),
            ("Quartz",          "Quartz",           ""),
            ("Rock",            "Rock",             ""),
            ("Rock_Rough",      "Rock_Rough",       ""),
            ("Terracotta",      "Terracotta",       ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for stone")                                 
    
    cat_rubber : EnumProperty(
            items=[   
            # RUBBER COLORS #
            ("None",       "None",       ""),
            ("Dried",      "Dried",      ""),
            ("Latex",      "Latex",      ""),
            ("Natural",    "Natural",    ""),
            ("Silicone",   "Silicone",   ""),
            ("Synthetic",  "Synthetic",  ""),
            ("Tire",       "Tire",       ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for rubber")                                           
    
    cat_plastic : EnumProperty(
            items=[   
            # PLASTIC COLORS #  
            ("None",            "None",             ""),
            ("Acrylic_Black",   "Acrylic_Black",    ""),
            ("Acrylic_White",   "Acrylic_White",    ""),
            ("Carbon",          "Carbon",           ""),
            ("Carbon_Abs",      "Carbon_Abs",       ""),
            ("Carbon_Fiber",    "Carbon_Fiber",     ""),
            ("Plastic_Grainy",  "Plastic_Grainy",   ""),
            ("Polyester",       "Polyester",        ""), 
            ("Polyethylene",    "Polyethylene",     ""),
            ("Polypropylene",   "Polypropylene",    ""),
            ("PVC",             "PVC",              ""),
            ("PVC_Blue",        "PVC_Blue",         ""),                  
            ("PVC_Green",       "PVC_Green",        ""),
            ("PVC_Red",         "PVC_Red",          ""),
            ("Teflon",          "Teflon",           ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for plastic")                                  

    cat_metal : EnumProperty(
            items=[   
            # METAL COLORS # 
            ("None",        "None",         ""),
            ("Aluminium",   "Aluminium",    ""),
            ("Anodized",    "Anodized",     ""),
            ("Bakelite",    "Bakelite",     ""),
            ("Brass",       "Brass",        ""), 
            ("Bronze",      "Bronze",       ""),
            ("Brushed",     "Brushed",      ""),                        
            ("Chrome",      "Chrome",       ""),
            ("Cobalt",      "Cobalt",       ""),
            ("Copper",      "Copper",       ""),
            ("Foil",        "Foil",         ""), 
            ("Gallium",     "Gallium",      ""), 
            ("Galvanized",  "Galvanized",   ""), 
            ("Gold",        "Gold",         ""), 
            ("Iron",        "Iron",         ""),
            ("Lead",        "Lead",         ""),
            ("Molybdenum",  "Molybdenum",   ""),
            ("Nickel",      "Nickel",       ""),
            ("Pewter",      "Pewter",       ""),                       
            ("Platinum",    "Platinum",     ""),
            ("Rhodium",     "Rhodium",      ""),
            ("Rust",        "Rust",         ""), 
            ("Silver",      "Silver",       ""),
            ("Steel",       "Steel",        ""),
            ("Tin",         "Tin",          ""),
            ("Titanium",    "Titanium",     ""),
            ("Tungsten",    "Tungsten",     ""),
            ("Vanadium",    "Vanadium",     ""),
            ("Zinc",        "Zinc",         ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for metal")                                            

    cat_contrast : EnumProperty(
            items=[   
            # CONTRAST # 
            ("None",    "None",    ""),
            ("Black",   "Black",   ""),
            ("Gray20",  "Gray20",  ""),
            ("Gray40",  "Gray40",  ""),
            ("Gray50",  "Gray50",  ""),
            ("Gray60",  "Gray60",  ""),
            ("Gray80",  "Gray80",  ""),
            ("White",   "White",   ""),
            ],                                        
            name="",
            default = "None",    
            description="ids for greyscale")   





    mat_presets_type : EnumProperty(
            items=[("Custom"     ,"Custom"      ,"custom"),           
                    ("Acrylic"    ,"Acryl"      ,"dialectric"),
                    ("Brick"      ,"Brick"      ,"dialectric"),  
                    ("Ceramic"    ,"Ceramic"    ,"dialectric"),  
                    ("Cotton"     ,"Cotton"     ,"dialectric"),  
                    ("Dirt"       ,"Dirt"       ,"dialectric"),  
                    ("Glass"      ,"Glass"      ,"dialectric"),  
                    ("Glossy"     ,"Glossy"     ,"dialectric"),
                    ("Latex"      ,"Latex"      ,"dialectric"),
                    ("Leather"    ,"Leather"    ,"dialectric"),                             
                    ("Matte"      ,"Matte"      ,"dialectric"),
                    ("Metal"      ,"Metal"      ,"dialectric"),                                                                        
                    ("Mirror"     ,"Mirror"     ,"dialectric"),                                                    
                    ("Mud"        ,"Mud"        ,"dialectric"),                                                                       
                    ("Plaster"    ,"Plaster"    ,"dialectric"),                                                     
                    ("Plastic"    ,"Plastic"    ,"dialectric"),                                             
                    ("PVC"        ,"PVC"        ,"dialectric"),                             
                    ("Rock"       ,"Rock"       ,"dialectric"),
                    ("Rubber"     ,"Rubber"     ,"dialectric"),
                    ("Silicone"   ,"Silicone"   ,"dialectric"),                                                                                                        
                    ("Wood"       ,"Wood"       ,"dialectric"),                                                        
                    ],                                
                    name="",
                    default = "Custom",    
                    description="material shader presets")


    mat_presets_type_bsdf : EnumProperty(
              items=[("Custom"     ,"Custom"        ,"custom"),
                     ("Acryl"      ,"Acryl"         ,"dialectric"),
                     ("Asphalt"    ,"Asphalt"       ,"dialectric"),
                     ("Atmosphere" ,"Atmosphere*"   ,"dialectric"),
                     ("Bark"       ,"Bark"          ,"dialectric"),
                     ("Blood"      ,"Blood*"        ,"dialectric"),
                     ("Brick"      ,"Brick"         ,"dialectric"),
                     ("Carbon"     ,"Carbon"        ,"dialectric"),
                     ("Ceramic"    ,"Ceramic"       ,"dialectric"),
                     ("Car"        ,"Car"           ,"dialectric"),
                     ("Chalk"      ,"Chalk"         ,"dialectric"),
                     ("Cloth"      ,"Cloth"         ,"dialectric"),
                     ("Cloud"      ,"Cloud*"        ,"dialectric"),
                     ("Coal"       ,"Coal"          ,"dialectric"),
                     ("Concrete"   ,"Concrete"      ,"dialectric"),
                     ("Cotton"     ,"Cotton"        ,"dialectric"),                      
                     ("Curtain"    ,"Curtain*"      ,"dialectric"),
                     ("Dirt"       ,"Dirt"          ,"dialectric"),
                     ("Glass"      ,"Glass"         ,"dialectric"),                  
                     ("Latex"      ,"Latex"         ,"dialectric"),
                     ("Leather"    ,"Leather"       ,"dialectric"),     
                     ("Light"      ,"Light*"        ,"dialectric"),
                     ("Matte"      ,"Matte"         ,"dialectric"),                    
                     ("Metal"      ,"Metal"         ,"metal"),                
                     ("Milk"       ,"Milk"          ,"dialectric"),                
                     ("Mirror"     ,"Mirror"        ,"dialectric"),                
                     ("Mud"        ,"Mud"           ,"dialectric"),
                     ("Ocean"      ,"Ocean*"        ,"dialectric"),
                     ("Particles"  ,"Particles*"    ,"dialectric"),
                     ("Paper"      ,"Paper"         ,"dialectric"),
                     ("Plaster"    ,"Plaster"       ,"dialectric"),
                     ("Plastic"    ,"Plastic"       ,"dialectric"),
                     ("PBRD"       ,"PBR-D*"        ,"pbr-metallic-displace"),                         
                     ("PBRE"       ,"PBR-E*"        ,"pbr-metallic-emission"),                        
                     ("PBRM"       ,"PBR-M*"        ,"pbr-metallic"),                                       
                     ("PVC"        ,"PVC"           ,"dialectric"),                     
                     ("Rock"       ,"Rock"          ,"dialectric"),
                     ("Rubber"     ,"Rubber"        ,"dialectric"),
                     ("Rust"       ,"Rust"          ,"dialectric"),
                     ("Sand"       ,"Sand"          ,"dialectric"),
                     ("Satin"      ,"Satin"         ,"dialectric"),
                     ("Silicone"   ,"Silicone"      ,"dialectric"),                      
                     ("Skin"       ,"Skin*"         ,"dialectric"),
                     ("Snow"       ,"Snow*"         ,"dialectric"),
                     ("SSS"        ,"SSS"           ,"dialectric"),                
                     ("Transparent","Transparent*"  ,"dialectric"),
                     ("Wax"        ,"Wax*"          ,"dialectric"),
                     ("Wood"       ,"Wood"          ,"dialectric"),
                     ],                                
                     name="",
                     default = "Custom",    
                     description="material shader presets")


    metal_type : EnumProperty(
            items=[("Custom"           ,"Custom"           ,""),
                   ("Aluminium"        ,"Aluminium"        ,""),
                   ("Beryllium"        ,"Beryllium"        ,""),
                   ("Bismuth"          ,"Bismuth"          ,""),
                   ("Brass"            ,"Brass"            ,""),
                   ("Bronze"           ,"Bronze"           ,""),
                   ("Chromium"         ,"Chromium"         ,""),
                   ("Cobalt"           ,"Cobalt"           ,""),
                   ("Copper"           ,"Copper"           ,""),
                   ("Gallium"          ,"Gallium"          ,""),
                   ("Germanium"        ,"Germanium"        ,""),
                   ("Gold"             ,"Gold"             ,""),
                   ("Iridium"          ,"Iridium"          ,""),
                   ("Iron"             ,"Iron"             ,""),
                   ("Lead"             ,"Lead"             ,""),
                   ("Lithium"          ,"Lithium"          ,""),
                   ("Mercury"          ,"Mercury"          ,""),           
                   ("Molybdenum"       ,"Molybdenum"       ,""),
                   ("Nickel"           ,"Nickel"           ,""),
                   ("Palladium"        ,"Palladium"        ,""),
                   ("Platinum"         ,"Platinum"         ,""),
                   ("Silver"           ,"Silver"           ,""),
                   ("Titanium"         ,"Titanium"         ,""),
                   ("Zinc"             ,"Zinc"             ,""),
                   ("Zirconium"        ,"Zirconium"        ,""),                            
                   ],                                
                   name="",
                   default = "Custom",    
                   description="metal shader presets")


    mat_presets_metal : EnumProperty(
            items=[           
                   ('Anodized'    ,'Anodized'    ,''),
                   ('Brushed'     ,'Brushed'     ,''),
                   ('Cartridge'   ,'Cartridge'   ,''),
                   ('Corrosion'   ,'Corrosion'   ,''),
                   ('Cracked'     ,'Cracked'     ,''),
                   ('Dented'      ,'Dented'      ,''),
                   ('Directional' ,'Directional' ,''),
                   ('Dusty'       ,'Dusty'       ,''),
                   ('Foil'        ,'Foil'        ,''),
                   ('Galvanized'  ,'Galvanized'  ,''),
                   ('Hammered'    ,'Hammered'    ,''),
                   ('Matte'       ,'Matte'       ,''),
                   ('Old'         ,'Old'         ,''),
                   ('Oxidized'    ,'Oxidized'    ,''),
                   ('Painted'     ,'Painted'     ,''),
                   ('Patinated'   ,'Patinated'   ,''),
                   ('Polished'    ,'Polished'    ,''),
                   ('Rough'       ,'Rough'       ,''),
                   ('Rusted'      ,'Rusted'      ,''),
                   ('Rugged'      ,'Rugged'      ,''),
                   ('Sandblasted' ,'Sandblasted' ,''),
                   ('Scratched'   ,'Scratched'   ,''),
                   ('Smooth'      ,'Smooth'      ,''),
                   ('Smudged'     ,'Smudged'     ,''),
                   ('Standard'    ,'Standard'    ,''),
                   ('Worn'        ,'Worn'        ,''),
                   ('Wrought'     ,'Wrought'     ,''),                                                        
                   ],                                
                   name="",
                   default = "Standard",    
                   description="metal shader type")


    mat_ior_values : EnumProperty(
    items = [
                    ("ior000", "Custom",                      " custom value "),               
                    ("ior001", "Acetone",                     " 1.360 "),
                    ("ior002", "Acrylic glass",               " 1.490 - 1.492 "),
                    ("ior003", "Actinolite",                  " 1.618 "),
                    ("ior004", "Agalmatoite",                 " 1.550 "),
                    ("ior005", "Agate",                       " 1.544 - 1.55 "),
                    ("ior006", "Agate, Moss",                 " 1.540 "),
                    ("ior007", "Air",                         " 1.000 "),
                    ("ior008", "Alcohol",                     " 1.329 "),
                    ("ior009", "Alcohol, Ethyl (grain)",      " 1.360 "),
                    ("ior010", "Alcohol, Methyl (wood)",      " 1.329 "),
                    ("ior011", "Alexandrite",                 " 1.746 - 1.755 "),
                    ("ior012", "Almandine",                   " 1.244 "),
                    ("ior013", "Aluminum",                    " 1.244 "),
                    ("ior014", "Aluminum Chloride",           " 2.700 "),
                    ("ior015", "Aluminum Oxide",              " 1.665 "),
                    ("ior016", "Amber",                       " 1.539 - 1.546 "),
                    ("ior017", "Amblygonite",                 " 1.611 "),
                    ("ior018", "Amethyst",                    " 1.532 - 1.554 "),
                    ("ior019", "Ammolite",                    " 1.520 - 1.680 "),
                    ("ior020", "Amorphous Selenium",          " 2.920 "),
                    ("ior021", "Anatase",                     " 2.490 "),
                    ("ior022", "Andalusite",                  " 1.629 - 1.650 "),
                    ("ior023", "Anhydrite",                   " 1.571 "),
                    ("ior024", "Apatite",                     " 1.420 - 1.632 "),
                    ("ior025", "Apophyllite",                 " 1.536 "),
                    ("ior026", "Aquamarine",                  " 1.567 "),
                    ("ior027", "Aragonite",                   " 1.530 "),
                    ("ior028", "Argon",                       " 1.000 "),
                    ("ior029", "Argonite",                    " 1.530 "),
                    ("ior030", "Asphalt",                     " 1.635 "),
                    ("ior031", "Augelite",                    " 1.574 "),
                    ("ior032", "Axenite",                     " 1.674 - 1.704 "),
                    ("ior033", "Axinite",                     " 1.675 "),
                    ("ior034", "Azurite",                     " 1.730 "), 
                    ("ior035", "Barite",                      " 1.636 "),
                    ("ior036", "Barytocalcite",               " 1.684 "),
                    ("ior037", "Beer",                        " 1.345 "),
                    ("ior038", "Benitoite",                   " 1.757 "),
                    ("ior039", "Benzene",                     " 1.501 "),
                    ("ior040", "Beryl",                       " 1.570 - 1.600 "),
                    ("ior041", "Beryl, Red",                  " 1.570 - 1.598 "),
                    ("ior042", "Beryllonite",                 " 1.553 "),
                    ("ior043", "Borax",                       " 1.446 "),
                    ("ior044", "Brazilianite",                " 1.603 "),
                    ("ior045", "Bromine (liquid)",            " 1.661 "),
                    ("ior046", "Bronze",                      " 1.180 "),
                    ("ior047", "Brownite",                    " 1.567 "), 
                    ("ior048", "Calcite",                     " 1.486 "),
                    ("ior049", "Calspar",                     " 1.486 1.660 "),
                    ("ior050", "Cancrinite",                  " 1.491 "),
                    ("ior051", "Carbon Dioxide",              " 1.000 "),
                    ("ior052", "Carbon Disulfide",            " 1.628 "),
                    ("ior053", "Carbon Tetrachloride",        " 1.460 "),
                    ("ior054", "Carbonated Beverages",        " 1.340 "),
                    ("ior055", "Cassiterite",                 " 1.997 "),
                    ("ior056", "Celestite",                   " 1.622 "),
                    ("ior057", "Cerussite",                   " 1.804 "),
                    ("ior058", "Ceylanite",                   " 1.770 "),
                    ("ior059", "Chalcedony",                  " 1.544 - 1.553 "),
                    ("ior060", "Chalk",                       " 1.510 "),
                    ("ior061", "Chalybite",                   " 1.630 "),
                    ("ior062", "Chlorine (gas)",              " 1.001 "),
                    ("ior063", "Chlorine (liquid)",           " 1.385 "),
                    ("ior064", "Chrome Green",                " 2.400 "),
                    ("ior065", "Chrome Red",                  " 2.420 "),
                    ("ior066", "Chrome Tourmaline",           " 1.610 - 1.640 "),
                    ("ior067", "Chrome Yellow",               " 2.310 "),
                    ("ior068", "Chromium",                    " 2.970 "),
                    ("ior069", "Chromium Oxide",              " 2.705 "),
                    ("ior070", "Chrysoberyl",                 " 1.745 "),
                    ("ior071", "Chrysocolla",                 " 1.500 "),
                    ("ior072", "Chrysoprase",                 " 1.534 "),
                    ("ior073", "Cinnabar Mecury Sulfide",     " 3.020 "),
                    ("ior074", "Citrine",                     " 1.532 "),
                    ("ior075", "Cleaner all purpose",         " 1.293 "),
                    ("ior076", "Clinohumite",                 " 1.625 "),
                    ("ior077", "Clinozoisite",                " 1.724 "),
                    ("ior078", "Cobalt Blue",                 " 1.740 "),
                    ("ior079", "Cobalt Green",                " 1.970 "),
                    ("ior080", "Cobalt Violet",               " 1.710 "),
                    ("ior081", "Colemanite",                  " 1.586 "),
                    ("ior082", "Copper",                      " 1.100 - 2.430 "),
                    ("ior083", "Copper Oxide",                " 2.705 "),
                    ("ior084", "Coral",                       " 1.486 "),
                    ("ior085", "Cordierite",                  " 1.540 "),
                    ("ior086", "Corundum",                    " 1.766 "),
                    ("ior087", "Cranberry Juice 25%",         " 1.351 "),
                    ("ior088", "Crocoite",                    " 2.310 "),
                    ("ior089", "Cromite",                     " 2.160 "),
                    ("ior090", "Crown Glass impure",          " 1.485 - 1.755 "),
                    ("ior091", "Crown Glass pure",            " 1.500 - 1.540 "),
                    ("ior092", "Cryolite",                    " 1.338 "),
                    ("ior093", "Crysoberyl, Catseye",         " 1.746 - 1.755 "),
                    ("ior094", "Crystal",                     " 2.000 "),
                    ("ior095", "Cubic Zirconia",              " 2.150 - 2.180 "),
                    ("ior096", "Cuprite",                     " 2.850 "), 
                    ("ior097", "Danburite",                   " 1.627 - 1.641 "),
                    ("ior098", "Diamond",                     " 2.418 "),
                    ("ior099", "Diopside",                    " 1.680 "),
                    ("ior100", "Dolomite",                    " 1.503 "),
                    ("ior101", "Dumortierite",                " 1.686 "), 
                    ("ior102", "Ebonite",                     " 1.660 "),
                    ("ior103", "Ekanite",                     " 1.600 "),
                    ("ior104", "Elaeolite",                   " 1.532 "),
                    ("ior105", "Emerald",                     " 1.560 - 1.605 "),
                    ("ior106", "Emerald Catseye",             " 1.560 - 1.605 "),
                    ("ior107", "Emerald, Synth Flux",         " 1.561 "),
                    ("ior108", "Emerald, Synth Hydro",        " 1.568 "),
                    ("ior109", "Enstatite",                   " 1.663 "),
                    ("ior110", "Epidote",                     " 1.733 "),
                    ("ior111", "Ethanol",                     " 1.360 "),
                    ("ior112", "Ethyl Alcohol",               " 1.360 "),
                    ("ior113", "Euclase",                     " 1.652 "),
                    ("ior114", "Eye, Aqueous Humor",          " 1.330 "),
                    ("ior115", "Eye, Cornea",                 " 1.380 "),
                    ("ior116", "Eye, Lens",                   " 1.410 "),
                    ("ior117", "Eye, Vitreous Humor",         " 1.340 "),
                    ("ior118", "Fabulite",                    " 2.409 "),
                    ("ior119", "Feldspar, Adventurine",       " 1.532 "),
                    ("ior120", "Feldspar, Albite",            " 1.525 "),
                    ("ior121", "Feldspar, Amazonite",         " 1.525 "),
                    ("ior122", "Feldspar, Labrodorite",       " 1.565 "),
                    ("ior123", "Feldspar, Microcline",        " 1.525 "),
                    ("ior124", "Feldspar, Oligoclase",        " 1.539 "),
                    ("ior125", "Feldspar, Orthoclase",        " 1.525 "),
                    ("ior126", "Flint Glass impure",          " 1.523 - 1.925 "),
                    ("ior127", "Flint Glass pure",            " 1.600 - 1.620 "),
                    ("ior128", "Flourite",                    " 1.433 "),
                    ("ior129", "Fluoride",                    " 1.560 "),
                    ("ior130", "Fluorite",                    " 1.434 "),
                    ("ior131", "Formica",                     " 1.470 "),
                    ("ior132", "Fused Quartz",                " 1.460 "), 
                    ("ior133", "GalliumIII Arsenide",         " 3.927 "),
                    ("ior134", "GalliumIII Phosphide",        " 3.500 "),
                    ("ior135", "Garnet, Almandine",           " 1.760 "),
                    ("ior136", "Garnet, Almandite",           " 1.790 "),
                    ("ior137", "Garnet, Andradite",           " 1.820 "),
                    ("ior138", "Garnet, Demantiod",           " 1.880 - 1.900 "),
                    ("ior139", "Garnet, Grossular",           " 1.720 - 1.800 "),
                    ("ior140", "Garnet, Hessonite",           " 1.745 "),
                    ("ior141", "Garnet, Mandarin",            " 1.790 - 1.800 "),
                    ("ior142", "Garnet, Pyrope",              " 1.730 - 1.760 "),
                    ("ior143", "Garnet, Rhodolite",           " 1.740 - 1.770 "),
                    ("ior144", "Garnet, Spessartite",         " 1.810 "),
                    ("ior145", "Garnet, Tsavorite",           " 1.739 - 1.744 "),
                    ("ior146", "Garnet, Uvarovite",           " 1.740 - 1.870 "),
                    ("ior147", "Gaylussite",                  " 1.517 "),
                    ("ior148", "Glass",                       " 1.500 "),
                    ("ior149", "Glass, Albite",               " 1.489 "),
                    ("ior150", "Glass, Arsenic Trisulfide",   " 2.040 "),
                    ("ior151", "Glass, Crown",                " 1.520 "),
                    ("ior152", "Glass, Crown, Zinc",          " 1.517 "),
                    ("ior153", "Glass, Flint, 29%",           " 1.569 "),
                    ("ior154", "Glass, Flint, 55%",           " 1.669 "),
                    ("ior155", "Glass, Flint, 71% ",          " 1.805 "),
                    ("ior156", "Glass, Flint, Dense",         " 1.660 "),
                    ("ior157", "Glass, Flint, Heaviest",      " 1.890 "),
                    ("ior158", "Glass, Flint, Heavy",         " 1.655 "),
                    ("ior159", "Glass, Flint, Lanthanum",     " 1.800 "),
                    ("ior160", "Glass, Flint, Light",         " 1.580 "),
                    ("ior161", "Glass, Flint, Medium",        " 1.627 "),
                    ("ior162", "Glass, Fused Silica",         " 1.459 "),
                    ("ior163", "Glass, Pyrex",                " 1.474 "),
                    ("ior164", "Glycerine",                   " 1.473 "),
                    ("ior165", "Glycerol",                    " 1.473 "),
                    ("ior166", "Gold",                        " 0.470 "),
                    ("ior167", "Gypsium",                     " 1.519 "),
                    ("ior168", "Hambergite",                  " 1.559 "),
                    ("ior169", "Hauyn",                       " 1.490 - 1.505 "),
                    ("ior170", "Hauynite",                    " 1.502 "),
                    ("ior171", "Heaviest Flint Glass",        " 1.890 "),
                    ("ior172", "Heavy Flint Glass",           " 1.650 "),
                    ("ior173", "Helium",                      " 1.000 "),
                    ("ior174", "Hematite",                    " 2.940 "),
                    ("ior175", "Hemimorphite",                " 1.614 "),
                    ("ior176", "Hiddenite",                   " 1.655 "),
                    ("ior177", "Honey, 13% water content",    " 1.504 "),
                    ("ior178", "Honey, 17% water content",    " 1.494 "),
                    ("ior179", "Honey, 21% water content",    " 1.484 "),
                    ("ior180", "Howlite",                     " 1.586 "),
                    ("ior181", "Hydrogen gas",                " 1.000 "),
                    ("ior182", "Hydrogen liquid",             " 1.097 "),
                    ("ior183", "Hypersthene",                 " 1.670 "),  
                    ("ior184", "Ice",                         " 1.309 "),
                    ("ior185", "Idocrase",                    " 1.713 "),
                    ("ior186", "Iodine Crystal",              " 3.340 "),
                    ("ior187", "Iolite",                      " 1.522 - 1.578 "),
                    ("ior188", "Iron",                        " 2.950 "),
                    ("ior189", "Ivory",                       " 1.540 "), 
                    ("ior190", "Jade, Jadeite",               " 1.640 - 1.667 "),
                    ("ior191", "Jade, Nephrite",              " 1.600 - 1.641 "),
                    ("ior192", "Jadeite",                     " 1.665 "),
                    ("ior193", "Jasper",                      " 1.540 "),
                    ("ior194", "Jet",                         " 1.660 "),  
                    ("ior195", "Kornerupine",                 " 1.665 "),
                    ("ior196", "Kunzite",                     " 1.660 - 1.676 "),
                    ("ior197", "Kyanite",                     " 1.715 "), 
                    ("ior198", "Labradorite",                 " 1.560 - 1.572 "),
                    ("ior199", "Lapis Gem",                   " 1.500 "),
                    ("ior200", "Lapis Lazuli",                " 1.500 - 1.550 "),
                    ("ior201", "Lazulite",                    " 1.615 "),
                    ("ior202", "Lead",                        " 2.010 "),
                    ("ior203", "Lead Nitrate",                " 1.782 "),
                    ("ior204", "Leucite",                     " 1.509 "),
                    ("ior205", "Light Flint Glass",           " 1.575 "),
                    ("ior206", "Liquid Carbon Dioxide",       " 1.200 "),
                    ("ior207", "Liquid Water 20°C",           " 1.333 "),
                    ("ior208", "Lucite",                      " 1.495 "), 
                    ("ior209", "Magnesite",                   " 1.515 "),
                    ("ior210", "Malachite",                   " 1.655 "),
                    ("ior211", "Meerschaum",                  " 1.530 "),
                    ("ior212", "Mercury liquid",              " 1.620 "),
                    ("ior213", "Methanol",                    " 1.329 "),
                    ("ior214", "Milk",                        " 1.350 "),
                    ("ior215", "Moissanite",                  " 2.650 - 2.690 "),
                    ("ior216", "Moldavite",                   " 1.500 "),
                    ("ior217", "Moonstone",                   " 1.518 - 1.526 "),
                    ("ior218", "Moonstone, Adularia",         " 1.525 "),
                    ("ior219", "Moonstone, Albite",           " 1.535 "),
                    ("ior220", "Morganite",                   " 1.585 - 1.594 "),
                    ("ior221", "Mylar",                       " 1.650 "), 
                    ("ior222", "Natrolite",                   " 1.480 "),
                    ("ior223", "Nephrite",                    " 1.600 "),
                    ("ior224", "Nickel",                      " 1.080 "),
                    ("ior225", "Nitrogen gas",                " 1.000 "),
                    ("ior226", "Nitrogen liquid",             " 1.205 "),
                    ("ior227", "Nylon",                       " 1.530 "),
                    ("ior228", "Obsidian",                    " 1.486 - 1.500 "),
                    ("ior229", "Oil of Wintergreen",          " 1.536 "),
                    ("ior230", "Oil, Clove",                  " 1.535 "),
                    ("ior231", "Oil, Lemon",                  " 1.481 "),
                    ("ior232", "Oil, Neroli",                 " 1.482 "),
                    ("ior233", "Oil, Orange",                 " 1.473 "),
                    ("ior234", "Oil, Safflower",              " 1.466 "),
                    ("ior235", "Oil, vegetable 50°C",         " 1.470 "),
                    ("ior236", "Olivine",                     " 1.670 "),
                    ("ior237", "Onyx",                        " 1.486 "),
                    ("ior238", "Onyx Marble",                 " 1.486 "),
                    ("ior239", "Opal",                        " 1.450 "),
                    ("ior240", "Opal, Black",                 " 1.440 - 1.460 "),
                    ("ior241", "Opal, Fire",                  " 1.430 - 1.460 "),
                    ("ior242", "Opal, White",                 " 1.440 - 1.460 "),
                    ("ior243", "Oregon Sunstone",             " 1.560 - 1.572 "),
                    ("ior244", "Oxygen gas",                  " 1.000 "),
                    ("ior245", "Oxygen liquid",               " 1.221 "),  
                    ("ior246", "Padparadja",                  " 1.760 - 1.773 "),
                    ("ior247", "Painite",                     " 1.787 "),
                    ("ior248", "Pearl",                       " 1.530 - 1.690 "),
                    ("ior249", "Periclase",                   " 1.740 "),
                    ("ior250", "Peristerite",                 " 1.525 "),
                    ("ior251", "PET",                         " 1.575 "),
                    ("ior252", "Petalite",                    " 1.502 "),
                    ("ior253", "PETg",                        " 1.570 "),
                    ("ior254", "Phenakite",                   " 1.650 "),
                    ("ior255", "Phosgenite",                  " 2.117 "),
                    ("ior256", "Plastic",                     " 1.460 "),
                    ("ior257", "Platinum",                    " 2.330 "),
                    ("ior258", "Plexiglas",                   " 1.500 "),
                    ("ior259", "PMMA",                        " 1.489 - 1.490 "),
                    ("ior260", "Polycarbonate",               " 1.584 "),
                    ("ior261", "Polystyrene",                 " 1.550 "),
                    ("ior262", "Prase",                       " 1.540 "),
                    ("ior263", "Prasiolite",                  " 1.540 "),
                    ("ior264", "Prehnite",                    " 1.610 "),
                    ("ior265", "Proustite",                   " 2.790 "),
                    ("ior266", "Purpurite",                   " 1.840 "),
                    ("ior267", "Pyrite",                      " 1.810 "),
                    ("ior268", "Pyrope",                      " 1.740 "),
                    ("ior269", "Quartz",                      " 1.544 - 1.644 "),
                    ("ior270", "Quartz, Fused",               " 1.458 "),  
                    ("ior271", "Rhodizite",                   " 1.690 "),
                    ("ior272", "Rhodochrisite",               " 1.600 "),
                    ("ior273", "Rhodonite",                   " 1.735 "),
                    ("ior274", "Rock salt",                   " 1.516 - 1.544 "),
                    ("ior275", "Rubber, Natural",             " 1.519 "),
                    ("ior276", "Ruby",                        " 1.757 - 1.779 "),
                    ("ior277", "Rum, White",                  " 1.361 "),
                    ("ior278", "Rutile",                      " 2.620 "), 
                    ("ior279", "Salt NaCl",                   " 1.544 "),
                    ("ior280", "Sanidine",                    " 1.522 "),
                    ("ior291", "Sapphire",                    " 1.757 - 1.779 "),
                    ("ior292", "Sapphire, Star",              " 1.760 - 1.773 "),
                    ("ior293", "Scapolite",                   " 1.540 "),
                    ("ior294", "Scapolite, Yellow",           " 1.555 "),
                    ("ior295", "Scheelite",                   " 1.920 "),
                    ("ior296", "Selenium, Amorphous",         " 2.920 "),
                    ("ior297", "Serpentine",                  " 1.560 "),
                    ("ior298", "Shampoo",                     " 1.362 "),
                    ("ior299", "Shell",                       " 1.530 "),
                    ("ior290", "Shower gel",                  " 1.510 "),
                    ("ior291", "Silicon",                     " 4.010 - 4.240 "),
                    ("ior292", "Sillimanite",                 " 1.658 "),
                    ("ior293", "Silver",                      " 0.180 - 1.350 "),
                    ("ior294", "Sinhalite",                   " 1.699 "),
                    ("ior295", "Smaragdite",                  " 1.608 "),
                    ("ior296", "Smithsonite",                 " 1.621 "),
                    ("ior297", "Sodalite",                    " 1.483 "),
                    ("ior298", "Sodium Chloride",             " 1.544 - 1.644 "),
                    ("ior299", "Spessarite",                  " 1.790 - 1.810 "),
                    ("ior300", "Sphalerite",                  " 2.368 "),
                    ("ior301", "Sphene",                      " 1.885 "),
                    ("ior302", "Spinel",                      " 1.712 - 1.717 "),
                    ("ior303", "Spinel, Blue",                " 1.712 1.747 "),
                    ("ior304", "Spinel, Red",                 " 1.708 - 1.735 "),
                    ("ior305", "Spodumene",                   " 1.650 "),
                    ("ior306", "Star Ruby",                   " 1.760 - 1.773 "),
                    ("ior307", "Staurolite",                  " 1.739 "),
                    ("ior308", "Steatite",                    " 1.539 "),
                    ("ior309", "Steel",                       " 2.500 "),
                    ("ior310", "Stichtite",                   " 1.520 "),
                    ("ior311", "Strontium Titanate",          " 2.410 "),
                    ("ior312", "Styrofoam",                   " 1.595 "),
                    ("ior313", "Styrene",                     " 1.519 "),
                    ("ior314", "Sugar Solution 30%",          " 1.380 "),
                    ("ior315", "Sugar Solution 80%",          " 1.490 "),
                    ("ior316", "Sulphur",                     " 1.960 "),
                    ("ior317", "Synthetic Spinel",            " 1.730 "), 
                    ("ior318", "Taaffeite",                   " 1.720 "),
                    ("ior319", "Tantalite",                   " 2.240 "),
                    ("ior320", "Tanzanite",                   " 1.692 - 1.700 "),
                    ("ior321", "Teflon",                      " 1.350 - 1.380 "),
                    ("ior322", "Thomsonite",                  " 1.530 "),
                    ("ior323", "Tiger eye",                   " 1.544 "),
                    ("ior324", "Tin Iodide",                  " 2.106 "),
                    ("ior325", "Titanium",                    " 2.160 "),
                    ("ior326", "Topaz",                       " 1.607 - 1.627 "),
                    ("ior327", "Topaz, Blue",                 " 1.610 "),
                    ("ior328", "Topaz, Imperial",             " 1.605 - 1.640 "),
                    ("ior329", "Topaz, Pink",                 " 1.620 "),
                    ("ior330", "Topaz, White",                " 1.630 "),
                    ("ior331", "Topaz, Yellow",               " 1.620 "),
                    ("ior332", "Tourmaline",                  " 1.603 - 1.655 "),
                    ("ior333", "Tourmaline, Blue",            " 1.610 - 1.640 "),
                    ("ior334", "Tourmaline, Catseye",         " 1.610 - 1.640 "),
                    ("ior335", "Tourmaline, Green",           " 1.610 - 1.640 "),
                    ("ior336", "Tourmaline, Paraiba",         " 1.610 - 1.650 "),
                    ("ior337", "Tourmaline, Red",             " 1.610 - 1.640 "),
                    ("ior338", "Tremolite",                   " 1.600 "),
                    ("ior339", "Tugtupite",                   " 1.496 "),
                    ("ior340", "Turpentine",                  " 1.472 "),
                    ("ior341", "Turquoise",                   " 1.610 - 1.650 "), 
                    ("ior342", "Ulexite",                     " 1.490 "),
                    ("ior343", "Uvarovite",                   " 1.870 "),
                    ("ior344", "Vacuum",                      " 1.000 "),
                    ("ior345", "Variscite",                   " 1.550 "),
                    ("ior346", "Vivianite",                   " 1.580 "),
                    ("ior347", "Vodka",                       " 1.363 "),
                    ("ior348", "Wardite",                     " 1.590 "),
                    ("ior349", "Water 0°C",                   " 1.333 "),
                    ("ior350", "Water 100°C",                 " 1.318 "),
                    ("ior351", "Water 20°C",                  " 1.333 "),
                    ("ior352", "Water gas",                   " 1.000 "),
                    ("ior353", "Water 35°C",                  " 1.325 "),
                    ("ior354", "Water Ice",                   " 1.310 "),
                    ("ior355", "Whisky",                      " 1.356 "),
                    ("ior356", "Wulfenite",                   " 2.300 "),   
                    ("ior357", "Zinc Crown Glass",            " 1.517 "),
                    ("ior358", "Zincite",                     " 2.010 "),
                    ("ior359", "Zircon",                      " 1.777 - 1.987 "),
                    ("ior360", "Zircon, High",                " 1.960 "),
                    ("ior361", "Zircon, Low",                 " 1.800 "),
                    ("ior362", "Zirconia, Cubic",             " 2.173 - 2.210 ")], 
                    name="",
                    default = "ior000",
                    description="index of refraction values")





    circle_type : EnumProperty(
            items=[ ('Custom',  'Custom',   ''),

                    # CONTRAST
                    ('gray_00', '0x000000', ''), 
                    ('gray_20', '0x333333', ''), 
                    ('gray_40', '0x666666', ''), 
                    ('gray_50', '0x7F7F7F', ''), 
                    ('gray_60', '0x999999', ''), 
                    ('gray_80', '0xCCCCCC', ''), 
                    ('gray_10', '0xFFFFFF', ''), 

                    # RED COLORS #
                    ('0x601600', '0x601600', ''),
                    ('0x861900', '0x861900', ''),
                    ('0xb41b00', '0xb41b00', ''),
                    ('0xd21c00', '0xd21c00', ''),
                    ('0xef1f00', '0xef1f00', ''),
                    ('0xee3d1a', '0xee3d1a', ''),
                    ('0xf05d42', '0xf05d42', ''),
                    ('0xf1826a', '0xf1826a', ''),
                    ('0xf4aa97', '0xf4aa97', ''),
                    ('0xf8d4c2', '0xf8d4c2', ''),
                    ('0x600000', '0x600000', ''),
                    ('0x870000', '0x870000', ''),
                    ('0xb20000', '0xb20000', ''),
                    ('0xcf0000', '0xcf0000', ''),
                    ('0xec0000', '0xec0000', ''),
                    ('0xee1a1f', '0xee1a1f', ''),
                    ('0xef3e44', '0xef3e44', ''),
                    ('0xf0686f', '0xf0686f', ''),
                    ('0xef9394', '0xef9394', ''),
                    ('0xf7c8cb', '0xf7c8cb', ''),
                    ('0x550020', '0x550020', ''),
                    ('0x750027', '0x750027', ''),
                    ('0x9a002e', '0x9a002e', ''),
                    ('0xb30033', '0xb30033', ''),
                    ('0xce003b', '0xce003b', ''),
                    ('0xd51252', '0xd51252', ''),
                    ('0xdc3670', '0xdc3670', ''),
                    ('0xe05d8e', '0xe05d8e', ''),
                    ('0xde91af', '0xde91af', ''),
                    ('0xefc2d3', '0xefc2d3', ''),
                    ('0x490031', '0x490031', ''),
                    ('0x640040', '0x640040', ''),
                    ('0x83004f', '0x83004f', ''),
                    ('0x970056', '0x970056', ''),
                    ('0xac0069', '0xac0069', ''),
                    ('0xb51380', '0xb51380', ''),
                    ('0xc02e93', '0xc02e93', ''),
                    ('0xcf57ac', '0xcf57ac', ''),
                    ('0xdb85c6', '0xdb85c6', ''),
                    ('0xecbbdc', '0xecbbdc', ''),
                    ('0x410048', '0x410048', ''),
                    ('0x580061', '0x580061', ''),
                    ('0x70007f', '0x70007f', ''),
                    ('0x830093', '0x830093', ''),
                    ('0x9500a7', '0x9500a7', ''),
                    ('0xa600ae', '0xa600ae', ''),
                    ('0xb42cc2', '0xb42cc2', ''),
                    ('0xc450d1', '0xc450d1', ''),
                    ('0xd481e4', '0xd481e4', ''),
                    ('0xecb5f8', '0xecb5f8', ''),
                    ('0x250041', '0x250041', ''),
                    ('0x300056', '0x300056', ''),
                    ('0x3d0070', '0x3d0070', ''),
                    ('0x430082', '0x430082', ''),
                    ('0x490090', '0x490090', ''),
                    ('0x5d00a6', '0x5d00a6', ''),
                    ('0x752baf', '0x752baf', ''),
                    ('0x8c52c6', '0x8c52c6', ''),
                    ('0xad7dd7', '0xad7dd7', ''),
                    ('0xd4b5f0', '0xd4b5f0', ''),

                    # BLUE COLORS #     
                    ('0x160042', '0x160042', ''),
                    ('0x1b005a', '0x1b005a', ''),
                    ('0x1e0075', '0x1e0075', ''),
                    ('0x200084', '0x200084', ''),
                    ('0x220098', '0x220098', ''),
                    ('0x3300a4', '0x3300a4', ''),
                    ('0x4c2bbb', '0x4c2bbb', ''),
                    ('0x6d51ca', '0x6d51ca', ''),
                    ('0x957fd9', '0x957fd9', ''),
                    ('0xc7b9f1', '0xc7b9f1', ''),
                    ('0x060642', '0x060642', ''),
                    ('0x0B0058', '0x0B0058', ''),
                    ('0x0B0072', '0x0B0072', ''),
                    ('0x0b0088', '0x0b0088', ''),
                    ('0x0c009a', '0x0c009a', ''),
                    ('0x1d1dad', '0x1d1dad', ''),
                    ('0x373bbb', '0x373bbb', ''),
                    ('0x5b5ccd', '0x5b5ccd', ''),
                    ('0x8286df', '0x8286df', ''),
                    ('0xb9c0f0', '0xb9c0f0', ''),
                    ('0x0d1944', '0x0d1944', ''),
                    ('0x111d60', '0x111d60', ''),
                    ('0x11227a', '0x11227a', ''),
                    ('0x14268d', '0x14268d', ''),
                    ('0x1729a6', '0x1729a6', ''),
                    ('0x233dae', '0x233dae', ''),
                    ('0x3c57bd', '0x3c57bd', ''),
                    ('0x5b76cb', '0x5b76cb', ''),
                    ('0x899dda', '0x899dda', ''),
                    ('0xb5cbf4', '0xb5cbf4', ''),
                    ('0x112649', '0x112649', ''),
                    ('0x153063', '0x153063', ''),
                    ('0x193b80', '0x193b80', ''),
                    ('0x1c438f', '0x1c438f', ''),
                    ('0x1d4ba4', '0x1d4ba4', ''),
                    ('0x2b5faf', '0x2b5faf', ''),
                    ('0x4176c2', '0x4176c2', ''),
                    ('0x5e91d9', '0x5e91d9', ''),
                    ('0x8bb3e3', '0x8bb3e3', ''),
                    ('0xc1d3ef', '0xc1d3ef', ''),
                    ('0x162f4a', '0x162f4a', ''),
                    ('0x193e66', '0x193e66', ''),
                    ('0x204f86', '0x204f86', ''),
                    ('0x205c96', '0x205c96', ''),
                    ('0x226aac', '0x226aac', ''),
                    ('0x327bbd', '0x327bbd', ''),
                    ('0x4690c8', '0x4690c8', ''),
                    ('0x65aad1', '0x65aad1', ''),
                    ('0x90c0e2', '0x90c0e2', ''),
                    ('0xc2def5', '0xc2def5', ''),
                    ('0x193d4e', '0x193d4e', ''),
                    ('0x21546c', '0x21546c', ''),
                    ('0x266c8b', '0x266c8b', ''),
                    ('0x2a7da4', '0x2a7da4', ''),
                    ('0x2e8bb7', '0x2e8bb7', ''),
                    ('0x3b9fc4', '0x3b9fc4', ''),
                    ('0x4dadce', '0x4dadce', ''),
                    ('0x6bc0de', '0x6bc0de', ''),
                    ('0x93d0e7', '0x93d0e7', ''),
                    ('0xc2edf0', '0xc2edf0', ''),

                    # GREEN COLORS #
                    ('0x1c4927', '0x1c4927', ''),
                    ('0x246533', '0x246533', ''),
                    ('0x2c8240', '0x2c8240', ''),
                    ('0x319845', '0x319845', ''),
                    ('0x36aa4e', '0x36aa4e', ''),
                    ('0x3fbb61', '0x3fbb61', ''),
                    ('0x53c47e', '0x53c47e', ''),
                    ('0x6dd598', '0x6dd598', ''),
                    ('0x93e2b5', '0x93e2b5', ''),
                    ('0xc2efd8', '0xc2efd8', ''),
                    ('0x1c4500', '0x1c4500', ''),
                    ('0x225d00', '0x225d00', ''),
                    ('0x2a7900', '0x2a7900', ''),
                    ('0x308e00', '0x308e00', ''),
                    ('0x359f00', '0x359f00', ''),
                    ('0x40ae00', '0x40ae00', ''),
                    ('0x54bf2a', '0x54bf2a', ''),
                    ('0x6ed252', '0x6ed252', ''),
                    ('0x98da8a', '0x98da8a', ''),
                    ('0xc0efbb', '0xc0efbb', ''),
                    ('0x264a00', '0x264a00', ''),
                    ('0x336600', '0x336600', ''),
                    ('0x3e8400', '0x3e8400', ''),
                    ('0x479800', '0x479800', ''),
                    ('0x4eaf00', '0x4eaf00', ''),
                    ('0x5fbd00', '0x5fbd00', ''),
                    ('0x78c62a', '0x78c62a', ''),
                    ('0x95d45c', '0x95d45c', ''),
                    ('0xb4e27e', '0xb4e27e', ''),
                    ('0xd4efc0', '0xd4efc0', ''),
                    ('0x3a5000', '0x3a5000', ''),
                    ('0x4e6f00', '0x4e6f00', ''),
                    ('0x629100', '0x629100', ''),
                    ('0x71a600', '0x71a600', ''),
                    ('0x80bf00', '0x80bf00', ''),
                    ('0x91cd00', '0x91cd00', ''),
                    ('0xa4d32d', '0xa4d32d', ''),
                    ('0xb5da56', '0xb5da56', ''),
                    ('0xcdee82', '0xcdee82', ''),
                    ('0xe2f7b3', '0xe2f7b3', ''),
                    ('0x5e6b00', '0x5e6b00', ''),
                    ('0x788600', '0x788600', ''),
                    ('0x9eb000', '0x9eb000', ''),
                    ('0xbdd400', '0xbdd400', ''),
                    ('0xd1ed00', '0xd1ed00', ''),
                    ('0xe1f400', '0xe1f400', ''),
                    ('0xdef22d', '0xdef22d', ''),
                    ('0xe5f65a', '0xe5f65a', ''),
                    ('0xeef98b', '0xeef98b', ''),
                    ('0xf6fdc6', '0xf6fdc6', ''),
                    ('0x676800', '0x676800', ''),
                    ('0x939300', '0x939300', ''),
                    ('0xc0c200', '0xc0c200', ''),
                    ('0xeaee00', '0xeaee00', ''),
                    ('0xffff00', '0xffff00', ''),
                    ('0xfffe00', '0xfffe00', ''),
                    ('0xfefe30', '0xfefe30', ''),
                    ('0xfefe5a', '0xfefe5a', ''),
                    ('0xfffe8d', '0xfffe8d', ''),
                    ('0xfefdc9', '0xfefdc9', ''),

                    # BROWN COLORS #
                    ('0x612700', '0x612700', ''),
                    ('0x883000', '0x883000', ''),
                    ('0xb53c00', '0xb53c00', ''),
                    ('0xd14500', '0xd14500', ''),
                    ('0xf04c00', '0xf04c00', ''),
                    ('0xf16618', '0xf16618', ''),
                    ('0xf0803c', '0xf0803c', ''),
                    ('0xf29c6f', '0xf29c6f', ''),
                    ('0xf6bd94', '0xf6bd94', ''),
                    ('0xfee3d0', '0xfee3d0', ''),
                    ('0x602f00', '0x602f00', ''),
                    ('0x873e00', '0x873e00', ''),
                    ('0xb24f00', '0xb24f00', ''),
                    ('0xd45800', '0xd45800', ''),
                    ('0xf06300', '0xf06300', ''),
                    ('0xf47a19', '0xf47a19', ''),
                    ('0xf6943a', '0xf6943a', ''),
                    ('0xf1ad65', '0xf1ad65', ''),
                    ('0xf6c798', '0xf6c798', ''),
                    ('0xfae3c4', '0xfae3c4', ''),
                    ('0x633900', '0x633900', ''),
                    ('0x8c4c00', '0x8c4c00', ''),
                    ('0xb76100', '0xb76100', ''),
                    ('0xcf7000', '0xcf7000', ''),
                    ('0xf17900', '0xf17900', ''),
                    ('0xf48e00', '0xf48e00', ''),
                    ('0xf5a637', '0xf5a637', ''),
                    ('0xf7bb67', '0xf7bb67', ''),
                    ('0xf9d19a', '0xf9d19a', ''),
                    ('0xfde7c9', '0xfde7c9', ''),
                    ('0x614400', '0x614400', ''),
                    ('0x8a5c00', '0x8a5c00', ''),
                    ('0xb57800', '0xb57800', ''),
                    ('0xd68a00', '0xd68a00', ''),
                    ('0xf59a00', '0xf59a00', ''),
                    ('0xf4ad00', '0xf4ad00', ''),
                    ('0xf8bf38', '0xf8bf38', ''),
                    ('0xf9cb63', '0xf9cb63', ''),
                    ('0xf9da9a', '0xf9da9a', ''),
                    ('0xfdebc7', '0xfdebc7', ''),
                    ('0x655100', '0x655100', ''),
                    ('0x8f7000', '0x8f7000', ''),
                    ('0xbd9100', '0xbd9100', ''),
                    ('0xd9a400', '0xd9a400', ''),
                    ('0xf7bd00', '0xf7bd00', ''),
                    ('0xf8ca00', '0xf8ca00', ''),
                    ('0xf9d338', '0xf9d338', ''),
                    ('0xf8de64', '0xf8de64', ''),
                    ('0xfde791', '0xfde791', ''),
                    ('0xfdf4c8', '0xfdf4c8', ''),
                    ('0x685f00', '0x685f00', ''),
                    ('0x938700', '0x938700', ''),
                    ('0xbdb200', '0xbdb200', ''),
                    ('0xf1e200', '0xf1e200', ''),
                    ('0xfcec00', '0xfcec00', ''),
                    ('0xfcf022', '0xfcf022', ''),
                    ('0xfdf133', '0xfdf133', ''),
                    ('0xfef870', '0xfef870', ''),
                    ('0xfef78f', '0xfef78f', ''),
                    ('0xfdfcc2', '0xfdfcc2', ''),
                    ],                               
                    name="",
                    default = "Custom",    
                    description="colorchart")        



    # obj = context.active_object     
    # if obj:
    #     obj_type = obj.type                                                                
    #     if obj_type in GEOM and context.mode in EDIT:

    def draw(self, context):
        layout = self.layout   
        mat_props_draw_ops(self, layout)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):
        settings_write(self) 

        prefs = get_prefs()
        mat_prefs = prefs.mat_type

        view_layer = bpy.context.view_layer
        active = view_layer.objects.active  
        selected = bpy.context.selected_objects                 

        # store mode
        current_mode = bpy.context.active_object.mode 

        obj_list = [obj for obj in selected]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}      

        obj = view_layer.objects.active
        mat_material_creation(self, mat_prefs, obj)

        # restore active
        view_layer.objects.active = active

        # restore mode
        bpy.ops.object.mode_set(mode=current_mode)         

        return {'FINISHED'}


