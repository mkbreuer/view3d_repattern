import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_edit_curve_ui(self, context):
    layout = self.layout.column(align=True)  

    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    curve_prefs = prefs.curve_type 

    ob = context.object  
    obj = context.object

    col = layout.column(align=True)

    if panel_prefs.editcurve_layout == "tp_c0": 

        row = box.row(align=True)      
        row.prop(context.object.data, "dimensions", expand=True)
        
        box.separator()  
        
        row = box.row(align=True)      
        row.prop(context.object.data, "fill_mode", text="")           
        
        show = bpy.context.object.data.dimensions
        if show == '3D':
                
            active_bevel = bpy.context.object.data.bevel_depth            
            if active_bevel == 0.0:              
                row.operator("rts_ot.toggle_curve_bevel", text="Bevel on", icon='MOD_WARP')
            else:   
                row.operator("rts_ot.toggle_curve_bevel", text="Bevel off", icon='MOD_WARP')                 
        
        else:                                      
            row.operator("rts_ot.curve_extrude_2d", text="Extrude", icon='EMPTY_SINGLE_ARROW')                                                                 
        
        box.separator()                    
        row = box.row(align=True)                          
        row.prop(context.object.data, "use_fill_deform")

        box.separator()  
        box.separator()  
        
        row = box.row(align=True) 
        row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
        #row.prop(context.scene.curvetools, "curve_vertcolor", text="")                             
                    
        row = box.row(align=True)
        row.prop(context.object.data, "resolution_u", text="Rings")          
        row.prop(context.object.data, "bevel_resolution", text="Loops")

        row = box.row(align=True)
        row.prop(context.object.data, "offset")
        row.prop(context.object.data, "extrude", text="Height")

        box.separator()
        box.separator()

        row = box.row(align=True) 
        if panel_prefs.display_bevel_reso == True:                                 
            icon_reso=('DISCLOSURE_TRI_DOWN')                 
        else:                 
            icon_reso=('DISCLOSURE_TRI_RIGHT') 
        row.prop(panel_prefs, "display_bevel_reso", text="Loop Resolution", icon=icon_reso)        
                                
        if panel_prefs.display_bevel_reso:                                                  
            box.separator()
            
            row = box.column_flow(columns=2, align=False)
            row.label(text="Rings", icon = "ALIGN_JUSTIFY")  
            row.label(text="1 = 4",) 
            row.label(text="2 = 8") 
            row.label(text="4 = 16") 
            row.label(text="8 = 32")
            row.label(text="(+4) Full Circle")          

            row.label(text="Loops", icon = "ALIGN_JUSTIFY")  
            row.label(text="0 = 4",) 
            row.label(text="2 = 8") 
            row.label(text="4 = 12") 
            row.label(text="8 = 16")           
            row.label(text="(+2) Along Curve")                                 

        box.separator() 
        

    if panel_prefs.editcurve_layout == "tp_c1": 

        box = col.box().column(align=True)
        
        row = box.row(align=True)  
        row.prop(panel_prefs, "display_curve_select", text="", icon="TRIA_DOWN", emboss = False)            
        row.label(text="Curve Select")    

        box.separator()   
        box.separator()  

        row = box.row(align=True)                 
        sub = row.row()
        sub.scale_x = 0.3
        sub.operator("curve.select_more",text="+")
        sub.operator("curve.select_all",text="All").action = 'TOGGLE'  
        sub.operator("curve.select_less",text="-")   

        box.separator()

        row = box.row(align=True) 
        row.operator("curve.select_all", text="Inverse").action = 'INVERT'
        row.menu("VIEW3D_MT_edit_curve_showhide") 

        row = box.row(align=True) 
        row.operator("curve.select_random", text="Random") 
        row.operator("curve.select_similar", text="Similar") 

        row = box.row(align=True)
        row.operator("curve.select_linked", text="Linked")             
        row.operator("curve.select_nth", text="Checker")
        
        box.separator()
         
        row = box.row(align=True) 
        row.operator("curve.de_select_first", text="First")
        row.operator("curve.de_select_last", text="Last")
        
        row = box.row(align=True)             
        row.operator("curve.select_next", text="Next")
        row.operator("curve.select_previous", text="Previous")

        box.separator() 


    if panel_prefs.editcurve_layout == "tp_c2": 
                      
         box = col.box().column(align=True)

         row = box.row(align=True)
         row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
         row.prop(context.object.data, "resolution_u", text="Resolution")
         row.operator("rts_ot.wire_all", text="", icon='WIRE') 

         box.separator()  
         box.separator()  

         row = box.row(align=True) 
         row.operator("curve.bezier_length","Lenght")                                
         row.operator("curve.surfsk_first_points", text="Set First")                   

         row = box.row(align=True) 
         row.operator("curve.cyclic_toggle","Cyclic")  
         row.operator("curve.switch_direction", text="Direction")                   
 
         box.separator()   
         box.separator() 

         row = box.row(align=True)
         row.label(text="Subdivide")      
         row.operator("curve.bezier_subdivide","3xBezièr")                  
         
         row = box.row(align=True) 
         row.operator("curve.subdivide", text="1").number_cuts=1        
         row.operator("curve.subdivide", text="2").number_cuts=2
         row.operator("curve.subdivide", text="3").number_cuts=3
         row.operator("curve.subdivide", text="4").number_cuts=4
         row.operator("curve.subdivide", text="5").number_cuts=5        
         row.operator("curve.subdivide", text="6").number_cuts=6  

         box.separator()  
         box.separator()             
          

         row = box.row(align=True)
         row.operator("curve.extrude_move", text="Extrude")                                             
         row.operator("curve.remove_doubles", text="RemDoubles") 
  
         row = box.row(align=True)     
         row.operator("curve.make_segment",  text="Weld") 
         row.operator("curve.bezier_merge_ends","MergeEnd")  

         box.separator() 

         row = box.row(align=True)               
         row.operator("curve.trim_tool", text="Trim")  
         row.operator("curve.bezier_intersection","Intersect")                   

         row = box.row(align=True) 
         row.operator("curve.separate",  text="Separate") 
         row.operator("curve.split",  text="Split")     

         box.separator() 

         row = box.row(align=True)  
         row.operator("curve.smooth", text="Smooth") 
         row.operator("curve.bezier_circle","Circle")  
        
         row = box.row(align=True)   
         row.operator("curve.bezier_offset","Offset") 
         row.operator("object.curve_outline", text = "Outline") 

         box.separator() 

         row = box.row(align=True) 
         row.operator("curve.radius_set", "Radius")  
         row.operator("transform.tilt", text="Tilt")  
    
         row = box.row(align=True)                                    
         row.operator("transform.vertex_random", text="Random") 
         row.operator("curve.tilt_clear", "Clear Tilt")                 


         box.separator() 

         row = box.row(align=True) 
        
         vertex = []
         selected = []
         n = 0
         obj = context.active_object
         if obj != None:
             if obj.type == 'CURVE':
                 for i in obj.data.splines:
                     for j in i.bezier_points:
                         n += 1
                         if j.select_control_point:
                             selected.append(n)
                             vertex.append(obj.matrix_world * j.co)



             if len(vertex) == 1 and n > 0:
              
                data = context.active_object.data
                points = data.splines.active.bezier_points

                selected_points = [idx for idx, p in enumerate(points) if p.select_control_point]
                
                if len(selected_points) > 0:
                    idx = selected_points[0]
                    point = points[idx]

                    box.separator() 

                    row = box.row(align=True)                             
                    row.prop(point, "weight_softbody", text='weight')
                    row.operator("curve.smooth_weight", text="", icon="LAYER_USED")                            
                    
                    row = box.row(align=True) 
                    row.prop(point, "radius", text='radius')
                    row.operator("curve.smooth_radius", text="", icon="LAYER_USED")                             
                    
                    
                    row = box.row(align=True) 
                    row.prop(point, "tilt", text='tilt')
                    row.operator("curve.smooth_tilt", text="", icon="LAYER_USED") 
                 
                    box.separator()       


             if len(vertex) > 0 and n > 2:
                 simple_edit = row.operator("curve.bezier_points_fillet", text='Curve Fillet')       
                 
                 box.separator()                        
             
             
             if len(vertex) > 0 and n > 2:
                row.operator("curve.extend_tool", text="Curve Extend")
                
                box.separator()   


             if len(vertex) == 2:
                 if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':    

                     box.separator() 
                    
                     row = box.row(align=True)   
                     simple_edit = row.operator("rts_ot.quader_curve","Beveled Quarter", icon="BLANK1")   

                     box.separator()   


             if len(vertex) == 1:
                 if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':    

                     box.separator() 
                   
                     row = box.row(align=True)
                     simple_edit = row.operator("rts_ot.half_curve","Beveled Half-Circle", icon="BLANK1")               

                     box.separator()                   


             if len(vertex) > 0:

                box.separator()  

                box = col.box().column(align=True)   
             
                box.separator()                      
           
                row = box.column(align=True)
                                
                if context.object.data.splines.active.type == 'POLY':
                    row.prop(context.object.data.splines.active, "use_cyclic_u", text="U Cyclic")                        
                    row.prop(context.object.data.splines.active, "use_smooth")
                else:
                    if context.object.data.splines.active.type == 'NURBS':
                        row.prop(context.object.data.splines.active, "use_cyclic_u", text="U Cyclic")

                    if context.object.data.splines.active.type == 'NURBS':
                        row.prop(context.object.data.splines.active, "use_bezier_u", text="U Bezier")
                        row.prop(context.object.data.splines.active, "use_endpoint_u", text="U Endpoint")
                        row.prop(context.object.data.splines.active, "order_u", text="U Order")
         
                    if context.object.data.splines.active.type == 'SURFACE':
                        row.prop(context.object.data.splines.active, "use_cyclic_v", text="V Cyclic")
                        row.prop(context.object.data.splines.active, "use_bezier_v", text="V Bezier")
                        row.prop(context.object.data.splines.active, "use_endpoint_v", text="V Endpoint")
                        row.prop(context.object.data.splines.active, "order_v", text="V Order")

                    if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':

                        row.alignment = 'CENTER'
                        row.label(text="Interpolation:")
                        
                        box.separator()  
                        
                        row = box.column(align=True)                                                      
                        row.prop(context.object.data.splines.active, "tilt_interpolation", text="Tilt")
                        row.prop(context.object.data.splines.active, "radius_interpolation", text="Radius")
                    
                    box.separator()          
                    
                    row = box.column(align=True)                                     
                    row.prop(context.object.data.splines.active, "use_smooth")

                box.separator() 

             else:
                pass

    


    if panel_prefs.editcurve_layout == "tp_c3": 


        box = col.box().column(align=True)
                        
        row = box.row(align=True)      
        row.prop(context.object.data, "fill_mode", text="")           
        
        show = bpy.context.object.data.dimensions
        if show == '3D':
             
            active_bevel = bpy.context.object.data.bevel_depth            
            if active_bevel == 0.0:              
             row.operator("rts_ot.enable_bevel", text="Bevel on", icon='MOD_WARP')
            else:   
             row.operator("rts_ot.enable_bevel", text="Bevel off", icon='MOD_WARP')                 
                      
        row = box.row(align=True)                          
        row.prop(context.object.data, "use_fill_deform")

        box.separator()  
        box.separator()  
        
        row = box.row(align=True) 
        active_wire = bpy.context.object.show_wire                                                        
        if active_wire == True:
            row.operator("rts_ot.wire_off", "", icon = 'SOLID')              
        else:                       
            row.operator("rts_ot.wire_on", "", icon = 'WIRE') 
        row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')   
        
        row = box.row(align=True)
        row.prop(context.object.data, "resolution_u", text="Rings")          
        row.prop(context.object.data, "bevel_resolution", text="Loops")

        row = box.row(align=True)
        row.prop(context.object.data, "offset")
        row.prop(context.object.data, "extrude","Height")

        box.separator()
        box.separator()

        row = box.row(align=True) 
        if panel_prefs.display_bevel_reso:                                 
            row.prop(panel_prefs, "display_bevel_reso", text="Loop Resolution", icon='TRIA_DOWN_BAR')                 
        else:                 
            row.prop(panel_prefs, "display_bevel_reso", text="Loop Resolution", icon='TRIA_UP_BAR')        
                               
        if panel_prefs.display_bevel_reso:       
                               
            row = box.column_flow(2)
            row.label(text="Value Rings", icon = "PROP_CON")  
            row.label(text="1 = 4",) 
            row.label(text="2 = 8") 
            row.label(text="4 = 16") 
            row.label(text="8 = 32")
            row.label(text="(+4) Full Circle")          

            row.label(text="Value Loops", icon = "COLLAPSEMENU")  
            row.label(text="0 = 4",) 
            row.label(text="2 = 8") 
            row.label(text="4 = 12") 
            row.label(text="8 = 16")           
            row.label(text="(+2) Along Curve")                                 

        box.separator()  
        box.separator()  

        box = col.box().column(align=True)  
       
        box.separator()  
       
        row = box.row(align=True) 
        row.alignment = 'CENTER'
        row.label(text="Path / Deform / Twist:")

        box.separator() 

        row = box.row(align=True)
        row.prop(context.object.data, "use_radius")
        row.prop(context.object.data, "use_stretch")
        
        row = box.row(align=True)
        row.prop(context.object.data, "use_deform_bounds")   
        
        row = box.row(align=True)                        
        row.prop(context.object.data,"twist_mode", text="")
        row.prop(context.object.data, "twist_smooth", text="Smooth")    

        box.separator()    
    
    
    
        

