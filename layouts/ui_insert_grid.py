import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_grid_ui(self, context):
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_REGION_WIN'
    layout.operator_context = 'INVOKE_AREA'

    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    grid_prefs = prefs.grid_type

    box = layout.box().column(align=True)       
    box.separator()

    row = box.row(align=True) 
    if panel_prefs.display_rp_wrap_grid:            
        icon_grid="DISCLOSURE_TRI_DOWN"
    else:
        icon_grid="DISCLOSURE_TRI_RIGHT"        
    row.prop(panel_prefs, "display_rp_wrap_grid", text="", icon=icon_grid, emboss=False) 
    row.label(text="Grid")   
    row.operator("rts_ot.repattern_reference_grid", text="", icon="CHECKMARK")

    box.separator()  
 
    if panel_prefs.display_rp_wrap_grid: 
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



    # SUBGRID #
    layout = self.layout.column(align=True)  
    box = layout.box().column(align=True)       
    box.separator()

    row = box.row(align=True) 
    if panel_prefs.display_rp_wrap_subgrid:            
        icon_subgrid="DISCLOSURE_TRI_DOWN"
    else:
        icon_subgrid="DISCLOSURE_TRI_RIGHT"    
    row.prop(panel_prefs, "display_rp_wrap_subgrid", text="", icon=icon_subgrid, emboss=False)    
    row.label(text="SubGrid") 
    row.operator("rts_ot.repattern_subgrid", text="", icon="CHECKMARK")

    box.separator()
 
    if panel_prefs.display_rp_wrap_subgrid:     
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



    # GRID FLOOR #
    layout = self.layout.column(align=True)  
    box = layout.box().column(align=True)       
    box.separator()
    
    row = box.row(align=True)              
    if panel_prefs.display_rp_grid:            
        icon_floor="DISCLOSURE_TRI_DOWN"
    else:
        icon_floor="DISCLOSURE_TRI_RIGHT"      
    row.prop(panel_prefs, "display_rp_grid", text="", icon=icon_floor, emboss=False) 
    row.label(text="Grid Floor")  
    row.prop(context.space_data.overlay, "show_floor", text="", icon ="GRID")     

    box.separator()  
 
    if panel_prefs.display_rp_grid:      
        box = layout.box().column(align=True)    
        box.separator()                        
  
        row = box.row(align=True)                 

        row.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 0.75    
        sub.prop(context.space_data.overlay, "show_axis_x", text="X", toggle=True)
        sub.prop(context.space_data.overlay, "show_axis_y", text="Y", toggle=True)
        sub.prop(context.space_data.overlay, "show_axis_z", text="Z", toggle=True)

        row.separator() 
        row.operator("rts_ot.units_metric_cm", text="Metric", icon="SCENE_DATA")

        box.separator() 
       
        row = box.column(align=True)
        row.prop(context.space_data.overlay, "grid_lines", text="Lines")
        row.prop(context.space_data.overlay, "grid_scale", text="Scale")
        row.prop(context.space_data.overlay, "grid_subdivisions", text="Subdivisions")
        
        box.separator()       

