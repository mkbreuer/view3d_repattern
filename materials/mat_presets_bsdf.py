import bpy
from ..utilities.utils import get_prefs

# set material property presets  
def mat_presets_shader_bsdf(self, node):                 
    
    if self.mat_presets_type_bsdf =="Acryl":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness

    if self.mat_presets_type_bsdf =="Asphalt":
        node.inputs[5].default_value =  0.25 #specular
        node.inputs[7].default_value =  0.55 #roughness

    if self.mat_presets_type_bsdf =="Bark":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.60 #roughness

    if self.mat_presets_type_bsdf =="Brick":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness

    if self.mat_presets_type_bsdf =="Car":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  1.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #roughness

    if self.mat_presets_type_bsdf =="Carbon":
        node.inputs[4].default_value =  1.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.25 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat

    if self.mat_presets_type_bsdf =="Ceramic":
        node.inputs[1].default_value =  1.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.53 #specular
        node.inputs[7].default_value =  0.00 #roughness

    if self.mat_presets_type_bsdf =="Chalk":
        node.inputs[5].default_value =  0.56 #specular
        node.inputs[7].default_value =  0.65 #roughness

    if self.mat_presets_type_bsdf =="Cloth":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.80 #roughness
        node.inputs[10].default_value = 1.00 #sheen
        node.inputs[11].default_value = 0.00 #sheen_tint

    if self.mat_presets_type_bsdf =="Coal":
        node.inputs[5].default_value =  0.43 #specular
        node.inputs[7].default_value =  0.65 #roughness

    if self.mat_presets_type_bsdf =="Concrete":
        node.inputs[5].default_value =  1.20 #specular
        node.inputs[7].default_value =  0.75 #roughness
    
    if self.mat_presets_type_bsdf =="Cotton":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Dirt":
        node.inputs[5].default_value =  0.75 #specular
        node.inputs[7].default_value =  0.78 #roughness

    if self.mat_presets_type_bsdf =="Glass":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.05 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission
    
    if self.mat_presets_type_bsdf =="Latex":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Leather":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Matte":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Metal":
        node.inputs[4].default_value =  1.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness

    if self.mat_presets_type_bsdf =="Milk":
        node.inputs[1].default_value =  0.10 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.55 #specular
        node.inputs[7].default_value =  0.40 #roughness
        node.inputs[14].default_value = 1.35 #ior        

    if self.mat_presets_type_bsdf =="Mirror":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  1.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[14].default_value = 1.45 #ior

    if self.mat_presets_type_bsdf =="Mud":
        node.inputs[5].default_value =  2.23 #specular
        node.inputs[7].default_value =  0.62 #roughness

    if self.mat_presets_type_bsdf =="Paper":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Plaster":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.85 #roughness     

    if self.mat_presets_type_bsdf =="Plastic":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="PVC":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Rock":
        node.inputs[5].default_value =  0.63 #specular
        node.inputs[7].default_value =  0.80 #roughness

    if self.mat_presets_type_bsdf =="Rubber":
        node.inputs[5].default_value =  0.43 #specular
        node.inputs[7].default_value =  0.80 #roughness

    if self.mat_presets_type_bsdf =="Rust":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.82 #roughness

    if self.mat_presets_type_bsdf =="Sand":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.80 #roughness
        node.inputs[10].default_value = 1.00 #sheen
        node.inputs[11].default_value = 0.00 #sheen_tint

    if self.mat_presets_type_bsdf =="Satin":
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.80 #roughness
        node.inputs[10].default_value = 1.00 #sheen
        node.inputs[11].default_value = 0.00 #sheen_tint

    if self.mat_presets_type_bsdf =="Silicone":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="SSS":
        node.inputs[1].default_value =  0.03 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.50 #roughness
        node.inputs[14].default_value = 1.50 #ior  

        if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            bpy.context.object.active_material.use_sss_translucency = True          

    if self.mat_presets_type_bsdf =="Transparent":
        node.inputs[1].default_value =  0.00 #subsurface
        node.inputs[4].default_value =  0.00 #metallic
        node.inputs[5].default_value =  0.50 #specular
        node.inputs[7].default_value =  0.00 #roughness
        node.inputs[12].default_value = 1.00 #clearcoat
        node.inputs[13].default_value = 0.00 #clearcoat_roughness
        node.inputs[14].default_value = 1.50 #ior
        node.inputs[15].default_value = 1.00 #transmission

    if self.mat_presets_type_bsdf =="Wood":       
        node.inputs[5].default_value =  1.00 #specular
        node.inputs[7].default_value =  0.70 #roughness


