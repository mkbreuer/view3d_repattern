import bpy
    

def mat_presets_group_blood(node_tree0, mat_out_0): 

    node_tree1 = bpy.data.node_groups.get('Blood')
    if not node_tree1:
        node_tree1 = bpy.data.node_groups.new('Blood', 'ShaderNodeTree')
        # INPUTS
        node_tree1.inputs.new('NodeSocketColor', 'Albedo')
        node_tree1.inputs.new('NodeSocketFloat', 'Volume')
        node_tree1.inputs.new('NodeSocketFloat', 'IOR')
        node_tree1.inputs.new('NodeSocketVector', 'Normal')
        # OUTPUTS
        node_tree1.outputs.new('NodeSocketShader', 'Shader')
        node_tree1.outputs.new('NodeSocketShader', 'Volume')
        # NODES
        node_tree2 = bpy.data.node_groups.get('Particles Blood')
        if not node_tree2:
            node_tree2 = bpy.data.node_groups.new('Particles Blood', 'ShaderNodeTree')
            # INPUTS
            node_tree2.inputs.new('NodeSocketColor', 'Scatter Color')
            node_tree2.inputs.new('NodeSocketColor', 'Absorption Color')
            node_tree2.inputs.new('NodeSocketFloat', 'Scatter Density')
            node_tree2.inputs.new('NodeSocketFloat', 'Absorption Density')
            node_tree2.inputs.new('NodeSocketFloat', 'Anisotropy')
            # OUTPUTS
            node_tree2.outputs.new('NodeSocketShader', 'Shader')
            # NODES
            volume_scatter_2 = node_tree2.nodes.new('ShaderNodeVolumeScatter')
            if hasattr(volume_scatter_2, 'color'):
                volume_scatter_2.color = (0.60, 0.60, 0.60)
            if hasattr(volume_scatter_2, 'hide'):
                volume_scatter_2.hide = False
            if hasattr(volume_scatter_2, 'location'):
                volume_scatter_2.location = (-101.55, 86.32)
            if hasattr(volume_scatter_2, 'mute'):
                volume_scatter_2.mute = False
            if hasattr(volume_scatter_2, 'name'):
                volume_scatter_2.name = 'Volume Scatter'
            if hasattr(volume_scatter_2, 'use_custom_color'):
                volume_scatter_2.use_custom_color = False
            if hasattr(volume_scatter_2, 'width'):
                volume_scatter_2.width = 140.0
            volume_scatter_2.inputs[0].default_value = (0.80, 0.80, 0.80, 1.0)
            volume_scatter_2.inputs[1].default_value = 1.0
            volume_scatter_2.inputs[2].default_value = 0.0

            volume_absorption_2 = node_tree2.nodes.new('ShaderNodeVolumeAbsorption')
            if hasattr(volume_absorption_2, 'color'):
                volume_absorption_2.color = (0.60, 0.60, 0.60)
            if hasattr(volume_absorption_2, 'hide'):
                volume_absorption_2.hide = False
            if hasattr(volume_absorption_2, 'location'):
                volume_absorption_2.location = (-102.45, -86.32)
            if hasattr(volume_absorption_2, 'mute'):
                volume_absorption_2.mute = False
            if hasattr(volume_absorption_2, 'name'):
                volume_absorption_2.name = 'Volume Absorption'
            if hasattr(volume_absorption_2, 'use_custom_color'):
                volume_absorption_2.use_custom_color = False
            if hasattr(volume_absorption_2, 'width'):
                volume_absorption_2.width = 140.0
            volume_absorption_2.inputs[0].default_value = (0.80, 0.80, 0.80, 1.0)
            volume_absorption_2.inputs[1].default_value = 1.0

            add_shader_2 = node_tree2.nodes.new('ShaderNodeAddShader')
            if hasattr(add_shader_2, 'color'):
                add_shader_2.color = (0.60, 0.60, 0.60)
            if hasattr(add_shader_2, 'hide'):
                add_shader_2.hide = False
            if hasattr(add_shader_2, 'location'):
                add_shader_2.location = (102.45, -7.50)
            if hasattr(add_shader_2, 'mute'):
                add_shader_2.mute = False
            if hasattr(add_shader_2, 'name'):
                add_shader_2.name = 'Add Shader'
            if hasattr(add_shader_2, 'use_custom_color'):
                add_shader_2.use_custom_color = False
            if hasattr(add_shader_2, 'width'):
                add_shader_2.width = 140.0

            group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
            if hasattr(group_output_2, 'color'):
                group_output_2.color = (0.60, 0.60, 0.60)
            if hasattr(group_output_2, 'hide'):
                group_output_2.hide = False
            if hasattr(group_output_2, 'is_active_output'):
                group_output_2.is_active_output = True
            if hasattr(group_output_2, 'location'):
                group_output_2.location = (302.45, -0.0)
            if hasattr(group_output_2, 'mute'):
                group_output_2.mute = False
            if hasattr(group_output_2, 'name'):
                group_output_2.name = 'Group Output'
            if hasattr(group_output_2, 'use_custom_color'):
                group_output_2.use_custom_color = False
            if hasattr(group_output_2, 'width'):
                group_output_2.width = 140.0

            group_input_2 = node_tree2.nodes.new('NodeGroupInput')
            if hasattr(group_input_2, 'color'):
                group_input_2.color = (0.60, 0.60, 0.60)
            if hasattr(group_input_2, 'hide'):
                group_input_2.hide = False
            if hasattr(group_input_2, 'location'):
                group_input_2.location = (-405.54, 0.0)
            if hasattr(group_input_2, 'mute'):
                group_input_2.mute = False
            if hasattr(group_input_2, 'name'):
                group_input_2.name = 'Group Input'
            if hasattr(group_input_2, 'use_custom_color'):
                group_input_2.use_custom_color = False
            if hasattr(group_input_2, 'width'):
                group_input_2.width = 140.0
            group_input_2.outputs[0].default_value = (0.80, 0.80, 0.80, 1.0)
            group_input_2.outputs[1].default_value = (0.80, 0.80, 0.80, 1.0)
            group_input_2.outputs[2].default_value = 1.0
            group_input_2.outputs[3].default_value = 1.0
            group_input_2.outputs[4].default_value = 0.0

            # LINKS
            node_tree2.links.new(volume_scatter_2.outputs[0], add_shader_2.inputs[0])
            node_tree2.links.new(volume_absorption_2.outputs[0], add_shader_2.inputs[1])
            node_tree2.links.new(add_shader_2.outputs[0], group_output_2.inputs[0])
            node_tree2.links.new(group_input_2.outputs[0], volume_scatter_2.inputs[0])
            node_tree2.links.new(group_input_2.outputs[1], volume_absorption_2.inputs[0])
            node_tree2.links.new(group_input_2.outputs[2], volume_scatter_2.inputs[1])
            node_tree2.links.new(group_input_2.outputs[3], volume_absorption_2.inputs[1])
            node_tree2.links.new(group_input_2.outputs[4], volume_scatter_2.inputs[2])

        group_1 = node_tree1.nodes.new('ShaderNodeGroup')
        if hasattr(group_1, 'node_tree'):
            group_1.node_tree = bpy.data.node_groups.get('Particles Blood')
        if hasattr(group_1, 'color'):
            group_1.color = (0.60, 0.60, 0.60)
        if hasattr(group_1, 'hide'):
            group_1.hide = False
        if hasattr(group_1, 'location'):
            group_1.location = (3.10, -95.18)
        if hasattr(group_1, 'mute'):
            group_1.mute = False
        if hasattr(group_1, 'name'):
            group_1.name = 'Group'
        if hasattr(group_1, 'use_custom_color'):
            group_1.use_custom_color = False
        if hasattr(group_1, 'width'):
            group_1.width = 140.0
        group_1.inputs[0].default_value = (0.25, 0.01, 0.01, 1.0)
        group_1.inputs[1].default_value = (0.25, 0.01, 0.01, 1.0)
        group_1.inputs[2].default_value = 3.0
        group_1.inputs[3].default_value = 3.0
        group_1.inputs[4].default_value = 0.0

        group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
        if hasattr(group_output_1, 'color'):
            group_output_1.color = (0.60, 0.60, 0.60)
        if hasattr(group_output_1, 'hide'):
            group_output_1.hide = False
        if hasattr(group_output_1, 'is_active_output'):
            group_output_1.is_active_output = True
        if hasattr(group_output_1, 'location'):
            group_output_1.location = (203.08, -0.0)
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
            group_input_1.color = (0.60, 0.60, 0.60)
        if hasattr(group_input_1, 'hide'):
            group_input_1.hide = False
        if hasattr(group_input_1, 'location'):
            group_input_1.location = (-300.63, -13.11)
        if hasattr(group_input_1, 'mute'):
            group_input_1.mute = False
        if hasattr(group_input_1, 'name'):
            group_input_1.name = 'Group Input'
        if hasattr(group_input_1, 'use_custom_color'):
            group_input_1.use_custom_color = False
        if hasattr(group_input_1, 'width'):
            group_input_1.width = 140.0
        group_input_1.outputs[0].default_value = (0.25, 0.01, 0.01, 1.0)
        group_input_1.outputs[1].default_value = 3.0
        group_input_1.outputs[2].default_value = 1.33
        group_input_1.outputs[3].default_value = (0.0, 0.0, 0.0)

        glass_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_1, 'color'):
            glass_bsdf_1.color = (0.60, 0.60, 0.60)
        if hasattr(glass_bsdf_1, 'distribution'):
            glass_bsdf_1.distribution = 'MULTI_GGX'
        if hasattr(glass_bsdf_1, 'hide'):
            glass_bsdf_1.hide = False
        if hasattr(glass_bsdf_1, 'location'):
            glass_bsdf_1.location = (-3.08, 95.18)
        if hasattr(glass_bsdf_1, 'mute'):
            glass_bsdf_1.mute = False
        if hasattr(glass_bsdf_1, 'name'):
            glass_bsdf_1.name = 'Glass BSDF'
        if hasattr(glass_bsdf_1, 'use_custom_color'):
            glass_bsdf_1.use_custom_color = False
        if hasattr(glass_bsdf_1, 'width'):
            glass_bsdf_1.width = 150.0
        glass_bsdf_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        glass_bsdf_1.inputs[1].default_value = 0.0
        glass_bsdf_1.inputs[2].default_value = 1.33
        glass_bsdf_1.inputs[3].default_value = (0.0, 0.0, 0.0)

        # LINKS
        node_tree1.links.new(group_1.outputs[0], group_output_1.inputs[1])
        node_tree1.links.new(glass_bsdf_1.outputs[0], group_output_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[0], group_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[0], group_1.inputs[1])
        node_tree1.links.new(group_input_1.outputs[2], glass_bsdf_1.inputs[2])
        node_tree1.links.new(group_input_1.outputs[3], glass_bsdf_1.inputs[3])
        node_tree1.links.new(group_input_1.outputs[1], group_1.inputs[2])
        node_tree1.links.new(group_input_1.outputs[1], group_1.inputs[3])

    group_0 = node_tree0.nodes.new('ShaderNodeGroup')
    if hasattr(group_0, 'node_tree'):
        group_0.node_tree = bpy.data.node_groups.get('Blood') 
    if hasattr(group_0, 'color'):
        group_0.color = (0.60, 0.60, 0.60)
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
    group_0.inputs[0].default_value = (1.0, 0.0, 0.0, 1.0)
    group_0.inputs[1].default_value = 3.0
    group_0.inputs[2].default_value = 1.33
    group_0.inputs[3].default_value = (0.0, 0.0, 0.0)

    # LINKS
    node_tree0.links.new(group_0.outputs[0], mat_out_0.inputs[0])
    node_tree0.links.new(group_0.outputs[1], mat_out_0.inputs[1])
    

