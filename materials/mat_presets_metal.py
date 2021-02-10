import bpy


def mat_presets_metal(self, mat): 

    if self.metal_type == 'Custom':   
        mat.diffuse_color = self.mat_color 
        mat.roughness = self.mat_roughness
        mat.metallic = self.mat_metallic
        mat.specular_intensity = self.mat_specular

    if self.metal_type == 'Aluminium':   
        add_color = (0.91, 0.91, 0.91, 1) 
        add_rough = 0.30  

    if self.metal_type == 'Beryllium':   
        add_color = (0.54, 0.54, 0.54, 1) 
        add_rough = 0.17    

    if self.metal_type == 'Bismuth':   
        add_color = (0.56, 0.53, 0.48, 1) 
        add_rough =  0.42    

    if self.metal_type == 'Brass':   
        add_color = (0.93, 0.75, 0.41, 1) 
        add_rough = 0.30    

    if self.metal_type == 'Bronze':   
        add_color = (0.99, 0.68, 0.42, 1) 
        add_rough = 0.24    

    if self.metal_type == 'Chromium':   
        add_color = (0.55, 0.55, 0.55, 1) 
        add_rough = 0.05    

    if self.metal_type == 'Cobalt':   
        add_color = (0.68, 0.65, 0.62, 1) 
        add_rough = 0.16    

    if self.metal_type == 'Copper':   
        add_color = (0.95, 0.64, 0.54, 1) 
        add_rough = 0.14    

    if self.metal_type == 'Gallium':   
        add_color = (0.72, 0.80, 0.78, 1) 
        add_rough = 0.03    

    if self.metal_type == 'Germanium':   
        add_color = (0.51, 0.51, 0.46, 1) 
        add_rough = 0.30    

    if self.metal_type == 'Gold':   
        add_color = (1.00, 0.73, 0.34, 1) 
        add_rough = 0.07    

    if self.metal_type == 'Iridium':   
        add_color = (0.70, 0.69, 0.65, 1) 
        add_rough = 0.07    

    if self.metal_type == 'Iron':   
        add_color = (0.56, 0.55, 0.55, 1) 
        add_rough = 0.42    

    if self.metal_type == 'Lead':   
        add_color = (0.59, 0.63, 0.63, 1) 
        add_rough = 0.428    

    if self.metal_type == 'Lithium':   
        add_color = (0.92, 0.89, 0.81, 1) 
        add_rough = 0.26    

    if self.metal_type == 'Mercury':   
        add_color = (0.78, 0.78, 0.78, 1) 
        add_rough = 0.05    

    if self.metal_type == 'Molybdenum':   
        add_color = (0.57, 0.59, 0.58, 1) 
        add_rough = 0.17    

    if self.metal_type == 'Nickel':   
        add_color = (0.68, 0.62, 0.54, 1) 
        add_rough = 0.19    

    if self.metal_type == 'Palladium':   
        add_color = (0.73, 0.69, 0.65, 1) 
        add_rough = 0.06    

    if self.metal_type == 'Platinum':   
        add_color = (0.67, 0.64, 0.58, 1) 
        add_rough = 0.05    

    if self.metal_type == 'Silver':   
        add_color = (0.96, 0.94, 0.90, 1) 
        add_rough = 0.31    

    if self.metal_type == 'Titanium':   
        add_color = (0.58, 0.54, 0.49, 1) 
        add_rough = 0.18    

    if self.metal_type == 'Zinc':   
        add_color = (0.71, 0.80, 0.81, 1) 
        add_rough = 0.05    

    if self.metal_type == 'Zirconium':   
        add_color = (0.58, 0.56, 0.53, 1) 
        add_rough = 0.17    

    
    if self.metal_type != 'Custom': 

        mat.diffuse_color = add_color 
        mat.metallic = 1.0000    
        mat.roughness = add_rough
        mat.specular_intensity = 0.5000




# Metal Properties
def mat_presets_metal_type(self, mat): 

    
    if self.mat_presets_metal == 'Standard':
        pass
        #add_rough = 0.0000  

    if self.mat_presets_metal == 'Anodized':    
        add_rough = 0.26    
    
    if self.mat_presets_metal == 'Brushed': 
        add_rough = 0.63    
            
    if self.mat_presets_metal == 'Cartridge':   
        add_rough = 0.02    
            
    if self.mat_presets_metal == 'Corrosion':   
        add_rough = 0.69   
            
    if self.mat_presets_metal == 'Cracked':    
        add_rough = 0.35    
            
    if self.mat_presets_metal == 'Dented':
        add_rough = 0.50

    if self.mat_presets_metal == 'Directional':
        add_rough = 0.53

    if self.mat_presets_metal == 'Dusty':
        add_rough = 0.02

    if self.mat_presets_metal == 'Foil':
        add_rough = 0.33

    if self.mat_presets_metal == 'Galvanized':
        add_rough = 0.99

    if self.mat_presets_metal == 'Hammered':
        add_rough = 0.78

    if self.mat_presets_metal == 'Matte':
        add_rough = 0.42

    if self.mat_presets_metal == 'Old':
        add_rough = 0.36

    if self.mat_presets_metal == 'Oxidized':
        add_rough = 0.42

    if self.mat_presets_metal == 'Painted':
        add_rough = 0.29

    if self.mat_presets_metal == 'Patinated':
        add_rough = 0.24

    if self.mat_presets_metal == 'Polished':
        add_rough = 0.18

    if self.mat_presets_metal == 'Rough':
        add_rough = 0.44

    if self.mat_presets_metal == 'Rusted':
        add_rough = 0.66

    if self.mat_presets_metal == 'Rugged':
        add_rough = 0.63

    if self.mat_presets_metal == 'Sandblasted':
        add_rough = 0.79

    if self.mat_presets_metal == 'Scratched':
        add_rough = 0.13

    if self.mat_presets_metal == 'Smooth':
        add_rough = 0.31

    if self.mat_presets_metal == 'Smudged':
        add_rough = 0.31

    if self.mat_presets_metal == 'Standard':
        add_rough = 0.02

    if self.mat_presets_metal == 'Worn':
        add_rough = 0.67

    if self.mat_presets_metal == 'Wrought':
        add_rough = 0.63
   
    
    if self.mat_presets_metal != 'Standard':    
        mat.roughness = add_rough





