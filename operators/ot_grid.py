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
        sub.prop(grid_prefs, "grid_radius_metric", text="")

        if grid_prefs.grid_unit_mtc == 'custom':             
            box.separator()

            row = box.row(align=True)        
            row.label(text="Custom", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6   
            row.prop(grid_prefs, "custom_grid", text="") 
                  
        else:
            row = box.row(align=True) 
            row.label(text="Metric Units", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6      
            sub.label(text="1bu = 1m")

        box.separator()
        box = layout.box().column(align=True)  
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
        
        # system units
        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.length_unit = 'METERS'
        bpy.context.scene.unit_settings.scale_length = 1.0
        
        # grid floor
        bpy.context.space_data.overlay.grid_scale = 0.05
        bpy.context.space_data.overlay.grid_lines = 10
        bpy.context.space_data.overlay.grid_subdivisions = 10
        bpy.context.space_data.clip_end = 1000

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

        # grid position               
        if grid_prefs.set_axis_wall == True:  

            if grid_prefs.set_axis_xy == True or grid_prefs.axis_rota == 'rota_axis_xy':  

                if grid_prefs.grid_unit_mtc == "custom":  
                    loca_xy_axis_z = -grid_prefs.custom_grid
                else:
                    loca_xy_axis_z = -0.5

                loca_xy_axis_x = 0  
                loca_xy_axis_y = 0  
           

            if grid_prefs.set_axis_yz == True or grid_prefs.axis_rota == 'rota_axis_yz':   
                    
                if grid_prefs.grid_unit_mtc == "custom":  
                    loca_yz_axis_x = -grid_prefs.custom_grid  
                else:
                    loca_yz_axis_x = -0.5

                loca_yz_axis_y = 0 
                loca_yz_axis_z = 0             
      
          
            if grid_prefs.set_axis_xz == True or grid_prefs.axis_rota == 'rota_axis_xz':         
                    
                if grid_prefs.grid_unit_mtc == "custom":  
                    loca_xz_axis_y = grid_prefs.custom_grid                  
                else:
                    loca_xz_axis_y = 0.5

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


        # grid size
        if grid_prefs.grid_unit_mtc == "custom":  
            grid_radius = grid_prefs.custom_grid
        else:
            grid_radius = 3
                
        # grid type
        if grid_prefs.add_axis == True:                         

            bpy.ops.mesh.primitive_grid_add(x_subdivisions=0, y_subdivisions=0, size=grid_radius, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), enter_editmode=False, align='WORLD')               
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

        # move to scene collection
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


        if grid_prefs.grid_unit_mtc == "custom":  
            bpy.context.object.name = "Refz_Grid_Custom" 
        else:
            bpy.context.object.name = "Refz_Grid_1bu/m"
        
        bpy.context.object.data.name = bpy.context.object.name


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
     
        if grid_prefs.grid_z_offset == True: 
            bpy.ops.rts_ot.repattern_bbox_origin(box_level='bottom')
            bpy.context.object.location[2] = 0

        return {'FINISHED'}

