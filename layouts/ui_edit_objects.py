import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_edit_objects_ui(self, context):
    layout = self.layout.column(align=True)   
   
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    cutout_prefs = prefs.cutout_type  
    clean_prefs = prefs.clean_type  

    box = layout.box().column(align=True) 

    selobj = context.selected_objects
    if selobj:    
        obj = context.active_object
        if obj:

            box.separator()  
            
            obj_type = obj.type

            if obj.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:  

                if context.mode == "OBJECT":
                                   
                    box.separator()                 
                
                    row = box.column(align=True)  
                    row.scale_y = 1.3  
                    row.operator("object.join", text="Join Objects", icon = "AUTOMERGE_ON")     

                    box.separator() 
              
                    row = box.column(align=True)  
                    row.scale_y = 1.3 
                    row.operator("rts_ot.repattern_merge_instances", text="Wrap-Merge", icon = "FULLSCREEN_EXIT")   
                    row.operator("rts_ot.repattern_separate_instances", text="Wrap-Unlink", icon = "FULLSCREEN_ENTER")   

                    box.separator()                 
                    box.separator()  
                

                    row = box.row(align=True)                
                    row.prop(cutout_prefs, "cutout_edit", text="", icon="EDITMODE_HLT")
                    row.prop(cutout_prefs, "cutout_reso", text="")
                    row.operator("rts_ot.repattern_cutout_center")

                    if cutout_prefs.cutout_reso == 'custom':
                             
                        box.separator()

                        row = box.row(align=True)
                        row.scale_y = 1.3                             
                        row.prop(cutout_prefs, "custom_cutout")     

                    box.separator()                

                    row = box.row(align=True) 
                    row.prop(clean_prefs, "cleanup_edit", text="", icon = "EDITMODE_HLT")
                    row.prop(clean_prefs, "cleanup_reso", text="")
                    row.operator("rts_ot.repattern_cleanup_pattern", text="CleanUp")

                    if clean_prefs.cleanup_reso == 'custom':
                             
                        box.separator()

                        row = box.row(align=True)
                        row.scale_y = 1.3         
                        row.prop(clean_prefs, "custom_cleanup")     


                    box.separator()                
                    box.separator()                
                    
                    row = box.row(align=True)
                    row.scale_y = 1.3                      
                    row.operator_context = 'INVOKE_AREA'
                    row.operator("outliner.orphans_purge", text="Orphans Purge", icon = "TRASH") 

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





