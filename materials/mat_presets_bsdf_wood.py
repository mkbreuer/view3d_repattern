import bpy
from .mat_utils import *

def mat_presets_wood_bsdf(self,node): 

    if "Custom" in self.wood_type: 
        node.inputs[0].default_value = self.mat_color

    if  "Acacia_steamed"  in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x6C4A27)
    if  "Apple_india"     in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xB77747)
    if  "Ash"             in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xEED2AE)
    if  "Bamboo_steamed"  in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xBC8147)
    if  "Bangkirai"       in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x915E25)
    if  "Beech_steamed"   in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xE1AE80)
    if  "Cherry_amer"     in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xAB7C43)
    if  "Cherry_eur"      in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xD1965E)
    if  "Cumaru"          in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x744A32)
    if  "Doussie"         in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x87562E)
    if  "Garapa"          in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xBA8133)
    if  "Ipe"             in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x81562C)
    if  "Iroko_kambala"   in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xBC803A)
    if  "Jacaranda"       in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x8D582C)
    if  "Jatoba"          in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x6F401E)
    if  "Kempas"          in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xAF662F)
    if  "Larch"           in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xE0A873)
    if  "Macassar"        in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x423022)
    if  "Maple_can"       in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xF3D6B4)
    if  "Maple_eur"       in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xECDBBF)
    if  "Massaranduba"    in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x804B2A)
    if  "Merbau"          in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x8B4F24)
    if  "Oak"             in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xD3A46E)
    if  "Oak_darkbrown"   in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x362920)
    if  "Oak_middlebraun" in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x95744B)
    if  "Oak_redbrown"    in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x81582A)
    if  "Oak_smoked_core" in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x694A2E)
    if  "Oak_white"       in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xBD9875)
    if  "Olive"           in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xC3864F)
    if  "Panga_panga"     in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x5C3D31)
    if  "Pear"            in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x965C36)
    if  "Teak"            in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xBA7F38)
    if  "Walnut_amer"     in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x9E7349)
    if  "Walnut_eur"      in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x593B2E)
    if  "Wenge"           in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0x5E3E28)
    if  "Willow"          in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xE0BC94)
    if  "Zebrano"         in self.wood_type: node.inputs[0].default_value = hex_to_rgb_new(0xBE8C59) 
    
                                      
