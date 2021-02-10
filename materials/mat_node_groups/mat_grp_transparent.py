import bpy
    

def mat_presets_group_transparent(node_tree0, mat_out_0): 

    node_tree1 = bpy.data.node_groups.get('Transparent')
    if not node_tree1:
        node_tree1 = bpy.data.node_groups.new('Transparent', 'ShaderNodeTree')
        # INPUTS
        node_tree1.inputs.new('NodeSocketColor', 'Color')
        node_tree1.inputs.new('NodeSocketFloat', 'IOR')
        node_tree1.inputs.new('NodeSocketFloatFactor', 'Rough')
        node_tree1.inputs.new('NodeSocketFloat', 'Caustics')
        node_tree1.inputs.new('NodeSocketVector', 'Normal')
        # OUTPUTS
        node_tree1.outputs.new('NodeSocketShader', 'Shader')
        # NODES
        mix_shader_002_1 = node_tree1.nodes.new('ShaderNodeMixShader')
        if hasattr(mix_shader_002_1, 'color'):
            mix_shader_002_1.color = (0.61, 0.61, 0.61)
        if hasattr(mix_shader_002_1, 'hide'):
            mix_shader_002_1.hide = True
        if hasattr(mix_shader_002_1, 'location'):
            mix_shader_002_1.location = (1429.83, -838.23)
        if hasattr(mix_shader_002_1, 'mute'):
            mix_shader_002_1.mute = False
        if hasattr(mix_shader_002_1, 'name'):
            mix_shader_002_1.name = 'Mix Shader.002'
        if hasattr(mix_shader_002_1, 'use_custom_color'):
            mix_shader_002_1.use_custom_color = False
        if hasattr(mix_shader_002_1, 'width'):
            mix_shader_002_1.width = 140.0
        mix_shader_002_1.inputs[0].default_value = 0.5

        transparent_bsdf_001_1 = node_tree1.nodes.new('ShaderNodeBsdfTransparent')
        if hasattr(transparent_bsdf_001_1, 'color'):
            transparent_bsdf_001_1.color = (0.61, 0.61, 0.61)
        if hasattr(transparent_bsdf_001_1, 'hide'):
            transparent_bsdf_001_1.hide = False
        if hasattr(transparent_bsdf_001_1, 'location'):
            transparent_bsdf_001_1.location = (1240.33, -893.77)
        if hasattr(transparent_bsdf_001_1, 'mute'):
            transparent_bsdf_001_1.mute = False
        if hasattr(transparent_bsdf_001_1, 'name'):
            transparent_bsdf_001_1.name = 'Transparent BSDF.001'
        if hasattr(transparent_bsdf_001_1, 'use_custom_color'):
            transparent_bsdf_001_1.use_custom_color = False
        if hasattr(transparent_bsdf_001_1, 'width'):
            transparent_bsdf_001_1.width = 140.0
        transparent_bsdf_001_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)

        group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
        if hasattr(group_output_1, 'color'):
            group_output_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_output_1, 'hide'):
            group_output_1.hide = False
        if hasattr(group_output_1, 'is_active_output'):
            group_output_1.is_active_output = True
        if hasattr(group_output_1, 'location'):
            group_output_1.location = (1617.61, -843.21)
        if hasattr(group_output_1, 'mute'):
            group_output_1.mute = False
        if hasattr(group_output_1, 'name'):
            group_output_1.name = 'Group Output'
        if hasattr(group_output_1, 'use_custom_color'):
            group_output_1.use_custom_color = False
        if hasattr(group_output_1, 'width'):
            group_output_1.width = 80.0

        group_input_1 = node_tree1.nodes.new('NodeGroupInput')
        if hasattr(group_input_1, 'color'):
            group_input_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_input_1, 'hide'):
            group_input_1.hide = False
        if hasattr(group_input_1, 'location'):
            group_input_1.location = (666.33, -798.59)
        if hasattr(group_input_1, 'mute'):
            group_input_1.mute = False
        if hasattr(group_input_1, 'name'):
            group_input_1.name = 'Group Input'
        if hasattr(group_input_1, 'use_custom_color'):
            group_input_1.use_custom_color = False
        if hasattr(group_input_1, 'width'):
            group_input_1.width = 140.0
        group_input_1.outputs[0].default_value = (0.80, 0.80, 0.80, 1.0)
        group_input_1.outputs[1].default_value = 1.45
        group_input_1.outputs[2].default_value = 0.0
        group_input_1.outputs[3].default_value = 3.0
        group_input_1.outputs[4].default_value = (0.0, 0.0, 0.0)

        light_path_1 = node_tree1.nodes.new('ShaderNodeLightPath')
        if hasattr(light_path_1, 'color'):
            light_path_1.color = (0.61, 0.61, 0.61)
        if hasattr(light_path_1, 'hide'):
            light_path_1.hide = False
        if hasattr(light_path_1, 'location'):
            light_path_1.location = (1053.41, -365.40)
        if hasattr(light_path_1, 'mute'):
            light_path_1.mute = False
        if hasattr(light_path_1, 'name'):
            light_path_1.name = 'Light Path'
        if hasattr(light_path_1, 'use_custom_color'):
            light_path_1.use_custom_color = False
        if hasattr(light_path_1, 'width'):
            light_path_1.width = 140.0
        light_path_1.outputs[0].default_value = 0.0
        light_path_1.outputs[1].default_value = 0.0
        light_path_1.outputs[2].default_value = 0.0
        light_path_1.outputs[3].default_value = 0.0
        light_path_1.outputs[4].default_value = 0.0
        light_path_1.outputs[5].default_value = 0.0
        light_path_1.outputs[6].default_value = 0.0
        light_path_1.outputs[7].default_value = 0.0
        light_path_1.outputs[8].default_value = 0.0
        light_path_1.outputs[9].default_value = 0.0
        light_path_1.outputs[10].default_value = 0.0
        light_path_1.outputs[11].default_value = 0.0
        light_path_1.outputs[12].default_value = 0.0

        math_1 = node_tree1.nodes.new('ShaderNodeMath')
        if hasattr(math_1, 'color'):
            math_1.color = (0.61, 0.61, 0.61)
        if hasattr(math_1, 'hide'):
            math_1.hide = True
        if hasattr(math_1, 'location'):
            math_1.location = (883.07, -838.63)
        if hasattr(math_1, 'mute'):
            math_1.mute = False
        if hasattr(math_1, 'name'):
            math_1.name = 'Math'
        if hasattr(math_1, 'operation'):
            math_1.operation = 'POWER'
        if hasattr(math_1, 'use_clamp'):
            math_1.use_clamp = False
        if hasattr(math_1, 'use_custom_color'):
            math_1.use_custom_color = False
        if hasattr(math_1, 'width'):
            math_1.width = 140.0
        math_1.inputs[0].default_value = 0.5
        math_1.inputs[1].default_value = 2.0
        math_1.inputs[2].default_value = 0.0
        math_1.outputs[0].default_value = 0.0

        node_tree2 = bpy.data.node_groups.get('Caustics')
        if not node_tree2:
            node_tree2 = bpy.data.node_groups.new('Caustics', 'ShaderNodeTree')
            # INPUTS
            node_tree2.inputs.new('NodeSocketColor', 'Color')
            node_tree2.inputs.new('NodeSocketFloat', 'Intensity')
            # OUTPUTS
            node_tree2.outputs.new('NodeSocketColor', 'Color')
            # NODES
            group_input_2 = node_tree2.nodes.new('NodeGroupInput')
            if hasattr(group_input_2, 'color'):
                group_input_2.color = (0.61, 0.61, 0.61)
            if hasattr(group_input_2, 'hide'):
                group_input_2.hide = False
            if hasattr(group_input_2, 'location'):
                group_input_2.location = (-662.99, -0.0)
            if hasattr(group_input_2, 'mute'):
                group_input_2.mute = False
            if hasattr(group_input_2, 'name'):
                group_input_2.name = 'Group Input'
            if hasattr(group_input_2, 'use_custom_color'):
                group_input_2.use_custom_color = False
            if hasattr(group_input_2, 'width'):
                group_input_2.width = 140.0
            group_input_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
            group_input_2.outputs[1].default_value = 3.0

            geometry_2 = node_tree2.nodes.new('ShaderNodeNewGeometry')
            if hasattr(geometry_2, 'color'):
                geometry_2.color = (0.61, 0.61, 0.61)
            if hasattr(geometry_2, 'hide'):
                geometry_2.hide = False
            if hasattr(geometry_2, 'location'):
                geometry_2.location = (-476.75, -208.93)
            if hasattr(geometry_2, 'mute'):
                geometry_2.mute = False
            if hasattr(geometry_2, 'name'):
                geometry_2.name = 'Geometry'
            if hasattr(geometry_2, 'use_custom_color'):
                geometry_2.use_custom_color = False
            if hasattr(geometry_2, 'width'):
                geometry_2.width = 140.0
            geometry_2.outputs[0].default_value = (0.0, 0.0, 0.0)
            geometry_2.outputs[1].default_value = (0.0, 0.0, 0.0)
            geometry_2.outputs[2].default_value = (0.0, 0.0, 0.0)
            geometry_2.outputs[3].default_value = (0.0, 0.0, 0.0)
            geometry_2.outputs[4].default_value = (0.0, 0.0, 0.0)
            geometry_2.outputs[5].default_value = (0.0, 0.0, 0.0)
            geometry_2.outputs[6].default_value = 0.0
            geometry_2.outputs[7].default_value = 0.0
            geometry_2.outputs[8].default_value = 0.0

            group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
            if hasattr(group_output_2, 'color'):
                group_output_2.color = (0.61, 0.61, 0.61)
            if hasattr(group_output_2, 'hide'):
                group_output_2.hide = False
            if hasattr(group_output_2, 'is_active_output'):
                group_output_2.is_active_output = True
            if hasattr(group_output_2, 'location'):
                group_output_2.location = (686.26, -119.75)
            if hasattr(group_output_2, 'mute'):
                group_output_2.mute = False
            if hasattr(group_output_2, 'name'):
                group_output_2.name = 'Group Output'
            if hasattr(group_output_2, 'use_custom_color'):
                group_output_2.use_custom_color = False
            if hasattr(group_output_2, 'width'):
                group_output_2.width = 140.0
            group_output_2.inputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_2 = node_tree2.nodes.new('ShaderNodeMixRGB')
            if hasattr(mix_2, 'blend_type'):
                mix_2.blend_type = 'MULTIPLY'
            if hasattr(mix_2, 'color'):
                mix_2.color = (0.61, 0.61, 0.61)
            if hasattr(mix_2, 'hide'):
                mix_2.hide = False
            if hasattr(mix_2, 'location'):
                mix_2.location = (220.40, -175.99)
            if hasattr(mix_2, 'mute'):
                mix_2.mute = False
            if hasattr(mix_2, 'name'):
                mix_2.name = 'Mix'
            if hasattr(mix_2, 'use_alpha'):
                mix_2.use_alpha = False
            if hasattr(mix_2, 'use_clamp'):
                mix_2.use_clamp = False
            if hasattr(mix_2, 'use_custom_color'):
                mix_2.use_custom_color = False
            if hasattr(mix_2, 'width'):
                mix_2.width = 140.0
            mix_2.inputs[0].default_value = 1.0
            mix_2.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
            mix_2.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_003_2 = node_tree2.nodes.new('ShaderNodeMixRGB')
            if hasattr(mix_003_2, 'blend_type'):
                mix_003_2.blend_type = 'MULTIPLY'
            if hasattr(mix_003_2, 'color'):
                mix_003_2.color = (0.61, 0.61, 0.61)
            if hasattr(mix_003_2, 'hide'):
                mix_003_2.hide = False
            if hasattr(mix_003_2, 'location'):
                mix_003_2.location = (448.17, -122.69)
            if hasattr(mix_003_2, 'mute'):
                mix_003_2.mute = False
            if hasattr(mix_003_2, 'name'):
                mix_003_2.name = 'Mix.003'
            if hasattr(mix_003_2, 'use_alpha'):
                mix_003_2.use_alpha = False
            if hasattr(mix_003_2, 'use_clamp'):
                mix_003_2.use_clamp = False
            if hasattr(mix_003_2, 'use_custom_color'):
                mix_003_2.use_custom_color = False
            if hasattr(mix_003_2, 'width'):
                mix_003_2.width = 140.0
            mix_003_2.inputs[0].default_value = 0.5
            mix_003_2.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
            mix_003_2.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
            mix_003_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            vector_math_2 = node_tree2.nodes.new('ShaderNodeVectorMath')
            if hasattr(vector_math_2, 'color'):
                vector_math_2.color = (0.61, 0.61, 0.61)
            if hasattr(vector_math_2, 'hide'):
                vector_math_2.hide = True
            if hasattr(vector_math_2, 'location'):
                vector_math_2.location = (-291.43, -298.05)
            if hasattr(vector_math_2, 'mute'):
                vector_math_2.mute = False
            if hasattr(vector_math_2, 'name'):
                vector_math_2.name = 'Vector Math'
            if hasattr(vector_math_2, 'operation'):
                vector_math_2.operation = 'DOT_PRODUCT'
            if hasattr(vector_math_2, 'use_custom_color'):
                vector_math_2.use_custom_color = False
            if hasattr(vector_math_2, 'width'):
                vector_math_2.width = 140.0
            vector_math_2.inputs[0].default_value = (0.5, 0.5, 0.5)
            vector_math_2.inputs[1].default_value = (0.5, 0.5, 0.5)
            vector_math_2.inputs[2].default_value = (0.0, 0.0, 0.0)
            vector_math_2.inputs[3].default_value = 1.0
            vector_math_2.outputs[0].default_value = (0.0, 0.0, 0.0)
            vector_math_2.outputs[1].default_value = 0.0

            colorramp_001_2 = node_tree2.nodes.new('ShaderNodeValToRGB')
            if hasattr(colorramp_001_2, 'color'):
                colorramp_001_2.color = (0.61, 0.61, 0.61)
            if hasattr(colorramp_001_2, 'color_ramp'):
                if hasattr(colorramp_001_2.color_ramp, 'color_mode'):
                    colorramp_001_2.color_ramp.color_mode = 'RGB'
                if hasattr(colorramp_001_2.color_ramp, 'elements'):
                    if 0 >= len(colorramp_001_2.color_ramp.elements):
                        colorramp_001_2.color_ramp.elements.new(0.5)
                    if hasattr(colorramp_001_2.color_ramp.elements[0], 'alpha'):
                        colorramp_001_2.color_ramp.elements[0].alpha = 1.0
                    if hasattr(colorramp_001_2.color_ramp.elements[0], 'color'):
                        colorramp_001_2.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
                    if hasattr(colorramp_001_2.color_ramp.elements[0], 'position'):
                        colorramp_001_2.color_ramp.elements[0].position = 0.5
                    if 1 >= len(colorramp_001_2.color_ramp.elements):
                        colorramp_001_2.color_ramp.elements.new(0.701)
                    if hasattr(colorramp_001_2.color_ramp.elements[1], 'alpha'):
                        colorramp_001_2.color_ramp.elements[1].alpha = 1.0
                    if hasattr(colorramp_001_2.color_ramp.elements[1], 'color'):
                        colorramp_001_2.color_ramp.elements[1].color = (0.25, 0.25, 0.25, 1.0)
                    if hasattr(colorramp_001_2.color_ramp.elements[1], 'position'):
                        colorramp_001_2.color_ramp.elements[1].position = 0.70
                    if 2 >= len(colorramp_001_2.color_ramp.elements):
                        colorramp_001_2.color_ramp.elements.new(0.88)
                    if hasattr(colorramp_001_2.color_ramp.elements[2], 'alpha'):
                        colorramp_001_2.color_ramp.elements[2].alpha = 1.0
                    if hasattr(colorramp_001_2.color_ramp.elements[2], 'color'):
                        colorramp_001_2.color_ramp.elements[2].color = (0.0, 0.0, 0.0, 1.0)
                    if hasattr(colorramp_001_2.color_ramp.elements[2], 'position'):
                        colorramp_001_2.color_ramp.elements[2].position = 0.88
                    if 3 >= len(colorramp_001_2.color_ramp.elements):
                        colorramp_001_2.color_ramp.elements.new(1.0)
                    if hasattr(colorramp_001_2.color_ramp.elements[3], 'alpha'):
                        colorramp_001_2.color_ramp.elements[3].alpha = 1.0
                    if hasattr(colorramp_001_2.color_ramp.elements[3], 'color'):
                        colorramp_001_2.color_ramp.elements[3].color = (1.0, 1.0, 1.0, 1.0)
                    if hasattr(colorramp_001_2.color_ramp.elements[3], 'position'):
                        colorramp_001_2.color_ramp.elements[3].position = 1.0
                if hasattr(colorramp_001_2.color_ramp, 'hue_interpolation'):
                    colorramp_001_2.color_ramp.hue_interpolation = 'NEAR'
                if hasattr(colorramp_001_2.color_ramp, 'interpolation'):
                    colorramp_001_2.color_ramp.interpolation = 'LINEAR'
            if hasattr(colorramp_001_2, 'display_in_settings'):
                colorramp_001_2.display_in_settings = False
            if hasattr(colorramp_001_2, 'hide'):
                colorramp_001_2.hide = False
            if hasattr(colorramp_001_2, 'location'):
                colorramp_001_2.location = (-114.09, -206.66)
            if hasattr(colorramp_001_2, 'mute'):
                colorramp_001_2.mute = False
            if hasattr(colorramp_001_2, 'name'):
                colorramp_001_2.name = 'ColorRamp.001'
            if hasattr(colorramp_001_2, 'use_custom_color'):
                colorramp_001_2.use_custom_color = False
            if hasattr(colorramp_001_2, 'width'):
                colorramp_001_2.width = 240.0
            colorramp_001_2.inputs[0].default_value = 0.5
            colorramp_001_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_001_2.outputs[1].default_value = 0.0

            # LINKS
            node_tree2.links.new(group_input_2.outputs[0], mix_003_2.inputs[2])
            node_tree2.links.new(geometry_2.outputs[1], vector_math_2.inputs[0])
            node_tree2.links.new(geometry_2.outputs[4], vector_math_2.inputs[1])
            node_tree2.links.new(vector_math_2.outputs[1], colorramp_001_2.inputs[0])
            node_tree2.links.new(mix_2.outputs[0], mix_003_2.inputs[1])
            node_tree2.links.new(group_input_2.outputs[1], mix_2.inputs[2])
            node_tree2.links.new(mix_003_2.outputs[0], group_output_2.inputs[0])
            node_tree2.links.new(colorramp_001_2.outputs[0], mix_2.inputs[1])

        group_001_1 = node_tree1.nodes.new('ShaderNodeGroup')
        if hasattr(group_001_1, 'node_tree'):
            group_001_1.node_tree = bpy.data.node_groups.get('Caustics')
        if hasattr(group_001_1, 'color'):
            group_001_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_001_1, 'hide'):
            group_001_1.hide = False
        if hasattr(group_001_1, 'location'):
            group_001_1.location = (1049.85, -936.66)
        if hasattr(group_001_1, 'mute'):
            group_001_1.mute = False
        if hasattr(group_001_1, 'name'):
            group_001_1.name = 'Group.001'
        if hasattr(group_001_1, 'use_custom_color'):
            group_001_1.use_custom_color = False
        if hasattr(group_001_1, 'width'):
            group_001_1.width = 140.0
        group_001_1.inputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
        group_001_1.inputs[1].default_value = 3.0
        group_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

        glass_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_1, 'color'):
            glass_bsdf_1.color = (0.61, 0.61, 0.61)
        if hasattr(glass_bsdf_1, 'distribution'):
            glass_bsdf_1.distribution = 'MULTI_GGX'
        if hasattr(glass_bsdf_1, 'hide'):
            glass_bsdf_1.hide = False
        if hasattr(glass_bsdf_1, 'location'):
            glass_bsdf_1.location = (1050.55, -701.03)
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
        glass_bsdf_1.inputs[2].default_value = 1.45
        glass_bsdf_1.inputs[3].default_value = (0.0, 0.0, 0.0)

        math_001_1 = node_tree1.nodes.new('ShaderNodeMath')
        if hasattr(math_001_1, 'color'):
            math_001_1.color = (0.61, 0.61, 0.61)
        if hasattr(math_001_1, 'hide'):
            math_001_1.hide = False
        if hasattr(math_001_1, 'location'):
            math_001_1.location = (966.81, -769.83)
        if hasattr(math_001_1, 'mute'):
            math_001_1.mute = False
        if hasattr(math_001_1, 'name'):
            math_001_1.name = 'Math.001'
        if hasattr(math_001_1, 'operation'):
            math_001_1.operation = 'POWER'
        if hasattr(math_001_1, 'use_clamp'):
            math_001_1.use_clamp = False
        if hasattr(math_001_1, 'use_custom_color'):
            math_001_1.use_custom_color = False
        if hasattr(math_001_1, 'width'):
            math_001_1.width = 140.0
        math_001_1.inputs[0].default_value = 0.5
        math_001_1.inputs[1].default_value = 0.5
        math_001_1.inputs[2].default_value = 0.0
        math_001_1.outputs[0].default_value = 0.0

        # LINKS
        node_tree1.links.new(mix_shader_002_1.outputs[0], group_output_1.inputs[0])
        node_tree1.links.new(transparent_bsdf_001_1.outputs[0], mix_shader_002_1.inputs[2])
        node_tree1.links.new(group_input_1.outputs[0], group_001_1.inputs[0])
        node_tree1.links.new(group_001_1.outputs[0], transparent_bsdf_001_1.inputs[0])
        node_tree1.links.new(light_path_1.outputs[1], mix_shader_002_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[3], group_001_1.inputs[1])
        node_tree1.links.new(group_input_1.outputs[2], math_1.inputs[0])
        node_tree1.links.new(glass_bsdf_1.outputs[0], mix_shader_002_1.inputs[1])
        node_tree1.links.new(group_input_1.outputs[0], glass_bsdf_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[1], glass_bsdf_1.inputs[2])
        node_tree1.links.new(group_input_1.outputs[4], glass_bsdf_1.inputs[3])
        node_tree1.links.new(math_1.outputs[0], math_001_1.inputs[0])
        node_tree1.links.new(math_001_1.outputs[0], glass_bsdf_1.inputs[1])

    group_0 = node_tree0.nodes.new('ShaderNodeGroup')
    if hasattr(group_0, 'node_tree'):
        group_0.node_tree = bpy.data.node_groups.get('Transparent')
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
    group_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
    group_0.inputs[1].default_value = 1.517
    group_0.inputs[2].default_value = 0.0
    group_0.inputs[3].default_value = 4.0
    group_0.inputs[4].default_value = (0.0, 0.0, 0.0)

    # LINKS
    node_tree0.links.new(group_0.outputs[0], mat_out_0.inputs[0])
