import bpy
    

def mat_presets_group_wax(node_tree0, mat_out_0): 

    wax_0 = node_tree0.nodes.new('ShaderNodeBsdfPrincipled')
    if hasattr(wax_0, 'color'):
        wax_0.color = (0.61, 0.61, 0.61)
    if hasattr(wax_0, 'distribution'):
        wax_0.distribution = 'MULTI_GGX'
    if hasattr(wax_0, 'hide'):
        wax_0.hide = False
    if hasattr(wax_0, 'location'):
        wax_0.location = (0.0, 0.0)
    if hasattr(wax_0, 'mute'):
        wax_0.mute = False
    if hasattr(wax_0, 'name'):
        wax_0.name = 'Wax'
    if hasattr(wax_0, 'subsurface_method'):
        wax_0.subsurface_method = 'RANDOM_WALK'
    if hasattr(wax_0, 'use_custom_color'):
        wax_0.use_custom_color = False
    if hasattr(wax_0, 'width'):
        wax_0.width = 240.0
    wax_0.inputs[0].default_value = (0.26, 0.08, 0.22, 1.0)
    wax_0.inputs[1].default_value = 1.0
    wax_0.inputs[2].default_value = (1.0, 0.20, 0.10)
    wax_0.inputs[3].default_value = (0.26, 0.08, 0.22, 1.0)
    wax_0.inputs[4].default_value = 0.0
    wax_0.inputs[5].default_value = 0.5
    wax_0.inputs[6].default_value = 0.0
    wax_0.inputs[7].default_value = 0.30
    wax_0.inputs[8].default_value = 0.0
    wax_0.inputs[9].default_value = 0.0
    wax_0.inputs[10].default_value = 0.0
    wax_0.inputs[11].default_value = 0.5
    wax_0.inputs[12].default_value = 0.0
    wax_0.inputs[13].default_value = 0.03
    wax_0.inputs[14].default_value = 1.45
    wax_0.inputs[15].default_value = 0.0
    wax_0.inputs[16].default_value = 0.0
    wax_0.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
    wax_0.inputs[18].default_value = 1.0
    wax_0.inputs[19].default_value = 1.0
    wax_0.inputs[20].default_value = (0.0, 0.0, 0.0)
    wax_0.inputs[21].default_value = (0.0, 0.0, 0.0)
    wax_0.inputs[22].default_value = (0.0, 0.0, 0.0)

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
    rgb_0.outputs[0].default_value = (1.0, 0.40, 0.16, 1.0)

    # LINKS
    node_tree0.links.new(wax_0.outputs[0], mat_out_0.inputs[0])
    node_tree0.links.new(rgb_0.outputs[0], wax_0.inputs[2])
