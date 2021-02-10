import bpy
import bmesh
from bpy.props import *
import operator
import time
from mathutils import Vector
from collections import defaultdict
from math import pi
from mathutils import Color
from random import random

from ..utilities.utils import get_prefs
from ..utilities.cache import settings_load, settings_write


class RTS_UL_RePattern_Material_Preview(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        obj = data
        slot = item
        mat = slot.material
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=mat.name if mat else "", translate=False, icon_value=icon)
            if mat and not context.scene.render.use_shading_nodes:
                mat_node = mat.active_node_material
                if mat_node:
                    layout.label(text="Node %s" % mat_node.name, translate=False, icon_value=layout.icon(mat_node))
                elif mat.use_nodes:
                    layout.label(text="Node <none>", translate=False)
                else:
                    layout.label(text="")
        
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)



global_color = (0.830, 0.037, 1, 1)

def makeMaterial(name, diffuse):
    if name in bpy.data.materials:
        material = bpy.data.materials[name]
        material.diffuse_color = diffuse
    else:
        material = bpy.data.materials.new(name)
        material.diffuse_color = diffuse
    return material


def update_color(self, context):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type

    try:    
        global global_color
        global global_mesh_object

        material = makeMaterial(mat_prefs.mat_to_assign, mat_prefs.mat_color)    
        if bpy.data.objects[global_mesh_object].data.materials:
            bpy.data.objects[global_mesh_object].data.materials[0] = material
        else:
            bpy.data.objects[global_mesh_object].data.materials.append(material)       
        add_color = material.mat_color
        global_color = (add_color[0], add_color[1], add_color[2], add_color[3])
            
    except Exception as e:
        print("Select mesh object")



def assign_slot(obj, index):
    if index < len(obj.material_slots):
        obj.material_slots[index].material = get_material(index)
        assign_color(index)



def assign_color(index):
    #prefs = get_prefs()
    #mat_prefs = prefs.mat_type  

    material = get_material(index)
    if material:

        # material.use_nodes = mat_prefs.
        
        rgb = get_color(index)
        rgba = (rgb[0], rgb[1], rgb[2], 1)

        if material.use_nodes and bpy.context.scene.render.engine == 'CYCLES' or material.use_nodes and bpy.context.scene.render.engine == 'BLENDER_EEVEE' :
            # Cycles material (Preferred for baking)
            material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = rgba
            material.diffuse_color = rgba

        elif not material.use_nodes and bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            # Legacy render engine, not suited for baking
            material.diffuse_color = rgba


def get_material(index):
    name = get_name(index)

    # Material already exists?
    if name in bpy.data.materials:
        material = bpy.data.materials[name];

        # Check for incorrect matreials for current render engine
        if not material:
            replace_material(index)

        if not material.use_nodes and bpy.context.scene.render.engine == 'CYCLES':
            replace_material(index)

        elif material.use_nodes and bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            replace_material(index)

        else:
            return material;

    #print("Could nt find {} , create a new one??".format(name))

    material = create_material(index)
    assign_color(index)
    return material


def safe_color(color):
    if len(color) == 3:
        if bpy.app.version > (2, 80, 0):
            # Newer blender versions use RGBA
            return (color[0], color[1], color[2], 1)
        else:
            return color

    elif len(color) == 4:
        if bpy.app.version > (2, 80, 0):
            # Newer blender versions use RGBA
            return color
        else:
            return (color[0], color[1], color[2])

    return color


def color_changed(self, context):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    
    for index in range(0, mat_prefs.color_ID_count):
        assign_color(index)


def color_dropdown_template(self, context):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type

    # change mesh uv channel
    hex_colors = mat_prefs.color_ID_templates.split(',')
    mat_prefs.color_ID_count = len(hex_colors)

    # assign color slots
    for index in range(0, len(hex_colors)):
        color = hex_to_color("#"+hex_colors[index])
        set_color(index, color)
        assign_color(index)





# Replace an existing material with a new one
# This is sometimes necessary after switching the render engine
def replace_material(index):
    name = get_name(index)
    #print("Replace material and create new")

    # check if material exists
    if name in bpy.data.materials:
        material = bpy.data.materials[name];

        # Collect material slots we have to re-assign
        slots = []
        for obj in bpy.context.view_layer.objects: 
            for slot in obj.material_slots:
                if slot.material == material:
                    slots.append(slot)

        # Get new material
        material.user_clear()
        bpy.data.materials.remove(material)
        
        # Re-assign new material to all previous slots
        material = create_material(index)
        for slot in slots:
            slot.material = material;



def create_material(index):
    name = get_name(index)

    # Create new image instead
    material = bpy.data.materials.new(name)
    material.preview_render_type = 'FLAT'
    
    # Cycles: prefer nodes as it simplifies baking
    if bpy.context.scene.render.engine == 'CYCLES': 
        material.use_nodes = True 

    return material



# material_prefix = "RTS_MAT_"
def get_name(index):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    return (mat_prefs.mat_to_assign+'_'+"{:02d}").format(index)
    
    # default return black
def get_color(index):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type   
    if index < mat_prefs.color_ID_count:
        return getattr(mat_prefs, "color_ID_color_{}".format(index))
    return (0, 0, 0)


def set_color(index, color):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    if index < mat_prefs.color_ID_count:
        setattr(mat_prefs, "color_ID_color_{}".format(index), color)


# validate face colors and material slots
def validate_face_colors(obj):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type 

    previous_mode = bpy.context.object.mode;
    count = mat_prefs.color_ID_count

    # verify enough material slots
    if len(obj.material_slots) < count:
        for i in range(count):
            if len(obj.material_slots) < count:
                bpy.ops.object.material_slot_add()
                assign_slot(obj, len(obj.material_slots)-1)
            else:
                break

    # TODO: Check face.material_index
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(obj.data);
    for face in bm.faces:
        face.material_index%= count
    obj.data.update()

    # remove unsed material slots
    if len(obj.material_slots) > count:
        bpy.ops.object.mode_set(mode='OBJECT')
        for i in range(len(obj.material_slots) - count):
            if len(obj.material_slots) > count:
                # Remove last
                bpy.context.object.active_material_index = len(obj.material_slots)-1
                bpy.ops.object.material_slot_remove()

    # reloade previous mode
    bpy.ops.object.mode_set(mode=previous_mode)


def color_count_changed(self, context):
    if bpy.context.active_object != None:
        validate_face_colors(bpy.context.active_object)



gamma = 2.2
def hex_to_color(hex):  
    hex = hex.strip('#')
    lv = len(hex)
    fin = list(int(hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    r = pow(fin[0] / 255, gamma)
    g = pow(fin[1] / 255, gamma)
    b = pow(fin[2] / 255, gamma)
    fin.clear()
    fin.append(r)
    fin.append(g)
    fin.append(b)
    return tuple(fin)


def color_to_hex(color):
    rgb = []
    for i in range(3):
        rgb.append( pow(color[i] , 1.0/gamma) )
    r = int(rgb[0]*255)
    g = int(rgb[1]*255)
    b = int(rgb[2]*255)
    return "#{:02X}{:02X}{:02X}".format(r,g,b)


# get unique color
def get_color_id(index, count):
    color = Color()
    color.hsv = ( index / (count) ), 0.9, 1.0   
    return color



# https://blender.stackexchange.com/questions/158896/how-set-hex-in-rgb-node-python?noredirect=1#comment269316_158896

def srgb_to_linearrgb(c):
    if   c < 0:       return 0
    elif c < 0.04045: return c/12.92
    else:             return ((c+0.055)/1.055)**2.4

def hex_to_rgb_new(h,alpha=1):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)] + [alpha])
