import bpy
from ..utilities.utils import get_prefs
from .mat_presets_bsdf_ior import mat_presets_bsdf_ior


# Principled BSDF - Material with nodes
def mat_presets_custom_bsdf(self, node): 
                                                                   
    node.distribution = self.mat_distribution
    node.subsurface_method = self.mat_subsurface_method                                          
    
    node.inputs[0].default_value = self.mat_color  
                                          
    node.inputs[1].default_value = self.mat_subsurface
    node.inputs[2].default_value[0] = self.mat_subsurface_rd1
    node.inputs[2].default_value[1] = self.mat_subsurface_rd2
    node.inputs[2].default_value[2] = self.mat_subsurface_rd3
    node.inputs[3].default_value = self.mat_subsurface_color
    node.inputs[4].default_value = self.mat_metallic
    node.inputs[5].default_value = self.mat_specular
    node.inputs[6].default_value = self.mat_specular_tint
    node.inputs[7].default_value = self.mat_roughness
    node.inputs[8].default_value = self.mat_anisotropic
    node.inputs[9].default_value = self.mat_anisotropic_rotation 
    node.inputs[10].default_value = self.mat_sheen
    node.inputs[11].default_value = self.mat_sheen_tint
    node.inputs[12].default_value = self.mat_clearcoat
    node.inputs[13].default_value = self.mat_clearcoat_roughness
    
    #node.inputs[14].default_value = self.mat_ior
    mat_presets_bsdf_ior(self, node)
    
    node.inputs[15].default_value = self.mat_transmission
    if self.mat_distribution == 'GGX':
        node.inputs[16].default_value = self.mat_transmission_roughness
    node.inputs[17].default_value = self.mat_emission_color
    node.inputs[18].default_value = self.mat_alpha   



def mat_presets_default_bsdf(node): 
                                                                   
    node.distribution = 'GGX'
    node.subsurface_method = 'BURLEY'                                           
    node.inputs[0].default_value = (0.8, 0.8, 0.8, 1) #color                                           
    node.inputs[1].default_value = 0.00 #subsurface
    node.inputs[2].default_value[0] = 1.00 #subsurface_rd1
    node.inputs[2].default_value[1] = 0.20 #subsurface_rd2
    node.inputs[2].default_value[2] = 0.10 #subsurface_rd3
    node.inputs[3].default_value = (0.8, 0.8, 0.8, 1) #subsurface_color
    node.inputs[4].default_value = 0.00 #metallic
    node.inputs[5].default_value = 0.50 #specular
    node.inputs[6].default_value = 0.00 #specular_tint
    node.inputs[7].default_value = 0.50 #roughness
    node.inputs[8].default_value = 0.00 #anisotropic
    node.inputs[9].default_value = 0.00 #anisotropic_rotation 
    node.inputs[10].default_value = 0.00 #sheen
    node.inputs[11].default_value = 0.50 #sheen_tint
    node.inputs[12].default_value = 0.00 #clearcoat
    node.inputs[13].default_value = 0.03 #clearcoat_roughness
    node.inputs[14].default_value = 1.45 #ior
    node.inputs[15].default_value = 0.00 #transmission
    node.inputs[17].default_value = (0, 0, 0, 1) #emission_color
    node.inputs[18].default_value = 1.00 #alpha   


