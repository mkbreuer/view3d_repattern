import bpy


class RTS_MT_RePattern_MAT_Delete(bpy.types.Menu):
    bl_idname = "RTS_MT_RePattern_MAT_Delete"
    bl_label = "RTS MAT Delete"


    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_DEFAULT'
   
        layout.operator('rts_ot.remove_all_material', text='Remove unused Slots').mode='mat_slots_unused' 
        
        layout.separator()

        layout.operator('rts_ot.remove_all_material', text='Remove all Slots').mode='mat_slots_all'      
        layout.operator('rts_ot.remove_all_material', text='Remove Slot Slider').mode='mat_slots_amount'       

        layout.separator()
        layout.operator('rts_ot.remove_all_material', text='Remove & Purge').mode='mat_purge_slot' 
        layout.operator('rts_ot.remove_all_material', text='Purge Prefix').mode='mat_purge_prefix'           
        layout.operator('rts_ot.remove_all_material', text='Purge').mode='mat_purge_all' 
           
        temp_remove = eval("bpy.data.materials") 
        prefix = 'Dots Stroke'
        if prefix != '':                                                      
            for key, item in bpy.data.materials.items():
                if key.startswith(prefix):   
                    layout.separator()
                    layout.operator('rts_ot.remove_dots_stroke', text='Remove Dots Stroke')


