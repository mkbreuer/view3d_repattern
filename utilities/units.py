import bpy

from ..utilities.utils import get_prefs

# Jayanam https://www.youtube.com/watch?v=mHfGBjZFBYE
def get_current_units():

    lenght = bpy.context.scene.unit_settings.length_unit

    if lenght == 'KILOMETERS':
        return ('km', 1000) 
    elif lenght == 'METERS':        
        return ('m', 1)
    elif lenght == 'CENTIMETERS':        
        return ('cm', 1 / 100)
    elif lenght == 'MILLIMETERS':         
        return ('mm', 1 / 1000) 
    elif lenght == 'MICROMETERS':        
        return ('mcm', 1 / 1000000)
    elif lenght == 'MILES':        
        return ('mi', 1760)
    elif lenght == 'FEET':        
        return ('ft', 1 / 3)
    elif lenght == 'INCHES':         
        return ('in', 1 / 36) 
    elif lenght == 'THOU':        
        return ('thou', 1 / 3600)
    else:
        return ('bu', 1)

def bu_to_unit (value, scale):
    return value / scale

def unit_to_bu (value, scale):
    return value * scale


#from ..utilities.units import get_current_units, bu_to_unit, unit_to_bu

# get_unit_metric()
# bu_to_unit (value, scale)
# unit_to_bu (value, scale)

 # unit_value = def get_current_units():()
 # unit_value[0]  # show string from list
 # unit_value[1]  # use value from list
 

    # unitinfo = get_current_units()   
    # size_value = 10
    # unit_valve = bu_to_unit(size_value, unitinfo[1])
    # default_value = str(unit_valve)            
    # base_value : StringProperty(name="Name", default=default_value)  

    # apply_value = float(base_value)  
    # unit_apply = unit_to_bu(apply_value , unitinfo[1])
    # base_value_apply : FloatProperty(name="Name", default= unit_apply)  
