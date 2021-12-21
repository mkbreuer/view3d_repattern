import bpy
from bpy import *
from bpy.props import *
import bmesh

from ..utilities.utils import get_prefs
from ..utilities.utils import func_find_collection, func_make_collection
from ..utilities.utils import func_collection
from ..utilities.utils import toggle_expand


# LISTS FOR SELECTED #
name_list = []
dummy_list = []

# INSERT: GRID #
class RTS_OT_RePattern_Grid_Reference(bpy.types.Operator):
    """create a wired square object as reference"""
    bl_idname = "rts_ot.repattern_reference_grid"
    bl_label = "RefzGrid"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}  

    def draw(self, context):
        layout = self.layout

        prefs = get_prefs()
        grid_prefs = prefs.grid_type          
           
        box = layout.box().column(align=True)    
        box.separator()

        row = box.row(align=True) 
        row.label(text="XY Div", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.6 
        sub.prop(grid_prefs, "grid", text="")

        box.separator()   

        row = box.row(align=True) 
        row.label(text="Grid Result", icon="DOT")
        sub = row.row(align=True)
        sub.scale_x = 0.6      
        sub.prop(grid_prefs, "grid_result", text="")

        if grid_prefs.grid_result == 'custom':             
            box.separator()

            row = box.row(align=True)        
            row.label(text="Custom", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6   
            row.prop(grid_prefs, "custom_grid", text="")        

        box.separator()
        
        row = box.row(align=True) 
        row.prop(grid_prefs, "pock_grid")  
        row.prop(grid_prefs, "grid_z_offset")

        box.separator()

        row = box.row(align=True) 
        row.prop(grid_prefs, "grid_snappoints", text="SnapDiv:") 
        row.prop(grid_prefs, "grid_div")
        
        box.separator()          
        box.separator()
        
        row = box.row(align=True)   
        row.prop(grid_prefs, 'add_axis')        
        row.prop(grid_prefs, 'set_axis_wall')  
        row.prop(grid_prefs, 'set_axis_cube')  
       
        box.separator()
      
        row = box.row(align=True)  
        if grid_prefs.add_axis == True:
      
            row.prop(grid_prefs, 'set_axis_xy')  
            row.prop(grid_prefs, 'set_axis_yz')  
            row.prop(grid_prefs, 'set_axis_xz')  

        else:
            row.prop(grid_prefs, 'axis_rota', expand=True) 

        box.separator()    
        box.separator()

        row = box.row(align=True)  
        row.prop(grid_prefs, "lock_grid")  
        row.prop(grid_prefs, "render_grid")  

        row = box.row(align=True) 
        row.prop(grid_prefs, "collapse_parent", text='Child Col')  
        row.prop(grid_prefs, "collapse_toggle", text='Collapse Col')  

        box.separator()

        box.separator()
    
        row = box.row(align=True)   
        row.label(text="Make Collection")        

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="New Name...")
        row.prop(grid_prefs, "rb_collection_name_grid", text="")

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="Parent to...")
        row.prop(grid_prefs, "rb_collection_name_exist_grid", text="")

        box.separator()  


    def execute(self, context):   
        prefs = get_prefs()
        grid_prefs = prefs.grid_type  
        
        bpy.ops.object.select_all(action='DESELECT')
  
        view_layer = bpy.context.view_layer
        selected = bpy.context.selected_objects

        if context.mode == ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]:      
            bpy.ops.object.editmode_toggle()                        
        else:
            pass
        
        bpy.ops.view3d.snap_cursor_to_center()

        # manage collection                         
        if grid_prefs.rb_collection_name_exist_grid != '':
            collect_exist = grid_prefs.rb_collection_name_exist_grid
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

                        
        if grid_prefs.set_axis_wall == True:  

            if grid_prefs.set_axis_xy == True or grid_prefs.axis_rota == 'rota_axis_xy':  

                if grid_prefs.grid_result == "32px":  
                    loca_xy_axis_z = -1.5625   

                if grid_prefs.grid_result == "64px":   
                    loca_xy_axis_z = -3.125   

                if grid_prefs.grid_result == "128px":  
                    loca_xy_axis_z = -6.25   

                if grid_prefs.grid_result == "256px":
                    loca_xy_axis_z = -12.5  

                if grid_prefs.grid_result == "512px":    
                    loca_xy_axis_z = -25   

                if grid_prefs.grid_result == "1024px":  
                    loca_xy_axis_z = -50   

                if grid_prefs.grid_result == "2048px":  
                    loca_xy_axis_z = -100   

                if grid_prefs.grid_result == "4096px":  
                    loca_xy_axis_z = -200   
                    
                if grid_prefs.grid_result == "custom":  
                    loca_xy_axis_z = -grid_prefs.custom_grid

                loca_xy_axis_x = 0  
                loca_xy_axis_y = 0  
           

            if grid_prefs.set_axis_yz == True or grid_prefs.axis_rota == 'rota_axis_yz':   

                if grid_prefs.grid_result == "32px":  
                    loca_yz_axis_x = -1.5625   

                if grid_prefs.grid_result == "64px":   
                    loca_yz_axis_x = -3.125   

                if grid_prefs.grid_result == "128px":  
                    loca_yz_axis_x = -6.25   

                if grid_prefs.grid_result == "256px":
                    loca_yz_axis_x = -12.5  

                if grid_prefs.grid_result == "512px":    
                    loca_yz_axis_x = -25   

                if grid_prefs.grid_result == "1024px":  
                    loca_yz_axis_x = -50   

                if grid_prefs.grid_result == "2048px":  
                    loca_yz_axis_x = -100   

                if grid_prefs.grid_result == "4096px":  
                    loca_yz_axis_x = -200   
                    
                if grid_prefs.grid_result == "custom":  
                    loca_yz_axis_x = -grid_prefs.custom_grid  

                loca_yz_axis_y = 0 
                loca_yz_axis_z = 0             
      
          
            if grid_prefs.set_axis_xz == True or grid_prefs.axis_rota == 'rota_axis_xz':         
                
                if grid_prefs.grid_result == "32px":  
                    loca_xz_axis_y = 1.5625   

                if grid_prefs.grid_result == "64px":   
                    loca_xz_axis_y = 3.125   

                if grid_prefs.grid_result == "128px":  
                    loca_xz_axis_y = 6.25   

                if grid_prefs.grid_result == "256px":
                    loca_xz_axis_y = 12.5  

                if grid_prefs.grid_result == "512px":    
                    loca_xz_axis_y = 25   

                if grid_prefs.grid_result == "1024px":  
                    loca_xz_axis_y = 50   

                if grid_prefs.grid_result == "2048px":  
                    loca_xz_axis_y = 100   

                if grid_prefs.grid_result == "4096px":  
                    loca_xz_axis_y = 200   
                    
                if grid_prefs.grid_result == "custom":  
                    loca_xz_axis_y = grid_prefs.custom_grid                  
                
                loca_xz_axis_x = 0  
                loca_xz_axis_z = 0  
        
        else:

            loca_xy_axis_x = 0  
            loca_xy_axis_y = 0  
            loca_xy_axis_z = 0  
            
            loca_yz_axis_x = 0
            loca_yz_axis_y = 0 
            loca_yz_axis_z = 0   

            loca_xz_axis_x = 0  
            loca_xz_axis_y = 0 
            loca_xz_axis_z = 0  

        #4.697
        if grid_prefs.grid_result == "32px":  
            grid_radius = 9.38

        if grid_prefs.grid_result == "64px":   
            grid_radius = 18.75

        if grid_prefs.grid_result == "128px":  
            grid_radius = 37.5

        if grid_prefs.grid_result == "256px":
            grid_radius = 75

        if grid_prefs.grid_result == "512px":    
            grid_radius = 150

        if grid_prefs.grid_result == "1024px":  
            grid_radius = 300

        if grid_prefs.grid_result == "2048px":  
            grid_radius = 600

        if grid_prefs.grid_result == "4096px":  
            grid_radius = 900
            
        if grid_prefs.grid_result == "custom":  
            grid_radius = grid_prefs.custom_grid


        if grid_prefs.add_axis == True:                         

            bpy.ops.mesh.primitive_grid_add(x_subdivisions=0, y_subdivisions=0, size=300, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')               
            bpy.ops.object.mode_set(mode='EDIT')                   
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='VERT')
    
            if grid_prefs.set_axis_xy == True:                     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.grid, y_subdivisions=grid_prefs.grid, size=grid_radius, location=(loca_xy_axis_x, loca_xy_axis_y, loca_xy_axis_z), rotation=(0, 0, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')
        
            if grid_prefs.set_axis_yz == True: 
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.grid, y_subdivisions=grid_prefs.grid, size=grid_radius, location=(loca_yz_axis_x, loca_yz_axis_y, loca_yz_axis_z), rotation=(0, 1.5708, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')
                
            if grid_prefs.set_axis_xz == True:          
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.grid, y_subdivisions=grid_prefs.grid, size=grid_radius, location=(loca_xz_axis_x, loca_xz_axis_y, loca_xz_axis_z), rotation=(1.5708, 0, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')  
        
            bpy.ops.mesh.select_all(action='SELECT')                
            bpy.ops.object.mode_set(mode='OBJECT')   

        else:     
            
            if grid_prefs.axis_rota == 'rota_axis_xy':                     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.grid, y_subdivisions=grid_prefs.grid, size=grid_radius, location=(loca_xy_axis_x, loca_xy_axis_y, loca_xy_axis_z), rotation=(0, 0, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')

            if grid_prefs.axis_rota == 'rota_axis_yz': 
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.grid, y_subdivisions=grid_prefs.grid, size=grid_radius, location=(loca_yz_axis_x, loca_yz_axis_y, loca_yz_axis_z), rotation=(0, 1.5708, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')
       
            if grid_prefs.axis_rota == 'rota_axis_xz':     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.grid, y_subdivisions=grid_prefs.grid, size=grid_radius, location=(loca_xz_axis_x, loca_xz_axis_y, loca_xz_axis_z), rotation=(1.5708, 0, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')
           

        new_object_name = bpy.context.object.name
        bpy.data.objects[new_object_name].select_set(True)   

        #move to scene collection
        bpy.ops.object.move_to_collection(collection_index=0)

        # move to new collection        
        selected = bpy.context.selected_objects
        for obj in selected:
            if grid_prefs.rb_collection_name_exist_grid != '':
                bpy.data.collections[grid_prefs.rb_collection_name_exist_grid].objects.link(obj)
            else:
                bpy.data.collections[collect_exist].objects.link(obj)                
            bpy.context.scene.collection.objects.unlink(obj)

        # ADD GRID COLLECTION #        
        store_collection_name = bpy.data.objects[new_object_name]                                               
        bounds_collection = func_find_collection(bpy.context, store_collection_name)
   
        id = 0   
        numberDigits = 2  

        if grid_prefs.rb_collection_name_grid!= '':                         
            prefix = grid_prefs.rb_collection_name_grid                       
        else:   
            prefix = "RP_Grid"  

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

        # BIND COLLECTION #           
        new_collection.objects.link(store_collection_name)
        bounds_collection.objects.unlink(store_collection_name)   

        if grid_prefs.collapse_toggle == True:
            # collapse collection
            toggle_expand(bpy.context, 2)
            # 1 will expand all collections,
            # 2 will collapse them.


        if grid_prefs.grid_result == "32px":  
            bpy.context.object.name = "Refz_Grid_0.313m" 
            bpy.context.object.data.name = "Refz_Grid_0.313m"

        if grid_prefs.grid_result == "64px":   
            bpy.context.object.name = "Refz_Grid_0.625m" 
            bpy.context.object.data.name = "Refz_Grid_0.625m"

        if grid_prefs.grid_result == "128px":  
            bpy.context.object.name = "Refz_Grid_0.125m" 
            bpy.context.object.data.name = "Refz_Grid_0.125m"

        if grid_prefs.grid_result == "256px":
            bpy.context.object.name = "Refz_Grid_0.25m" 
            bpy.context.object.data.name = "Refz_Grid_0.25m"

        if grid_prefs.grid_result == "512px":    
            bpy.context.object.name = "Refz_Grid_0.5m" 
            bpy.context.object.data.name = "Refz_Grid_0.5m"

        if grid_prefs.grid_result == "1024px":  
            bpy.context.object.name = "Refz_Grid_1m" 
            bpy.context.object.data.name = "Refz_Grid_1m"

        if grid_prefs.grid_result == "2048px":  
            bpy.context.object.name = "Refz_Grid_2m" 
            bpy.context.object.data.name = "Refz_Grid_2m"  

        if grid_prefs.grid_result == "4096px":  
            bpy.context.object.name = "Refz_Grid_4m" 
            bpy.context.object.data.name = "Refz_Grid_4m" 

        if grid_prefs.grid_result == "custom":  
            bpy.context.object.name = "Refz_Grid_Custom" 
            bpy.context.object.data.name = "Refz_Grid_Custom" 


        bpy.ops.object.mode_set(mode='EDIT')                   
        bpy.ops.mesh.select_all(action='SELECT')
       
        if grid_prefs.pock_grid == True:
            bpy.ops.mesh.poke()
    
        if grid_prefs.set_axis_cube == True:                 
            bpy.ops.mesh.primitive_cube_add(size=grid_radius, align='WORLD', enter_editmode=False, location=(0, 0, 0))
            bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.delete(type='ONLY_FACE') 
        
        if grid_prefs.grid_snappoints == True:
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.subdivide(number_cuts=grid_prefs.grid_div, smoothness=0)

        bpy.ops.object.mode_set(mode='OBJECT')
     

        if grid_prefs.lock_grid == True:
            obj = bpy.context.view_layer.objects.active             
            store_name = obj.name                             
            bpy.data.objects[store_name].hide_select = True     

        if grid_prefs.render_grid == True:
            obj = bpy.context.view_layer.objects.active             
            store_name = obj.name                             
            bpy.data.objects[store_name].hide_render = True  
     
     
        if grid_prefs.grid_result == "32px":  
            clip_value = 100
     
        if grid_prefs.grid_result == "64px":   
            clip_value = 100
   
        if grid_prefs.grid_result == "128px":  
            clip_value = 100

        if grid_prefs.grid_result == "256px":
            clip_value = 100

        if grid_prefs.grid_result == "512px":    
            clip_value = 1000

        if grid_prefs.grid_result == "1024px":  
            clip_value = 10000

        if grid_prefs.grid_result == "2048px":  
            clip_value = 100000
       
        if grid_prefs.grid_result == "4096px":  
            clip_value = 1000000
       
        if grid_prefs.grid_result == "custom":  
            clip_value = 1000000

        bpy.context.space_data.clip_end = clip_value

        if grid_prefs.grid_z_offset == True: 
            bpy.ops.rts_ot.repattern_bbox_origin(box_level='bottom')
            bpy.context.object.location[2] = 0

        return {'FINISHED'}




# INSERT: SUBGRID #

class RTS_OT_RePattern_Grid_Sub(bpy.types.Operator):
    """create a wired square object as subgrid"""
    bl_idname = "rts_ot.repattern_subgrid"
    bl_label = "SubGrid"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}  


    def draw(self, context):
        layout = self.layout

        prefs = get_prefs()
        grid_prefs = prefs.grid_type     

        box = layout.box().column(align=True)       
        box.separator()

        row = box.row(align=True) 
        row.label(text="Subgrid Result", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.6 
        sub.prop(grid_prefs, "grid_result", text="")

        box.separator()

        row = box.row(align=True) 
        row.label(text="X SubDiv", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.6 
        sub.prop(grid_prefs, "subgrid_x", text="")

        box.separator()

        row = box.row(align=True) 
        row.label(text="Y SubDiv", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.6 
        sub.prop(grid_prefs, "subgrid_y", text="")
        
        if grid_prefs.grid_result == 'custom':
            box.separator()

            row = box.row(align=True)        
            row.label(text="Custom", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6   
            row.prop(grid_prefs, "custom_subgrid", text="")      

        box.separator()
        
        row = box.row(align=True)
        row.prop(grid_prefs, "pock_subgrid") 
        row.prop(grid_prefs, "subgrid_z_offset") 

        box.separator()
       
        row = box.row(align=True)
        row.prop(grid_prefs, "subgrid_snappoints", text="SnapDiv:") 
        row.prop(grid_prefs, "subgrid_div") 

        box.separator()        
        box.separator()
        
        row = box.row(align=True)   
        row.prop(grid_prefs, 'add_axis')        
        row.prop(grid_prefs, 'set_axis_wall')  
        row.prop(grid_prefs, 'set_axis_cube')  
       
        box.separator()
      
        row = box.row(align=True)  
        if grid_prefs.add_axis == True:
      
            row.prop(grid_prefs, 'set_axis_xy')  
            row.prop(grid_prefs, 'set_axis_yz')  
            row.prop(grid_prefs, 'set_axis_xz')  

        else:
            row.prop(grid_prefs, 'axis_rota', expand=True) 

        box.separator()          
        box.separator()
     
        row = box.row(align=True)  
        row.prop(grid_prefs, "lock_subgrid")  
        row.prop(grid_prefs, "render_subgrid")  

        row = box.row(align=True) 
        row.prop(grid_prefs, "collapse_parent", text='Child Col')  
        row.prop(grid_prefs, "collapse_toggle", text='Collapse Col')  
 
        box.separator()
        box.separator()     
    
        row = box.row(align=True)   
        row.label(text="Make Collection")        

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="New Name...")
        row.prop(grid_prefs, "rb_collection_name_subgrid", text="")

        box.separator()
        
        row = box.row(align=True)   
        row.label(text="Parent to...")
        row.prop(grid_prefs, "rb_collection_name_exist_subgrid", text="")

        box.separator()  


    def execute(self, context):   
        prefs = get_prefs()
        grid_prefs = prefs.grid_type  
     
        bpy.ops.object.select_all(action='DESELECT')

        view_layer = bpy.context.view_layer  
        selected = bpy.context.selected_objects
        
        if context.mode == ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]:      
            bpy.ops.object.editmode_toggle()                        
        else:
            pass
        
        bpy.ops.view3d.snap_cursor_to_center()

        # CREATE REPATTERN COLLECTION #           
        if grid_prefs.rb_collection_name_exist_subgrid != '':
            collect_exist = grid_prefs.rb_collection_name_exist_subgrid
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

        if grid_prefs.set_axis_wall == True:  

            if grid_prefs.set_axis_xy == True or grid_prefs.axis_rota == 'rota_axis_xy':  

                if grid_prefs.grid_result == "32px":  
                    loca_xy_axis_z = -1.5625   

                if grid_prefs.grid_result == "64px":   
                    loca_xy_axis_z = -3.125   

                if grid_prefs.grid_result == "128px":  
                    loca_xy_axis_z = -6.25   

                if grid_prefs.grid_result == "256px":
                    loca_xy_axis_z = -12.5  

                if grid_prefs.grid_result == "512px":    
                    loca_xy_axis_z = -25   

                if grid_prefs.grid_result == "1024px":  
                    loca_xy_axis_z = -50   

                if grid_prefs.grid_result == "2048px":  
                    loca_xy_axis_z = -100   

                if grid_prefs.grid_result == "4096px":  
                    loca_xy_axis_z = -200   
                    
                if grid_prefs.grid_result == "custom":  
                    loca_xy_axis_z = -grid_prefs.custom_subgrid

                loca_xy_axis_x = 0  
                loca_xy_axis_y = 0  
           

            if grid_prefs.set_axis_yz == True or grid_prefs.axis_rota == 'rota_axis_yz':   

                if grid_prefs.grid_result == "32px":  
                    loca_yz_axis_x = -1.5625   

                if grid_prefs.grid_result == "64px":   
                    loca_yz_axis_x = -3.125   

                if grid_prefs.grid_result == "128px":  
                    loca_yz_axis_x = -6.25   

                if grid_prefs.grid_result == "256px":
                    loca_yz_axis_x = -12.5  

                if grid_prefs.grid_result == "512px":    
                    loca_yz_axis_x = -25   

                if grid_prefs.grid_result == "1024px":  
                    loca_yz_axis_x = -50   

                if grid_prefs.grid_result == "2048px":  
                    loca_yz_axis_x = -100   

                if grid_prefs.grid_result == "4096px":  
                    loca_yz_axis_x = -200   
                    
                if grid_prefs.grid_result == "custom":  
                    loca_yz_axis_x = -grid_prefs.custom_subgrid  

                loca_yz_axis_y = 0 
                loca_yz_axis_z = 0             
      
          
            if grid_prefs.set_axis_xz == True or grid_prefs.axis_rota == 'rota_axis_xz':         
                
                if grid_prefs.grid_result == "32px":  
                    loca_xz_axis_y = 1.5625   

                if grid_prefs.grid_result == "64px":   
                    loca_xz_axis_y = 3.125   

                if grid_prefs.grid_result == "128px":  
                    loca_xz_axis_y = 6.25   

                if grid_prefs.grid_result == "256px":
                    loca_xz_axis_y = 12.5  

                if grid_prefs.grid_result == "512px":    
                    loca_xz_axis_y = 25   

                if grid_prefs.grid_result == "1024px":  
                    loca_xz_axis_y = 50   

                if grid_prefs.grid_result == "2048px":  
                    loca_xz_axis_y = 100   

                if grid_prefs.grid_result == "4096px":  
                    loca_xz_axis_y = 200   
                    
                if grid_prefs.grid_result == "custom":  
                    loca_xz_axis_y = grid_prefs.custom_subgrid                  
                
                loca_xz_axis_x = 0  
                loca_xz_axis_z = 0  
        
        else:

            loca_xy_axis_x = 0  
            loca_xy_axis_y = 0  
            loca_xy_axis_z = 0  
            
            loca_yz_axis_x = 0
            loca_yz_axis_y = 0 
            loca_yz_axis_z = 0   

            loca_xz_axis_x = 0  
            loca_xz_axis_y = 0 
            loca_xz_axis_z = 0  

        #1.5625
        if grid_prefs.grid_result == "32px":  
            grid_radius = 6.25

        if grid_prefs.grid_result == "64px":   
            grid_radius = 3.125

        if grid_prefs.grid_result == "128px":  
            grid_radius = 12.5

        if grid_prefs.grid_result == "256px":
            grid_radius = 25

        if grid_prefs.grid_result == "512px":    
            grid_radius = 50

        if grid_prefs.grid_result == "1024px":  
            grid_radius = 100

        if grid_prefs.grid_result == "2048px":  
            grid_radius = 200

        if grid_prefs.grid_result == "4096px":  
            grid_radius = 400
            
        if grid_prefs.grid_result == "custom":  
            grid_radius = grid_prefs.custom_subgrid


        if grid_prefs.add_axis == True:                         
            
            bpy.ops.mesh.primitive_grid_add(x_subdivisions=0, y_subdivisions=0, size=100, location=(0, 0, 0))               
            bpy.ops.object.mode_set(mode='EDIT')                   
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='VERT')

            if grid_prefs.set_axis_xy == True:                     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xy_axis_x, loca_xy_axis_y, loca_xy_axis_z), rotation=(0, 0, 0))
        
            if grid_prefs.set_axis_yz == True: 
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_yz_axis_x, loca_yz_axis_y, loca_yz_axis_z), rotation=(0, 1.5708, 0))
                
            if grid_prefs.set_axis_xz == True:          
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xz_axis_x, loca_xz_axis_y, loca_xz_axis_z), rotation=(1.5708, 0, 0))

            bpy.ops.mesh.select_all(action='SELECT')                
            bpy.ops.object.mode_set(mode='OBJECT')   

        else:     
            
            if grid_prefs.axis_rota == 'rota_axis_xy':                     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xy_axis_x, loca_xy_axis_y, loca_xy_axis_z), rotation=(0, 0, 0))

            if grid_prefs.axis_rota == 'rota_axis_yz': 
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_yz_axis_x, loca_yz_axis_y, loca_yz_axis_z), rotation=(0, 1.5708, 0))
       
            if grid_prefs.axis_rota == 'rota_axis_xz':     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xz_axis_x, loca_xz_axis_y, loca_xz_axis_z), rotation=(1.5708, 0, 0))


        new_object_name = view_layer.objects.active.name 
        bpy.data.objects[new_object_name].select_set(True)   
              
        #move to scene collection
        bpy.ops.object.move_to_collection(collection_index=0)

        # move to new collection        
        selected = bpy.context.selected_objects
        for obj in selected:
            if grid_prefs.rb_collection_name_exist_subgrid!= '':
                bpy.data.collections[grid_prefs.rb_collection_name_exist_subgrid].objects.link(obj)
            else:
                collect_exist = "RePattern"
                bpy.data.collections[collect_exist].objects.link(obj)                
            bpy.context.scene.collection.objects.unlink(obj)

       # ADD SUBGRID COLLECTION #
        store_collection_name = bpy.data.objects[new_object_name]                                                
        bounds_collection = func_find_collection(bpy.context, store_collection_name)    
   
        id = 0   
        numberDigits = 2  

        if grid_prefs.rb_collection_name_subgrid!= '':                         
            prefix = grid_prefs.rb_collection_name_subgrid                       
        else:   
            prefix = "RP_SubGrid"  

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
        
        if grid_prefs.collapse_toggle == True:
            # collapse collection
            toggle_expand(bpy.context, 2)
            # 1 will expand all collections,
            # 2 will collapse them.


        if grid_prefs.grid_result == "32px":  
            bpy.context.object.name = "SubGrid_0.313m" 
            bpy.context.object.data.name = "SubGrid_0.313m"

        if grid_prefs.grid_result == "64px":   
            bpy.context.object.name = "SubGrid_0.625m" 
            bpy.context.object.data.name = "SubGrid_0.625m"

        if grid_prefs.grid_result == "128px":  
            bpy.context.object.name = "SubGrid_0.125m" 
            bpy.context.object.data.name = "SubGrid_0.125m"

        if grid_prefs.grid_result == "256px":
            bpy.context.object.name = "SubGrid_0.25m" 
            bpy.context.object.data.name = "SubGrid_0.25m"

        if grid_prefs.grid_result == "512px":    
            bpy.context.object.name = "SubGrid_0.5m" 
            bpy.context.object.data.name = "SubGrid_0.5m"

        if grid_prefs.grid_result == "1024px":  
            bpy.context.object.name = "SubGrid_1m" 
            bpy.context.object.data.name = "SubGrid_1m"

        if grid_prefs.grid_result == "2048px":  
            bpy.context.object.name = "SubGrid_2m" 
            bpy.context.object.data.name = "SubGrid_2m"

        if grid_prefs.grid_result == "4096px":  
            bpy.context.object.name = "SubGrid_4m" 
            bpy.context.object.data.name = "SubGrid_4m"

        if grid_prefs.grid_result == "custom":  
            bpy.context.object.name = "Refz_Grid_Custom" 
            bpy.context.object.data.name = "Refz_Grid_Custom" 


        bpy.ops.object.mode_set(mode='EDIT')                   
        bpy.ops.mesh.select_all(action='SELECT')
       
        if grid_prefs.pock_subgrid == True:
            bpy.ops.mesh.poke()

        if grid_prefs.set_axis_cube == True:                 
            bpy.ops.mesh.primitive_cube_add(size=grid_radius, align='WORLD', enter_editmode=False, location=(0, 0, 0))
            bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.delete(type='ONLY_FACE') 
            
        if grid_prefs.subgrid_snappoints == True:
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.subdivide(number_cuts=grid_prefs.subgrid_div, smoothness=0)

        bpy.ops.object.mode_set(mode='OBJECT')

        if grid_prefs.lock_subgrid == True: 
            obj = bpy.context.view_layer.objects.active
            store_name = obj.name                                
            bpy.data.objects[store_name].hide_select = True     

        if grid_prefs.render_subgrid == True:
            obj = bpy.context.view_layer.objects.active             
            store_name = obj.name                             
            bpy.data.objects[store_name].hide_render = True  
     

        if grid_prefs.grid_result == "32px":  
            clip_value = 100
     
        if grid_prefs.grid_result == "64px":   
            clip_value = 100
   
        if grid_prefs.grid_result == "128px":  
            clip_value = 100

        if grid_prefs.grid_result == "256px":
            clip_value = 100

        if grid_prefs.grid_result == "512px":    
            clip_value = 100

        if grid_prefs.grid_result == "1024px":  
            clip_value = 1000

        if grid_prefs.grid_result == "2048px":  
            clip_value = 10000
       
        if grid_prefs.grid_result == "4096px":  
            clip_value = 100000
       
        if grid_prefs.grid_result == "custom":  
            clip_value = 100000

        bpy.context.space_data.clip_end = clip_value

        if grid_prefs.subgrid_z_offset == True: 
            bpy.ops.rts_ot.repattern_bbox_origin(box_level='bottom')
            bpy.context.object.location[2] = 0
      
        return {'FINISHED'}

