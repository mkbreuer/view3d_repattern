import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general

from ..utilities.units import get_current_units

def draw_instance_ui(self, context):
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_REGION_WIN'
    layout.operator_context = 'INVOKE_AREA'

    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    instance_prefs = prefs.instance_type 
    clone_prefs = prefs.clone_type 

    col = layout.column(align=True)
    box = col.box().column(align=True)       
    box.separator()

    row = box.row(align=True) 
    row.scale_y = 1.5        
   
    if instance_prefs.wrap_instances == True:   
        obj = context.active_object
        if obj:
            text_id = 'Wrap Selected Around'      
        else:
            text_id = 'Nothing Selected!'      
    else:
        text_id = 'Add Wrap Instances'           

    if panel_prefs.display_rp_wrap_name:            
        row.prop(panel_prefs, "display_rp_wrap_name", text="", icon="OUTLINER_OB_FONT")
    else:
        row.prop(panel_prefs, "display_rp_wrap_name", text="", icon="FONT_DATA") 
      
    if instance_prefs.wrap_instances == True: 
        obj = context.active_object
        if obj:
            row.operator("rts_ot.repattern_instances_fields", text=text_id)
        else:
            row.label(text='Nothing Selected!')
    else:
        row.operator("rts_ot.repattern_instances_fields", text=text_id)


    row.prop(instance_prefs, "wrap_instances", text="", icon = "FILE_REFRESH")  


    if panel_prefs.display_rp_wrap_name: 

        box.separator() 
        box.separator()   

        row = box.row(align=True) 
        row.prop(instance_prefs, "use_custom_name", text='')
        row.label(text='ReName: Instance Center')

        box.separator()   
      
        row = box.column(align=True)         
        row.prop(instance_prefs, "tp_name_prefix", text="prefix")
        row.prop(instance_prefs, "tp_name_object", text="name")
        row.prop(instance_prefs, "tp_name_suffix", text="suffix")

        box.separator()   
        box.separator()   
        box.separator()   

        row = box.row(align=True) 
        row.prop(instance_prefs, "use_custom_wrap", text='')
        row.label(text='ReName: Wrap Around')

        box.separator()   
       
        row = box.column(align=True)         
        row.prop(instance_prefs, "tp_wrap_prefix", text="prefix")
        row.prop(instance_prefs, "tp_wrap_object", text="name")
        row.prop(instance_prefs, "tp_wrap_suffix", text="suffix")

        box.separator()  
        box.separator()  
        box.separator()     
       
        row = box.row(align=True) 
        row.prop(instance_prefs, "use_custom_group", text='')
        row.label(text='ReName: Instance Group')

        box.separator()   

        row = box.column(align=True)           
        row.prop(instance_prefs, "tp_group_prefix", text="prefix")
        row.prop(instance_prefs, "tp_group_name", text="group")
        row.prop(instance_prefs, "tp_group_suffix", text="suffix")

        box.separator()   
        box.separator()   

    else:   

        if instance_prefs.wrap_instances == True:
            pass

        else:    

            box.separator() 
            box.separator()   

            row = box.row(align=True) 
            row.label(text="Object Type:")               
            row.prop(instance_prefs, "typ_geometry", text="")

            box.separator()   

            row = box.row(align=True) 
            row.label(text="Mesh Type:")               
            row.prop(instance_prefs, "typ_mesh", text="")

            box.separator() 


            if instance_prefs.typ_geometry == "typ_grid": 

                row = box.row(align=True) 
                row.label(text="Subdivide:") 
                
                sub0 = row.column(align=True)
                sub0.scale_x = 1
                sub0.prop(instance_prefs, "bounds_grid_subdivX")
                sub0.prop(instance_prefs, "bounds_grid_subdivY")   


            if instance_prefs.typ_geometry == "typ_cube": #default

                # row = box.row(align=True) 
                # row.label(text="Mesh Size:") 
                # sub1 = row.row(align=True)
                # sub1.scale_x = 0.7
                # sub1.prop(instance_prefs, 'bounds_cube_radius', text='') 
                # unitinfo = get_current_units()      
                # sub1.label(text=unitinfo[0])

                # box.separator()     

                row = box.row(align=True) 
                row.label(text="Subdivide:") 
                row.prop(instance_prefs, "mesh_subdiv")

                box.separator()           
              
                row = box.row(align=True)        
                row.label(text="Smooth:")      
                row.prop(instance_prefs, "mesh_subdiv_smooth")
      

            if instance_prefs.typ_geometry == "typ_cylinder": 

                row = box.row(align=True) 
                row.label(text="Fill Type:") 
                row.prop(instance_prefs, "end_fill_type", text="")

                box.separator()                 
             
                row = box.row(align=True) 
                row.label(text="Vertices:") 
                row.prop(instance_prefs, "bounds_cylinder_amount", text='')


            if instance_prefs.typ_geometry == "typ_cone": 

                row = box.row(align=True) 
                row.label(text="Fill Type:") 
                row.prop(instance_prefs, "end_fill_type", text='')

                box.separator()                 
                
                row = box.row(align=True) 
                row.label(text="Vertices:") 
                row.prop(instance_prefs, "bounds_cone_amount", text='') 


            if instance_prefs.typ_geometry == "typ_circle": 

                row = box.row(align=True) 
                row.label(text="Fill Type:") 
                row.prop(instance_prefs, "end_fill_type", text='')

                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Vertices:") 
                row.prop(instance_prefs, "bounds_circle_amount", text='') 


            if instance_prefs.typ_geometry == "typ_torus": 

                row = box.row(align=True) 
                row.label(text="Major:") 
                row.prop(instance_prefs, "bounds_torus_segments_1", text='') 

                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Minor:") 
                row.prop(instance_prefs, "bounds_torus_segments_2", text='') 


            if instance_prefs.typ_geometry == "typ_sphere": 

                row = box.row(align=True) 
                row.label(text="Rings:") 
                row.prop(instance_prefs, "bounds_sphere_ring", text='') 
             
                box.separator() 
               
                row = box.row(align=True) 
                row.label(text="Segments:") 
                row.prop(instance_prefs, "bounds_sphere_segments", text='') 


            if instance_prefs.typ_geometry == "typ_ico": 

                row = box.row(align=True) 
                row.label(text="Subdivide:") 
                row.prop(instance_prefs, "bounds_ico_subdiv", text='') 


            if instance_prefs.typ_geometry == "typ_curve":
               
                row = box.row(align=True) 
                row.label(text="Curve Type:") 
                row.prop(instance_prefs, "typ_curve", text='')            
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Shape Type:") 
                row.prop(instance_prefs, "bounds_curve_type", text='') 
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Fill Mode:") 
                row.prop(instance_prefs, "bounds_curve_fill", text='') 
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Bevel:") 
                row.prop(instance_prefs, "bounds_curve_geom_depth", text='') 
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Rings:") 
                row.prop(instance_prefs, "bounds_curve_geom_rings", text='') 
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Loops:") 
                row.prop(instance_prefs, "bounds_curve_geom_loops", text='') 
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Height:") 
                row.prop(instance_prefs, "bounds_curve_geom_extrude", text='') 
               
                box.separator() 
                
                row = box.row(align=True) 
                row.label(text="Offset:") 
                row.prop(instance_prefs, "bounds_curve_geom_offset", text='') 

                             
            if instance_prefs.typ_geometry == "typ_custom": 

                row = box.row(align=True) 
                row.label(text="Custom:")

        box.separator()
        
        row = box.row(align=True) 
        row.label(text="Setttings...")   
        if panel_prefs.display_rp_instance:            
            icon_grid="SETTINGS"
        else:
            icon_grid="SETTINGS"        
        row.prop(panel_prefs, "display_rp_instance", text="", icon=icon_grid, emboss=False) 

        box.separator()  
     
        if panel_prefs.display_rp_instance: 

            row = box.row(align=True)  
            row.label(text="Size:")
            row.prop(instance_prefs, "tp_geom_result", text='')
         
            if instance_prefs.wrap_instances == False:
                box.separator()                  
              
                row = box.row(align=True)  
                row.label(text="Local:")                
                row.prop(instance_prefs, "tp_geom_rota", text='')
           
            box.separator()             
    
            row = box.row(align=True)  
            row.label(text="Axis:")           
            row.prop(instance_prefs, "tp_instance_rota", text='')

            box.separator()    
            box.separator()    

            row = box.row(align=True) 
            row.prop(instance_prefs, "lock_instances")  
            row.prop(instance_prefs, "wired_instances")  

            row = box.row(align=True) 
            row.prop(instance_prefs, "parent_instances", text='Parent')  
            row.prop(instance_prefs, "editmode_toggle", text='Editmode')  

            row = box.row(align=True) 
            row.prop(instance_prefs, "collapse_parent", text='Child Coll')  
            row.prop(instance_prefs, "collapse_toggle", text='Collapse Coll')  

            if instance_prefs.wrap_instances == False:
                row = box.row(align=True) 
                row.prop(instance_prefs, "uvmap_toggle", text='UV Map')  

            box.separator()  


        # RADIAL CLONE #

        box = layout.box().column(align=True)     
        box.separator()  
 
        row = box.row(align=True)  
        row.scale_y = 1.5   
        row.prop(clone_prefs, "make_single", text='', icon='FULLSCREEN_ENTER')  
        row.operator("rts_ot.mft_radial_clone", text="Radial Clone")            
        row.prop(clone_prefs, "object_join", text='', icon='FULLSCREEN_EXIT')
       
        box.separator()  
       
        row = box.row(align=True)  
        row.label(text="Clones:")   
        row.prop(clone_prefs, "create_clones", text='')              
     
        box.separator()  
       
        row = box.row(align=True)  
        row.label(text="Angle")            
        row.prop(clone_prefs, 'radial_clones_angle', text="")               
     
        box.separator()  

        row = box.row(align=True)  
        row.label(text="Axis:")   
        row.prop(clone_prefs, "radial_clones_axis", text='')
      
        box.separator()  
       
        row = box.row(align=True)  
        row.label(text="Type:")   
        row.prop(clone_prefs, "radial_clones_axis_type", text='')
              
        box.separator()  
        
        row = box.row(align=True) 
        row.label(text="Setttings...")   
        if panel_prefs.display_rp_clones:            
            icon_grid="SETTINGS"
        else:
            icon_grid="SETTINGS"        
        row.prop(panel_prefs, "display_rp_clones", text="", icon=icon_grid, emboss=False) 

        box.separator()  
     
        if panel_prefs.display_rp_clones: 

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
       
