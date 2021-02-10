import bpy
    

def mat_presets_group_curtain(node_tree0, mat_out_0): 
    
    node_tree1 = bpy.data.node_groups.get('Curtain')
    if not node_tree1:
        node_tree1 = bpy.data.node_groups.new('Curtain', 'ShaderNodeTree')
        # INPUTS
        node_tree1.inputs.new('NodeSocketColor', 'Albedo')
        node_tree1.inputs.new('NodeSocketFloatFactor', 'Roughness')
        node_tree1.inputs.new('NodeSocketFloatFactor', 'Sheen')
        node_tree1.inputs.new('NodeSocketVector', 'Normal')
        # OUTPUTS
        node_tree1.outputs.new('NodeSocketShader', 'Shader')
        # NODES
        group_input_1 = node_tree1.nodes.new('NodeGroupInput')
        if hasattr(group_input_1, 'color'):
            group_input_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_input_1, 'hide'):
            group_input_1.hide = False
        if hasattr(group_input_1, 'location'):
            group_input_1.location = (-698.78, -0.0)
        if hasattr(group_input_1, 'mute'):
            group_input_1.mute = False
        if hasattr(group_input_1, 'name'):
            group_input_1.name = 'Group Input'
        if hasattr(group_input_1, 'use_custom_color'):
            group_input_1.use_custom_color = False
        if hasattr(group_input_1, 'width'):
            group_input_1.width = 140.0
        group_input_1.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
        group_input_1.outputs[1].default_value = 0.70
        group_input_1.outputs[2].default_value = 1.0
        group_input_1.outputs[3].default_value = (0.0, 0.0, 0.0)

        translucent_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfTranslucent')
        if hasattr(translucent_bsdf_1, 'color'):
            translucent_bsdf_1.color = (0.61, 0.61, 0.61)
        if hasattr(translucent_bsdf_1, 'hide'):
            translucent_bsdf_1.hide = False
        if hasattr(translucent_bsdf_1, 'location'):
            translucent_bsdf_1.location = (-282.62, -192.47)
        if hasattr(translucent_bsdf_1, 'mute'):
            translucent_bsdf_1.mute = False
        if hasattr(translucent_bsdf_1, 'name'):
            translucent_bsdf_1.name = 'Translucent BSDF'
        if hasattr(translucent_bsdf_1, 'use_custom_color'):
            translucent_bsdf_1.use_custom_color = False
        if hasattr(translucent_bsdf_1, 'width'):
            translucent_bsdf_1.width = 140.0
        translucent_bsdf_1.inputs[0].default_value = (0.80, 0.80, 0.80, 1.0)
        translucent_bsdf_1.inputs[1].default_value = (0.0, 0.0, 0.0)

        mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
        if hasattr(mix_shader_1, 'color'):
            mix_shader_1.color = (0.61, 0.61, 0.61)
        if hasattr(mix_shader_1, 'hide'):
            mix_shader_1.hide = False
        if hasattr(mix_shader_1, 'location'):
            mix_shader_1.location = (-29.89, -85.69)
        if hasattr(mix_shader_1, 'mute'):
            mix_shader_1.mute = False
        if hasattr(mix_shader_1, 'name'):
            mix_shader_1.name = 'Mix Shader'
        if hasattr(mix_shader_1, 'use_custom_color'):
            mix_shader_1.use_custom_color = False
        if hasattr(mix_shader_1, 'width'):
            mix_shader_1.width = 140.0
        mix_shader_1.inputs[0].default_value = 0.5

        layer_weight_1 = node_tree1.nodes.new('ShaderNodeLayerWeight')
        if hasattr(layer_weight_1, 'color'):
            layer_weight_1.color = (0.61, 0.61, 0.61)
        if hasattr(layer_weight_1, 'hide'):
            layer_weight_1.hide = False
        if hasattr(layer_weight_1, 'location'):
            layer_weight_1.location = (-65.04, 268.09)
        if hasattr(layer_weight_1, 'mute'):
            layer_weight_1.mute = False
        if hasattr(layer_weight_1, 'name'):
            layer_weight_1.name = 'Layer Weight'
        if hasattr(layer_weight_1, 'use_custom_color'):
            layer_weight_1.use_custom_color = False
        if hasattr(layer_weight_1, 'width'):
            layer_weight_1.width = 140.0
        layer_weight_1.inputs[0].default_value = 0.5
        layer_weight_1.inputs[1].default_value = (0.0, 0.0, 0.0)
        layer_weight_1.outputs[0].default_value = 0.0
        layer_weight_1.outputs[1].default_value = 0.0

        mix_shader_001_1 = node_tree1.nodes.new('ShaderNodeMixShader')
        if hasattr(mix_shader_001_1, 'color'):
            mix_shader_001_1.color = (0.61, 0.61, 0.61)
        if hasattr(mix_shader_001_1, 'hide'):
            mix_shader_001_1.hide = False
        if hasattr(mix_shader_001_1, 'location'):
            mix_shader_001_1.location = (407.26, 1.42)
        if hasattr(mix_shader_001_1, 'mute'):
            mix_shader_001_1.mute = False
        if hasattr(mix_shader_001_1, 'name'):
            mix_shader_001_1.name = 'Mix Shader.001'
        if hasattr(mix_shader_001_1, 'use_custom_color'):
            mix_shader_001_1.use_custom_color = False
        if hasattr(mix_shader_001_1, 'width'):
            mix_shader_001_1.width = 140.0
        mix_shader_001_1.inputs[0].default_value = 0.20

        group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
        if hasattr(group_output_1, 'color'):
            group_output_1.color = (0.61, 0.61, 0.61)
        if hasattr(group_output_1, 'hide'):
            group_output_1.hide = False
        if hasattr(group_output_1, 'is_active_output'):
            group_output_1.is_active_output = True
        if hasattr(group_output_1, 'location'):
            group_output_1.location = (667.10, 3.52)
        if hasattr(group_output_1, 'mute'):
            group_output_1.mute = False
        if hasattr(group_output_1, 'name'):
            group_output_1.name = 'Group Output'
        if hasattr(group_output_1, 'use_custom_color'):
            group_output_1.use_custom_color = False
        if hasattr(group_output_1, 'width'):
            group_output_1.width = 140.0

        principled_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfPrincipled')
        if hasattr(principled_bsdf_1, 'color'):
            principled_bsdf_1.color = (0.61, 0.61, 0.61)
        if hasattr(principled_bsdf_1, 'distribution'):
            principled_bsdf_1.distribution = 'MULTI_GGX'
        if hasattr(principled_bsdf_1, 'hide'):
            principled_bsdf_1.hide = False
        if hasattr(principled_bsdf_1, 'location'):
            principled_bsdf_1.location = (-286.78, 315.61)
        if hasattr(principled_bsdf_1, 'mute'):
            principled_bsdf_1.mute = False
        if hasattr(principled_bsdf_1, 'name'):
            principled_bsdf_1.name = 'Principled BSDF'
        if hasattr(principled_bsdf_1, 'subsurface_method'):
            principled_bsdf_1.subsurface_method = 'BURLEY'
        if hasattr(principled_bsdf_1, 'use_custom_color'):
            principled_bsdf_1.use_custom_color = False
        if hasattr(principled_bsdf_1, 'width'):
            principled_bsdf_1.width = 150.0
        principled_bsdf_1.inputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
        principled_bsdf_1.inputs[1].default_value = 0.0
        principled_bsdf_1.inputs[2].default_value = (1.0, 1.0, 1.0)
        principled_bsdf_1.inputs[3].default_value = (0.70, 0.10, 0.10, 1.0)
        principled_bsdf_1.inputs[4].default_value = 0.0
        principled_bsdf_1.inputs[5].default_value = 0.5
        principled_bsdf_1.inputs[6].default_value = 0.0
        principled_bsdf_1.inputs[7].default_value = 0.70
        principled_bsdf_1.inputs[8].default_value = 0.0
        principled_bsdf_1.inputs[9].default_value = 0.0
        principled_bsdf_1.inputs[10].default_value = 1.0
        principled_bsdf_1.inputs[11].default_value = 0.0
        principled_bsdf_1.inputs[12].default_value = 0.0
        principled_bsdf_1.inputs[13].default_value = 0.03
        principled_bsdf_1.inputs[14].default_value = 1.45
        principled_bsdf_1.inputs[15].default_value = 0.0
        principled_bsdf_1.inputs[16].default_value = 0.0
        principled_bsdf_1.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
        principled_bsdf_1.inputs[18].default_value = 1.0
        principled_bsdf_1.inputs[19].default_value = 1.0
        principled_bsdf_1.inputs[20].default_value = (0.0, 0.0, 0.0)
        principled_bsdf_1.inputs[21].default_value = (0.0, 0.0, 0.0)
        principled_bsdf_1.inputs[22].default_value = (0.0, 0.0, 0.0)

        transparent_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfTransparent')
        if hasattr(transparent_bsdf_1, 'color'):
            transparent_bsdf_1.color = (0.61, 0.61, 0.61)
        if hasattr(transparent_bsdf_1, 'hide'):
            transparent_bsdf_1.hide = False
        if hasattr(transparent_bsdf_1, 'location'):
            transparent_bsdf_1.location = (159.45, 0.49)
        if hasattr(transparent_bsdf_1, 'mute'):
            transparent_bsdf_1.mute = False
        if hasattr(transparent_bsdf_1, 'name'):
            transparent_bsdf_1.name = 'Transparent BSDF'
        if hasattr(transparent_bsdf_1, 'use_custom_color'):
            transparent_bsdf_1.use_custom_color = False
        if hasattr(transparent_bsdf_1, 'width'):
            transparent_bsdf_1.width = 143.01
        transparent_bsdf_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)

        rgb_curves_1 = node_tree1.nodes.new('ShaderNodeRGBCurve')
        if hasattr(rgb_curves_1, 'color'):
            rgb_curves_1.color = (0.61, 0.61, 0.61)
        if hasattr(rgb_curves_1, 'display_in_settings'):
            rgb_curves_1.display_in_settings = False
        if hasattr(rgb_curves_1, 'hide'):
            rgb_curves_1.hide = False
        if hasattr(rgb_curves_1, 'location'):
            rgb_curves_1.location = (108.03, 351.12)
        if hasattr(rgb_curves_1, 'mapping'):
            if hasattr(rgb_curves_1.mapping, 'black_level'):
                rgb_curves_1.mapping.black_level = (0.0, 0.0, 0.0)
            if hasattr(rgb_curves_1.mapping, 'clip_max_x'):
                rgb_curves_1.mapping.clip_max_x = 1.0
            if hasattr(rgb_curves_1.mapping, 'clip_max_y'):
                rgb_curves_1.mapping.clip_max_y = 1.0
            if hasattr(rgb_curves_1.mapping, 'clip_min_x'):
                rgb_curves_1.mapping.clip_min_x = 0.0
            if hasattr(rgb_curves_1.mapping, 'clip_min_y'):
                rgb_curves_1.mapping.clip_min_y = 0.0
            if hasattr(rgb_curves_1.mapping, 'curves'):
                if hasattr(rgb_curves_1.mapping.curves[0], 'points'):
                    if 0 >= len(rgb_curves_1.mapping.curves[0].points):
                        rgb_curves_1.mapping.curves[0].points.new(0.0, 0.0)
                    if hasattr(rgb_curves_1.mapping.curves[0].points[0], 'handle_type'):
                        rgb_curves_1.mapping.curves[0].points[0].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[0].points[0], 'location'):
                        rgb_curves_1.mapping.curves[0].points[0].location = (0.0, 0.0)
                    if hasattr(rgb_curves_1.mapping.curves[0].points[0], 'select'):
                        rgb_curves_1.mapping.curves[0].points[0].select = False
                    if 1 >= len(rgb_curves_1.mapping.curves[0].points):
                        rgb_curves_1.mapping.curves[0].points.new(1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[0].points[1], 'handle_type'):
                        rgb_curves_1.mapping.curves[0].points[1].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[0].points[1], 'location'):
                        rgb_curves_1.mapping.curves[0].points[1].location = (1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[0].points[1], 'select'):
                        rgb_curves_1.mapping.curves[0].points[1].select = False
                if hasattr(rgb_curves_1.mapping.curves[1], 'points'):
                    if 0 >= len(rgb_curves_1.mapping.curves[1].points):
                        rgb_curves_1.mapping.curves[1].points.new(0.0, 0.0)
                    if hasattr(rgb_curves_1.mapping.curves[1].points[0], 'handle_type'):
                        rgb_curves_1.mapping.curves[1].points[0].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[1].points[0], 'location'):
                        rgb_curves_1.mapping.curves[1].points[0].location = (0.0, 0.0)
                    if hasattr(rgb_curves_1.mapping.curves[1].points[0], 'select'):
                        rgb_curves_1.mapping.curves[1].points[0].select = False
                    if 1 >= len(rgb_curves_1.mapping.curves[1].points):
                        rgb_curves_1.mapping.curves[1].points.new(1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[1].points[1], 'handle_type'):
                        rgb_curves_1.mapping.curves[1].points[1].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[1].points[1], 'location'):
                        rgb_curves_1.mapping.curves[1].points[1].location = (1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[1].points[1], 'select'):
                        rgb_curves_1.mapping.curves[1].points[1].select = False
                if hasattr(rgb_curves_1.mapping.curves[2], 'points'):
                    if 0 >= len(rgb_curves_1.mapping.curves[2].points):
                        rgb_curves_1.mapping.curves[2].points.new(0.0, 0.0)
                    if hasattr(rgb_curves_1.mapping.curves[2].points[0], 'handle_type'):
                        rgb_curves_1.mapping.curves[2].points[0].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[2].points[0], 'location'):
                        rgb_curves_1.mapping.curves[2].points[0].location = (0.0, 0.0)
                    if hasattr(rgb_curves_1.mapping.curves[2].points[0], 'select'):
                        rgb_curves_1.mapping.curves[2].points[0].select = False
                    if 1 >= len(rgb_curves_1.mapping.curves[2].points):
                        rgb_curves_1.mapping.curves[2].points.new(1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[2].points[1], 'handle_type'):
                        rgb_curves_1.mapping.curves[2].points[1].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[2].points[1], 'location'):
                        rgb_curves_1.mapping.curves[2].points[1].location = (1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[2].points[1], 'select'):
                        rgb_curves_1.mapping.curves[2].points[1].select = False
                if hasattr(rgb_curves_1.mapping.curves[3], 'points'):
                    if 0 >= len(rgb_curves_1.mapping.curves[3].points):
                        rgb_curves_1.mapping.curves[3].points.new(0.0, 0.40)
                    if hasattr(rgb_curves_1.mapping.curves[3].points[0], 'handle_type'):
                        rgb_curves_1.mapping.curves[3].points[0].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[3].points[0], 'location'):
                        rgb_curves_1.mapping.curves[3].points[0].location = (0.0, 0.40)
                    if hasattr(rgb_curves_1.mapping.curves[3].points[0], 'select'):
                        rgb_curves_1.mapping.curves[3].points[0].select = False
                    if 1 >= len(rgb_curves_1.mapping.curves[3].points):
                        rgb_curves_1.mapping.curves[3].points.new(0.50, 0.55)
                    if hasattr(rgb_curves_1.mapping.curves[3].points[1], 'handle_type'):
                        rgb_curves_1.mapping.curves[3].points[1].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[3].points[1], 'location'):
                        rgb_curves_1.mapping.curves[3].points[1].location = (0.50, 0.55)
                    if hasattr(rgb_curves_1.mapping.curves[3].points[1], 'select'):
                        rgb_curves_1.mapping.curves[3].points[1].select = True
                    if 2 >= len(rgb_curves_1.mapping.curves[3].points):
                        rgb_curves_1.mapping.curves[3].points.new(1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[3].points[2], 'handle_type'):
                        rgb_curves_1.mapping.curves[3].points[2].handle_type = 'AUTO'
                    if hasattr(rgb_curves_1.mapping.curves[3].points[2], 'location'):
                        rgb_curves_1.mapping.curves[3].points[2].location = (1.0, 1.0)
                    if hasattr(rgb_curves_1.mapping.curves[3].points[2], 'select'):
                        rgb_curves_1.mapping.curves[3].points[2].select = False
            if hasattr(rgb_curves_1.mapping, 'extend'):
                rgb_curves_1.mapping.extend = 'EXTRAPOLATED'
            if hasattr(rgb_curves_1.mapping, 'tone'):
                rgb_curves_1.mapping.tone = 'STANDARD'
            if hasattr(rgb_curves_1.mapping, 'use_clip'):
                rgb_curves_1.mapping.use_clip = True
            if hasattr(rgb_curves_1.mapping, 'white_level'):
                rgb_curves_1.mapping.white_level = (1.0, 1.0, 1.0)
        if hasattr(rgb_curves_1, 'mute'):
            rgb_curves_1.mute = False
        if hasattr(rgb_curves_1, 'name'):
            rgb_curves_1.name = 'RGB Curves'
        if hasattr(rgb_curves_1, 'use_custom_color'):
            rgb_curves_1.use_custom_color = False
        if hasattr(rgb_curves_1, 'width'):
            rgb_curves_1.width = 240.0
        rgb_curves_1.inputs[0].default_value = 1.0
        rgb_curves_1.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        rgb_curves_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

        # LINKS
        node_tree1.links.new(translucent_bsdf_1.outputs[0], mix_shader_1.inputs[2])
        node_tree1.links.new(principled_bsdf_1.outputs[0], mix_shader_1.inputs[1])
        node_tree1.links.new(mix_shader_1.outputs[0], mix_shader_001_1.inputs[2])
        node_tree1.links.new(transparent_bsdf_1.outputs[0], mix_shader_001_1.inputs[1])
        node_tree1.links.new(layer_weight_1.outputs[1], rgb_curves_1.inputs[1])
        node_tree1.links.new(mix_shader_001_1.outputs[0], group_output_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[1], principled_bsdf_1.inputs[7])
        node_tree1.links.new(group_input_1.outputs[3], principled_bsdf_1.inputs[20])
        node_tree1.links.new(group_input_1.outputs[3], translucent_bsdf_1.inputs[1])
        node_tree1.links.new(group_input_1.outputs[0], principled_bsdf_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[2], principled_bsdf_1.inputs[10])
        node_tree1.links.new(rgb_curves_1.outputs[0], mix_shader_001_1.inputs[0])
        node_tree1.links.new(group_input_1.outputs[0], translucent_bsdf_1.inputs[0])

    group_0 = node_tree0.nodes.new('ShaderNodeGroup')
    if hasattr(group_0, 'node_tree'):
        group_0.node_tree = bpy.data.node_groups.get('Curtain')
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
    group_0.inputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
    group_0.inputs[1].default_value = 0.70
    group_0.inputs[2].default_value = 1.0
    group_0.inputs[3].default_value = (0.0, 0.0, 0.0)

    # LINKS
    node_tree0.links.new(group_0.outputs[0], mat_out_0.inputs[0])
