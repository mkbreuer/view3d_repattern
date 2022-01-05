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

        box.separator()

        if bpy.context.scene.unit_settings.system == 'METRIC':

            row = box.row(align=True) 
            row.label(text="SubGrid Result", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6      
            sub.prop(grid_prefs, "grid_radius_metric_sub", text="")

            if grid_prefs.grid_unit_mtc_sub == 'custom':             
                box.separator()

                row = box.row(align=True)        
                row.label(text="Custom", icon="DOT")
                sub = row.row(align=True)
                sub.scale_x = 0.6   
                row.prop(grid_prefs, "custom_subgrid", text="")        

        if bpy.context.scene.unit_settings.system == 'NONE':
            row = box.row(align=True) 
            row.label(text="Blender Units", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6      
            sub.label(text="1bu = 1m")

        if bpy.context.scene.unit_settings.system == 'IMPERIAL':

            row = box.row(align=True)                 
            row.label(text="Imperial Units not supported!", icon="DOT")

        box.separator()
        box = layout.box().column(align=True)  
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
        row.prop(grid_prefs, 'add_axis_sub')        
        row.prop(grid_prefs, 'set_axis_wall_sub')  
        row.prop(grid_prefs, 'set_axis_cube_sub')  
       
        box.separator()
      
        row = box.row(align=True)  
        if grid_prefs.add_axis_sub == True:
      
            row.prop(grid_prefs, 'set_axis_xy_sub')  
            row.prop(grid_prefs, 'set_axis_yz_sub')  
            row.prop(grid_prefs, 'set_axis_xz_sub')  

        else:
            row.prop(grid_prefs, 'axis_rota_sub', expand=True) 

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
                        

        if grid_prefs.set_axis_wall_sub == True:  

            if grid_prefs.set_axis_xy_sub == True or grid_prefs.axis_rota_sub == 'rota_axis_xy':  

                if grid_prefs.grid_unit_mtc_sub == "custom":  
                    loca_xy_axis_z = -grid_prefs.custom_subgrid
                else:
                    if bpy.context.scene.unit_settings.system == 'METRIC':
                        if bpy.context.scene.unit_settings.scale_length != 1.0:
                            loca_xy_axis_z = -float(grid_prefs.grid_metric_loc_sub)
                        else:
                            loca_xy_axis_z = -0.5
                    else:
                        loca_xy_axis_z = -0.5

                loca_xy_axis_x = 0  
                loca_xy_axis_y = 0  
           

            if grid_prefs.set_axis_yz_sub == True or grid_prefs.axis_rota_sub == 'rota_axis_yz':   
                    
                if grid_prefs.grid_unit_mtc_sub == "custom":  
                    loca_yz_axis_x = -grid_prefs.custom_grid  
                else:
                    if bpy.context.scene.unit_settings.system == 'METRIC':
                        if bpy.context.scene.unit_settings.scale_length != 1.0:
                            loca_yz_axis_x = float(grid_prefs.grid_metric_loc_sub)
                        else:
                            loca_yz_axis_x = 0.5
                    else:
                        loca_yz_axis_x = -0.5

                loca_yz_axis_y = 0 
                loca_yz_axis_z = 0             
      
          
            if grid_prefs.set_axis_xz_sub == True or grid_prefs.axis_rota_sub == 'rota_axis_xz':         
                    
                if grid_prefs.grid_unit_mtc_sub == "custom":  
                    loca_xz_axis_y = grid_prefs.custom_subgrid                  
                else:
                    if bpy.context.scene.unit_settings.system == 'METRIC':
                        if bpy.context.scene.unit_settings.scale_length != 1.0:
                            loca_xz_axis_y = float(grid_prefs.grid_metric_loc_sub)
                        else:
                            loca_xz_axis_y = 0.5
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


        if bpy.context.scene.unit_settings.system == 'METRIC':
                
            if grid_prefs.grid_unit_mtc_sub == "custom":  
                grid_radius = grid_prefs.custom_subgrid
            else:
                if bpy.context.scene.unit_settings.scale_length == 1.0:
                    grid_radius = 1
                else:
                    grid_radius = float(grid_prefs.grid_radius_metric_sub) 
                
        if bpy.context.scene.unit_settings.system == 'IMPERIAL':
            self.report({'INFO'}, "Imperial Units not suppoerted!") 
            return {'CANCELLED'}

        if bpy.context.scene.unit_settings.system == 'NONE':

            if grid_prefs.grid_unit_bu_sub == "custom":  
                grid_radius = grid_prefs.custom_subgrid                      
            else:
                grid_radius = 1


        if grid_prefs.add_axis_sub == True:                         
            
            bpy.ops.mesh.primitive_grid_add(x_subdivisions=0, y_subdivisions=0, size=grid_radius, location=(0, 0, 0))               
            bpy.ops.object.mode_set(mode='EDIT')                   
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='VERT')

            if grid_prefs.set_axis_xy_sub == True:                     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xy_axis_x, loca_xy_axis_y, loca_xy_axis_z), rotation=(0, 0, 0))
        
            if grid_prefs.set_axis_yz_sub == True: 
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_yz_axis_x, loca_yz_axis_y, loca_yz_axis_z), rotation=(0, 1.5708, 0))
                
            if grid_prefs.set_axis_xz_sub == True:          
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xz_axis_x, loca_xz_axis_y, loca_xz_axis_z), rotation=(1.5708, 0, 0))

            bpy.ops.mesh.select_all(action='SELECT')                
            bpy.ops.object.mode_set(mode='OBJECT')   

        else:     
            
            if grid_prefs.axis_rota_sub == 'rota_axis_xy':                     
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_xy_axis_x, loca_xy_axis_y, loca_xy_axis_z), rotation=(0, 0, 0))

            if grid_prefs.axis_rota_sub == 'rota_axis_yz': 
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=grid_prefs.subgrid_x, y_subdivisions=grid_prefs.subgrid_y, size=grid_radius, location=(loca_yz_axis_x, loca_yz_axis_y, loca_yz_axis_z), rotation=(0, 1.5708, 0))
       
            if grid_prefs.axis_rota_sub == 'rota_axis_xz':     
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

        if bpy.context.scene.unit_settings.system == 'METRIC':

            if grid_prefs.grid_radius_metric_sub == "9.38":  
                suffix = "0.625m"
                clip_value = 1000

            if grid_prefs.grid_radius_metric_sub == "18.75":   
                suffix = "0.625m"
                clip_value = 1000 

            if grid_prefs.grid_radius_metric_sub == "37.5":  
                suffix = "0.125m"
                clip_value = 1000 

            if grid_prefs.grid_radius_metric_sub == "75":
                suffix = "0.25m"
                clip_value = 1000 

            if grid_prefs.grid_radius_metric_sub == "150":    
                suffix = "0.5m"
                clip_value = 1000 

            if grid_prefs.grid_radius_metric_sub == "300":  
                suffix = "1m"
                clip_value = 10000 

            if grid_prefs.grid_radius_metric_sub == "600":  
                suffix = "2m"
                clip_value = 100000 

            if grid_prefs.grid_radius_metric_sub == "900":  
                suffix = "4m"
                clip_value = 1000000 

        else:
            suffix = "1bu/m"
            clip_value = 1000


        if grid_prefs.grid_unit_mtc_sub == "custom":  
            bpy.context.object.name = "Refz_SubGrid_Custom" 
        else:
            bpy.context.object.name = "Refz_SubGrid_" + suffix
        
        bpy.context.object.data.name = bpy.context.object.name
        bpy.context.space_data.clip_end = clip_value

        bpy.ops.object.mode_set(mode='EDIT')                   
        bpy.ops.mesh.select_all(action='SELECT')
       
        if grid_prefs.pock_subgrid == True:
            bpy.ops.mesh.poke()

        if grid_prefs.set_axis_cube_sub == True:                 
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
     
        if grid_prefs.subgrid_z_offset == True: 
            bpy.ops.rts_ot.repattern_bbox_origin(box_level='bottom')
            bpy.context.object.location[2] = 0
      
        return {'FINISHED'}

