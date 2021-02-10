import bpy
from bpy import *
from bpy.props import *

from ..utilities.utils import get_prefs
from ..utilities.utils import func_find_collection, func_make_collection
from ..utilities.utils import func_collection
from ..utilities.utils import lock_object, unlock_object


class RTS_OT_RePattern_Camera(bpy.types.Operator):
    """create camera for rendering"""
    bl_idname = "rts_ot.repattern_camera"
    bl_label = "Camera"
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout

        prefs = get_prefs()
        cam_prefs = prefs.camera_type

        col = layout.column(align=True)

        box = col.box().column(align=True)             
        box.separator()
      
        row = box.column(align=True)  
        row.prop(cam_prefs, 'cam_reso')

        row.separator()

        row.prop(cam_prefs, 'cam_lens')                   

        box.separator()        
        box.separator()
    
        row = box.row(align=True)   
        row.label(text="Make Collection")        

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="New Name...")
        row.prop(cam_prefs, "rb_collection_name_camera", text="")

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="Parent to...")
        row.prop(cam_prefs, "rb_collection_name_exist_camera", text="")

        box.separator()  


    def execute(self, context):   

        prefs = get_prefs()
        cam_prefs = prefs.camera_type
        coll_prefs = prefs.coll_type

        bpy.ops.view3d.snap_cursor_to_center()  

        rota_x = 0
        rota_y = 0
        rota_z = 0
        
        loca_x = 0 
        loca_y = 0

        if cam_prefs.cam_reso == '32px':              
            loca_z = 31.25  
        
        if cam_prefs.cam_reso == '64px':              
            loca_z = 62.5  
       
        if cam_prefs.cam_reso == '128px':              
            loca_z = 125  
        
        if cam_prefs.cam_reso == '256px':              
            loca_z = 250 
       
        if cam_prefs.cam_reso == '512px':              
            loca_z = 500
      
        if cam_prefs.cam_reso == '1024px':              
            loca_z = 1000 
      
        if cam_prefs.cam_reso == '2048px':
            loca_z = 2000 

        if cam_prefs.cam_reso == '4096px':
            loca_z = 4000    


         # manage collection                         
        if cam_prefs.rb_collection_name_exist_camera != '':
            collect_exist = cam_prefs.rb_collection_name_exist_camera
            bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collect_exist]                                   
        else:   
            collect_exist = "RePattern"
            if collect_exist in bpy.data.collections:
                bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collect_exist]    
            else:
                # create repattern collation
                func_collection(self, context)     

                # set active scene collection
                scene_collection = bpy.context.view_layer.layer_collection
                bpy.context.view_layer.active_layer_collection = scene_collection  
                   
       
        # add camera   
        bpy.ops.object.camera_add(align='WORLD', enter_editmode=False, location=(loca_x, loca_y, loca_z), rotation=(rota_x, rota_y, rota_z))
        bpy.context.object.name = 'RP_Camera_Top'
        bpy.context.object.data.name = 'RP_Camera_Top'

        # store camera # 
        store_camera = bpy.context.view_layer.objects.active   
   
        new_object_name = bpy.context.object.name
        bpy.data.objects[new_object_name].select_set(True) 

        #move to scene collection
        bpy.ops.object.move_to_collection(collection_index=0)

        # move to new collection        
        selected = bpy.context.selected_objects
        for obj in selected:
            if cam_prefs.rb_collection_name_exist_camera!= '':
                bpy.data.collections[cam_prefs.rb_collection_name_exist_camera].objects.link(obj)
            else:
                collect_exist = "RePattern"
                bpy.data.collections[collect_exist].objects.link(obj)                
            bpy.context.scene.collection.objects.unlink(obj)

       # ADD SUBGRID COLLECTION #
        store_collection_name = bpy.data.objects[new_object_name]                                                
        bounds_collection = func_find_collection(bpy.context, store_collection_name)    
   
        id = 0   
        numberDigits = 2  

        if cam_prefs.rb_collection_name_camera!= '':                         
            prefix = cam_prefs.rb_collection_name_camera                      
        else:   
            prefix = "RP_Camera"  

        # CUSTOM COLLECTION #  
        for key, collections in bpy.data.collections.items():
            if key.startswith(prefix):

                addZero = 0  
                for i in range(1,numberDigits):
                    mod = int(id / (pow(numberDigits,i)))
                    if mod == 0:
                        addZero += 1

                newNameId = str(id)
                for i in range(0,addZero):                                          
                    newNameId = '' + newNameId
              
                new_name = prefix + '_' + newNameId  
                id += 1   

                new_collection = func_make_collection(self, new_name, bounds_collection)              
            else:            
                new_collection = func_make_collection(self, prefix, bounds_collection)     
                                    
        new_collection.objects.link(store_collection_name)  
        bounds_collection.objects.unlink(store_collection_name) 


        # lens          
        if cam_prefs.cam_lens == 'ortho':             
            
            # switch orthogonal scale  
            bpy.context.object.data.type = 'ORTHO'
           
            if cam_prefs.cam_reso == '32px':              
                scale_o  = 3.125 
                scale_c  = 100 
            
            if cam_prefs.cam_reso == '64px':              
                scale_o = 6.25  
                scale_c = 100
           
            if cam_prefs.cam_reso == '128px':              
                scale_o = 12.5  
                scale_c = 100  
            
            if cam_prefs.cam_reso == '256px':              
                scale_o = 25  
                scale_c = 100  
           
            if cam_prefs.cam_reso == '512px':              
                scale_o = 50 
                scale_c = 1000 
          
            if cam_prefs.cam_reso == '1024px':              
                scale_o = 100  
                scale_c = 1000  
          
            if cam_prefs.cam_reso == '2048px':
                scale_o = 200  
                scale_c = 10000  

            if cam_prefs.cam_reso == '4096px':
                scale_o = 400    
                scale_c = 100000
                bpy.context.object.data.clip_end = 100000
        
            bpy.context.object.data.ortho_scale = scale_o
            bpy.context.object.data.clip_end = scale_c

        # lens   
        if cam_prefs.cam_lens == 'persp':  
                       
            # switch perspective scale 
            bpy.context.object.data.type = 'PERSP'

            scale_f = 32                      
            bpy.context.object.data.lens = scale_f            

        # jump to camera view        
        bpy.ops.view3d.object_as_camera()
        bpy.ops.view3d.view_camera()  

        # set render resolution
        bpy.context.scene.render.resolution_x = 1024
        bpy.context.scene.render.resolution_y = 1024        
        bpy.context.scene.render.resolution_percentage = 100

        # reload camera
        bpy.context.view_layer.objects.active = bpy.data.objects[store_camera.name] 
        bpy.data.objects[store_camera.name].select_set(True)
        
        bpy.ops.view3d.view_camera() 

        # restrict transorm
        lock_object(self, context)
      
        #print(self)
        self.report({'INFO'}, "Added Camera!")   
        return {'FINISHED'}




class RTS_OT_RePattern_Camera_Jump(bpy.types.Operator):
    """Camera Render Setup"""
    bl_idname = "rts_ot.repattern_camera_jump"
    bl_label = "Jump To Camera"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):               
        bpy.ops.object.select_all(action='DESELECT')            

        cam_name = bpy.context.scene.collection_rp_select_list_cameras                    
        #cam_name = 'RP_Camera_Top'

        if cam_name in bpy.data.cameras:
            bpy.context.scene.camera = bpy.data.objects[cam_name]    
            bpy.context.view_layer.objects.active = bpy.data.objects[cam_name] 
            bpy.data.objects[cam_name].select_set(True)              
            bpy.ops.view3d.object_as_camera()            

            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    area.spaces[0].region_3d.view_perspective = 'CAMERA'
                    break

            bpy.context.view_layer.objects.active = bpy.data.objects[cam_name] 
            bpy.data.objects[cam_name].select_set(True)   
        
            #print(self)
            self.report({'INFO'}, "Jump To Camera!")  

        else:
            self.report({'INFO'}, "Nope :(!")        
        return {'FINISHED'}



# https://blender.stackexchange.com/questions/30643/how-to-toggle-to-camera-view-via-python
# [‘PERSP’, ‘ORTHO’, ‘CAMERA’]
class RTS_OT_RePattern_Camera_Align(bpy.types.Operator):
    """Camera Render Setup"""
    bl_idname = "rts_ot.repattern_camera_align"
    bl_label = "Align Camera"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context): 
        
        if bpy.data.cameras:
                                         
            bpy.ops.view3d.camera_to_view()

            view_layer = bpy.context.view_layer  
            selected = bpy.context.selected_objects
            if selected:    
                obj = view_layer.objects.active 
                if obj:                
                    # store active # 
                    target = view_layer.objects.active  
          
            bpy.ops.object.select_all(action='DESELECT')            
           
            cam_name = bpy.context.scene.collection_rp_select_list_cameras       
            if cam_name in bpy.data.cameras:
                bpy.context.scene.camera = bpy.data.objects[cam_name]    
                bpy.context.view_layer.objects.active = bpy.data.objects[cam_name] 
                bpy.data.objects[cam_name].select_set(True)
                           
                bpy.ops.view3d.object_as_camera()            
                  
                for area in bpy.context.screen.areas:
                    if area.type == 'VIEW_3D':
                        area.spaces[0].region_3d.view_perspective = 'ORTHO'
                        break

                if selected:    
                    obj = view_layer.objects.active 
                    if obj:          
                        # reload active #     
                        view_layer.objects.active = target 
                        target.select_set(True)
                       
                        bpy.ops.view3d.camera_to_view_selected() 
            
                    #print(self)
                    self.report({'INFO'}, "Align Camera!")  
        else:
            self.report({'INFO'}, "Nope :(!")              
        return {'FINISHED'}



class RTS_OT_RePattern_Camera_Remove(bpy.types.Operator):
    """remve repattern camera"""
    bl_idname = "rts_ot.repattern_camera_remove"
    bl_label = "Camera Remove"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):

        # make active
        bpy.ops.object.select_all(action='DESELECT')                        
            
        cam_name = bpy.context.scene.collection_rp_select_list_cameras
        #cam_name = "RP_Camera_Top"
       
        if cam_name in bpy.data.objects:
            bpy.context.view_layer.objects.active = bpy.data.objects[cam_name] 
            bpy.data.objects[cam_name].select_set(True)  

            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            bpy.ops.view3d.view_persportho()
                            bpy.ops.view3d.snap_cursor_to_center()
                            #bpy.ops.view3d.view_all(center=True)
                            #bpy.ops.view3d.view_center_cursor()

            temp_remove = bpy.data.cameras
            temp_remove.remove(temp_remove[cam_name], do_unlink=True, do_id_user=True, do_ui_user=True)
       
            self.report({'INFO'}, "Removed Camera!") 

        else:
            self.report({'INFO'}, "Nope :(!")   
        return {'FINISHED'}



