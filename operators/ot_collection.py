# https://blender.stackexchange.com/questions/167428/create-a-collection-inside-another-collection-with-python?noredirect=1&lq=1

import bpy
from bpy.props import *

from ..utilities.utils import get_prefs
from ..utilities.utils import toggle_expand


class RTS_OT_RePattern_Coll_Collapse(bpy.types.Operator):
    bl_idname = "rts_ot.coll_collpase"
    bl_label = "Collapse Collection"
    bl_description = "collapse all collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):                          
        toggle_expand(bpy.context, 2)
        # 1 will expand all collections,
        # 2 will collapse them.
        self.report({'INFO'}, "Collpase  Collections!")     
        return {'FINISHED'}


# https://blender.stackexchange.com/questions/75185/limit-prop-search-to-specific-types-of-objects
class RTS_OT_RePattern_Coll_Selection(bpy.types.Operator):
    """Select all existing boundings in the scene"""
    bl_idname = "rts_ot.rp_coll_selection"
    bl_label = "Collection"     
    bl_options = {'REGISTER', 'UNDO'}
    
    def draw(self, context):
        layout = self.layout.column(align=True)        
        layout.scale_y = 1.2  

        prefs = get_prefs()
        coll_props = prefs.coll_type

        col = layout.column(align=True)    
        box = layout.box().column(align=False)       
        box.separator() 
      
        row = box.row(align=True)
        row.prop_search(data = context.scene, property = 'collection_rp_select_list', search_data = bpy.data, search_property = 'collections',  text="")
    
        box.separator()   
        
        row = box.row(align=True)
        if coll_props.rp_hide_select == True:
            icon_select='RESTRICT_SELECT_ON'
        else:
            icon_select='RESTRICT_SELECT_OFF'   
        row.label(text="Selection:", icon=icon_select)  
        row.prop(coll_props, "rp_hide_select", text="")         
    
        box.separator()   

        row = box.row(align=True)
        if coll_props.rp_hide_view == True:
            icon_hide='HIDE_ON'
        else:
            icon_hide='HIDE_OFF'                    
        row.label(text="UnHide:", icon=icon_hide)  
        row.prop(coll_props, "rp_hide_view", text="")         

        box.separator()      

        row = box.row(align=True)
        if coll_props.rp_hide_viewport == True:
            icon_view='RESTRICT_VIEW_ON'
        else:
            icon_view='RESTRICT_VIEW_OFF'    
        row.label(text="Viewport:", icon=icon_view)  
        row.prop(coll_props, "rp_hide_viewport", text="")         
    
        box.separator()   

        row = box.row(align=True)
        if coll_props.rp_hide_render == True:
            icon_render='RESTRICT_RENDER_ON'
        else:
            icon_render='RESTRICT_RENDER_OFF'  
        row.label(text="Render:", icon=icon_render)  
        row.prop(coll_props, "rp_hide_render", text="")         

        box.separator()      

        row = box.row(align=True)
        if coll_props.rp_holdout == True:
            icon_holdout='HOLDOUT_OFF'
        else:
            icon_holdout='HOLDOUT_ON'  
        row.label(text="HoldOut:", icon=icon_holdout)  
        row.prop(coll_props, "rp_holdout", text="")         
    
        box.separator()   

        row = box.row(align=True)
        if coll_props.rp_indirect_only == True:
            icon_indirect='INDIRECT_ONLY_OFF'
        else:
            icon_indirect='INDIRECT_ONLY_ON'  
        row.label(text="Indirect only:", icon=icon_indirect)  
        row.prop(coll_props, "rp_indirect_only", text="")         

        box.separator() 

        row = box.row(align=True)
        row.label(text="Collections:", icon='TRASH')  
        row.prop(coll_props, "delete_coll", text="")         

        box.separator()  
        box = layout.box().column(align=True) 
        box.separator()  
       
        row = box.row(align=True)
        if coll_props.rp_hide_select_obj == True:
            icon_select_obj='RESTRICT_SELECT_ON'
        else:
            icon_select_obj='RESTRICT_SELECT_OFF'   
        row.label(text="Selection:", icon=icon_select_obj)  
        row.prop(coll_props, "rp_hide_select_obj", text="")         
    
        box.separator()   

        row = box.row(align=True)
        if coll_props.rp_hide_view_obj == True:
            icon_hide_obj='HIDE_ON'
        else:
            icon_hide_obj='HIDE_OFF'                    
        row.label(text="UnHide:", icon=icon_hide_obj)  
        row.prop(coll_props, "rp_hide_view_obj", text="")         

        box.separator()      

        row = box.row(align=True)
        if coll_props.rp_hide_viewport_obj == True:
            icon_view_obj='RESTRICT_VIEW_ON'
        else:
            icon_view_obj='RESTRICT_VIEW_OFF'    
        row.label(text="Viewport:", icon=icon_view_obj)  
        row.prop(coll_props, "rp_hide_viewport_obj", text="")         
    
        box.separator()   

        row = box.row(align=True)
        if coll_props.rp_hide_render_obj == True:
            icon_render_obj='RESTRICT_RENDER_ON'
        else:
            icon_render_obj='RESTRICT_RENDER_OFF'  
        row.label(text="Render:", icon=icon_render_obj)  
        row.prop(coll_props, "rp_hide_render_obj", text="")         

        box.separator()      

        row = box.row(align=True)
        row.label(text="Objects:", icon='TRASH')  
        row.prop(coll_props, "delete_selected", text="")         
        
        box.separator()  
        box = layout.box().column(align=True) 
        box.separator()      

        row = box.row(align=True)
        row.label(text="Purge unused:", icon='TRASH')  
        row.prop(coll_props, "purge_data", text="")      

        box.separator()        


    def execute(self, context):   

        prefs = get_prefs()
        coll_props = prefs.coll_type    

        view_layer = bpy.context.view_layer    
        
        bpy.ops.object.select_all(action='DESELECT')

        #check if collection exist
        collection_name = bpy.context.scene.collection_rp_select_list 
        if collection_name in bpy.data.collections:
            #layer_collection = bpy.context.view_layer.layer_collection.children[collection_name]
            #bpy.context.view_layer.active_layer_collection = layer_collection             
            
            bpy.ops.outliner.collection_show
            bpy.ops.outliner.collection_enable      
            
            bpy.ops.object.collection_objects_select()            

            for obj in bpy.data.collections[collection_name].objects:
                obj.select_set(state=True)   
                bpy.context.view_layer.objects.active = obj                                                       
                get_name = obj.name
                  
            # removes collection orphanless                        
            if coll_props.delete_selected == True or coll_props.delete_coll == True:                                       

                if coll_props.delete_selected == True:                 
                    for collection in bpy.data.collections:
                        collection_objects = collection.objects
                        if collection_objects:
                            if get_name in collection.objects and obj in collection_objects[:]:
                                #bpy.data.objects.remove(obj)
                                bpy.ops.collection.objects_remove(collection=collection_name)    
                                coll_props.report({'INFO'}, 'Removed! :)')  
                else:  
                    bpy.data.collections.remove(bpy.data.collections.get(collection_name), do_unlink=True, do_id_user=True, do_ui_user=True)                   
                    coll_props.report({'INFO'}, 'Removed! :)')            

                # only worry about data in the startup scene
                #https://docs.blender.org/api/current/bpy.types.BlendDataMeshes.html
                if coll_props.purge_data == True:  
                    for temp_remove in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.metaballs, bpy.data.lattices, bpy.data.materials, bpy.data.images, 
                                        bpy.data.cameras, bpy.data.lightprobes, bpy.data.lights, bpy.data.armatures, bpy.data.fonts, bpy.data.speakers, bpy.data.grease_pencils):
                       
                        for id_data in temp_remove:                
                            if id_data.users == 0:
                                temp_remove.remove(id_data)
                                #temp_remove.remove(id_data, do_unlink=True, do_id_user=True, do_ui_user=True)
                    self.report({'INFO'}, 'Removed + Purged! :)') 
           
            else:
                
                for obj in bpy.data.collections[collection_name].objects:
                    obj.select_set(state=True)   
                    bpy.context.view_layer.objects.active = obj                                                       
                    get_name = obj.name
                    
                    bpy.data.objects[get_name].hide_select = self.rp_hide_select_obj
                    #bpy.data.objects.hide_viewport = self.rp_hide_view_obj
                    bpy.data.objects[get_name].hide_viewport = self.rp_hide_viewport_obj
                    bpy.data.objects[get_name].hide_render = self.rp_hide_render_obj
                
                bpy.data.collections[collection_name].hide_select = self.rp_hide_select
                bpy.data.collections[collection_name].hide_viewport = self.rp_hide_viewport
                bpy.data.collections[collection_name].hide_render = self.rp_hide_render

                bpy.context.view_layer.active_layer_collection.hide_viewport = self.rp_hide_view
                bpy.context.view_layer.active_layer_collection.holdout = self.rp_holdout
                bpy.context.view_layer.active_layer_collection.indirect_only = self.rp_indirect_only

                self.report({'INFO'}, 'Done! :)')  
        else:
            self.report({'INFO'}, 'Nope! :(')    
               
        # update scene, if needed
        dg = bpy.context.evaluated_depsgraph_get() 
        dg.update()
        return {'FINISHED'}     


