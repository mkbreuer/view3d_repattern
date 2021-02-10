import bpy


def register_addon():

    # Operators
    from ..operators import register_operators
    register_operators()

    # Properties
    from ..properties import register_properties
    register_properties()
 
    # Icons
    from .icon import register_icons
    register_icons()

    # Panels
    from ..panels import update_panel
    update_panel(None, bpy.context) 

    # KeyMap
    from ..menus import update_menus
    update_menus(None, bpy.context) 

    # Material
    from ..materials import update_color
    update_color(None, bpy.context) 

    # Material
    from ..materials import register_material
    register_material() 

    from ..menus import register_material_menus
    register_material_menus()     
  
    # Icons
    from ..icons.palette import load_icons
    load_icons()


def unregister_addon():

    # Operators
    from ..operators import unregister_operators
    unregister_operators()

    # Properties
    from ..properties import unregister_properties
    unregister_properties()

    # Icons
    from .icon import unregister_icons
    unregister_icons()

    # Material
    from ..materials import unregister_material
    unregister_material()

    from ..menus import unregister_material_menus
    unregister_material_menus() 

    # Icons
    from ..icons.palette import clear_icons
    clear_icons()