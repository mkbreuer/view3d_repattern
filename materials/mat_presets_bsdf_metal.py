import bpy


def mat_presets_metal_bsdf(self, node): 

    if self.metal_type == 'Aluminium':   
        node.inputs[0].default_value = (0.91, 0.91, 0.91, 1) #color
        node.inputs[7].default_value = 0.30 #roughness 
        node.inputs[14].default_value = 1.244 #ior

    if self.metal_type == 'Beryllium':   
        node.inputs[0].default_value = (0.54, 0.54, 0.54, 1) #color
        node.inputs[7].default_value = 0.17 #roughness   
        node.inputs[14].default_value = 1.85 #ior

    if self.metal_type == 'Bismuth':   
        node.inputs[0].default_value = (0.56, 0.53, 0.48, 1) #color
        node.inputs[7].default_value =  0.42 #roughness   
        node.inputs[14].default_value = 1.450 #ior

    if self.metal_type == 'Brass':   
        node.inputs[0].default_value = (0.93, 0.75, 0.41, 1) #color
        node.inputs[7].default_value = 0.30 #roughness   
        node.inputs[14].default_value = 1.450 #ior

    if self.metal_type == 'Bronze':   
        node.inputs[0].default_value = (0.99, 0.68, 0.42, 1) #color
        node.inputs[7].default_value = 0.24 #roughness   
        node.inputs[14].default_value = 1.180 #ior

    if self.metal_type == 'Chromium':   
        node.inputs[0].default_value = (0.55, 0.55, 0.55, 1) #color
        node.inputs[7].default_value = 0.05 #roughness   
        node.inputs[14].default_value = 2.79 #ior

    if self.metal_type == 'Cobalt':   
        node.inputs[0].default_value = (0.68, 0.65, 0.62, 1) #color
        node.inputs[7].default_value = 0.16 #roughness   
        node.inputs[14].default_value = 1.710 #ior

    if self.metal_type == 'Copper':   
        node.inputs[0].default_value = (0.95, 0.64, 0.54, 1) #color
        node.inputs[7].default_value = 0.14 #roughness   
        node.inputs[14].default_value = 1.100 #ior

    if self.metal_type == 'Gallium':   
        node.inputs[0].default_value = (0.72, 0.80, 0.78, 1) #color
        node.inputs[7].default_value = 0.03 #roughness   
        node.inputs[14].default_value = 3.500 #ior

    if self.metal_type == 'Germanium':   
        node.inputs[0].default_value = (0.51, 0.51, 0.46, 1) #color
        node.inputs[7].default_value = 0.30 #roughness   
        node.inputs[14].default_value = 1.450 #ior

    if self.metal_type == 'Gold':   
        node.inputs[0].default_value = (1.00, 0.73, 0.34, 1) #color
        node.inputs[7].default_value = 0.07 #roughness   
        node.inputs[14].default_value = 0.470 #ior

    if self.metal_type == 'Iridium':   
        node.inputs[0].default_value = (0.70, 0.69, 0.65, 1) #color
        node.inputs[7].default_value = 0.07 #roughness   
        node.inputs[14].default_value = 1.450 #ior

    if self.metal_type == 'Iron':   
        node.inputs[0].default_value = (0.56, 0.55, 0.55, 1) #color
        node.inputs[7].default_value = 0.42 #roughness   
        node.inputs[14].default_value = 2.950 #ior

    if self.metal_type == 'Lead':   
        node.inputs[0].default_value = (0.59, 0.63, 0.63, 1) #color
        node.inputs[7].default_value = 0.428 #roughness   
        node.inputs[14].default_value = 2.010 #ior

    if self.metal_type == 'Lithium':   
        node.inputs[0].default_value = (0.92, 0.89, 0.81, 1) #color
        node.inputs[7].default_value = 0.26 #roughness   
        node.inputs[14].default_value = 1.450 #ior
  
    if self.metal_type == 'Mercury':   
        node.inputs[0].default_value = (0.78, 0.78, 0.78, 1) #color
        node.inputs[7].default_value = 0.05 #roughness   
        node.inputs[14].default_value = 1.620 #ior
  
    if self.metal_type == 'Molybdenum':   
        node.inputs[0].default_value = (0.57, 0.59, 0.58, 1) #color
        node.inputs[7].default_value = 0.17 #roughness   
        node.inputs[14].default_value = 1.450 #ior
  
    if self.metal_type == 'Nickel':   
        node.inputs[0].default_value = (0.68, 0.62, 0.54, 1) #color
        node.inputs[7].default_value = 0.19 #roughness   
        node.inputs[14].default_value = 1.080 #ior
  
    if self.metal_type == 'Palladium':   
        node.inputs[0].default_value = (0.73, 0.69, 0.65, 1) #color
        node.inputs[7].default_value = 0.06 #roughness   
        node.inputs[14].default_value = 1.450 #ior
  
    if self.metal_type == 'Platinum':   
        node.inputs[0].default_value = (0.67, 0.64, 0.58, 1) #color
        node.inputs[7].default_value = 0.05 #roughness   
        node.inputs[14].default_value = 2.330 #ior
  
    if self.metal_type == 'Silver':   
        node.inputs[0].default_value = (0.96, 0.94, 0.90, 1) #color
        node.inputs[7].default_value = 0.31 #roughness   
        node.inputs[14].default_value = 0.128 #ior

    if self.metal_type == 'Titanium':   
        node.inputs[0].default_value = (0.58, 0.54, 0.49, 1) #color
        node.inputs[7].default_value = 0.18 #roughness   
        node.inputs[14].default_value = 2.160 #ior

    if self.metal_type == 'Zinc':   
        node.inputs[0].default_value = (0.71, 0.80, 0.81, 1) #color
        node.inputs[7].default_value = 0.05 #roughness   
        node.inputs[14].default_value = 1.517 #ior

    if self.metal_type == 'Zirconium':   
        node.inputs[0].default_value = (0.58, 0.56, 0.53, 1) #color
        node.inputs[7].default_value = 0.17 #roughness   
        node.inputs[14].default_value = 1.800 #ior
   
    node.inputs[4].default_value =  1.00 #metallic
    node.inputs[5].default_value =  0.50 #specular

    if self.metal_type == 'Custom':   
        node.inputs[0].default_value = self.mat_color #color
        node.inputs[4].default_value = self.mat_metallic #metallic
        node.inputs[5].default_value = self.mat_specular #specular
        node.inputs[7].default_value = self.mat_roughness #roughness
        node.inputs[14].default_value = self.mat_ior #ior



# Metal Properties
def mat_presets_metal_type_bsdf(self, node): 

    if self.mat_presets_metal == 'Standard':
        pass
        #node.inputs[7].default_value = 0.0000  

    if self.mat_presets_metal == 'Anodized':
        node.inputs[7].default_value = 0.26
    
    if self.mat_presets_metal == 'Brushed': 
        node.inputs[7].default_value = 0.63    
            
    if self.mat_presets_metal == 'Cartridge':   
        node.inputs[7].default_value = 0.02    
            
    if self.mat_presets_metal == 'Corrosion':   
        node.inputs[7].default_value = 0.69   
            
    if self.mat_presets_metal == 'Cracked':    
        node.inputs[7].default_value = 0.35    
            
    if self.mat_presets_metal == 'Dented':
        node.inputs[7].default_value = 0.50

    if self.mat_presets_metal == 'Directional':
        node.inputs[7].default_value = 0.53

    if self.mat_presets_metal == 'Dusty':
        node.inputs[7].default_value = 0.02

    if self.mat_presets_metal == 'Foil':
        node.inputs[7].default_value = 0.33

    if self.mat_presets_metal == 'Galvanized':
        node.inputs[7].default_value = 0.99

    if self.mat_presets_metal == 'Hammered':
        node.inputs[7].default_value = 0.78

    if self.mat_presets_metal == 'Matte':
        node.inputs[7].default_value = 0.42

    if self.mat_presets_metal == 'Old':
        node.inputs[7].default_value = 0.36

    if self.mat_presets_metal == 'Oxidized':
        node.inputs[7].default_value = 0.42

    if self.mat_presets_metal == 'Painted':
        node.inputs[7].default_value = 0.29

    if self.mat_presets_metal == 'Patinated':
        node.inputs[7].default_value = 0.24

    if self.mat_presets_metal == 'Polished':
        node.inputs[7].default_value = 0.18

    if self.mat_presets_metal == 'Rough':
        node.inputs[7].default_value = 0.44

    if self.mat_presets_metal == 'Rusted':
        node.inputs[7].default_value = 0.66

    if self.mat_presets_metal == 'Rugged':
        node.inputs[7].default_value = 0.63

    if self.mat_presets_metal == 'Sandblasted':
        node.inputs[7].default_value = 0.79

    if self.mat_presets_metal == 'Scratched':
        node.inputs[7].default_value = 0.13

    if self.mat_presets_metal == 'Smooth':
        node.inputs[7].default_value = 0.31

    if self.mat_presets_metal == 'Smudged':
        node.inputs[7].default_value = 0.31

    if self.mat_presets_metal == 'Standard':
        node.inputs[7].default_value = 0.02

    if self.mat_presets_metal == 'Worn':
        node.inputs[7].default_value = 0.67

    if self.mat_presets_metal == 'Wrought':
        node.inputs[7].default_value = 0.63

