import bpy
from ..utilities.utils import get_prefs
from ..menus.menu_context import RTS_MT_RePattern
from ..menus.menu_pie import RTS_MT_PIE_RePattern



# MENUS: KEY REGISTRY 
addon_keymaps = []
def update_menus(self, context):
    try:
        bpy.utils.unregister_class(RTS_MT_RePattern) 
        bpy.utils.unregister_class(RTS_MT_PIE_RePattern)

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

        if prefs.keymap_type.rst_menu_type == False:

            bpy.utils.register_class(RTS_MT_RePattern)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new("wm.call_menu", "Q", "PRESS", alt=True)  # shift=True, ctrl=True, alt=True
            kmi.properties.name = "RTS_MT_RePattern"                        
            addon_keymaps.append((km,kmi))

        else:
            bpy.utils.register_class(RTS_MT_PIE_RePattern)
            
            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new("wm.call_menu_pie", "Q", "PRESS", alt=True)  
            kmi.properties.name = "RTS_MT_PIE_RePattern"
            addon_keymaps.append((km,kmi))  



# MENUS
from ..menus.menu_mat_del import RTS_MT_RePattern_MAT_Delete

classes = (
    RTS_MT_RePattern_MAT_Delete,
    )

def register_material_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_material_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)