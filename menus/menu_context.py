import bpy


class RTS_MT_RePattern(bpy.types.Menu):
    bl_idname = "RTS_MT_RePattern"
    bl_label = "RePattern"


    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_DEFAULT'

        layout.operator("rts_ot.fake_ops")

        layout.separator()
   
        layout.operator("rts_ot.fake_ops")
        
        layout.separator()

        layout.operator("rts_ot.fake_ops")

        layout.separator()

        layout.operator("rts_ot.fake_ops")        
