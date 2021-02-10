import bpy


# Layout AddonPrefs
def draw_props_info(self, layout):

    layout.label(text='Welcome!',  icon='INFO')

    # Tools
    box = layout.box().column(align=True)   
    box.separator() 

    row = box.column(align=True)       
    row.label(text="> Template")       
    row.label(text="> Template ")                     
    row.label(text="> Template")                     
                
    row.separator()             
    
    row.label(text="> Have Fun! ;)")  

    box.separator()
