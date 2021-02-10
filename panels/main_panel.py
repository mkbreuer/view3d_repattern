import bpy
import os
import addon_utils  
from .. import addon_updater_ops
from ..utilities.utils import get_path, get_prefs
from ..icons.general import get_icon_id_general

from ..layouts.ui_display            import draw_display
from ..layouts.ui_edit_curve         import draw_edit_curve_ui
from ..layouts.ui_edit_mesh          import draw_edit_mesh_ui
from ..layouts.ui_edit_objects       import draw_edit_objects_ui
from ..layouts.ui_insert_grid        import draw_grid_ui
from ..layouts.ui_insert_instance    import draw_instance_ui
from ..layouts.ui_insert_primitive   import draw_primitive_ui
from ..layouts.ui_material_panel     import draw_mat_ui
from ..layouts.ui_modifier_array     import draw_array_ui
from ..layouts.ui_render_camera      import draw_camera_ui
from ..layouts.ui_render_light       import draw_light_ui
from ..layouts.ui_render_studio      import draw_render_ui


EDIT = ["OBJECT", "SCULPT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_METABALL", "EDIT_ARMATURE", "EDIT_PARTICLE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']


class RTS_PT_RePattern_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ReTools"
    bl_idname = "RTS_PT_RePattern_Panel"
    bl_label = "RePattern"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)  
#        obj = bpy.context.view_layer.objects.active  
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:
#                return isModelingMode and context.mode in EDIT                
        return isModelingMode 

    def draw_header(self, context):
        layout = self.layout
        layout.operator("wm.url_open", text="", icon_value=get_icon_id_general("logo")).url = os.path.join(get_path(), "docs", "index.mhtml")           

    def draw(self, context):
        layout = self.layout.column(align=True)        
        layout.operator_context = 'INVOKE_REGION_WIN'       

        prefs = get_prefs()
        panel_prefs = prefs.panel_type
        mat_prefs = prefs.mat_type

        # PRIMITIVE # 
        if panel_prefs.toggle_primitive_ui == True:   
            draw_primitive_ui(self, context) 

        layout = self.layout 
        layout = self.layout.column(align=True)  
    
        # TOOLS #         
        if context.mode == "OBJECT":  
          
            # LAYOUT LIST # 
            if panel_prefs.toggle_list_ui == False:   
                box = layout.box().column(align=True)     
                box.separator()  
               
                row = box.row(align=True)          
                row.alignment = 'CENTER'         
                row.prop(panel_prefs, "toggle_switch_ui", text="")                 

                box.separator()  

            # LAYOUT BUTTONS # 
            else:   
                box = layout.box().column(align=True)     
                box.separator()  
 
                row = box.row(align=True)          
                row.scale_x = 1.5  
                row.scale_y = 1.5  
                row.alignment = 'CENTER'               
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L1', text="", icon='GRID')
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L2', text="", icon='MOD_MESHDEFORM')
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L3', text="", icon='GROUP')             
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L4', text="", icon='MOD_ARRAY')
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L5', text="", icon='MATERIAL')    
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L6', text="", icon='LIGHT')    
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L7', text="", icon='CAMERA_DATA')           
                row.prop_enum(panel_prefs, "toggle_switch_ui", 'L8', text="", icon='RENDER_STILL')   


                box.separator()  
                

            if panel_prefs.toggle_switch_ui == 'L1': 
                draw_grid_ui(self, context)                         
            
            if panel_prefs.toggle_switch_ui == 'L2':  
                draw_instance_ui(self, context) 

            if panel_prefs.toggle_switch_ui == 'L3':    
                draw_edit_objects_ui(self, context) 
         
            if panel_prefs.toggle_switch_ui == 'L4':                                        
                draw_array_ui(self, context)  

            if panel_prefs.toggle_switch_ui == 'L5':     
                draw_mat_ui(self, context) 

            if panel_prefs.toggle_switch_ui == 'L6':     
                draw_light_ui(self, context) 

            if panel_prefs.toggle_switch_ui == 'L7':        
                draw_camera_ui(self, context) 

            if panel_prefs.toggle_switch_ui == 'L8':         
                draw_render_ui(self, context) 
   

        # TOOLS #         
        if context.mode == "EDIT_MESH":
            box = layout.box().column(align=True)     
            box.separator()  

            row = box.row(align=True)          
            row.scale_x = 1.2 
            row.scale_y = 1.2  
            row.alignment = 'CENTER'     
            row.prop_enum(panel_prefs, "toggle_switch_ui", 'L3', text="", icon='EDITMODE_HLT')
            row.prop_enum(panel_prefs, "toggle_switch_ui", 'L5', text="", icon='MATERIAL')         
            
            box.separator()  

            if panel_prefs.toggle_switch_ui == 'L3':                  
                draw_edit_mesh_ui(self, context)         

            if panel_prefs.toggle_switch_ui == 'L5':                  
                draw_mat_ui(self, context)    


        if context.mode == "EDIT_CURVE":                     
            draw_edit_curve_ui(self, context)                     
            

        # GLOBAL SETTINGS #
        layout = self.layout.column(align=True)

        col = layout.row(align=True)
        col.alignment ='CENTER' 
        obj = context.object
        if obj:        
            col.prop(context.object, "show_in_front", text="", icon='ZOOM_IN')
            col.prop(context.space_data.overlay, "show_face_orientation", text="", icon='ZOOM_SELECTED')   
            col.prop(context.space_data.shading, "show_backface_culling", text="", icon='META_BALL')
            #col.prop(context.space_data.overlay, "show_wireframes", text="", icon='SHADING_WIRE')
            col.operator("rts_ot.display_set_shading", text="", icon='SHADING_RENDERED')
            col.operator("rts_ot.display_set_wire", text="", icon='SHADING_WIRE')
         
            if bpy.context.object.display_type == 'WIRE':           
                col.prop_enum(context.object, "display_type", 'SOLID', text="", icon='GHOST_DISABLED')   
            else:            
                col.prop_enum(context.object, "display_type", 'WIRE', text="", icon='GHOST_ENABLED') 

            if bpy.context.object.lock_location[0] == True or bpy.context.object.lock_location[1] == True or \
               bpy.context.object.lock_location[2] == True or bpy.context.object.lock_rotation[0] == True or \
               bpy.context.object.lock_rotation[1] == True or bpy.context.object.lock_rotation[2] == True or \
               bpy.context.object.lock_scale[0] == True or bpy.context.object.lock_scale[1] == True or \
               bpy.context.object.lock_scale[2] == True:       
                ico_lock = 'LOCKED'
            else:
                ico_lock = 'UNLOCKED'       
            col.operator("rts_ot.transform_lock", text="", icon =ico_lock)                       
            col.separator()

            if obj.type in {'CURVE'}:  
                col.operator("rts_ot.dynamic_normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')   

        else:
            col.label(text="", icon='ERROR') 

        col.separator()

        obj = context.object       
        if obj:
            obj_type = obj.type
            if obj_type: 
                     
                is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
                is_wire = (obj_type in {'CAMERA', 'EMPTY'})
                is_empty_image = (obj_type == 'EMPTY' and obj.empty_display_type == 'IMAGE')
                is_dupli = (obj.instance_type != 'NONE')
                is_gpencil = (obj_type == 'GPENCIL')

            if bpy.context.space_data.shading.color_type == 'OBJECT':                
                if is_geometry or is_dupli or is_empty_image or is_gpencil:                                       
                    sub = col.row(align=True)
                    sub.scale_x = 0.325
                    sub.prop(obj, "color", text='')               
                else:
                    pass
            else:           
                sub = col.row(align=True)                
                mat = bpy.context.object.active_material
                if mat:                
                    if mat.use_nodes:                       
                        mat_base = mat.node_tree.nodes.active
                        if mat_base:                          
                            sub.scale_x = 0.325
                            mat_base_node = mat_base.inputs[0]
                            sub.prop(mat_base_node,'default_value', text='')                           
                        else:
                            sub.scale_x = 1
                            sub.operator('rts_ot.select_bsdf_node', text="", icon='NODE')
                    else:
                        sub.scale_x = 0.325
                        sub.prop(mat, "diffuse_color", text="")  
                else:
                    sub.scale_x = 1
                    sub.operator("rts_ot.repattern_shader_custom", text="", icon='MATERIAL')
           

            if bpy.context.space_data.shading.color_type == 'OBJECT':           
                col.prop_enum(context.space_data.shading, "color_type", 'MATERIAL', text="", icon='RESTRICT_COLOR_ON')   
            else:            
                col.prop_enum(context.space_data.shading, "color_type", 'OBJECT', text="", icon='RESTRICT_COLOR_OFF')   
       
      
        col.separator()        
        col.prop(panel_prefs, "display_settings_rp", text="", icon='SETTINGS')  

        if panel_prefs.display_settings_rp == True:
            
            layout = self.layout.column(align=True)                         
            box = layout.box().column(align=True)
            box.separator()   
          
            row = box.row()           
            row.prop(panel_prefs, "display_settings_type_rp", expand=True) 
     
            box.separator()          
          
            if panel_prefs.display_settings_type_rp == 'global':
                
                box = layout.box().column(align=True)
                box.separator() 
                                             
                row = box.column(align=True)                  
                row.operator("preferences.addon_show", text="Addon Preferences", icon="TOOL_SETTINGS").module="view3d_repattern"
               
                box.separator()    

                addon_updater_ops.check_for_update_background()
                # call built-in function with draw code/checks
                addon_updater_ops.update_notice_box_ui(self, context)          
               
          
            if panel_prefs.display_settings_type_rp == 'display':
                draw_display(self, context)


