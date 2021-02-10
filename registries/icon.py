import bpy

from ..icons.general import initialize_icons_collection_general, unload_icons_general
from ..icons.contrast import initialize_icons_collection_contrast, unload_icons_contrast
from ..icons.circle import initialize_icons_collection_circle, unload_icons_circle
from ..icons.fabric import initialize_icons_collection_fabric, unload_icons_fabric
from ..icons.pencils import initialize_icons_collection_pencils, unload_icons_pencils
from ..icons.wood import initialize_icons_collection_wood, unload_icons_wood
from ..icons.skin import initialize_icons_collection_skin, unload_icons_skin
from ..icons.metal import initialize_icons_collection_metal, unload_icons_metal

def register_icons():
    initialize_icons_collection_general()
    initialize_icons_collection_contrast()
    initialize_icons_collection_circle()
    initialize_icons_collection_fabric()
    initialize_icons_collection_pencils()
    initialize_icons_collection_wood()
    initialize_icons_collection_skin()
    initialize_icons_collection_metal()

def unregister_icons():
    unload_icons_general()
    unload_icons_contrast()
    unload_icons_circle()
    unload_icons_fabric()
    unload_icons_pencils()
    unload_icons_wood()
    unload_icons_skin()
    unload_icons_metal()