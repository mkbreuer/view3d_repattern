import bpy
    

def mat_presets_group_atmo(node_tree0, mat_out_0): 

    node_tree1 = bpy.data.node_groups.get('Atmosphere')
    if not node_tree1:
        node_tree1 = bpy.data.node_groups.new('Atmosphere', 'ShaderNodeTree')
        # INPUTS
        node_tree1.inputs.new('NodeSocketColor', 'Scatter Color')
        node_tree1.inputs.new('NodeSocketColor', 'Absorption Color')
        node_tree1.inputs.new('NodeSocketFloat', 'Volume')
        # OUTPUTS
        node_tree1.outputs.new('NodeSocketShader', 'Volume')
        # NODES
        volume_absorption_1 = node_tree1.nodes.new('ShaderNodeVolumeAbsorption')
        if hasattr(volume_absorption_1, 'color'):
            volume_absorption_1.color = (0.61, 0.61, 0.61)
        if hasattr(volume_absorption_1, 'hide'):
            volume_absorption_1.hide = False
        if hasattr(volume_absorption_1, 'location'):
            volume_absorption_1.location = (-102.47, -86.32)
        if hasattr(volume_absorption_1, 'mute'):
            volume_absorption_1.mute = False
        if hasattr(volume_absorption_1, 'name'):
            volume_absorption_1.name = 'Volume Absorption'
        if hasattr(volume_absorption_1, 'use_custom_color'):
            volume_absorption_1.use_custom_color = False
        if hasattr(volume_absorption_1, 'width'):
            volume_absorption_1.width = 140.0
        volume_absorption_1.inputs[0].default_value = (0.22, 0.45, 0.95, 1.0)
        volume_absorption_1.inputs[1].default_value = 1.0

        group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
        if hasattr(group_output_1, 'color'):
            group_output_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_output_1, 'hide'):
            group_output_1.hide = False
        if hasattr(group_output_1, 'is_active_output'):
            group_output_1.is_active_output = True
        if hasattr(group_output_1, 'location'):
            group_output_1.location = (302.456787109375, -0.0)
        if hasattr(group_output_1, 'mute'):
            group_output_1.mute = False
        if hasattr(group_output_1, 'name'):
            group_output_1.name = 'Group Output'
        if hasattr(group_output_1, 'use_custom_color'):
            group_output_1.use_custom_color = False
        if hasattr(group_output_1, 'width'):
            group_output_1.width = 140.0

        group_input_1 = node_tree1.nodes.new('NodeGroupInput')
        if hasattr(group_input_1, 'color'):
            group_input_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_input_1, 'hide'):
            group_input_1.hide = False
        if hasattr(group_input_1, 'location'):
            group_input_1.location = (-405.54, 0.0)
        if hasattr(group_input_1, 'mute'):
            group_input_1.mute = False
        if hasattr(group_input_1, 'name'):
            group_input_1.name = 'Group Input'
        if hasattr(group_input_1, 'use_custom_color'):
            group_input_1.use_custom_color = False
        if hasattr(group_input_1, 'width'):
            group_input_1.width = 140.0
        group_input_1.outputs[0].default_value = (0.02, 0.09, 0.99, 1.0)
        group_input_1.outputs[1].default_value = (0.22, 0.45, 0.95, 1.0)
        group_input_1.outputs[2].default_value = 1.0

        volume_scatter_1 = node_tree1.nodes.new('ShaderNodeVolumeScatter')
        if hasattr(volume_scatter_1, 'color'):
            volume_scatter_1.color = (0.61, 0.61, 0.61)
        if hasattr(volume_scatter_1, 'hide'):
            volume_scatter_1.hide = False
        if hasattr(volume_scatter_1, 'location'):
            volume_scatter_1.location = (-101.55, 86.38)
        if hasattr(volume_scatter_1, 'mute'):
            volume_scatter_1.mute = False
        if hasattr(volume_scatter_1, 'name'):
            volume_scatter_1.name = 'Volume Scatter'
        if hasattr(volume_scatter_1, 'use_custom_color'):
            volume_scatter_1.use_custom_color = False
        if hasattr(volume_scatter_1, 'width'):
            volume_scatter_1.width = 140.0
        volume_scatter_1.inputs[0].default_value = (0.02, 0.09, 0.99, 1.0)
        volume_scatter_1.inputs[1].default_value = 1.0
        volume_scatter_1.inputs[2].default_value = 0.25

        mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
        if hasattr(mix_shader_1, 'color'):
            mix_shader_1.color = (0.61, 0.61, 0.61)
        if hasattr(mix_shader_1, 'hide'):
            mix_shader_1.hide = False
        if hasattr(mix_shader_1, 'location'):
            mix_shader_1.location = (101.52, 16.72)
        if hasattr(mix_shader_1, 'mute'):
            mix_shader_1.mute = False
        if hasattr(mix_shader_1, 'name'):
            mix_shader_1.name = 'Mix Shader'
        if hasattr(mix_shader_1, 'use_custom_color'):
            mix_shader_1.use_custom_color = False
        if hasattr(mix_shader_1, 'width'):
            mix_shader_1.width = 140.0
        mix_shader_1.inputs[0].default_value = 0.30

        # LINKS
        node_tree1.links.new(volume_scatter_1.outputs[0], mix_shader_1.inputs[1])
        node_tree1.links.new(volume_absorption_1.outputs[0], mix_shader_1.inputs[2])
        node_tree1.links.new(group_input_1.outputs[0], volume_scatter_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[1], volume_absorption_1.inputs[0])
        node_tree1.links.new(mix_shader_1.outputs[0], group_output_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[2], volume_scatter_1.inputs[1])
        node_tree1.links.new(group_input_1.outputs[2], volume_absorption_1.inputs[1])

    group_0 = node_tree0.nodes.new('ShaderNodeGroup')
    if hasattr(group_0, 'node_tree'):
        group_0.node_tree = bpy.data.node_groups.get('Atmosphere')
    if hasattr(group_0, 'color'):
        group_0.color = (0.61, 0.61, 0.61)
    if hasattr(group_0, 'hide'):
        group_0.hide = False
    if hasattr(group_0, 'location'):
        group_0.location = (0.0, 0.0)
    if hasattr(group_0, 'mute'):
        group_0.mute = False
    if hasattr(group_0, 'name'):
        group_0.name = 'Group'
    if hasattr(group_0, 'use_custom_color'):
        group_0.use_custom_color = False
    if hasattr(group_0, 'width'):
        group_0.width = 140.0
    group_0.inputs[0].default_value = (0.024, 0.088, 0.99, 1.0)
    group_0.inputs[1].default_value = (0.22, 0.45, 0.95, 1.0)
    group_0.inputs[2].default_value = 1.0

    # LINKS
    node_tree0.links.new(group_0.outputs[0], mat_out_0.inputs[1])
