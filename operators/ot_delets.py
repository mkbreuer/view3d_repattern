import bpy


class RTS_OT_RePattern_Purge_Groups(bpy.types.Operator):
    '''purge all unused orphaned groups data'''
    bl_idname="rts_ot.unused_group_data"
    bl_label="Purge Groups"
    bl_options = {"REGISTER", 'UNDO'}    

    def execute(self, context):
        target_coll = eval("bpy.data.groups")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)
        
        print(self)
        self.report({'INFO'}, "Purge group datas!")            
        return {'FINISHED'}



