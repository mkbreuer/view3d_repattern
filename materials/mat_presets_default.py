import bpy
from ..utilities.utils import get_prefs

# Material without nodes
def mat_presets_diffuse(self, mat): 

    mat.specular_intensity = self.mat_specular
    
    if self.mat_presets_type =='Custom':
        mat.metallic = self.mat_metallic
        mat.roughness = self.mat_roughness          

  
    if self.mat_presets_type =='Metal':  
        mat.metallic = 1.00
        mat.roughness = 0.00


    if self.mat_presets_type =='Acrylic':  
        mat.metallic = 0.00
        mat.roughness = 0.39

    if self.mat_presets_type =='Brick':  
        mat.metallic = 0.00
        mat.roughness = 0.23

    if self.mat_presets_type =='Ceramic':  
        mat.metallic = 0.00
        mat.roughness = 0.43

    if self.mat_presets_type =='Cotton':  
        mat.metallic = 0.00
        mat.roughness = 0.79

    if self.mat_presets_type =='Dirt':  
        mat.metallic = 0.00
        mat.roughness = 0.06

    if self.mat_presets_type =='Glass':  
        mat.metallic = 0.00
        mat.roughness = 0.01
  
    if self.mat_presets_type =='Glossy':  
        mat.metallic = 0.00
        mat.roughness = 0.05

    if self.mat_presets_type =='Latex':  
        mat.metallic = 0.00
        mat.roughness = 0.10

    if self.mat_presets_type =='Leather':  
        mat.metallic = 0.00
        mat.roughness = 0.05

    if self.mat_presets_type =='Matte':  
        mat.metallic = 0.50
        mat.roughness = 0.50

    if self.mat_presets_type =='Mirror':  
        mat.metallic = 1.00
        mat.roughness = 0.00

    if self.mat_presets_type =='Mud':  
        mat.metallic = 0.00
        mat.roughness = 0.18

    if self.mat_presets_type =='Plaster':  
        mat.metallic = 0.00
        mat.roughness = 0.14

    if self.mat_presets_type =='Plastic':  
        mat.metallic = 0.00
        mat.roughness = 0.28

    if self.mat_presets_type =='PVC':  
        mat.metallic = 0.00
        mat.roughness = 0.20

    if self.mat_presets_type =='Rock':  
        mat.metallic = 0.00
        mat.roughness = 0.67

    if self.mat_presets_type =='Rubber':  
        mat.metallic = 0.00
        mat.roughness = 0.33

    if self.mat_presets_type =='Silicone':  
        mat.metallic = 0.00
        mat.roughness = 0.56

    if self.mat_presets_type =='Wood':  
        mat.metallic = 0.00
        mat.roughness = 0.32


