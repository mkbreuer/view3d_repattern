import bpy


class RTS_OT_RePattern_FakeOps(bpy.types.Operator):
    """fake operator: do nothing"""
    bl_idname = "rts_ot.fake_ops"
    bl_label = "Do Nothing"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #print(self)
        self.report({'INFO'}, "Fake Operator!") 
        return {'FINISHED'}


