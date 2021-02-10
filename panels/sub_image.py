import bpy


class RTS_PT_Repattern_Color_Management(bpy.types.Panel):
    bl_category = "Color"
    bl_idname = "RTS_PT_Repattern_Color_Management"
    bl_label = "Color Managment"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column(align=True)
        layout.operator_context = 'INVOKE_DEFAULT'

        scene = context.scene
        view = scene.view_settings
                
        box = layout.box().column(align=True)
        box.separator()        
       
        row = box.row(align=True)         
        row.use_property_split = True
        row.use_property_decorate = False  # No animation.

        flow = row.grid_flow(row_major=True, columns=0, even_columns=False, even_rows=False, align=True)

        col = flow.column()
        col.prop(scene.display_settings, "display_device")

        col.separator()

        col.prop(view, "view_transform")
        col.prop(view, "look")

        col = flow.column()
        col.prop(view, "exposure")
        col.prop(view, "gamma")

        col.separator()

        col.prop(scene.sequencer_colorspace_settings, "name", text="Sequencer")
      
        box.separator()         
    
        row = box.row(align=True)  
        row.label(text="Use Curves:") 
        row.prop(view, "use_curve_mapping", text="")
  
        box.separator()         

        if view.use_curve_mapping == True:
   
            row = box.column()  
            row.enabled = view.use_curve_mapping
            row.template_curve_mapping(view, "curve_mapping", type='COLOR', levels=True)
            
            box.separator()         

