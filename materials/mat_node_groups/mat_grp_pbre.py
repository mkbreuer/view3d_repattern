import bpy
    

def mat_presets_group_pbre(node_tree0, mat_out_0): 


    normal_map_0 = node_tree0.nodes.new('ShaderNodeNormalMap')
    if hasattr(normal_map_0, 'color'):
        normal_map_0.color = (0.61, 0.61, 0.61)
    if hasattr(normal_map_0, 'hide'):
        normal_map_0.hide = False
    if hasattr(normal_map_0, 'location'):
        normal_map_0.location = (-873.64, -780.13)
    if hasattr(normal_map_0, 'mute'):
        normal_map_0.mute = False
    if hasattr(normal_map_0, 'name'):
        normal_map_0.name = 'Normal Map'
    if hasattr(normal_map_0, 'space'):
        normal_map_0.space = 'TANGENT'
    if hasattr(normal_map_0, 'use_custom_color'):
        normal_map_0.use_custom_color = False
    if hasattr(normal_map_0, 'width'):
        normal_map_0.width = 150.0
    normal_map_0.inputs[0].default_value = 1.0
    normal_map_0.inputs[1].default_value = (0.5, 0.5, 1.0, 1.0)
    normal_map_0.outputs[0].default_value = (0.0, 0.0, 0.0)

    mix_0 = node_tree0.nodes.new('ShaderNodeMixRGB')
    if hasattr(mix_0, 'blend_type'):
        mix_0.blend_type = 'MULTIPLY'
    if hasattr(mix_0, 'color'):
        mix_0.color = (0.61, 0.61, 0.61)
    if hasattr(mix_0, 'hide'):
        mix_0.hide = False
    if hasattr(mix_0, 'location'):
        mix_0.location = (-853.64, 59.87)
    if hasattr(mix_0, 'mute'):
        mix_0.mute = False
    if hasattr(mix_0, 'name'):
        mix_0.name = 'Mix'
    if hasattr(mix_0, 'use_alpha'):
        mix_0.use_alpha = False
    if hasattr(mix_0, 'use_clamp'):
        mix_0.use_clamp = False
    if hasattr(mix_0, 'use_custom_color'):
        mix_0.use_custom_color = False
    if hasattr(mix_0, 'width'):
        mix_0.width = 140.0
    mix_0.inputs[0].default_value = 0.5
    mix_0.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
    mix_0.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
    mix_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

    image_texture_004_0 = node_tree0.nodes.new('ShaderNodeTexImage')
    if hasattr(image_texture_004_0, 'color'):
        image_texture_004_0.color = (0.61, 0.61, 0.61)
    if hasattr(image_texture_004_0, 'extension'):
        image_texture_004_0.extension = 'REPEAT'
    if hasattr(image_texture_004_0, 'hide'):
        image_texture_004_0.hide = False
    if hasattr(image_texture_004_0, 'interpolation'):
        image_texture_004_0.interpolation = 'Linear'
    if hasattr(image_texture_004_0, 'location'):
        image_texture_004_0.location = (-1173.64, -780.13)
    if hasattr(image_texture_004_0, 'mute'):
        image_texture_004_0.mute = False
    if hasattr(image_texture_004_0, 'name'):
        image_texture_004_0.name = 'Image Texture.004'
    if hasattr(image_texture_004_0, 'projection'):
        image_texture_004_0.projection = 'FLAT'
    if hasattr(image_texture_004_0, 'projection_blend'):
        image_texture_004_0.projection_blend = 0.0
    if hasattr(image_texture_004_0, 'show_in_parent'):
        image_texture_004_0.show_in_parent = False
    if hasattr(image_texture_004_0, 'use_custom_color'):
        image_texture_004_0.use_custom_color = False
    if hasattr(image_texture_004_0, 'width'):
        image_texture_004_0.width = 240.0
    image_texture_004_0.inputs[0].default_value = (0.0, 0.0, 0.0)
    image_texture_004_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    image_texture_004_0.outputs[1].default_value = 0.0

    image_texture_003_0 = node_tree0.nodes.new('ShaderNodeTexImage')
    if hasattr(image_texture_003_0, 'color'):
        image_texture_003_0.color = (0.61, 0.61, 0.61)
    if hasattr(image_texture_003_0, 'extension'):
        image_texture_003_0.extension = 'REPEAT'
    if hasattr(image_texture_003_0, 'hide'):
        image_texture_003_0.hide = False
    if hasattr(image_texture_003_0, 'interpolation'):
        image_texture_003_0.interpolation = 'Linear'
    if hasattr(image_texture_003_0, 'location'):
        image_texture_003_0.location = (-1173.64, -540.13)
    if hasattr(image_texture_003_0, 'mute'):
        image_texture_003_0.mute = False
    if hasattr(image_texture_003_0, 'name'):
        image_texture_003_0.name = 'Image Texture.003'
    if hasattr(image_texture_003_0, 'projection'):
        image_texture_003_0.projection = 'FLAT'
    if hasattr(image_texture_003_0, 'projection_blend'):
        image_texture_003_0.projection_blend = 0.0
    if hasattr(image_texture_003_0, 'show_in_parent'):
        image_texture_003_0.show_in_parent = False
    if hasattr(image_texture_003_0, 'use_custom_color'):
        image_texture_003_0.use_custom_color = False
    if hasattr(image_texture_003_0, 'width'):
        image_texture_003_0.width = 240.0
    image_texture_003_0.inputs[0].default_value = (0.0, 0.0, 0.0)
    image_texture_003_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    image_texture_003_0.outputs[1].default_value = 0.0

    image_texture_002_0 = node_tree0.nodes.new('ShaderNodeTexImage')
    if hasattr(image_texture_002_0, 'color'):
        image_texture_002_0.color = (0.61, 0.61, 0.61)
    if hasattr(image_texture_002_0, 'extension'):
        image_texture_002_0.extension = 'REPEAT'
    if hasattr(image_texture_002_0, 'hide'):
        image_texture_002_0.hide = False
    if hasattr(image_texture_002_0, 'interpolation'):
        image_texture_002_0.interpolation = 'Linear'
    if hasattr(image_texture_002_0, 'location'):
        image_texture_002_0.location = (-1173.64, -300.13)
    if hasattr(image_texture_002_0, 'mute'):
        image_texture_002_0.mute = False
    if hasattr(image_texture_002_0, 'name'):
        image_texture_002_0.name = 'Image Texture.002'
    if hasattr(image_texture_002_0, 'projection'):
        image_texture_002_0.projection = 'FLAT'
    if hasattr(image_texture_002_0, 'projection_blend'):
        image_texture_002_0.projection_blend = 0.0
    if hasattr(image_texture_002_0, 'show_in_parent'):
        image_texture_002_0.show_in_parent = False
    if hasattr(image_texture_002_0, 'use_custom_color'):
        image_texture_002_0.use_custom_color = False
    if hasattr(image_texture_002_0, 'width'):
        image_texture_002_0.width = 240.0
    image_texture_002_0.inputs[0].default_value = (0.0, 0.0, 0.0)
    image_texture_002_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    image_texture_002_0.outputs[1].default_value = 0.0

    image_texture_001_0 = node_tree0.nodes.new('ShaderNodeTexImage')
    if hasattr(image_texture_001_0, 'color'):
        image_texture_001_0.color = (0.61, 0.61, 0.61)
    if hasattr(image_texture_001_0, 'extension'):
        image_texture_001_0.extension = 'REPEAT'
    if hasattr(image_texture_001_0, 'hide'):
        image_texture_001_0.hide = False
    if hasattr(image_texture_001_0, 'interpolation'):
        image_texture_001_0.interpolation = 'Linear'
    if hasattr(image_texture_001_0, 'location'):
        image_texture_001_0.location = (-1173.64, -60.14)
    if hasattr(image_texture_001_0, 'mute'):
        image_texture_001_0.mute = False
    if hasattr(image_texture_001_0, 'name'):
        image_texture_001_0.name = 'Image Texture.001'
    if hasattr(image_texture_001_0, 'projection'):
        image_texture_001_0.projection = 'FLAT'
    if hasattr(image_texture_001_0, 'projection_blend'):
        image_texture_001_0.projection_blend = 0.0
    if hasattr(image_texture_001_0, 'show_in_parent'):
        image_texture_001_0.show_in_parent = False
    if hasattr(image_texture_001_0, 'use_custom_color'):
        image_texture_001_0.use_custom_color = False
    if hasattr(image_texture_001_0, 'width'):
        image_texture_001_0.width = 240.0
    image_texture_001_0.inputs[0].default_value = (0.0, 0.0, 0.0)
    image_texture_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    image_texture_001_0.outputs[1].default_value = 0.0

    image_texture_0 = node_tree0.nodes.new('ShaderNodeTexImage')
    if hasattr(image_texture_0, 'color'):
        image_texture_0.color = (0.61, 0.61, 0.61)
    if hasattr(image_texture_0, 'extension'):
        image_texture_0.extension = 'REPEAT'
    if hasattr(image_texture_0, 'hide'):
        image_texture_0.hide = False
    if hasattr(image_texture_0, 'interpolation'):
        image_texture_0.interpolation = 'Linear'
    if hasattr(image_texture_0, 'location'):
        image_texture_0.location = (-1173.64, 179.87)
    if hasattr(image_texture_0, 'mute'):
        image_texture_0.mute = False
    if hasattr(image_texture_0, 'name'):
        image_texture_0.name = 'Image Texture'
    if hasattr(image_texture_0, 'projection'):
        image_texture_0.projection = 'FLAT'
    if hasattr(image_texture_0, 'projection_blend'):
        image_texture_0.projection_blend = 0.0
    if hasattr(image_texture_0, 'show_in_parent'):
        image_texture_0.show_in_parent = False
    if hasattr(image_texture_0, 'use_custom_color'):
        image_texture_0.use_custom_color = False
    if hasattr(image_texture_0, 'width'):
        image_texture_0.width = 240.0
    image_texture_0.inputs[0].default_value = (0.0, 0.0, 0.0)
    image_texture_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    image_texture_0.outputs[1].default_value = 0.0

    emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
    if hasattr(emission_0, 'color'):
        emission_0.color = (0.61, 0.61, 0.61)
    if hasattr(emission_0, 'hide'):
        emission_0.hide = False
    if hasattr(emission_0, 'location'):
        emission_0.location = (-73.64, -120.132)
    if hasattr(emission_0, 'mute'):
        emission_0.mute = False
    if hasattr(emission_0, 'name'):
        emission_0.name = 'Emission'
    if hasattr(emission_0, 'use_custom_color'):
        emission_0.use_custom_color = False
    if hasattr(emission_0, 'width'):
        emission_0.width = 140.0
    emission_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
    emission_0.inputs[1].default_value = 1.0

    mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
    if hasattr(mix_shader_0, 'color'):
        mix_shader_0.color = (0.61, 0.61, 0.61)
    if hasattr(mix_shader_0, 'hide'):
        mix_shader_0.hide = False
    if hasattr(mix_shader_0, 'location'):
        mix_shader_0.location = (106.36, -0.13)
    if hasattr(mix_shader_0, 'mute'):
        mix_shader_0.mute = False
    if hasattr(mix_shader_0, 'name'):
        mix_shader_0.name = 'Mix Shader'
    if hasattr(mix_shader_0, 'use_custom_color'):
        mix_shader_0.use_custom_color = False
    if hasattr(mix_shader_0, 'width'):
        mix_shader_0.width = 140.0
    mix_shader_0.inputs[0].default_value = 0.5

    image_texture_005_0 = node_tree0.nodes.new('ShaderNodeTexImage')
    if hasattr(image_texture_005_0, 'color'):
        image_texture_005_0.color = (0.61, 0.61, 0.61)
    if hasattr(image_texture_005_0, 'extension'):
        image_texture_005_0.extension = 'REPEAT'
    if hasattr(image_texture_005_0, 'hide'):
        image_texture_005_0.hide = False
    if hasattr(image_texture_005_0, 'interpolation'):
        image_texture_005_0.interpolation = 'Linear'
    if hasattr(image_texture_005_0, 'location'):
        image_texture_005_0.location = (-353.64, -160.132)
    if hasattr(image_texture_005_0, 'mute'):
        image_texture_005_0.mute = False
    if hasattr(image_texture_005_0, 'name'):
        image_texture_005_0.name = 'Image Texture.005'
    if hasattr(image_texture_005_0, 'projection'):
        image_texture_005_0.projection = 'FLAT'
    if hasattr(image_texture_005_0, 'projection_blend'):
        image_texture_005_0.projection_blend = 0.0
    if hasattr(image_texture_005_0, 'show_in_parent'):
        image_texture_005_0.show_in_parent = False
    if hasattr(image_texture_005_0, 'use_custom_color'):
        image_texture_005_0.use_custom_color = False
    if hasattr(image_texture_005_0, 'width'):
        image_texture_005_0.width = 240.0
    image_texture_005_0.inputs[0].default_value = (0.0, 0.0, 0.0)
    image_texture_005_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    image_texture_005_0.outputs[1].default_value = 0.0

    pbr_emission_0 = node_tree0.nodes.new('ShaderNodeBsdfPrincipled')
    if hasattr(pbr_emission_0, 'color'):
        pbr_emission_0.color = (0.61, 0.61, 0.61)
    if hasattr(pbr_emission_0, 'distribution'):
        pbr_emission_0.distribution = 'MULTI_GGX'
    if hasattr(pbr_emission_0, 'hide'):
        pbr_emission_0.hide = False
    if hasattr(pbr_emission_0, 'location'):
        pbr_emission_0.location = (-633.64, -40.13)
    if hasattr(pbr_emission_0, 'mute'):
        pbr_emission_0.mute = False
    if hasattr(pbr_emission_0, 'name'):
        pbr_emission_0.name = 'PBR Emission'
    if hasattr(pbr_emission_0, 'subsurface_method'):
        pbr_emission_0.subsurface_method = 'BURLEY'
    if hasattr(pbr_emission_0, 'use_custom_color'):
        pbr_emission_0.use_custom_color = False
    if hasattr(pbr_emission_0, 'width'):
        pbr_emission_0.width = 240.0
    pbr_emission_0.inputs[0].default_value = (0.90, 0.90, 0.90, 1.0)
    pbr_emission_0.inputs[1].default_value = 0.0
    pbr_emission_0.inputs[2].default_value = (1.0, 0.20, 0.10)
    pbr_emission_0.inputs[3].default_value = (0.90, 0.90, 0.90, 1.0)
    pbr_emission_0.inputs[4].default_value = 0.0
    pbr_emission_0.inputs[5].default_value = 0.5
    pbr_emission_0.inputs[6].default_value = 0.0
    pbr_emission_0.inputs[7].default_value = 0.5
    pbr_emission_0.inputs[8].default_value = 0.0
    pbr_emission_0.inputs[9].default_value = 0.0
    pbr_emission_0.inputs[10].default_value = 0.0
    pbr_emission_0.inputs[11].default_value = 0.5
    pbr_emission_0.inputs[12].default_value = 0.0
    pbr_emission_0.inputs[13].default_value = 0.0
    pbr_emission_0.inputs[14].default_value = 1.45
    pbr_emission_0.inputs[15].default_value = 0.0
    pbr_emission_0.inputs[16].default_value = 0.0
    pbr_emission_0.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
    pbr_emission_0.inputs[18].default_value = 1.0
    pbr_emission_0.inputs[19].default_value = 1.0
    pbr_emission_0.inputs[20].default_value = (0.0, 0.0, 0.0)
    pbr_emission_0.inputs[21].default_value = (0.0, 0.0, 0.0)
    pbr_emission_0.inputs[22].default_value = (0.0, 0.0, 0.0)

    # LINKS
    node_tree0.links.new(image_texture_002_0.outputs[0], pbr_emission_0.inputs[4])
    node_tree0.links.new(image_texture_003_0.outputs[0], pbr_emission_0.inputs[7])
    node_tree0.links.new(image_texture_004_0.outputs[0], normal_map_0.inputs[1])
    node_tree0.links.new(normal_map_0.outputs[0], pbr_emission_0.inputs[20])
    node_tree0.links.new(image_texture_005_0.outputs[0], emission_0.inputs[0])
    node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[2])
    node_tree0.links.new(pbr_emission_0.outputs[0], mix_shader_0.inputs[1])
    node_tree0.links.new(mix_shader_0.outputs[0], mat_out_0.inputs[0])
    node_tree0.links.new(image_texture_0.outputs[0], mix_0.inputs[1])
    node_tree0.links.new(image_texture_001_0.outputs[0], mix_0.inputs[2])
    node_tree0.links.new(mix_0.outputs[0], pbr_emission_0.inputs[0])
