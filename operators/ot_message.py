import bpy
from bpy.props import StringProperty

class RTS_OT_RePattern_Report(bpy.types.Operator):
    bl_idname = "rts_ot.report_message"
    bl_label = "Message"

    message : StringProperty()
 
    def draw(self, context):
        self.layout.label(text=self.message)

    def execute(self, context):
        self.report({'INFO'}, self.message)
        #print(self.message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager     
        return wm.invoke_popup(self, width=200)