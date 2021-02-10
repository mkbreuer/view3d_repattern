import bpy
from bpy import *
from bpy.props import *

from ..utilities.utils import get_prefs
from ..utilities.utils import func_find_collection, func_make_collection
from ..utilities.utils import func_collection
from ..utilities.utils import lock_object, unlock_object


class RTS_OT_RePattern_Light_Add(bpy.types.Operator):
    """add lights to the scene"""
    bl_idname = "rts_ot.repattern_add_light"
    bl_label = "Add Lights"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}  

    def draw(self, context):
        layout = self.layout
        
        prefs = get_prefs()
        light_props = prefs.light_type

        col = layout.column(align=True)

        box = col.box().column(align=True)             
        box.separator()
      
        row = box.column(align=True)  
        row.prop(light_props, 'light_radius')

        box.separator()
      
        row = box.column(align=True)  
        row.prop(light_props, 'light_reso')
       
        if light_props.light_reso == 'custom':
           
            row.separator()
            row.prop(light_props, 'custom_switch')             
            row.separator()
            
            if light_props.custom_switch == False:        
                row.prop(light_props, 'custom_grid') 
                           
            else:
                row.prop(light_props, 'custom_grid_top_x') 
                row.prop(light_props, 'custom_grid_top_y') 
                row.prop(light_props, 'custom_grid_top_z')       
 
        box.separator()

        row = box.row(align=True)  
        row.prop(light_props, 'light_rotation', text='')
        row.label(text='Rotation')
        row.prop(light_props, 'light_rotation_type', text='')
        
        if light_props.light_rotation_type == 'custom':
           
            box.separator()
            
            row = box.row(align=True)  
            row.prop(light_props, 'custom_rotation')         


        box.separator()
        box.separator()
    
        row = box.row(align=True)   
        row.label(text="Make Collection")        

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="New Name...")
        row.prop(light_props, "rb_collection_name_lights", text="")

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="Parent to...")
        row.prop(light_props, "rb_collection_name_exist_lights", text="")

        box.separator()  


    def execute(self, context):   

        prefs = get_prefs()
        light_props = prefs.light_type

        bpy.ops.view3d.snap_cursor_to_center()  

        # manage collection                         
        if light_props.rb_collection_name_exist_lights != '':
            collect_exist = light_props.rb_collection_name_exist_lights
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

                
        # light location        
        if light_props.light_reso == "1024px":   

            a_loca_x = 0                               
            a_loca_y = 0                  
            a_loca_z = 200                     

        if light_props.light_reso == "2048px":   

            a_loca_x = 0                               
            a_loca_y = 0                  
            a_loca_z = 300                     

        if light_props.light_reso == "4096px":     

            a_loca_x = 0                               
            a_loca_y = 0                  
            a_loca_z = 500                                
            

        if light_props.light_reso == "custom":     

            if light_props.custom_switch == False:   
           
                a_loca_x = 0                               
                a_loca_y = 0                  
                a_loca_z =  light_props.custom_grid                    

            else:
                a_loca_x = light_props.custom_grid_top_x                             
                a_loca_y = light_props.custom_grid_top_y                 
                a_loca_z = light_props.custom_grid_top_z                    


        # light radius 
        if light_props.light_reso == "1024px":   
            light_radius = 300                               

        if light_props.light_reso == "2048px":   
            light_radius = 600                                               

        if light_props.light_reso == "4096px":     
            light_radius = 900

        if light_props.light_reso == "custom": 
            light_radius=light_props.light_radius


        bpy.ops.object.light_add(type='AREA', radius=light_radius, align='WORLD', location=(a_loca_x, a_loca_y, a_loca_z))  
        bpy.context.object.name = 'RP_Light_Top'
        bpy.context.object.data.name = 'RP_Light_Top'
        bpy.context.object.data.energy = 1000000

        new_object_name = bpy.context.object.name
        obj = bpy.data.objects['RP_Light_Top']          
        obj.select_set(True)
          
        #move to scene collection
        bpy.ops.object.move_to_collection(collection_index=0)

        # move to new collection        
        selected = bpy.context.selected_objects
        for obj in selected:
            if light_props.rb_collection_name_exist_lights!= '':
                bpy.data.collections[light_props.rb_collection_name_exist_lights].objects.link(obj)
            else:
                collect_exist = "RePattern"
                bpy.data.collections[collect_exist].objects.link(obj)                
            bpy.context.scene.collection.objects.unlink(obj)

       # ADD SUBGRID COLLECTION #
        store_collection_name = bpy.data.objects[new_object_name]                                                
        bounds_collection = func_find_collection(bpy.context, store_collection_name)    
   
        id = 0   
        numberDigits = 2  

        if light_props.rb_collection_name_lights!= '':                         
            prefix = light_props.rb_collection_name_lights                       
        else:   
            prefix = "RP_Lights"  

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

        # restrict transorm
        lock_object(self, context)
        
        #print(self)
        self.report({'INFO'}, "Insert Light!")   
        return {'FINISHED'}




class RTS_OT_RePattern_Light_Jump(bpy.types.Operator):
    """selecte light"""
    bl_idname = "rts_ot.repattern_light_jump"
    bl_label = "Select Light"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):               
        bpy.ops.object.select_all(action='DESELECT')            
               
        lights_name = bpy.context.scene.collection_rp_select_list_lights
       
        if lights_name in bpy.data.lights:
            bpy.context.view_layer.objects.active = bpy.data.objects[lights_name] 
            bpy.data.objects[lights_name].select_set(True)  

        #print(self)
        self.report({'INFO'}, "Light selected!")  
        return {'FINISHED'}

                   

class RTS_OT_RePattern_Light_Remove(bpy.types.Operator):
    """remove repattern lights and purge all unused"""
    bl_idname = "rts_ot.repattern_light_remove"
    bl_label = "Remove Light"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):

        # make active
        bpy.ops.object.select_all(action='DESELECT')                        

        lights_name = bpy.context.scene.collection_rp_select_list_lights    
        #lights_name = 'RP_Light_Top'        

        if lights_name in bpy.data.objects:  
            obj = bpy.data.objects[lights_name]   
            obj.select_set(True)
      
            #bpy.ops.object.delete(use_global=False)
            temp_remove = bpy.data.lights       
            temp_remove.remove(temp_remove[lights_name], do_unlink=True, do_id_user=True, do_ui_user=True)

            #print(self)
            self.report({'INFO'}, "Removed Light!") 
    
        else:
            self.report({'INFO'}, "Nope :(!") 
        return {'FINISHED'}


# LAMP SELECTION #
class RTS_OT_RePattern_Light_Selection(bpy.types.Operator):
    """select light by name"""
    bl_idname = "rts_ot.repattern_light_selection"
    bl_label = "Light Selection"
    bl_options = {'REGISTER', 'UNDO'}
         
    light_mode : StringProperty(default="")
    extend_light : BoolProperty(name="Extend Light Selection",  description="Extend Light Selection", default=False)   

    def execute(self, context):
        
        if self.extend_light == False:       
            bpy.ops.object.select_all(action='DESELECT')
                       
        if bpy.data.objects.get("RP_Light_Top") is not None:
            if "top" in self.light_mode:
                bpy.ops.object.select_pattern(pattern="RP_Light_Top", extend = self.extend_light)     
                    
                if self.extend_light == False:
                    bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Top"]             
        else:
            pass          
       
        if bpy.data.objects.get("RP_Light_Key") is not None:          
            if "key" in self.light_mode:
                bpy.ops.object.select_pattern(pattern="RP_Light_Key", extend=self.extend_light)
               
                if self.extend_light == False:
                    bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Key"] 
        else:
            pass          
    
        if bpy.data.objects.get("RP_Light_Rim") is not None:             
            if "rim" in self.light_mode:
                bpy.ops.object.select_pattern(pattern="RP_Light_Rim", extend=self.extend_light) 
         
                if self.extend_light == False:
                    bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Rim"] 
        else:
            pass            

        if bpy.data.objects.get("RP_Light_Fill_A") is not None:
            if "fill_a" in self.light_mode:
                bpy.ops.object.select_pattern(pattern="RP_Light_Fill_A", extend=self.extend_light)

                if self.extend_light == False:
                    bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Fill_A"] 
        else:
            pass          
            
        if bpy.data.objects.get("RP_Light_Fill_B") is not None:
            if "fill_b" in self.light_mode:
                bpy.ops.object.select_pattern(pattern="RP_Light_Fill_B", extend=self.extend_light)

                if self.extend_light == False: 
                    bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Fill_B"] 
        else:
            pass          
      
        bpy.ops.wm.tool_set_by_id(name="builtin.move")

        return {'FINISHED'}



# LAMP CONSTRAINTS #
class RTS_OT_RePattern_Light_Constraints(bpy.types.Operator):
    """select constraint to adjust light position"""
    bl_idname = "rts_ot.repattern_light_constraints"
    bl_label = "Light Constraints"
    bl_options = {'REGISTER', 'UNDO'}
         
    mode : StringProperty(default="")

    def execute(self, context):
        
        bpy.ops.object.select_all(action='DESELECT')

        if bpy.data.objects.get("RP_Light_Center") is not None:

            if "center" in self.mode:
                bpy.data.objects['RP_Light_Center'].hide_select = False  
                bpy.ops.object.select_pattern(pattern="RP_Light_Center", extend=False)             
                bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Center"] 
        else:
            pass          

        if bpy.data.objects.get("RP_Light_Track") is not None:       
      
            if "track" in self.mode:
                bpy.data.objects['RP_Light_Track'].hide_select = False  
                bpy.ops.object.select_pattern(pattern="RP_Light_Track", extend=False)        
                bpy.context.view_layer.objects.active = bpy.data.objects["RP_Light_Track"] 
        else:
            pass          

        bpy.ops.wm.tool_set_by_id(name="builtin.move")
        return {'FINISHED'}



# LAMP RESTRICT #
class RTS_OT_RePattern_Light_Restrict(bpy.types.Operator):
    """restrict light constraints"""
    bl_idname = "rts_ot.repattern_light_restrict"
    bl_label = "Freeze"
    bl_options = {'REGISTER', 'UNDO'}

    mode : StringProperty(default="")

    def execute(self, context):

        if "rp_lock_rotation" in self.mode:  
            bpy.data.objects["RP_Light_Center"].hide_select = True          
        else:
            print(self)
            self.report({'INFO'}, "Not added!")   


        if "rp_lock_move" in self.mode:  
            bpy.data.objects["RP_Light_Track"].hide_select = True
        else:
            print(self)
            self.report({'INFO'}, "Not added!")   

        bpy.ops.wm.tool_set_by_id(name="builtin.move")    
        return {'FINISHED'}
    


class RTS_OT_RePattern_Light_Bake(bpy.types.Operator):
    """Back lights with irredance volume"""
    bl_idname = "rts_ot.repattern_light_back"
    bl_label = "Back Lights"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}


    def draw(self, context):
        layout = self.layout
        
        prefs = get_prefs()
        light_props = prefs.light_type

        col = layout.column(align=True)

        box = col.box().column(align=True)             
        box.separator()
      
        row = box.column(align=True)  
        row.prop(light_props, 'light_reso')
       
        if light_props.light_reso == 'custom':        
            
            row.separator()
            row.prop(light_props, 'light_vradius')   
        
        row.separator()

        row.prop(light_props, 'custom_vgrid_x') 
        row.prop(light_props, 'custom_vgrid_y') 
        row.prop(light_props, 'custom_vgrid_z')       


        box.separator()
        box.separator()
    
        row = box.row(align=True)   
        row.label(text="Make Collection")        

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="New Name...")
        row.prop(light_props, "rb_collection_name_lights", text="")

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="Parent to...")
        row.prop(light_props, "rb_collection_name_exist_lights", text="")

        box.separator()  

 
    def execute(self, context):   

        prefs = get_prefs()
        light_props = prefs.light_type

        bpy.ops.view3d.snap_cursor_to_center()  

        # manage collection                         
        if light_props.rb_collection_name_exist_lights != '':
            collect_exist = light_props.rb_collection_name_exist_lights
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

                
        # light radius 
        if light_props.light_reso == "1024px":   
            light_radius = 50                               

        if light_props.light_reso == "2048px":   
            light_radius = 100                                              

        if light_props.light_reso == "4096px":     
            light_radius = 200

        if light_props.light_reso == "custom": 
            light_radius=light_props.light_vradius

        bpy.ops.object.lightprobe_add(type='GRID', radius=light_radius, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = 'RP_Light_Volume'
        bpy.context.object.data.name = 'RP_Light_Volume'

        bpy.context.object.data.grid_resolution_y = light_props.custom_vgrid_x
        bpy.context.object.data.grid_resolution_x = light_props.custom_vgrid_x
        bpy.context.object.data.grid_resolution_z = light_props.custom_vgrid_x


        new_object_name = bpy.context.object.name
        obj = bpy.data.objects['RP_Light_Volume']          
        obj.select_set(True)
          
        #move to scene collection
        bpy.ops.object.move_to_collection(collection_index=0)

        # move to new collection        
        selected = bpy.context.selected_objects
        for obj in selected:
            if light_props.rb_collection_name_exist_lights!= '':
                bpy.data.collections[light_props.rb_collection_name_exist_lights].objects.link(obj)
            else:
                collect_exist = "RePattern"
                bpy.data.collections[collect_exist].objects.link(obj)                
            bpy.context.scene.collection.objects.unlink(obj)

       # ADD SUBGRID COLLECTION #
        store_collection_name = bpy.data.objects[new_object_name]                                                
        bounds_collection = func_find_collection(bpy.context, store_collection_name)    
   
        id = 0   
        numberDigits = 2  

        if light_props.rb_collection_name_lights!= '':                         
            prefix = light_props.rb_collection_name_lights                       
        else:   
            prefix = "RP_Lights_Bake"  

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

        # restrict transorm
        lock_object(self, context)
        
        #print(self)
        self.report({'INFO'}, "Probe: Irradiance Volume")   
        return {'FINISHED'}
