import bpy
import bmesh
from bpy import *
from bpy.props import *
from mathutils import Vector
from math import radians
from math import pi
from random import random

from ..utilities.utils import get_prefs
from ..utilities.utils import func_find_collection, func_make_collection
from ..utilities.utils import func_collection
from ..utilities.utils import toggle_expand



# BOUND GEOMETRY #
def func_build_grid(instance_props):
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=instance_props.bounds_grid_subdivX, y_subdivisions=instance_props.bounds_grid_subdivY, 
                                    size=instance_props.bounds_grid_size, 
                                    rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z), 
                                    calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)

def func_build_cube(instance_props):
    bpy.ops.mesh.primitive_cube_add(size=instance_props.bounds_cube_radius, 
                                    rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z), 
                                    calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)

def func_build_circle(instance_props):
    bpy.ops.mesh.primitive_circle_add(vertices=instance_props.bounds_circle_amount, radius=instance_props.bounds_circle_radius, 
                                      fill_type=instance_props.end_fill_type, 
                                      rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z),
                                      calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)                                     

def func_build_cylinder(instance_props):
    bpy.ops.mesh.primitive_cylinder_add(vertices=instance_props.bounds_cylinder_amount, radius=instance_props.bounds_cylinder_radius, 
                                        depth=instance_props.bounds_cylinder_depth, end_fill_type=instance_props.end_fill_type, 
                                        rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z),
                                        calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)                                            

def func_build_cone(instance_props):
    bpy.ops.mesh.primitive_cone_add(vertices=instance_props.bounds_cone_amount, radius1=instance_props.bounds_cone_radius_1, 
                                    radius2=instance_props.bounds_cone_radius_2, 
                                    depth=instance_props.bounds_cone_depth, end_fill_type=instance_props.end_fill_type, 
                                    rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z),
                                    calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)     
                                 

def func_build_torus(instance_props):
    bpy.ops.mesh.primitive_torus_add(major_segments=instance_props.bounds_torus_segments_1, minor_segments=instance_props.bounds_torus_segments_2, 
                                     mode=instance_props.bounds_torus_dimension, 
                                     major_radius=instance_props.bounds_torus_size_1, minor_radius=instance_props.bounds_torus_size_2,
                                     rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z),
                                     generate_uvs=instance_props.uvmap_toggle, align=instance_props.align)

def func_build_sphere(instance_props):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=instance_props.bounds_sphere_segments, ring_count=instance_props.bounds_sphere_ring, 
                                         radius=instance_props.bounds_sphere_size, 
                                         rotation =(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z), 
                                         calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)

def func_build_ico(instance_props):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=instance_props.bounds_ico_subdiv, radius=instance_props.bounds_ico_size, 
                                          rotation =(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z), 
                                          calc_uvs=instance_props.uvmap_toggle, enter_editmode=False, align=instance_props.align)


def func_type_curve(instance_props):
    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.curve.spline_type_set(type=instance_props.typ_curve)#, use_handles=self.use_handles)
    bpy.ops.curve.handle_type_set(type='AUTOMATIC') 
    bpy.ops.object.editmode_toggle()


def func_build_curve(instance_props):
    bpy.ops.curve.primitive_bezier_circle_add(radius=instance_props.bounds_curve_radius, 
                                              rotation=(instance_props.rota_x, instance_props.rota_y, instance_props.rota_z), 
                                              enter_editmode=False, align=instance_props.align)

    bpy.context.object.data.dimensions = instance_props.bounds_curve_type
    bpy.context.object.data.twist_mode = instance_props.bounds_curve_twist
    bpy.context.object.data.twist_smooth = instance_props.bounds_curve_smooth
   
    bpy.context.object.data.fill_mode = instance_props.bounds_curve_fill
    bpy.context.object.data.use_fill_deform = instance_props.bounds_curve_deformed
    bpy.context.object.data.use_radius = instance_props.bounds_curve_use_radius
    bpy.context.object.data.use_stretch = instance_props.bounds_curve_stretch
    bpy.context.object.data.use_deform_bounds = instance_props.bounds_curve_clamp

    bpy.context.object.data.offset = instance_props.bounds_curve_geom_offset
    bpy.context.object.data.extrude = instance_props.bounds_curve_geom_extrude
    bpy.context.object.data.bevel_depth = instance_props.bounds_curve_geom_depth
    bpy.context.object.data.bevel_resolution = instance_props.bounds_curve_geom_loops
    bpy.context.object.data.resolution_u = instance_props.bounds_curve_geom_rings

    bpy.context.object.data.bevel_factor_start = instance_props.bounds_curve_geom_start
    bpy.context.object.data.bevel_factor_end = instance_props.bounds_curve_geom_end
    bpy.context.object.data.bevel_factor_mapping_start = instance_props.bounds_curve_geom_start_map
    bpy.context.object.data.bevel_factor_mapping_end = instance_props.bounds_curve_geom_end_map

    # APPLY SCALE FOR BEVELED CURVE #             
    if instance_props.typ_geometry == "typ_curve":
        if bpy.context.object.data.bevel_depth > 0:        
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)   

    if instance_props.typ_curve != "BEZIER":
        func_type_curve(instance_props)


# MESH: SUBDIVIDE (SMOOTH) #
def func_subdivide(instance_props):
    bpy.ops.object.editmode_toggle()              
    bpy.ops.mesh.select_all(action='SELECT')                                                                       
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.mesh.subdivide(number_cuts=instance_props.mesh_subdiv, smoothness=instance_props.mesh_subdiv_smooth, 
                           ngon=True, quadcorner='INNERVERT', 
                           fractal=0.000, fractal_along_normal=0.000, seed=1)
    bpy.ops.object.editmode_toggle()  
    


# INSERT INSTANCES #
class RTS_OT_RePattern_Instances(bpy.types.Operator):
    """wrap around primitive or selected as instances"""
    bl_idname = "rts_ot.repattern_instances_fields"
    bl_label = "Wrap Around Instances"
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        
        prefs = get_prefs()
        instance_props = prefs.instance_type  
        
        col = layout.column(align=True)

        box = col.box().column(align=True)                    
        box.separator()   

        if instance_props.editmode_toggle == True:

            row = box.row(align=True)  
            row.label(text='properties are todo!')              
           
        else:            
            row = box.column(align=True)  
            row.prop(instance_props, 'tp_geom_result') 

            row.separator()
            
            if instance_props.wrap_instances == False:
                row.prop(instance_props, 'tp_geom_rota') 
            row.prop(instance_props, 'tp_instance_rota') 

            row.separator()
            

            if instance_props.wrap_instances == True:

                box.separator()
                
                row = box.column(align=True) 
                row.label(text="! wrap selected around !")
                
            else:    

                row = box.row(align=True) 
                row.label(text="Object Type:")               
                row.prop(instance_props, "typ_geometry", text="")

                box.separator()   

                row = box.row(align=True) 
                row.label(text="Mesh Type:")               
                row.prop(instance_props, "typ_mesh", text="")

                box.separator() 

                if instance_props.typ_geometry == "typ_grid": 
                    row = box.row(align=True) 
                    row.label(text="Subdivide:") 
                    
                    sub0 = row.column(align=True)
                    sub0.scale_x = 1
                    sub0.prop(instance_props, "bounds_grid_subdivX")
                    sub0.prop(instance_props, "bounds_grid_subdivY")   

                if instance_props.typ_geometry == "typ_cube": #default
                    row = box.row(align=True) 
                    row.label(text="Subdivide:") 
                    row.prop(instance_props, "mesh_subdiv")
             
                    row = box.row(align=True)        
                    row.label(text=" ")      
                    row.prop(instance_props, "mesh_subdiv_smooth")
          
                if instance_props.typ_geometry == "typ_cylinder": 
                    row = box.row(align=True) 
                    row.label(text="Fill Type:") 
                    row.prop(instance_props, "end_fill_type")
                    
                    row = box.row(align=True) 
                    row.label(text="Vertices:") 
                    row.prop(instance_props, "bounds_cylinder_amount", text='')

                if instance_props.typ_geometry == "typ_cone": 
                    row = box.row(align=True) 
                    row.label(text="Fill Type:") 
                    row.prop(instance_props, "end_fill_type")
                    
                    row = box.row(align=True) 
                    row.label(text="Vertices:") 
                    row.prop(instance_props, "bounds_cone_amount", text='') 

                if instance_props.typ_geometry == "typ_circle": 
                    row = box.row(align=True) 
                    row.label(text="Fill Type:") 
                    row.prop(instance_props, "end_fill_type")
                    
                    row = box.row(align=True) 
                    row.label(text="Vertices:") 
                    row.prop(instance_props, "bounds_circle_amount", text='') 

                if instance_props.typ_geometry == "typ_torus": 
                    row = box.row(align=True) 
                    row.label(text="Major:") 
                    row.prop(instance_props, "bounds_torus_segments_1", text='') 

                    row = box.row(align=True) 
                    row.label(text="Minor:") 
                    row.prop(instance_props, "bounds_torus_segments_2", text='') 

                if instance_props.typ_geometry == "typ_sphere": 
                    row = box.row(align=True) 
                    row.label(text="Rings:") 
                    row.prop(instance_props, "bounds_sphere_ring", text='') 

                    row = box.row(align=True) 
                    row.label(text="Segments:") 
                    row.prop(instance_props, "bounds_sphere_segments", text='') 

                if instance_props.typ_geometry == "typ_ico": 
                    row = box.row(align=True) 
                    row.label(text="Subdivide:") 
                    row.prop(instance_props, "bounds_ico_subdiv", text='') 

                if instance_props.typ_geometry == "typ_curve":
                    row = box.row(align=True) 
                    row.label(text="Curve Type:") 
                    row.prop(instance_props, "typ_curve", text='')            
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Shape Type:") 
                    row.prop(instance_props, "bounds_curve_type", text='') 
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Fill Mode:") 
                    row.prop(instance_props, "bounds_curve_fill", text='') 
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Bevel:") 
                    row.prop(instance_props, "bounds_curve_geom_depth", text='') 
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Rings:") 
                    row.prop(instance_props, "bounds_curve_geom_rings", text='') 
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Loops:") 
                    row.prop(instance_props, "bounds_curve_geom_loops", text='') 
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Height:") 
                    row.prop(instance_props, "bounds_curve_geom_extrude", text='') 
                   
                    box.separator() 
                    
                    row = box.row(align=True) 
                    row.label(text="Offset:") 
                    row.prop(instance_props, "bounds_curve_geom_offset", text='') 

                                 
                if instance_props.typ_geometry == "typ_custom": 
                    row = box.row(align=True) 
                    row.label(text="Custom (WIP)")

                box.separator()              
                                
            box.separator()    
            box.separator()    

            row = box.row(align=True) 
            row.prop(instance_props, "lock_instances")  
            row.prop(instance_props, "wired_instances")  

            row = box.row(align=True) 
            row.prop(instance_props, "parent_instances")  
            row.prop(instance_props, "editmode_toggle", text='Editmode')  
           
            if instance_props.wrap_instances == True:
                row = box.row(align=True) 
                row.prop(instance_props, "uvmap_toggle", text='UV Map')  
         
            box.separator()  

        box.separator()
        box.separator()
       
        # ADD GEOMETRY OR WRAP AROUND #    
        if instance_props.wrap_instances == False:        
            row = box.column(align=True)   
            row.prop(instance_props, "rb_collection_name_exist_instance", icon="BLANK1")
            box.separator()       
        else:
            row = box.column(align=True)   
            row.prop(instance_props, "rb_collection_name_exist_clone", icon="BLANK1")
            box.separator()  


    def execute(self, context):   
        prefs = get_prefs()
        instance_props = prefs.instance_type       

        view_layer = bpy.context.view_layer     
        
        if context.mode == ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]:      
            bpy.ops.object.editmode_toggle()                        
        else:
            pass

        # set and store cursor
        bpy.ops.view3d.snap_cursor_to_center()              
        cursor = bpy.context.scene.cursor.location 

        # list for selection
        name_list = []
        dummy_list = []    


        # manage collection                         
        if instance_props.rb_collection_name_exist_instance != '':
            collect_exist = instance_props.rb_collection_name_exist_instance
            bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collect_exist]                                   
        else:   
            collect_exist = "RePattern"
            if collect_exist in bpy.data.collections:
                bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collect_exist]    
            else:
                # create repattern collation
                func_collection(self, context)     

                # set active scene collection
                #scene_collection = bpy.context.view_layer.layer_collection
                #bpy.context.view_layer.active_layer_collection = scene_collection  
                bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collect_exist]   


        # ADD GEOMETRY OR WRAP AROUND #    
        if instance_props.wrap_instances == False:

            # BUILD GEOMETRY #
            #if self.typ_geometry == "typ_custom":                                         
                #func_build_custom(self)

            if instance_props.typ_geometry == "typ_grid":               
                func_build_grid(instance_props, instance_props)                                              

            if instance_props.typ_geometry == "typ_cube":                                                        
                func_build_cube(instance_props)

                # subdivide
                if instance_props.mesh_subdiv != 0:
                    func_subdivide(instance_props)  

            if instance_props.typ_geometry == "typ_cylinder":                                         
                    func_build_cylinder(instance_props)
           
            if instance_props.typ_geometry == "typ_cone":                                         
                    func_build_cone(instance_props)
           
            if instance_props.typ_geometry == "typ_circle":                                         
                    func_build_circle(instance_props)
           
            if instance_props.typ_geometry == "typ_torus":                                         
                    func_build_torus(instance_props)
           
            if instance_props.typ_geometry == "typ_sphere":                                         
                    func_build_sphere(instance_props)
         
            if instance_props.typ_geometry == "typ_ico":                                         
                    func_build_ico(instance_props)

            if instance_props.typ_geometry == "typ_curve":                                         
                    func_build_curve(instance_props)

            # SHADED MESH #
            if instance_props.typ_mesh == "typ_00":
                pass
            
            # SHADLESS MESH #                        
            if instance_props.typ_mesh == "typ_01":            
                bpy.context.object.display_type = 'WIRE'               
                                 
            # WIRED MESH #
            if instance_props.typ_mesh == "typ_02":            
                if instance_props.typ_geometry != "typ_curve":  
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.delete(type='ONLY_FACE')
                    bpy.ops.object.editmode_toggle()
            
        else:
            # ADD GEOMETRY OR WRAP AROUND #    
            if instance_props.wrap_instances == True:
               
                selected = bpy.context.selected_objects         
                obj_list = [obj for obj in selected]
                if obj_list:

                    #move to scene collection
                    bpy.ops.object.move_to_collection(collection_index=0)

                    # move to new collection        
                    for obj in selected:
                        if instance_props.rb_collection_name_exist_clone != '':
                            bpy.data.collections[instance_props.rb_collection_name_exist_clone].objects.link(obj)
                        else:
                            bpy.data.collections[collect_exist].objects.link(obj)                
                        bpy.context.scene.collection.objects.unlink(obj)

                else:            
                    self.report({'INFO'}, 'No Selection!') 
                    return {'CANCELLED'}



        if instance_props.use_custom_wrap == True:

            # INSTANCE CUSTOM WRAP NAME #        
            if instance_props.wrap_instances == False:            
                            
                bpy.context.object.name = instance_props.tp_wrap_prefix + instance_props.tp_wrap_object + instance_props.tp_wrap_suffix
                bpy.context.object.data.name = instance_props.tp_wrap_prefix + instance_props.tp_wrap_object + instance_props.tp_wrap_suffix   

            else:
                bpy.context.object.name = instance_props.tp_wrap_prefix + bpy.context.object.name + instance_props.tp_wrap_suffix
                bpy.context.object.data.name = instance_props.tp_wrap_prefix + bpy.context.object.name + instance_props.tp_wrap_suffix                        
   
        else:

            # INSTANCE CUSTOM WRAP NAME #        
            if instance_props.wrap_instances == False:            
                            
                bpy.context.object.name = 'Instances_Grid'
                bpy.context.object.data.name = 'Instances_Grid'  

            else:        
                bpy.context.object.name = bpy.context.object.name + "_Grid"
                bpy.context.object.data.name = bpy.context.object.name + "_Grid"


        # ADD COLLECTION #
        new_object_name = bpy.context.object.name
        store_collection_name = bpy.data.objects[new_object_name]                                               
        bounds_collection = func_find_collection(bpy.context, store_collection_name)
                     
        id = 0   
        numberDigits = 2  

        # CUSTOM COLLECTION #                                                      
        if instance_props.rb_collection_name_instance != '':                         
            prefix = instance_props.rb_collection_name_instance                        
        else:
            prefix = "RP_Instance"   
      
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


        if instance_props.collapse_toggle == True:
            # collapse collection
            toggle_expand(bpy.context, 2)
            # 1 will expand all collections,
            # 2 will collapse them.
            

        # INSTANCE XY HORIZONTAL #
        if instance_props.tp_instance_rota == 'rota_axis_xy':

            if instance_props.tp_geom_result == "32px":   
                
                a_loca_x = 0                  
                a_loca_y = -3.13133                     
                a_loca_z = 0                    
                
                b_loca_x = -3.13133                  
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 3.13133                     
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 3.13133                     
                d_loca_z = 0                     
                              
                e_loca_x = 3.13133                    
                e_loca_y = 0                    
                e_loca_z = 0                     
                
                f_loca_x = 3.13133                      
                f_loca_y = 0                    
                f_loca_z = 0                    
                
                g_loca_x = 0                   
                g_loca_y = -3.13133                    
                g_loca_z = 0                   
                                
                h_loca_x = 0                  
                h_loca_y = -3.13133                     
                h_loca_z = 0                    


            if instance_props.tp_geom_result == "64px":   

                a_loca_x = 0                   
                a_loca_y = -6.25333                    
                a_loca_z = 0                    
                
                b_loca_x = -6.25333                     
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 6.25333                    
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 6.25333                    
                d_loca_z = 0                     
                              
                e_loca_x = 6.25333                    
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 6.25333                     
                f_loca_y = 0                    
                f_loca_z = 0                    
                
                g_loca_x = 0                    
                g_loca_y = -6.25333                   
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -6.25333                   
                h_loca_z = 0   


            if instance_props.tp_geom_result == "128px":   

                a_loca_x = 0                                
                a_loca_y = -12.5                   
                a_loca_z = 0                    
                
                b_loca_x = -12.5                    
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 12.5                   
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 12.5                    
                d_loca_z = 0                     
                              
                e_loca_x = 12.5                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 12.5                    
                f_loca_y = 0                   
                f_loca_z = 0                    
                
                g_loca_x = 0                   
                g_loca_y = -12.5                  
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -12.5                   
                h_loca_z = 0   


            if instance_props.tp_geom_result == "256px":   

                a_loca_x = 0                                
                a_loca_y = -25                   
                a_loca_z = 0                    
                
                b_loca_x = -25                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 25                   
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 25                    
                d_loca_z = 0                     
                              
                e_loca_x = 25                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 25                    
                f_loca_y = 0                   
                f_loca_z = 0                    
                
                g_loca_x = 0                 
                g_loca_y = -25                  
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -25                   
                h_loca_z = 0   


            if instance_props.tp_geom_result == "512px":   

                a_loca_x = 0                               
                a_loca_y = -50                   
                a_loca_z = 0                    
                
                b_loca_x = -50                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 50                   
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 50                    
                d_loca_z = 0                     
                              
                e_loca_x = 50                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 50                    
                f_loca_y = 0                  
                f_loca_z = 0                    
                
                g_loca_x = 0                  
                g_loca_y = -50                  
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -50                   
                h_loca_z = 0   


            if instance_props.tp_geom_result == "1024px":   

                a_loca_x = 0                               
                a_loca_y = -100                   
                a_loca_z = 0                    
                
                b_loca_x = -100                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 100                   
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 100                    
                d_loca_z = 0                     
                              
                e_loca_x = 100                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 100                    
                f_loca_y = 0                 
                f_loca_z = 0                    
                
                g_loca_x = 0                 
                g_loca_y = -100                  
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -100                   
                h_loca_z = 0   


            if instance_props.tp_geom_result == "2048px":   

                a_loca_x = 0                              
                a_loca_y = -200                   
                a_loca_z = 0                    
                
                b_loca_x = -200                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 200                   
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 200                    
                d_loca_z = 0                     
                              
                e_loca_x = 200                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 200                    
                f_loca_y = 0                 
                f_loca_z = 0                    
                
                g_loca_x = 0                
                g_loca_y = -200                  
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -200                   
                h_loca_z = 0   


            if instance_props.tp_geom_result == "4096px":     

                a_loca_x = 0                               
                a_loca_y = -400                   
                a_loca_z = 0                    
                
                b_loca_x = -400                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 400                   
                c_loca_z = 0                    
               
                d_loca_x = 0                     
                d_loca_y = 400                    
                d_loca_z = 0                     
                              
                e_loca_x = 400                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 400                    
                f_loca_y = 0                 
                f_loca_z = 0                    
                
                g_loca_x = 0               
                g_loca_y = -400                  
                g_loca_z = 0                   
                                
                h_loca_x = 0                    
                h_loca_y = -400                   
                h_loca_z = 0   



        # INSTANCE YZ VERTICAL #
        if instance_props.tp_instance_rota == 'rota_axis_yz': 

            if instance_props.tp_geom_result == "32px":   
                
                a_loca_x = 0                  
                a_loca_y = 0                  
                a_loca_z = -3.13133                      
                
                b_loca_x = 0                 
                b_loca_y = -3.13133                      
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                    
                c_loca_z = 3.13133                     
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 3.13133                     
                              
                e_loca_x = 0                  
                e_loca_y = 3.13133                     
                e_loca_z = 0                     
                
                f_loca_x = 0                    
                f_loca_y = 3.13133                      
                f_loca_z = 0                    
                
                g_loca_x = 0                   
                g_loca_y = 0                   
                g_loca_z = -3.13133                   
                                
                h_loca_x = 0                  
                h_loca_y = 0                     
                h_loca_z = -3.13133                     


            if instance_props.tp_geom_result == "64px":   

                a_loca_x = 0                   
                a_loca_y = 0                   
                a_loca_z = -6.25333                     
                
                b_loca_x = 0                     
                b_loca_y = -6.25333                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                    
                c_loca_z = 6.25333                   
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 6.25333                     
                              
                e_loca_x = 0                   
                e_loca_y = 6.25333                   
                e_loca_z = 0                     
                
                f_loca_x = 0                     
                f_loca_y = 6.25333                    
                f_loca_z = 0                    
                
                g_loca_x = 0                    
                g_loca_y = 0                   
                g_loca_z = -6.25333                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -6.25333   


            if instance_props.tp_geom_result == "128px":   

                a_loca_x = 0                                
                a_loca_y = 0                 
                a_loca_z = -12.5                      
                
                b_loca_x = 0                    
                b_loca_y = -12.5                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 12.5                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 12.5                     
                              
                e_loca_x = 0                   
                e_loca_y = 12.5                     
                e_loca_z = 0                     
                
                f_loca_x = 0                    
                f_loca_y = 12.5                   
                f_loca_z = 0                    
                
                g_loca_x = 0                   
                g_loca_y = 0                  
                g_loca_z = -12.5                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -12.5   


            if instance_props.tp_geom_result == "256px":   

                a_loca_x = 0                                
                a_loca_y = 0                   
                a_loca_z = -25                    
                
                b_loca_x = 0                   
                b_loca_y = -25                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 25                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 25                     
                              
                e_loca_x = 0                   
                e_loca_y = 25                     
                e_loca_z = 0                     
                
                f_loca_x = 0                    
                f_loca_y = 25                  
                f_loca_z = 0                    
                
                g_loca_x = 0                 
                g_loca_y = 0                  
                g_loca_z = -25                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -25   


            if instance_props.tp_geom_result == "512px":   

                a_loca_x = 0                               
                a_loca_y = 0                   
                a_loca_z = -50                    
                
                b_loca_x = 0                  
                b_loca_y = -50                     
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 50                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 50                     
                              
                e_loca_x = 0                   
                e_loca_y = 50                     
                e_loca_z = 0                     
                
                f_loca_x = 0                    
                f_loca_y = 50                  
                f_loca_z = 0                    
                
                g_loca_x = 0                  
                g_loca_y = 0                  
                g_loca_z = -50                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -50   


            if instance_props.tp_geom_result == "1024px":   

                a_loca_x = 0                               
                a_loca_y = 0                  
                a_loca_z = -100                    
                
                b_loca_x = 0                  
                b_loca_y = -100                     
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 100                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 100                    
                              
                e_loca_x = 0                   
                e_loca_y = 100                     
                e_loca_z = 0                     
                
                f_loca_x = 0                    
                f_loca_y = 100                 
                f_loca_z = 0                    
                
                g_loca_x = 0                 
                g_loca_y = 0                  
                g_loca_z = -100                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -100   


            if instance_props.tp_geom_result == "2048px":   

                a_loca_x = 0                              
                a_loca_y = 0                  
                a_loca_z = -200                    
                
                b_loca_x = 0                  
                b_loca_y = -200                     
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                  
                c_loca_z = 200                     
               
                d_loca_x = 0                     
                d_loca_y = 0                   
                d_loca_z = 200                      
                              
                e_loca_x = 0                   
                e_loca_y = 200                     
                e_loca_z = 0                     
                
                f_loca_x = 0                    
                f_loca_y = 200                 
                f_loca_z = 0                    
                
                g_loca_x = 0                
                g_loca_y = 0                 
                g_loca_z = -200                    
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -200    


            if instance_props.tp_geom_result == "4096px":     

                a_loca_x = 0                               
                a_loca_y = 0                  
                a_loca_z = -400                     
                
                b_loca_x = 0                 
                b_loca_y = -400                     
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 400                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 400                     
                              
                e_loca_x = 0                   
                e_loca_y = 400                     
                e_loca_z = 0                     
                
                f_loca_x = 0                   
                f_loca_y = 400                 
                f_loca_z = 0                    
                
                g_loca_x = 0               
                g_loca_y = 0                  
                g_loca_z = -400                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -400  

  


        # INSTANCE XZ VERTICAL #
        if instance_props.tp_instance_rota == 'rota_axis_xz':  

            if instance_props.tp_geom_result == "32px":   
                
                a_loca_x = 0                  
                a_loca_y = 0                  
                a_loca_z = -3.13133                      
                
                b_loca_x = -3.13133                  
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                    
                c_loca_z = 3.13133                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 3.13133                     
                              
                e_loca_x = 3.13133                    
                e_loca_y = 0                    
                e_loca_z = 0                     
                
                f_loca_x = 3.13133                      
                f_loca_y = 0                    
                f_loca_z = 0                    
                
                g_loca_x = 0                   
                g_loca_y = 0                    
                g_loca_z = -3.13133                 
                                
                h_loca_x = 0                  
                h_loca_y = 0                    
                h_loca_z = -3.13133                   


            if instance_props.tp_geom_result == "64px":   

                a_loca_x = 0                   
                a_loca_y = 0                   
                a_loca_z = -6.25333                     
                
                b_loca_x = -6.25333                     
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                    
                c_loca_z = 6.25333                     
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 6.25333                     
                              
                e_loca_x = 6.25333                    
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 6.25333                     
                f_loca_y = 0                    
                f_loca_z = 0                    
                
                g_loca_x = 0                    
                g_loca_y = 0                   
                g_loca_z = -6.25333                    
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -6.25333    


            if instance_props.tp_geom_result == "128px":   

                a_loca_x = 0                                
                a_loca_y = 0                 
                a_loca_z = -12.5                      
                
                b_loca_x = -12.5                    
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 12.5                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 12.5                     
                              
                e_loca_x = 12.5                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 12.5                    
                f_loca_y = 0                   
                f_loca_z = 0                    
                
                g_loca_x = 0                   
                g_loca_y = 0                 
                g_loca_z = -12.5                    
                                
                h_loca_x = 0                    
                h_loca_y = 0                  
                h_loca_z = -12.5   


            if instance_props.tp_geom_result == "256px":   

                a_loca_x = 0                                
                a_loca_y = 0                   
                a_loca_z = -25                    
                
                b_loca_x = -25                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 25                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 25                     
                              
                e_loca_x = 25                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 25                    
                f_loca_y = 0                   
                f_loca_z = 0                    
                
                g_loca_x = 0                 
                g_loca_y = 0                  
                g_loca_z = -25                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -25   


            if instance_props.tp_geom_result == "512px":   

                a_loca_x = 0                               
                a_loca_y = 0                   
                a_loca_z = -50                    
                
                b_loca_x = -50                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 50                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 50                     
                              
                e_loca_x = 50                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 50                    
                f_loca_y = 0                  
                f_loca_z = 0                    
                
                g_loca_x = 0                  
                g_loca_y = 0                 
                g_loca_z = -50                    
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -50    


            if instance_props.tp_geom_result == "1024px":   

                a_loca_x = 0                               
                a_loca_y = 0                  
                a_loca_z = -100                    
                
                b_loca_x = -100                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                   
                c_loca_z = 100                    
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 100                    
                              
                e_loca_x = 100                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 100                    
                f_loca_y = 0                 
                f_loca_z = 0                    
                
                g_loca_x = 0                 
                g_loca_y = 0                 
                g_loca_z = -100                    
                                
                h_loca_x = 0                    
                h_loca_y = 0                  
                h_loca_z = -100    


            if instance_props.tp_geom_result == "2048px":   

                a_loca_x = 0                              
                a_loca_y = 0                  
                a_loca_z = -200                    
                
                b_loca_x = -200                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                  
                c_loca_z = 200                     
               
                d_loca_x = 0                     
                d_loca_y = 0                    
                d_loca_z = 200                      
                              
                e_loca_x = 200                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 200                    
                f_loca_y = 0                 
                f_loca_z = 0                    
                
                g_loca_x = 0                
                g_loca_y = 0                  
                g_loca_z = -200                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                  
                h_loca_z = -200   


            if instance_props.tp_geom_result == "4096px":     

                a_loca_x = 0                               
                a_loca_y = 0                  
                a_loca_z = -400                     
                
                b_loca_x = -400                   
                b_loca_y = 0                    
                b_loca_z = 0                    
                              
                c_loca_x = 0                    
                c_loca_y = 0                  
                c_loca_z = 400                     
               
                d_loca_x = 0                     
                d_loca_y = 0                   
                d_loca_z = 400                      
                              
                e_loca_x = 400                   
                e_loca_y = 0                     
                e_loca_z = 0                     
                
                f_loca_x = 400                    
                f_loca_y = 0                 
                f_loca_z = 0                    
                
                g_loca_x = 0               
                g_loca_y = 0                  
                g_loca_z = -400                   
                                
                h_loca_x = 0                    
                h_loca_y = 0                   
                h_loca_z = -400    


        store_main_name = bpy.context.object.name                            

        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(a_loca_x, a_loca_y, a_loca_z), "orient_type":'GLOBAL'})
        
        obj = bpy.context.view_layer.objects.active             
        store_name = obj.name                   
        bpy.data.objects[store_name].select_set(True)           
        bpy.data.objects[store_name].hide_render = True 
                          
        if instance_props.wired_instances == True:
            bpy.context.object.display_type = 'WIRE'    
    
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(b_loca_x, b_loca_y, b_loca_z), "orient_type":'GLOBAL'})
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(c_loca_x, c_loca_y, c_loca_z), "orient_type":'GLOBAL'})
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(d_loca_x, d_loca_y, d_loca_z), "orient_type":'GLOBAL'})
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(e_loca_x, e_loca_y, e_loca_z), "orient_type":'GLOBAL'})
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(f_loca_x, f_loca_y, f_loca_z), "orient_type":'GLOBAL'})
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(g_loca_x, g_loca_y, g_loca_z), "orient_type":'GLOBAL'})
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(h_loca_x, h_loca_y, h_loca_z), "orient_type":'GLOBAL'})

        # CUSTOM COLLECTION #                                                      
        if instance_props.rb_collection_name_instance != '':    
            prefix = rb_collection_name_instance                     
            for key, collections in bpy.data.collections.items():
                if key.startswith(prefix):  
                    col = bpy.data.collections[key]

        else:                                           
            prefix = "RP_Instance"                       
            for key, collections in bpy.data.collections.items():
                if key.startswith(prefix):                           
                    col = bpy.data.collections[key]  
                    
        if col:
           for obj in col.objects:
               obj.select_set(True)                   
               if instance_props.lock_instances == True: 
                   obj.hide_select=True
               else:    
                   obj.hide_select=False


        bpy.ops.object.select_all(action='DESELECT') 
       
        bpy.context.view_layer.objects.active = bpy.data.objects[store_main_name]
        bpy.data.objects[store_main_name].hide_select = False
        bpy.data.objects[store_main_name].select_set(True)  
        bpy.ops.object.select_pattern(pattern=store_main_name) 
   

        if instance_props.use_custom_name == True:
            
            if instance_props.wrap_instances == False:
                
                # INSTANCE CUSTOM NAME #                         
                bpy.context.object.name = instance_props.tp_name_prefix + instance_props.tp_name_object + instance_props.tp_name_suffix
                bpy.context.object.data.name = instance_props.tp_name_prefix + instance_props.tp_name_object + instance_props.tp_name_suffix       

                store_new_name = bpy.context.object.name   
                bpy.context.view_layer.objects.active = bpy.data.objects[store_new_name] 
                bpy.ops.object.select_pattern(pattern=store_new_name)  

            else:
                         
                # INSTANCE CUSTOM NAME #                        
                bpy.context.object.name = bpy.context.object.name + instance_props.tp_name_suffix 
                bpy.context.object.data.name = bpy.context.object.name + instance_props.tp_name_suffix      
                
                store_new_name = bpy.context.object.name   
                bpy.context.view_layer.objects.active = bpy.data.objects[store_new_name] 
                bpy.ops.object.select_pattern(pattern=store_new_name)  

        else:

            if instance_props.wrap_instances == False:
                
                # INSTANCE CUSTOM NAME #                         
                bpy.context.object.name = 'Instance_Center'
                bpy.context.object.data.name = 'Instance_Center'       

                store_new_name = bpy.context.object.name   
                bpy.context.view_layer.objects.active = bpy.data.objects[store_new_name] 
                bpy.ops.object.select_pattern(pattern=store_new_name)  

            else:

                bpy.context.object.name = bpy.context.object.name + '_Center'
                bpy.context.object.data.name = bpy.context.object.name + '_Center'      

                store_new_name = bpy.context.object.name   
                bpy.context.view_layer.objects.active = bpy.data.objects[store_new_name] 
                bpy.ops.object.select_pattern(pattern=store_new_name)  

 
        if instance_props.parent_instances == True:
            bpy.ops.object.select_grouped(type='COLLECTION')
            #bpy.ops.object.select_linked(type='LIBRARY_OBDATA')
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

        bpy.ops.wm.tool_set_by_id(name="builtin.move")        
        
        if instance_props.editmode_toggle == True:
            bpy.ops.object.editmode_toggle()            
            bpy.ops.wm.tool_set_by_id(name="builtin.move")        
           
        if instance_props.tp_geom_rota == 'rota_axis_xy':
            rotate_value = 0                     
            axis_x = True                     
            axis_y = False                     
            axis_z = False                    
            orient_axis = 'X'
                 
        if instance_props.tp_geom_rota == 'rota_axis_yz': 
            rotate_value = -1.5708                   
            axis_x = False                     
            axis_y = False                     
            axis_z = False   
            orient_axis = 'Y'

        if instance_props.tp_geom_rota == 'rota_axis_xz':  
            rotate_value = -1.5708                                    
            axis_x = True                     
            axis_y = False                     
            axis_z = False                    
            orient_axis = 'X'
        
        bpy.ops.transform.rotate(value=rotate_value, orient_axis=orient_axis, orient_type='GLOBAL', constraint_axis=(axis_x, axis_y, axis_z))

        self.report({'INFO'}, 'Added Instances!') 
        return {'FINISHED'}
 




class RTS_OT_RePattern_Instances_Merge(bpy.types.Operator):
    """select center object to merge with wrapped instances"""
    bl_idname = "rts_ot.repattern_merge_instances"
    bl_label = "Wrap Merge"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        prefs = get_prefs()
        instance_props = prefs.instance_type     
    
        store_mode = bpy.context.object.mode 
        store_name = bpy.context.object.name  

        if instance_props.rb_collection_name_exist_instance != '':            
            prefix = instance_props.rb_collection_name_exist_instance
        else:                        
            prefix = "RP_Instance"                       

        for key, collections in bpy.data.collections.items():
            if key.startswith(prefix):
                bpy.data.collections[key].hide_select = False
 
                col = bpy.data.collections.get(key)
                if col:
                    for obj in col.objects:
                       obj.select_set(True)     
                       obj.hide_select = False 

        bpy.ops.object.select_all(action='DESELECT')                 

        bpy.context.view_layer.objects.active = bpy.data.objects[store_name] 
        bpy.data.objects[store_name].select_set(True)
        
        bpy.ops.object.select_linked(type='OBDATA')

        selected = bpy.context.selected_objects
        n = len(selected) 
        if n == 1:                         
            bpy.ops.object.select_grouped(type='COLLECTION')

        bpy.ops.object.join()                        

        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_mode(type='VERT')  
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent()    
        bpy.ops.object.editmode_toggle() 
 
        bpy.context.view_layer.objects.active = bpy.data.objects[store_name] 
        bpy.data.objects[store_name].select_set(True)
                      
        bpy.context.object.name = bpy.context.object.name + '_merged'  
        bpy.context.object.data.name = bpy.context.object.name 
        bpy.ops.object.mode_set(mode=store_mode)
        
        self.report({'INFO'}, 'Merged Instances!') 
        return {'FINISHED'}



class RTS_OT_RePattern_Instances_Separate(bpy.types.Operator):
    """select center object to separate all instances"""
    bl_idname = "rts_ot.repattern_separate_instances"
    bl_label = "Wrap Separate"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
       
        store_mode = bpy.context.object.mode 
        store_name = bpy.context.object.name  

        bpy.ops.object.select_linked(type='OBDATA')
        
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True, material=False, animation=False)

        bpy.context.view_layer.objects.active = bpy.data.objects[store_name] 
        bpy.data.objects[store_name].select_set(True)  

        bpy.context.object.name = bpy.context.object.name + '_separated'  
        bpy.context.object.data.name = bpy.context.object.name
        bpy.ops.object.mode_set(mode=store_mode)
        
        self.report({'INFO'}, 'Instances separated!')
        return {'FINISHED'}



class RTS_OT_RePattern_Instances_Draw_Type(bpy.types.Operator):
    """select center object to toggle the draw type of instances"""
    bl_idname = "rts_ot.repattern_draw_type_instances"
    bl_label = "Solid / Wired"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
       
        store_mode = bpy.context.object.mode 
        store_name = bpy.context.object.name  

        if context.mode == "EDIT_MESH":            
            bpy.ops.object.editmode_toggle() 
       
        bpy.ops.object.select_linked(type='OBDATA')
     
        selected = bpy.context.selected_objects
        for obj in selected:
            bpy.context.view_layer.objects.active = obj

            if bpy.context.object.display_type == 'WIRE':        
                bpy.context.object.display_type = 'SOLID'
                self.report({'INFO'}, 'Set Solid!') 
            else:
                bpy.context.object.display_type = 'WIRE'
                self.report({'INFO'}, 'Set Wire!')
      
        bpy.context.view_layer.objects.active = bpy.data.objects[store_name] 
        bpy.data.objects[store_name].select_set(True)  
        bpy.context.object.draw_type = 'SOLID'
        bpy.ops.object.mode_set(mode=store_mode)

        return {'FINISHED'}

