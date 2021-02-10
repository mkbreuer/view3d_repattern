import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_array_ui(self, context):
    layout = self.layout.column(align=True) 
    layout.operator_context = 'INVOKE_DEFAULT'

    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    modif_prefs = prefs.modif_type 

    col = layout.column(align=True)
    box = col.box().column(align=True)

    selobj = context.selected_objects
    if selobj:    
        obj = context.active_object
        if obj:

            box.separator()      

            row = box.row(align=True)               
            row.scale_y = 1.3
            row.prop(modif_prefs, "xy_array", text="")
            row.operator("rts_ot.repattern_modifier_arrays", text="Xy Array", icon ='MOD_ARRAY')               
            
            box.separator()
            box.separator()

            row = box.row(align=True)                                               
            row.prop(modif_prefs, "array_scale", text="")
            row.operator("rts_ot.repattern_array_scale",text="Xy Scale")    


            box.separator()
            box.separator()
       
            row = box.row(align=True)                                      
            row.prop(modif_prefs, "verts_offset", text="")
            row.operator("rts_ot.repattern_add_vertices_offset", text="Xy Offset")        

            row = box.row(align=True) 
            row.scale_y = 1.3
            row.prop(modif_prefs, "tp_verts_offset", text="")     
            row.prop(modif_prefs, "array_divide", text="")
                
            box.separator()  


            box = col.box().column(align=True) 
            box.separator() 

            row = box.row(align=True)
            if modif_prefs.display_array:            
                icon_array="DISCLOSURE_TRI_DOWN"
            else:
                icon_array="DISCLOSURE_TRI_RIGHT"
            row.prop(modif_prefs, "display_array", text="", icon=icon_array, emboss=False)

           
            row.label(text="Array")
            
            box.separator()  

            obj = context.active_object
            if obj:
                
                is_array = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'ARRAY':
                        is_array = True
                    
                if is_array == True:

                    for mod in [m for m in obj.modifiers if m.type == 'ARRAY']:         
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")          
                    
                    row.operator("rts_ot.mods_remove_array", text="" , icon='PANEL_CLOSE')                                                                                                                                                     
                    row.operator("rts_ot.mods_apply_array", text="", icon_value=get_icon_id_general("apply"))   

                    box.separator()
                    
                    row = box.row(align=True)          
                    props = row.operator("rts_ot.mods_xyz_array",  text="X")
                    props.array_x = True
                    props.array_y = False
                    props.array_z = False
                   
                    props = row.operator("rts_ot.mods_xyz_array",  text="Y")
                    props.array_x = False
                    props.array_y = True
                    props.array_z = False
                   
                    props = row.operator("rts_ot.mods_xyz_array",  text="Z")
                    props.array_x = False
                    props.array_y = False
                    props.array_z = True

                    box.separator()


                else:   
                    sub = row.row(align=True)
                    sub.scale_x = 0.5                 
                    props = sub.operator("rts_ot.mods_xyz_array",  text="X")
                    props.array_x = True
                    props.array_y = False
                    props.array_z = False
                   
                    props = sub.operator("rts_ot.mods_xyz_array",  text="Y")
                    props.array_x = False
                    props.array_y = True
                    props.array_z = False
                   
                    props = sub.operator("rts_ot.mods_xyz_array",  text="Z")
                    props.array_x = False
                    props.array_y = False
                    props.array_z = True

            else:
                row = box.row(align=True)                            
                row.label(text="> nothing selected!", icon ='INFO')  

           
            if modif_prefs.display_array: 
          
                obj = context.active_object
                if obj:
         
                    mo_types = []
                    append = mo_types.append

                    for mo in obj.modifiers:
                        if mo.type == 'ARRAY':
                            if mo.fit_type == 'FIXED_COUNT':
                                append(mo.type)

                                box.separator() 
                                
                                split = box.split()

                                row = box.row(align=True)
                                row.label(text=mo.name)  
                                row.prop(mo, "count")
                                
                                box.separator() 
                                
                                row = box.row(align=True)  
                                row.prop(mo, "relative_offset_displace", text="")
                                
                                row = box.row(align=True) 
                                row.prop(mo, "start_cap", text="")
                                row.prop(mo, "end_cap", text="")  
                                                     
                                box.separator() 

                                row = box.row(align=True)
                                row.prop(mod, "use_merge_vertices", text="Merge")
                                row.prop(mod, "use_merge_vertices_cap", text="First Last")
                                
                                row = box.row(align=True)
                                row.prop(mod, "merge_threshold", text="Distance")
                                row.prop(mod, "offset_object", text="")   
                                
                                box.separator()                                
                                box.separator()



            else:
                obj = context.active_object
                if obj:
         
                    mo_types = []
                    append = mo_types.append

                    for mo in obj.modifiers:
                        if mo.type == 'ARRAY':
                            if mo.fit_type == 'FIXED_COUNT':
                                append(mo.type)

                                split = box.split()

                                row = box.row(align=True)
                                row.label(text=mo.name)  
                                row.prop(mo, "count")

                                box.separator() 
         


        else:     
            box.separator() 

            row = box.row(align=True) 
            row.label(text="! No Selection !") 
           
            box.separator() 
    
    else:        
        box.separator() 

        row = box.row(align=True) 
        row.label(text="! No Selection !") 
       
        box.separator() 

