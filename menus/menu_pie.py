import bpy


class RTS_MT_PIE_RePattern(bpy.types.Menu):
    bl_label = "RePattern"
    bl_idname = "RTS_MT_PIE_RePattern"   

    draw_as_box = True

    @classmethod
    def poll(cls, context):
        return context.mode == 'EDIT_MESH'

    def draw(self, context):     
        layout = self.layout
        #layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_DEFAULT'

        pie = layout.menu_pie()
        
        # 1 - LEFT
        box = pie.box()
        col = box.column(align=True)
        col.operator("rts_ot.fake_ops")

        
        # 2 - RIGHT
        box = pie.box()
        col = box.column(align=True)
        col.operator("rts_ot.fake_ops")
        
        # 3 - BOTTOM
        box = pie.box()

        col = box.column()
        # subrow = col.row(align=True)
        col.operator("rts_ot.fake_ops")

        
        # 4 - TOP
        box = pie.box()
        col = box.column(align=True)
        col.operator("rts_ot.fake_ops")



        # 5 - TOP - LEFT
        pie.separator()

        # 6 - TOP - RIGHT
        pie.separator()

        # 7 - BOTTOM - LEFT
        pie.separator()

        # 8 - BOTTOM - RIGHT
        pie.separator()
