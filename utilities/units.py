import bpy

def get_units_info(scale, unit_system, separate_units):
   
    if unit_system == 'METRIC':
        scale_steps = ((1000, 'km'), (1, 'm'), (1 / 100, 'cm'), (1 / 1000, 'mm'), (1 / 1000000, '\u00b5m'))
  
    elif unit_system == 'IMPERIAL':
        scale_steps = ((5280, 'mi'), (1, '\''), (1 / 12, '"'), (1 / 12000, 'thou'))
        scale /= 0.3048  # BU to feet
   
    else:
        scale_steps = ((1, ' BU'),) 
        separate_units = False

    return (scale, scale_steps, separate_units)


# bpy.context.scene.unit_settings.system = 'NONE' #'METRIC' #'IMPERIAL'
# bpy.context.scene.unit_settings.length_unit = 'CENTIMETERS'


# unit_name : EnumProperty(
#     items = [('-',  'None',        '1.0',    0),
#              ('px', 'Pixel',       '1.0',    1),
#              ('m',  'Meter',       '1.0',    2),
#              ('dm', 'Decimeter',   '0.1',    3),
#              ('cm', 'Centimeter',  '0.01',   4),
#              ('mm', 'Millimeter',  '0.001',  5),
#              ('yd', 'Yard',        '0.9144', 6),
#              ('ft', 'Foot',        '0.3048', 7),
#              ('in', 'Inch',        '0.0254', 8)],
#              name = "Unit",
#              default = "cm",
#              description=" ")

# #scale prop?

#     for unit in units:
#         if self.unit_name == unit[0]:
#             self.scale *= 1.0/float(unit[2])
#             break 
    
#     self.scale *= context.scene.unit_settings.scale_length
    


        