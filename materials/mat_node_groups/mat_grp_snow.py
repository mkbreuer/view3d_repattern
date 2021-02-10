import bpy
    

def mat_presets_group_snow(node_tree0, mat_out_0): 

    snow_0 = node_tree0.nodes.new('ShaderNodeBsdfPrincipled')
    if hasattr(snow_0, 'color'):
        snow_0.color = (0.61, 0.61, 0.61)
    if hasattr(snow_0, 'distribution'):
        snow_0.distribution = 'MULTI_GGX'
    if hasattr(snow_0, 'hide'):
        snow_0.hide = False
    if hasattr(snow_0, 'location'):
        snow_0.location = (0.0, 0.0)
    if hasattr(snow_0, 'mute'):
        snow_0.mute = False
    if hasattr(snow_0, 'name'):
        snow_0.name = 'Snow'
    if hasattr(snow_0, 'subsurface_method'):
        snow_0.subsurface_method = 'RANDOM_WALK'
    if hasattr(snow_0, 'use_custom_color'):
        snow_0.use_custom_color = False
    if hasattr(snow_0, 'width'):
        snow_0.width = 240.0
    snow_0.inputs[0].default_value = (0.90, 0.90, 0.90, 1.0)
    snow_0.inputs[1].default_value = 1.0
    snow_0.inputs[2].default_value = (1.0, 0.20, 0.10)
    snow_0.inputs[3].default_value = (0.90, 0.90, 0.90, 1.0)
    snow_0.inputs[4].default_value = 0.0
    snow_0.inputs[5].default_value = 1.25
    snow_0.inputs[6].default_value = 0.0
    snow_0.inputs[7].default_value = 0.5
    snow_0.inputs[8].default_value = 0.0
    snow_0.inputs[9].default_value = 0.0
    snow_0.inputs[10].default_value = 0.0
    snow_0.inputs[11].default_value = 0.5
    snow_0.inputs[12].default_value = 0.0
    snow_0.inputs[13].default_value = 0.03
    snow_0.inputs[14].default_value = 1.45
    snow_0.inputs[15].default_value = 0.0
    snow_0.inputs[16].default_value = 0.0
    snow_0.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
    snow_0.inputs[18].default_value = 1.0
    snow_0.inputs[19].default_value = 1.0
    snow_0.inputs[20].default_value = (0.0, 0.0, 0.0)
    snow_0.inputs[21].default_value = (0.0, 0.0, 0.0)
    snow_0.inputs[22].default_value = (0.0, 0.0, 0.0)

    rgb_0 = node_tree0.nodes.new('ShaderNodeRGB')
    if hasattr(rgb_0, 'color'):
        rgb_0.color = (0.61, 0.61, 0.61)
    if hasattr(rgb_0, 'hide'):
        rgb_0.hide = False
    if hasattr(rgb_0, 'location'):
        rgb_0.location = (-200.0, 0.0)
    if hasattr(rgb_0, 'mute'):
        rgb_0.mute = False
    if hasattr(rgb_0, 'name'):
        rgb_0.name = 'RGB'
    if hasattr(rgb_0, 'use_custom_color'):
        rgb_0.use_custom_color = False
    if hasattr(rgb_0, 'width'):
        rgb_0.width = 140.0
    rgb_0.outputs[0].default_value = (1.0, 0.97, 0.95, 1.0)

    # LINKS
    node_tree0.links.new(snow_0.outputs[0], mat_out_0.inputs[0])
    node_tree0.links.new(rgb_0.outputs[0], snow_0.inputs[2])
