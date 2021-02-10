import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general
  

def draw_display(self, context):       
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_REGION_WIN'   
    
    prefs = get_prefs()
    addon_prefs = prefs.panel_type
    global_props = prefs.panel_type 

    layout.scale_y = addon_prefs.ui_scale_y

    view_layer = bpy.context.view_layer
    selected = bpy.context.selected_objects         

    box = layout.box().column(align=True) 
    box.separator()

    row = box.row(align=True)                                                 
    row.operator('rts_ot.reset_view', text="Reset 3D View")

    box.separator()
    box = layout.box().column(align=True)         
    box.separator()    

    obj = context.object       
    if obj:
        obj_type = obj.type
        if obj_type:         
            is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
            is_wire = (obj_type in {'CAMERA', 'EMPTY'})
            is_empty_image = (obj_type == 'EMPTY' and obj.empty_display_type == 'IMAGE')
            is_dupli = (obj.instance_type != 'NONE')
            is_gpencil = (obj_type == 'GPENCIL')
    
            row = box.row(align=True)                                           
            row.label(text='Name', icon='DOT') 
            row.prop(obj, "show_name", text="")
            
            box.separator() 
            
            row = box.row(align=True)                                           
            row.label(text='Axis', icon='DOT')        
            row.prop(obj, "show_axis", text="")
            
            box.separator()  

            if is_geometry or is_dupli:
                row = box.row(align=True)                                           
                row.label(text='Wireframe', icon='DOT') 
                row.prop(obj, "show_wire", text="")
            
                box.separator()         
          
            if bpy.context.object.show_wire == True:
                if obj_type == 'MESH' or is_dupli:
                    row = box.row(align=True)                                           
                    row.label(text='All Edges', icon='DOT') 
                    row.prop(obj, "show_all_edges", text="")
                
                    box.separator()  

            if is_geometry:
                row = box.row(align=True)                                           
                row.label(text='Texture Space', icon='DOT') 
                row.prop(obj, "show_texture_space", text="")
            
                box.separator() 
                         
                row = box.row(align=True)                                           
                row.label(text='Shadow', icon='DOT') 
                row.prop(obj.display, "show_shadows", text="")
            
                box.separator() 
            

            box = layout.box().column(align=True) 
            box.separator()  
         
            row = box.row(align=True)                                           
            row.label(text='In Front', icon='DOT') 
            row.prop(obj, "show_in_front", text="")
            
            box.separator() 
                       
            row = box.row(align=True)                                           
            row.label(text='Wire Overlay', icon='DOT') 
            row.prop(context.space_data.overlay, "show_wireframes", text="")
            
            box.separator() 

            row = box.row(align=True)                                           
            row.label(text='Face Orientation', icon='DOT') 
            row.prop(context.space_data.overlay, "show_face_orientation", text="")  

            box.separator()              

            row = box.row(align=True)                                           
            row.label(text='Backface Culling', icon='DOT') 
            row.prop(context.space_data.shading, "show_backface_culling", text="")
            
            box.separator() 
          
            row = box.row(align=True)                                           
            row.label(text='Display As', icon='DOT') 
            sub = row.row(align=True)
            sub.scale_x = 0.86      
            sub.prop(obj, "display_type", text="")
            
            box.separator()  

    else:
        row = box.row(align=True)                                           
        row.label(text='Object Display!', icon='INFO')   

        row = box.row(align=True)                                           
        row.label(text='No Selection!', icon='ERROR')             

        box.separator()   

