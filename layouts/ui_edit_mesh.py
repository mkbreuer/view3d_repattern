import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_edit_mesh_ui(self, context):
    layout = self.layout.column(align=True)   
   
    prefs = get_prefs()
    panel_prefs = prefs.panel_type

    selobj = context.selected_objects
    if selobj:    
        obj = context.active_object
        if obj:

            box = layout.box().column(align=True) 
            box.separator()  
                           
            row = box.row(align=True) 
            row.label(text='Select Linked')
            row.operator("mesh.select_linked", text='', icon='DOT')
            
            box.separator() 
            
            row = box.row(align=True) 
            row.label(text='Select Flat Faces')            
            row.operator("mesh.faces_select_linked_flat", text='', icon='DOT')        
            
            box.separator()             
            box = layout.box().column(align=True) 
            box.separator()  
                           
            row = box.row(align=True) 
            row.label(text='Separate Selected')
            row.operator("mesh.separate", text='', icon='DOT').type='SELECTED'
            
            box.separator() 
            
            row = box.row(align=True) 
            row.label(text='Separate Loose Parts')            
            row.operator("mesh.separate", text='', icon='DOT').type='LOOSE'            
            
            box.separator() 
            
            row = box.row(align=True) 
            row.label(text='Separate by Materials')            
            row.operator("mesh.separate", text='', icon='DOT').type='MATERIAL'

            box.separator()             
            box = layout.box().column(align=True) 
            box.separator()  
                           
            row = box.row(align=True) 
            row.operator("rts_ot.recalculate_normals", icon='NORMALS_FACE')
            
            box.separator()                                   

       
        else:          
            box.separator() 
            row = box.row(align=True) 
            row.label(text="! Nothing Selected !")          
            box.separator() 
    
    else:       
        box.separator() 
        row = box.row(align=True) 
        row.label(text="! Nothing Selected !")      
        box.separator() 





