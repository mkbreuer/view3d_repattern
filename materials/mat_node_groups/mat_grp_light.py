import bpy
    
    
def mat_presets_group_light(node_tree0, mat_out_0): 

    emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
    if hasattr(emission_0, 'color'):
        emission_0.color = (0.61, 0.61, 0.61)
    if hasattr(emission_0, 'hide'):
        emission_0.hide = False
    if hasattr(emission_0, 'location'):
        emission_0.location = (0.0, 0.0)
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

    blackbody_0 = node_tree0.nodes.new('ShaderNodeBlackbody')
    if hasattr(blackbody_0, 'color'):
        blackbody_0.color = (0.61, 0.61, 0.61)
    if hasattr(blackbody_0, 'hide'):
        blackbody_0.hide = False
    if hasattr(blackbody_0, 'location'):
        blackbody_0.location = (-200.0, 0.0)
    if hasattr(blackbody_0, 'mute'):
        blackbody_0.mute = False
    if hasattr(blackbody_0, 'name'):
        blackbody_0.name = 'Blackbody'
    if hasattr(blackbody_0, 'use_custom_color'):
        blackbody_0.use_custom_color = False
    if hasattr(blackbody_0, 'width'):
        blackbody_0.width = 150.0
    blackbody_0.inputs[0].default_value = 3000.0
    blackbody_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

    # LINKS
    node_tree0.links.new(blackbody_0.outputs[0], emission_0.inputs[0])
    node_tree0.links.new(emission_0.outputs[0], material_output_0.inputs[0])