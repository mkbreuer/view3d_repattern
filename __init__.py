# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2021 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


bl_info = {
    "name": "RePattern",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 5),
    "blender": (2, 91, 0), 
    "location": "Default: 3D View > Sidebar [T] > Default Tab: ReP > Panel: RePattern",
    "description": "Tileable mesh and texture pattern creation",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/view3d_repattern",
    "category": "User Tools",
    }  


    
# REGISTRY
def register():
    # UPDATER
    from . import addon_updater_ops
    addon_updater_ops.register(bl_info)  

    from .registries import register_addon
    register_addon()


def unregister(): 
    # UPDATER
    from . import addon_updater_ops
    addon_updater_ops.unregister()  
         
    from .registries import unregister_addon
    unregister_addon()