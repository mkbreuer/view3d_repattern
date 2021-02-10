import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_property_ui(self, context):
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_DEFAULT'

    prefs = get_prefs()
    render_type = prefs.render_type   

    col = layout.column(align=True)

    selobj = context.selected_objects
    if selobj:    
        obj = context.active_object
        if obj:

            if context.mode == 'OBJECT':   
         

                obj_type = obj.type
                

                if obj.type in {'CAMERA'}:    
                    
                    box = layout.box().column(align=True)
                    box.separator() 

                    row = box.row(align=True)          
                    row.label(text="Camera", icon = "CAMERA_DATA")     

                    box.separator()
                    
                    row = box.row(align=True)
                    row.operator("view3d.viewnumpad","Jump to View", icon = "RENDER_REGION").type='CAMERA' 
                    
                    if bpy.context.space_data.lock_camera == False:
                        row.prop(context.space_data, "lock_camera", text="", icon = "UNLOCKED")                         
                    else:
                        row.prop(context.space_data, "lock_camera", text="", icon = "LOCKED")  

                    box.separator()
                    
                    row = box.column_flow(2)       
                    row.prop(context.object.data, "show_guide", text="Composition guides")           
                    row.prop(context.object.data, "show_limits", text="Limits")
                    row.prop(context.object.data, "show_mist", text="Mist")
                    row.prop(context.object.data, "show_sensor", text="Sensor")
                    row.prop(context.object.data, "show_name", text="Name")      
                    row.prop(context.object.data, "show_passepartout", text="Passepartout")                          
                    row.prop(context.object.data, "passepartout_alpha", text="Alpha", slider=True)

                    ###    
                    box.separator()     
                    box = layout.box().column(align=True)
                    box.separator()     

                    row = box.column(align=True)  
                    row.prop(context.object.data, "clip_start", text="ClipStart")
                    row.prop(context.object.data, "clip_end", text="ClipEnd")

                    box.separator()

                    row = box.column(align=True)  
                    row.prop(context.object.data, "shift_x", text="Shift X")
                    row.prop(context.object.data, "shift_y", text="Shift Y")

                    ###    
                    box.separator()     
                    box.separator()     



                if obj_type in {'LAMP'}:    

                    lamp = context.object.data
                    if lamp.type in {'POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'}:                          
                      
                        box = layout.box().column(align=True) 

                        box.separator() 
                                          
                        row = box.row(align=True)
                        row.prop(lamp, "type", expand=True)

                        row = box.row(align=True)
                        row.prop(lamp, "color", text="")
                        row.prop(lamp, "energy")

                        if lamp.type in {'POINT', 'SPOT'}:

                            row = box.row(align=True)
                            row.prop(lamp, "falloff_type", text="")
                            row.prop(lamp, "distance")

                            if lamp.falloff_type == 'LINEAR_QUADRATIC_WEIGHTED':                   
                                row = box.row(align=True)
                                row.prop(context.object.data, "linear_attenuation", slider=True, text="Linear")
                                row.prop(context.object.data, "quadratic_attenuation", slider=True, text="Quadratic")

                            row = box.row(align=True)
                            row.prop(lamp, "use_sphere")

                        if lamp.type == 'AREA':
                            row = box.row(align=True)
                            row.prop(lamp, "distance")
                            row.prop(lamp, "gamma")                   

                        ###    
                        box.separator()  
                        box.separator()  
                  
               
               
                if obj_type in {'EMPTY'}:    

                    box = layout.box().column(align=True) 

                    box.separator() 

                    obj = context.object
                  
                    row = box.row(align=True)
                    row.prop(obj, "empty_draw_type", text="Display")

                    if obj.empty_draw_type == 'IMAGE':                 

                        box.separator()                     
                     
                        row = box.row(align=True)                        
                        row.template_ID(obj, "data", open="image.open", unlink="object.unlink_data")
                        row.template_image(obj, "data", obj.image_user, compact=True)
                      
                        box.separator()                     
                     
                        row = box.row(align=True) 
                        row.prop(obj, "color", text="Transparency", index=3, slider=True)
                       
                        row = box.row(align=True)
                        row.prop(obj, "empty_image_offset", text="Offset X", index=0)
                        row.prop(obj, "empty_image_offset", text="Offset Y", index=1)

                    box.separator()                     
                 
                    row = box.row(align=True)
                    row.prop(obj, "empty_draw_size", text="Size")

                    box.separator()     
                    box.separator()     


        else:
            box = col.box().column(align=True)          
            box.separator() 

            row = box.row(align=True) 
            row.label(text="! no active selection !") 
           
            box.separator() 
    
    else:
        box = col.box().column(align=True)          
        box.separator() 

        row = box.row(align=True) 
        row.label(text="! nothing selected !") 
       
        box.separator() 


