import bpy

#https://blender.stackexchange.com/questions/4817/how-to-know-which-object-is-using-a-material
#https://blender.stackexchange.com/questions/13437/display-all-users-of-a-datablock?noredirect=1&lq=1
class RTS_OT_RePattern_Material_Select(bpy.types.Operator):
    bl_description = "select objects with active material"
    bl_idname = "rts_ot.select_obj_with_active_material"
    bl_label = "Select"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.select_all(action='DESELECT')
        mat = bpy.context.object.active_material
        objs = []

        for obj in bpy.data.objects:
            for slot in obj.material_slots:
                if slot.material == mat:
                    #objs.append(obj)
                    obj.select_set(True)
       
        return {'FINISHED'}  
    


class RTS_OT_RePattern_Material_Select_BSDF(bpy.types.Operator):
    bl_description = "if none: get principle bsdf or material output to preview properties"
    bl_idname = "rts_ot.select_bsdf_node"
    bl_label = "Get Output"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        mat = bpy.context.object.active_material
        if mat: 
            if mat.node_tree.nodes:                                                                               
                nodes = mat.node_tree.nodes         
                
                node_shader = nodes.get('Principled BSDF')              
                if node_shader is not None:
                    node_shader.select = True                 
                    nodes.active = node_shader
                    self.report({'INFO'}, "Principled BSDF / Open Shader Editor!")  
                else:
                    self.report({'INFO'}, "Material Output / Open Shader Editor!") 
                    nodes = mat.node_tree.nodes 
                    node_shader = nodes.get('Material Output')   
                    node_shader.select = True
                    nodes.active = node_shader   
           
            else:
                self.report({'INFO'}, "Found No Nodes!")             
            
        return {'FINISHED'}  


