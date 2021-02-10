import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_camera_ui(self, context):
    layout = self.layout.column(align=True)  
    layout.operator_context = 'INVOKE_DEFAULT'
    
    prefs = get_prefs()
    panel_prefs = prefs.panel_type
    cam_prefs = prefs.camera_type 

    scene = context.scene
    
    box = layout.box().column(align=True)
    box.separator()
    
    row = box.row(align=True) 
    row.scale_y = 1.3             
    row.label(text="Add Camera:") 
    row.operator("rts_ot.repattern_camera", text="", icon='CHECKMARK')

    box.separator()           
   
    row = box.row(align=True) 
    row.scale_y = 1.3 
    row.prop(cam_prefs, "cam_lens", text="")
    row.prop(cam_prefs, "cam_reso", text="")

    box.separator()    
    box.separator()
 
    row = box.row(align=True)
    row.scale_y = 1.3 
    row.prop_search(data = context.scene, property = 'collection_rp_select_list_cameras', search_data = bpy.data, search_property = 'cameras',  text="")
    
    box.separator()    
  
    row = box.row(align=True)                
    row.scale_y = 1.3 
    row.label(text="Select List Camera:") 
    row.operator("rts_ot.repattern_camera_jump", text="", icon='VIS_SEL_11') 

    box.separator()

    row = box.row(align=True)                
    row.label(text="Remove List Camera:") 
    row.operator("rts_ot.repattern_camera_remove", text="", icon='PANEL_CLOSE')

    box.separator()
    box.separator()    
  
    obj = context.active_object
    if obj:
        if obj.type in {'CAMERA'}:   
            
            row = box.row(align=True)            
            if panel_prefs.display_rp_camera:   
                icon_camset="DISCLOSURE_TRI_DOWN"               
            else:
                icon_camset="DISCLOSURE_TRI_RIGHT"  
            row.prop(panel_prefs, "display_rp_camera", text="Camera Propertys", icon=icon_camset, emboss=False)              
            
            #row.operator("view3d.view_camera", text="Jump to CamView")
            
            if bpy.context.space_data.lock_camera == False:
                row.prop(context.space_data, "lock_camera", text="", icon = "UNLOCKED", emboss=False)                         
            else:
                row.prop(context.space_data, "lock_camera", text="", icon = "LOCKED", emboss=False)  

            if panel_prefs.display_rp_camera: 
                
                box.separator()    
               
                row = box.row(align=True)  
                row.prop(context.object.data, "shift_x", text="X")
                row.prop(context.object.data, "shift_y", text="Y")
              
                if bpy.context.object.data.type =='ORTHO':
                
                    box.separator()
                    
                    row = box.row(align=True)  
                    row.prop(context.object.data, "ortho_scale", text='Ortho Scale')
                    
                    sub = row.row(align=True)
                    sub.scale_x = 0.5
                    sub.prop(context.object.data, "type", text='', icon = "VIEW_PERSPECTIVE")
               
                elif bpy.context.object.data.type == 'PERSP':
                   
                    box.separator()
                    
                    row = box.row(align=True)                     
                    row.prop(context.object.data, "lens", text='Focal Lenght')
                    sub = row.row(align=True)
                    sub.scale_x = 0.5
                    sub.prop(context.object.data, "type", text='', icon = "VIEW_PERSPECTIVE")
               
                else:            
                    box.separator()
                    
                    row = box.row(align=True)                     
                    row.prop(context.object.data, "lens", text='Focal Lenght')
                    sub = row.row(align=True)
                    sub.scale_x = 0.5
                    sub.prop(context.object.data, "type", text='', icon = "VIEW_PERSPECTIVE")         
        
                box.separator()                
                box.separator()

                row = box.column_flow(columns=2, align=False)      
                row.prop(context.object.data, "show_guide", text="Composition guides")           
                row.prop(context.object.data, "show_limits", text="Limits")
                row.prop(context.object.data, "show_mist", text="Mist")
                row.prop(context.object.data, "show_sensor", text="Sensor")
                row.prop(context.object.data, "show_name", text="Name")      
                row.prop(context.object.data, "show_passepartout", text="Passepartout")                          
                row.prop(context.object.data, "passepartout_alpha", text="Alpha", slider=True)

                box.separator()     
                box.separator()     

                row = box.column(align=True)  
                row.prop(context.object.data, "clip_start", text="ClipStart")
                row.prop(context.object.data, "clip_end", text="ClipEnd")

                box.separator()     
                box.separator()    

           
            box.separator()     
            box = layout.box().column(align=True)
            box.separator()
        
            cam = context.object.data                       
            use_multiview = context.scene.render.use_multiview
          
            row = box.row(align=True)
            row.use_property_split = True
            row.use_property_decorate = False
            if cam.show_background_images == True: 
                ico_cam='CHECKBOX_HLT'           
            else:         
                ico_cam='CHECKBOX_DEHLT'                      
            row.prop(cam, "show_background_images", text="", icon=ico_cam)            
            row.operator("view3d.background_image_add", text="Add Background Images")
            
            box.separator()
           
            if cam.show_background_images == True:           

                for i, bg in enumerate(cam.background_images):
                    layout.active = cam.show_background_images
                                                  
                    row = box.row(align=True)
                    row.prop(bg, "show_expanded", text="", emboss=False)
                 
                    if bg.source == 'IMAGE' and bg.image:
                        row.prop(bg.image, "name", text="", emboss=False)
                  
                    elif bg.source == 'MOVIE_CLIP' and bg.clip:
                        row.prop(bg.clip, "name", text="", emboss=False)
                  
                    elif bg.source and bg.use_camera_clip:
                        row.label(text="Active Clip")
                 
                    else:
                        row.label(text="Not Set")

                    row.prop(bg,"show_background_image", text="",emboss=False,icon='RESTRICT_VIEW_OFF' if bg.show_background_image else 'RESTRICT_VIEW_ON',)
                    row.operator("view3d.background_image_remove", text="", emboss=False, icon='X').index = i

                    box.separator()
                 
                    if bg.show_expanded:
                        row = box.row()
                        row.prop(bg, "source", expand=True)
                      
                        box.separator()
                      
                        has_bg = False
                        if bg.source == 'IMAGE':
                            row = box.row()
                            row.template_ID(bg, "image", open="image.open")
                        
                            box.separator()

                            if bg.image is not None:
                                box.template_image(bg, "image", bg.image_user, compact=True)
                                has_bg = True

                                if use_multiview:
                                    box.prop(bg.image, "use_multiview")

                                    column = box.column()
                                    column.active = bg.image.use_multiview

                                    column.label(text="Views Format:")
                                    column.row().prop(bg.image, "views_format", expand=True)

                                    sub = column.box()
                                    sub.active = bg.image.views_format == 'STEREO_3D'
                                    sub.template_image_stereo_3d(bg.image.stereo_3d_format)
                                                        
                                    box.separator()
                    
                        elif bg.source == 'MOVIE_CLIP':
                            box.prop(bg, "use_camera_clip", text="Active Clip")

                            column = box.column()
                            column.active = not bg.use_camera_clip
                            column.template_ID(bg, "clip", open="clip.open")

                            col.separator()

                            if bg.clip:
                                column.template_movieclip(bg, "clip", compact=True)

                            if bg.use_camera_clip or bg.clip:
                                has_bg = True

                            column = box.column()
                            column.active = has_bg
                            column.prop(bg.clip_user, "use_render_undistorted")
                            column.prop(bg.clip_user, "proxy_render_size")
                            
                            box.separator()


                        if has_bg:
                            col = box.column()
                            col.prop(bg, "alpha", slider=True)
                            col.separator()                      
                            col.row().prop(bg, "display_depth", expand=True)                     
                            col.separator()
                            col.row().prop(bg, "frame_method", expand=True)
                         
                            box.separator()
                       
                            row = box.row(align=True)                        
                            row.label(text="Offset")  
                            row.prop(bg, "offset", text="")

                            box.separator()
                            
                            row = box.row(align=True)                        
                            row.label(text="Rotation")                            
                            row.prop(bg, "rotation", text="")

                            box.separator()
                  
                            row = box.row(align=True)                         
                            row.label(text="Scale")    
                            row.prop(bg, "scale", text="")
                          
                            box.separator()
                         
                            col = box.column()                    
                            col.prop(bg, "use_flip_x")
                            col.prop(bg, "use_flip_y")

                            box.separator()
