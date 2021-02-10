import bpy
import os

def get_path():
    # open docs 
    #script_file = os.path.realpath(__file__)
    #directory = os.path.dirname(script_file)
    #docs_dir = os.path.join(directory, 'docs', 'index.html')
    #return os.path.dirname(os.path.realpath(__file__))
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_name():
    return os.path.basename(get_path())

def get_prefs():
    addon_name = __name__.partition('.')[0]
    return bpy.context.preferences.addons[addon_name].preferences


import addon_utils  
def addon_exists(name):
    for addon_name in bpy.context.preferences.addons.keys():
        if name in addon_name: return True
    return False	



# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(mat_prefs, key))

# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    prefs = get_prefs()
    mat_prefs = prefs.mat_type
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(mat_prefs, key, getattr(self, key))        



# COLLECTION: FIND EXISTING
def func_find_collection(context, item):
    collections = item.users_collection
    if len(collections) > 0:
        return collections[0]
    return context.scene.collection

# COLLECTION USE EXISTING COLLECTION OR CREATE NEW ONE
def func_make_collection(self, collection_name, parent_collection):    
    prefs = get_prefs()
    coll_prefs = prefs.coll_type

    if collection_name in bpy.data.collections: 
        return bpy.data.collections[collection_name]
    else:        
        new_collection = bpy.data.collections.new(collection_name)               
        if coll_prefs.collapse_parent == False:
            # move under child collection
            parent_collection.children.link(new_collection) 
        else:
            # move under to scene collection
            bpy.context.scene.collection.children.link(new_collection)        
        return new_collection

# COLLECTION
def func_collection(self, context):
    context = bpy.context
    scene = context.scene
    collection = bpy.data.collections.new(name="RePattern")
    scene.collection.children.link(collection)  
    collection = bpy.context.view_layer.layer_collection

# https://blenderartists.org/t/question-regarding-expanding-collapsing-collection-in-outliner-in-2-8/1175242/2
def toggle_expand(context, state):
    bpy.ops.wm.redraw_timer(type='DRAW_WIN', iterations=1)
    area = next(a for a in context.screen.areas if a.type == 'OUTLINER')
    bpy.ops.outliner.show_hierarchy({'area': area}, 'INVOKE_DEFAULT')
    for i in range(state):
        bpy.ops.outliner.expanded_toggle({'area': area})
    area.tag_redraw()



# LOCK TRANSFORM
def lock_object(self, context):
    bpy.context.object.lock_location[0] = True
    bpy.context.object.lock_location[1] = True
    bpy.context.object.lock_location[2] = True
    bpy.context.object.lock_rotation[0] = True
    bpy.context.object.lock_rotation[1] = True
    bpy.context.object.lock_rotation[2] = True
    bpy.context.object.lock_scale[0] = True
    bpy.context.object.lock_scale[1] = True
    bpy.context.object.lock_scale[2] = True

# UNLOCK TRANSFORM
def unlock_object(self, context):
    bpy.context.object.lock_scale[2] = False
    bpy.context.object.lock_scale[1] = False
    bpy.context.object.lock_scale[0] = False
    bpy.context.object.lock_rotation[2] = False
    bpy.context.object.lock_rotation[1] = False
    bpy.context.object.lock_rotation[0] = False
    bpy.context.object.lock_location[2] = False
    bpy.context.object.lock_location[1] = False
    bpy.context.object.lock_location[0] = False




