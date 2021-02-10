import bpy
from bpy import*
from bpy.props import *


class RTS_OT_RePattern_BSDF_Use_Nodes(bpy.types.Operator):
    """modal: toggle use nodes"""
    bl_idname = "rts_ot.bsdf_use_node"
    bl_label = "Use Nodes"
    bl_options = {'REGISTER', 'UNDO'}
     
    def execute(self, context):
        print(self)      
        return {'FINISHED'}

    event = None
    def invoke(self, context, event):
        ev = []    

        if bpy.context.object.active_material.use_nodes == True:                         
            ev.append("Nodes unabled!") 
            bpy.context.object.active_material.use_nodes = False

        else: 
            ev.append("Nodes enabled!")     
            bpy.context.object.active_material.use_nodes = True
           
            mat = bpy.context.object.active_material
            if mat.node_tree:                                                 
                nodes = mat.node_tree.nodes                                    
                node_shader = nodes.get('Principled BSDF')                                                                                                                             
                node_shader.select = True
                nodes.active = node_shader    

        #ev.append("Shade")
        self.report({'INFO'}, "".join(ev))        
        return {'FINISHED'}  
 


class RTS_OT_RePattern_Emission_Use_Nodes(bpy.types.Operator):
    """modal: toggle use nodes"""
    bl_idname = "rts_ot.emission_use_node"
    bl_label = "Use Nodes"
    bl_options = {'REGISTER', 'UNDO'}
     
    def execute(self, context):
        print(self)      
        return {'FINISHED'}

    event = None
    def invoke(self, context, event):
        ev = []    

        if bpy.context.object.data.use_nodes== True:                        
            ev.append("Nodes unabled!") 
            bpy.context.object.data.use_nodes = False

        else: 
            ev.append("Nodes enabled!") 
            #bpy.ops.cycles.use_shading_nodes()
            bpy.context.object.data.use_nodes = True
           
            mat = bpy.context.object.active_material
            if mat:#.node_tree:                                                 
                nodes = mat.node_tree.nodes                                    
                node_shader = nodes.get('Emission')                                                                                                                             
                node_shader.select = True
                nodes.active = node_shader    

        #ev.append("Shade")
        self.report({'INFO'}, "".join(ev))        
        return {'FINISHED'}  
                
                