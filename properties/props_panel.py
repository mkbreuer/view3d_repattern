import bpy
from bpy.props import *
from ..panels import update_panel
from ..materials import update_color

class PropsGroup_Panel(bpy.types.PropertyGroup):
  
    category: StringProperty(
        name="Tab Category", 
        description="move panel to named tab", 
        default="RePattern", 
        update=update_panel)

    switch_utils_tools : BoolProperty(name="", description="tools from addon: material utils", default=False)   
    ui_scale_y : FloatProperty(name="Scale Y",  description="scale layout space", default=1.1, min=1.0, max=1.5, precision=2)

    display_rp_title        : BoolProperty(name="Open", description="open/close expand panel", default=False)        
    display_rp_add          : BoolProperty(name="Open", description="open/close expand panel", default=False)        
    display_rp_tools        : BoolProperty(name="Open", description="open/close expand panel", default=False)                               
    display_rp_camera       : BoolProperty(name="Open", description="open/close expand panel", default=False)        
    display_rp_lights       : BoolProperty(name="Open", description="open/close expand panel", default=False)        
    display_rp_render       : BoolProperty(name="Open", description="open/close expand panel", default=False) 
    display_rp_opengl       : BoolProperty(name="Open", description="open/close expand panel", default=False) 
    display_rp_matopt       : BoolProperty(name="Open", description="open/close expand panel", default=False) 
    display_rp_matlib       : BoolProperty(name="Open", description="open/close expand panel", default=False) 
    display_rp_view         : BoolProperty(name="Open", description="open/close expand panel", default=False) 
    display_rp_world        : BoolProperty(name="Open", description="open/close expand panel", default=False) 
    display_rp_aoccl        : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_light        : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_grid         : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_wrap_name    : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_wrap_grid    : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_wrap_subgrid : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_settings     : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_bevel_reso      : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_instance     : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_clones       : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_rp_collections  : BoolProperty(name="Open", description="open/close expand panel", default=False)   
    display_settings_rp     : BoolProperty(name="Open", description="open/close expand panel", default=False)   
 
    display_settings_type_rp : EnumProperty(
      items = [("global",   "Global",  "global settings",  "", 1),
               ("display",  "Display", "object dispaly",   "", 2)],
               name = "Settings",
               default = "display",
               description="display settings type")

    typ_layout = [("L1"   ,"  1.  Grid"     ,"" ,"GRID"           ,1),
                  ("L2"   ,"  2.  Wrap"     ,"" ,"MOD_MESHDEFORM" ,2), 
                  ("L3"   ,"  3.  Edit"     ,"" ,"AUTOMERGE_ON"   ,3),
                  ("L4"   ,"  4.  Array"    ,"" ,"MOD_ARRAY"      ,4),
                  ("L5"   ,"  5.  Material" ,"" ,"MATERIAL"       ,5),
                  ("L6"   ,"  6.  Light"    ,"" ,"LIGHT"          ,6),
                  ("L7"   ,"  7.  Camera"   ,"" ,"CAMERA_DATA"    ,7),
                  ("L8"   ,"  8.  Render"   ,"" ,"RENDER_STILL"   ,8)]
    toggle_switch_ui : EnumProperty(name = " ", default = "L1", items = typ_layout) 


    toggle_primitive_ui : BoolProperty(name="UI Primitive", description="enable / disable", default=True)
    toggle_list_ui : BoolProperty(name="UI List", description="enable / disable", default=True)    
 
    layout_edit = [("L1"   ,"  1.  Edit"       ,"" ,"EDITMODE_HLT"  ,1),
                   ("L2"   ,"  2.  Materials"  ,"" ,"MATERIAL"      ,2)]
    toggle_edit_ui : EnumProperty(name = " ", default = "L1", items = layout_edit) 



def draw_props_panel(prefs, layout):
    
    layout.label(text='Panel',  icon='TOOL_SETTINGS')

    # Tools
    box = layout.box().column(align=True)
    box.separator()                                   
    
    row = box.row(align=True) 
    row.label(text="Tab Category:")             
    row.prop(prefs.panel_type, "category", text="")       
    
    box.separator() 
    
    row = box.row(align=True)  
    row.label(text="Layout Type:")                   
    row.prop(prefs.panel_type, 'toggle_list_ui', text='')            
    
    box.separator() 
    
    row = box.row(align=True)  
    row.label(text="Primitive UI:")                   
    row.prop(prefs.panel_type, 'toggle_primitive_ui', text='')         

    box.separator() 


    # row = box.row(align=True)  
    # row.label(text="Panel Layout:")                   
    # row.popover(panel="VIEW3D_PT_repattern_panel_ui", text="VIEW3D_PT_repattern_panel_ui")    
    
    # box.separator()        
    
    # row = box.row(align=True)  
    # row.label(text="SubPanel Layout:")      
    # row.popover(panel="VIEW3D_PT_repattern_color_management", text="VIEW3D_PT_repattern_color_management")    

    # box.separator() 

