import os
import bpy
import bpy.utils.previews

mkb_icon_collections = {}
mkb_icons_loaded = False

def load_icons():
    global mkb_icon_collections
    global mkb_icons_loaded

    if mkb_icons_loaded: return mkb_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))

    mkb_icons.load("icon_black" , os.path.join(icons_dir, "Black.png")  , 'IMAGE')    
    mkb_icons.load("icon_green" , os.path.join(icons_dir, "green.png")  , 'IMAGE')    
    mkb_icons.load("icon_blue"  , os.path.join(icons_dir, "blue.png")   , 'IMAGE')    
    mkb_icons.load("icon_brown" , os.path.join(icons_dir, "brown.png")  , 'IMAGE')    
    mkb_icons.load("icon_red"   , os.path.join(icons_dir, "red.png")    , 'IMAGE')    
    mkb_icons.load("icon_all"   , os.path.join(icons_dir, "all.png") , 'IMAGE')    

    mkb_icon_collections["main"] = mkb_icons
    mkb_icons_loaded = True

    return mkb_icon_collections["main"]

def clear_icons():
    global mkb_icons_loaded
    for icon in mkb_icon_collections.values():
        bpy.utils.previews.remove(icon)
    mkb_icon_collections.clear()
    mkb_icons_loaded = False
