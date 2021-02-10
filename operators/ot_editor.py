import bpy
from bpy import*
from bpy.props import*

# row.operator('rts_ot.open_editor',text="Show Editor", icon='NODETREE').mode = "uv"
# row.operator('rts_ot.open_editor',text="Show Editor", icon='NODETREE').mode = "image, view"
# row.operator('rts_ot.open_editor',text="Show Editor", icon='NODETREE').mode = "shader, object"


class RTS_OT_RePattern_Open_Editor(bpy.types.Operator):
    bl_idname = "rts_ot.open_editor"
    bl_label = "Open Editor"

    mode : StringProperty(default="")   
            
    def execute(self, context):

        if "uv" in self.mode: 
            if context.object.mode == 'OBJECT':
                bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
  
        for window in bpy.context.window_manager.windows:
            if len(window.screen.areas) == 1 and window.screen.areas[0].ui_type == 'PREFERENCES':

                if "image" in self.mode: 
                    window.screen.areas[0].ui_type = 'TextureNodeTree'
                                          
                    if "view" in self.mode:                                 
                        bpy.context.space_data.iu_mode = 'VIEW'

                    if "paint" in self.mode: 
                        bpy.context.space_data.iu_mode = 'PAINT'
                   
                    if "mask" in self.mode: 
                        bpy.context.space_data.iu_mode = 'MASK'
 
                if "uv" in self.mode: 
                    window.screen.areas[0].ui_type = 'UV'
               
                if "shader" in self.mode: 
                    window.screen.areas[0].ui_type = 'ShaderNodeTree'
                         
                    if "object" in self.mode:                                 
                        bpy.context.space_data.shader_type = 'OBJECT'
                        
                        mat = bpy.context.object.active_material
                        if mat: 
                            if mat.node_tree.nodes:                                                 
                                nodes = mat.node_tree.nodes 
                    
                                node_shader = nodes.get('Principled BSDF')
                                if node_shader is not None:
                                    node_shader.select = True
                                    nodes.active = node_shader  
                                else:
                                    node_shader = nodes.get('Material Output')                               
                                    node_shader.select = True
                                    nodes.active = node_shader          
                            else:
                                self.report({'INFO'}, "Found No Nodes!")   


                    if "lights" in self.mode:                                 
                        bpy.context.space_data.shader_type = 'OBJECT'
                        
                        mat = bpy.context.object.active_material
                        if mat: 
                            if mat.node_tree.nodes:                                                 
                                nodes = mat.node_tree.nodes 
                                
                                node_shader = nodes.get('Emission')
                                if node_shader is not None:
                                    node_shader.select = True
                                    nodes.active = node_shader  
                                else:
                                    node_shader = nodes.get('Material Output')                               
                                    node_shader.select = True
                                    nodes.active = node_shader  
                                
                                node_shader.select = True
                                nodes.active = node_shader   
                            else:
                                self.report({'INFO'}, "Found No Nodes!") 
                                  

                    if "world" in self.mode: 
                        bpy.context.space_data.shader_type = 'WORLD'
                   
                    if "line" in self.mode: 
                        bpy.context.space_data.shader_type = 'LINESTYLE'

                if "compositer" in self.mode: 
                    window.screen.areas[0].ui_type = 'CompositerNodeTree'

        return {'FINISHED'} 

