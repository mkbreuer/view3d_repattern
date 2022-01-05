import bpy
from ..utilities.utils      import get_prefs
from ..menus.menu_context   import RTS_MT_RePattern
from ..menus.menu_pie       import RTS_MT_PIE_RePattern
from ..menus.menu_mat_del   import RTS_MT_RePattern_MAT_Delete


menus = (
    RTS_MT_RePattern_MAT_Delete,
)

def register_menus():
    from bpy.utils import register_class
    for cls in menus:
        register_class(cls)

def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(menus):
        unregister_class(cls)



keymenus = (
    RTS_MT_RePattern,
    RTS_MT_PIE_RePattern,
)

# MENUS: KEY REGISTRY 
addon_keymaps = []
def update_keymenus(self, context):
    
    try:
        for menu in keymenus:
            bpy.utils.unregister_class(menu)        

        # Keymapping
        # remove keymaps when add-on is deactivated
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
        # clear the list
        addon_keymaps.clear()


    except:
        pass
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:   

        prefs = get_prefs()
        
        for menu in keymenus:
            bpy.utils.register_class(menu)

            if prefs.keymap_type.rst_menu_type == False:

                km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
                kmi = km.keymap_items.new("wm.call_menu", "Q", "PRESS", alt=True)  # shift=True, ctrl=True, alt=True
                kmi.properties.name = "RTS_MT_RePattern"                        
                addon_keymaps.append((km,kmi))

            else:
                        
                km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
                kmi = km.keymap_items.new("wm.call_menu_pie", "Q", "PRESS", alt=True)  
                kmi.properties.name = "RTS_MT_PIE_RePattern"
                addon_keymaps.append((km,kmi))  

           

