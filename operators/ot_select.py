import bpy
from bpy import*
from bpy.props import*



def get_AllObjectsInSelection():   
    return bpy.context.selected_objects

def get_hideSelectObjects(object_list):
    for i in object_list:
        i.hide_select = True
    bpy.ops.object.select_all(action='DESELECT')
    return True 

class RTS_OT_RePattern_Freeze(bpy.types.Operator):
    # base function from vismaya
    bl_idname = "rts_ot.freeze_selected"
    bl_label = "Freeze Selection"
    bl_description = "Disables Selection"
   
    def execute(self, context):
        selection = get_AllObjectsInSelection()
        n = len(selection)
        if n > 0:
            get_hideSelectObjects(selection)
            self.report({'INFO'}, "%d Object%s frozen." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        return{'FINISHED'} 




def get_AllObjectsInScene():   
    return bpy.data.objects

def get_dehideSelectObjects(object_list):
    hidedObjs = []
    for i in object_list:
        if i.hide_select == True:
            i.hide_select = False
            hidedObjs.append(i)
    return hidedObjs

def get_highlightObjects(selection_list):   
   for i in selection_list:
        bpy.data.objects[i.name].select_set(True)         

class RTS_OT_RePattern_Unfreeze(bpy.types.Operator):
    # base function from vismaya
    bl_idname = "rts_ot.unfreeze_selected"
    bl_label = "Unfreeze All"
    bl_description = "Enables Selection"
   
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        selection = get_AllObjectsInScene()
        n = len(selection)

        if n > 0:
            freezed_array = get_dehideSelectObjects(selection)
            get_highlightObjects(freezed_array)
            self.report({'INFO'}, "%d Object%s released." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        
        return{'FINISHED'} 




