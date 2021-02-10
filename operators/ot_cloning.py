import bpy
import math
import mathutils

from bpy.props import *
from mathutils import *

from ..utilities.utils import get_prefs
from ..utilities.utils import func_find_collection, func_make_collection
from ..utilities.utils import func_collection
from ..utilities.utils import toggle_expand


class RTS_OT_RePattern_Cloning(bpy.types.Operator):
    # base function from mift cloning
    bl_idname = "rts_ot.mft_radial_clone"
    bl_label = "Radial Clone"
    bl_description = "Radial Clone"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        
        prefs = get_prefs()
        clone_prefs = prefs.clone_type

        col = layout.column(align=True)

        box = col.box().column(align=True)             
        box.separator()
      
        row = box.row(align=True)   
        row.label(text="Clones")     
        row.prop(clone_prefs, 'create_clones', text="")

        box.separator()
       
        row = box.row(align=True)   
        row.label(text="Angle")            
        row.prop(clone_prefs, 'radial_clones_angle', text="")          
        
        box.separator()
          
        row = box.row(align=True)   
        row.label(text="Axis")            
        row.prop(clone_prefs, 'radial_clones_axis', text="")          
        
        box.separator() 
        row = box.row(align=True)   
        row.label(text="Type")      
        row.prop(clone_prefs, 'radial_clones_axis_type', text="")          
        
        box.separator()

        row = box.row(align=True) 
        row.prop(clone_prefs, "lock_clones")  
        row.prop(clone_prefs, "wired_clones") 
  
        row = box.row(align=True)           
        row.prop(clone_prefs, "parent_clones", text='Parent')  
        row.prop(clone_prefs, "editmode_toggle_clones")   

        row = box.row(align=True) 
        row.prop(clone_prefs, "object_join")  
        row.prop(clone_prefs, "make_single") 

        row = box.row(align=True)  
        row.prop(clone_prefs, "collapse_parent", text='Child Coll')
        row.prop(clone_prefs, "collapse_toggle", text='Collapse Coll')  

        box.separator()     
        box.separator()
    
        row = box.row(align=True)   
        row.label(text="Make Collection")        

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="New Name...")
        row.prop(clone_prefs, "rb_collection_name_clone", text="")

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="Parent to...")
        row.prop(clone_prefs, "rb_collection_name_exist_clone", text="")

        box.separator()  


    def execute(self, context):   
        prefs = get_prefs()
        clone_prefs = prefs.clone_type
     
        view_layer = bpy.context.view_layer  
                     
        selected = bpy.context.selected_objects             
        obj_list = [obj for obj in selected]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}    
        else:             
            for active_obj in selected:     
                view_layer.objects.active = active_obj
                active_obj.select_set(True)                         

        # CREATE REPATTERN COLLECTION #           
        if clone_prefs.rb_collection_name_exist_clone != '':
            collect_exist = clone_prefs.rb_collection_name_exist_clone
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
        
        source = view_layer.objects.active     
       
        #move to scene collection
        bpy.ops.object.move_to_collection(collection_index=0)

        # move to new collection        
        for obj in selected:
            if clone_prefs.rb_collection_name_exist_clone != '':
                bpy.data.collections[clone_prefs.rb_collection_name_exist_clone].objects.link(obj)
            else:
                bpy.data.collections[collect_exist].objects.link(obj)                
            bpy.context.scene.collection.objects.unlink(obj)

   
        # ADD CLONE COLLECTION #
        new_object_name = source.name
        store_collection_name = bpy.data.objects[new_object_name]                                                
        bounds_collection = func_find_collection(bpy.context, store_collection_name)    
   
        id = 0   
        numberDigits = 2  

        if clone_prefs.rb_collection_name_clone!= '':                         
            prefix = clone_prefs.rb_collection_name_clone                       
        else:   
            prefix = "RP_Radial"  

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

        if clone_prefs.collapse_toggle == True:
            # collapse collection
            toggle_expand(bpy.context, 2)
            # 1 will expand all collections,
            # 2 will collapse them.

        if clone_prefs.wired_clones == True:
            bpy.context.object.display_type = 'WIRE'    

        # FUNC: ROTATION #  
        source_matrix = source.matrix_world

        clones_count = clone_prefs.create_clones
        if clone_prefs.create_last_clone is False:
            clones_count = clone_prefs.create_clones - 1

        for i in range(clones_count):
            bpy.ops.object.duplicate(linked=True, mode='DUMMY')

            the_axis = None

            if clone_prefs.radial_clones_axis == 'X':
                if clone_prefs.radial_clones_axis_type == 'Local':
                    the_axis = (source_matrix[0][0], source_matrix[1][0], source_matrix[2][0])
                else:
                    the_axis = ('X')

            elif clone_prefs.radial_clones_axis == 'Y':
                if clone_prefs.radial_clones_axis_type == 'Local':
                    the_axis = (source_matrix[0][1], source_matrix[1][1], source_matrix[2][1])
                else:
                    the_axis = ('Y')

            elif clone_prefs.radial_clones_axis == 'Z':
                if clone_prefs.radial_clones_axis_type == 'Local':
                    the_axis = (source_matrix[0][2], source_matrix[1][2], source_matrix[2][2])
                else:
                    the_axis = ('Z')

            rotateValue = (math.radians(clone_prefs.radial_clones_angle) / float(clone_prefs.create_clones))        
            bpy.ops.transform.rotate(value=rotateValue, orient_axis=the_axis)
      

        # CUSTOM COLLECTION #                                                      
        if clone_prefs.rb_collection_name_clone != '':    
            prefix = rb_collection_name_clone                     
            for key, collections in bpy.data.collections.items():
                if key.startswith(prefix):  
                    col = bpy.data.collections[key]

        else:                                           
            prefix = "RP_Radial"                       
            for key, collections in bpy.data.collections.items():
                if key.startswith(prefix):                           
                    col = bpy.data.collections[key]  
                    
        if col:
           for obj in col.objects:
               obj.select_set(True)                   
               if clone_prefs.lock_clones == True: 
                   obj.hide_select=True
               else:    
                   obj.hide_select=False
                       

        bpy.ops.object.select_all(action='DESELECT')

        selected = bpy.context.selected_objects 
        for obj in selected:
            obj.select_set(True)
        selected = None
     
        view_layer.objects.active = source
      
        if clone_prefs.make_single == True and clone_prefs.object_join == False:
            bpy.ops.object.select_linked(type='OBDATA')
            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)       

        if clone_prefs.parent_clones == True:
            bpy.ops.object.select_grouped(type='COLLECTION')
            #bpy.ops.object.select_linked(type='LIBRARY_OBDATA')
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False) 

        if clone_prefs.object_join == True and clone_prefs.make_single == False:
            bpy.ops.object.select_linked(type='OBDATA')
            bpy.ops.object.join()
            bpy.context.object.name = new_object_name           
       
        if clone_prefs.editmode_toggle_clones == True:       
            bpy.ops.object.editmode_toggle()        

        self.report({'INFO'}, "Created %d Clones!" % clone_prefs.create_clones)     
        return {'FINISHED'}

