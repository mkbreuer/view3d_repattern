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
        sub.prop(grid_prefs, "grid_unit_mtc", text="")

        box.separator()

        if grid_prefs.grid_unit_mtc == 'custom':               

            row = box.row(align=True)        
            row.label(text="Custom", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6   
            sub.prop(grid_prefs, "custom_grid", text="") 
                  
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
        row.label(text="Y SubDiv", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.6 
        sub.prop(grid_prefs, "subgrid_y", text="")
        
        box.separator()

        row = box.row(align=True) 
        row.label(text="X SubDiv", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.6 
        sub.prop(grid_prefs, "subgrid_x", text="")

        box.separator()  

        row = box.row(align=True) 
        row.label(text="SubGrid Result", icon="DOT")
        sub = row.row(align=True)
        sub.scale_x = 0.6     
        sub.prop(grid_prefs, "grid_unit_mtc_sub", text="")

        box.separator()

        if grid_prefs.grid_unit_mtc_sub == 'custom':
            row = box.row(align=True)                       
            row.label(text="Custom Value", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6   
            sub.prop(grid_prefs, "custom_subgrid", text="")  
        else:
            row = box.row(align=True) 
            row.label(text="Metrics Units", icon="DOT")
            sub = row.row(align=True)
            sub.scale_x = 0.6      
            sub.label(text="1bu = 1m")

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
        row.label(text="Axis", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.75    
        sub.prop(context.space_data.overlay, "show_axis_x", text="X", toggle=True)
        sub.prop(context.space_data.overlay, "show_axis_y", text="Y", toggle=True)
        sub.prop(context.space_data.overlay, "show_axis_z", text="Z", toggle=True)

        box.separator() 
       
        row = box.row(align=True)                 
        row.label(text="Lines", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.75    
        sub.prop(context.space_data.overlay, "grid_lines", text="")
        
        box.separator() 

        row = box.row(align=True)                 
        row.label(text="Scale", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.75            
        sub.prop(context.space_data.overlay, "grid_scale", text="")
        
        box.separator() 

        row = box.row(align=True)                 
        row.label(text="Subdivisions", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.75            
        sub.prop(context.space_data.overlay, "grid_subdivisions", text="")
        
        box.separator()       



    # SCENE UNITS #
    layout = self.layout.column(align=True) 

    box = layout.box().column(align=True)       
    box.separator()
    
    row = box.row(align=True)
    if panel_prefs.display_rp_wrap_units:            
        icon_units="DISCLOSURE_TRI_DOWN"
    else:
        icon_units="DISCLOSURE_TRI_RIGHT"        
    row.prop(panel_prefs, "display_rp_wrap_units", text="", icon=icon_units, emboss=False) 
    row.label(text="Scene Units")   
    row.operator("rts_ot.units_metric", text="", icon="CHECKMARK")     
    
    box.separator()  
 
    if panel_prefs.display_rp_wrap_units:

        box = layout.box().column(align=True)
        box.separator() 

        row = box.row(align=True)
        row.label(text="System", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.8
        sub.label(text="Metric")  

        box.separator() 

        row = box.row(align=True)
        row.label(text="Measures", icon="DOT") 
        sub = row.row(align=True)
        sub.scale_x = 0.8 
        sub.label(text="1bu = 1m") 
        
        box.separator()   
        # box = layout.box().column(align=True)
        # box.separator() 

        # row = box.row(align=True)
        # row.label(text="Unit System", icon="DOT") 
        # sub = row.row(align=True)
        # sub.scale_x = 0.8 
        # sub.prop(bpy.context.scene.unit_settings, "system", text="")    

        # box.separator()  

        # # row = box.row(align=True)
        # # row.label(text="Unit Scale", icon="DOT") 
        # # sub = row.row(align=True)
        # # sub.scale_x = 0.8 
        # # sub.enabled = bpy.context.scene.unit_settings.system != 'NONE'
        # # sub.prop(bpy.context.scene.unit_settings, "scale_length", text="")    

        # # box.separator()

        # # row = box.row(align=True)
        # # row.label(text="Unit Lenght", icon="DOT") 
        # # sub = row.row(align=True)
        # # sub.scale_x = 0.8
        # # sub.enabled = bpy.context.scene.unit_settings.system != 'NONE' 
        # # sub.prop(bpy.context.scene.unit_settings, "length_unit", text="")    

        # # box.separator()   
        # # box = layout.box().column(align=True)
        # # box.separator() 

        # # row = box.row(align=True)
        # # row.label(text="Save User Preferences", icon="DOT") 
        # # sub = row.row(align=True)
        # # #sub.scale_x = 0.8
        # # sub.operator_context = 'EXEC_AREA'
        # # sub.operator("wm.save_userpref", text="", icon="TOOL_SETTINGS")    

        # # box.separator()    

 