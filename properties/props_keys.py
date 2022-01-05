import bpy
import rna_keymap_ui
from bpy.props import BoolProperty, EnumProperty

from ..utilities.getkey import get_key_mt, get_key_pie
from ..menus import update_keymenus


class PropsGroup_Keys(bpy.types.PropertyGroup):

    rst_menu_type : BoolProperty(
        name="Switch Menu Layout",
        description="switch menu layout type",
        default=True, 
        update = update_keymenus)  

    rst_menu_layouts : EnumProperty(
         name = '3D View Menus',
         description = 'enable or disable menu for 3D View',
         items=(('menu',   'Context Menu', 'enable menu for 3D View'),
                ('pie',    'Pie Menu',  'enable pie for 3D View'),
                ('off',    'Off',  'diable menus for 3D View')),
         default='menu', update = update_keymenus)


# Layout AddonPrefs
def draw_props_keys(prefs, layout):

    layout.label(text='Hotkeys',  icon='EVENT_OS')

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user  # override addon hotkey
    km = kc.keymaps['3D View']
    
    #Menu
    box = layout.box().column(align=True)
    
    row = box.row(align=True)            
    
    if prefs.keymap_type.rst_menu_type == True: 
        row.label(text="Menu:")
        kmi = get_key_mt(km, 'wm.call_menu', 'RTS_MT_RePattern')          
    
    else:             
        row.label(text="PieMenu:")    
        kmi = get_key_pie(km, 'wm.call_menu_pie', 'RTS_MT_PIE_RePattern')
    
    if kmi:
        row.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, row, 0)
    else:
        row.label(text="No hotkey entry found. Add >")
    
    box.separator()
