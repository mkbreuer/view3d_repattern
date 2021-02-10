import bpy

def mat_presets_pencil_bsdf(self, node):

    if "Custom" in self.pencil_type:    
        node.inputs[0].default_value = self.mat_color

    # AUTUMN COLORS #
    if "Light_Sienna" in self.pencil_type: #FECD94       
        node.inputs[0].default_value = (0.760525, 0.141263, 0.093059, 1)

    if "Solway_Blue" in self.pencil_type: #CEE2DB 
        node.inputs[0].default_value = (0.617207, 0.760525, 0.708376, 1)

    if "Ink_Blue" in self.pencil_type: #5B8287 
        node.inputs[0].default_value = (0.104617, 0.223228, 0.242281, 1)
    
    if "Smoke_Blue" in self.pencil_type: #ADDAC6
        node.inputs[0].default_value = (0.417885, 0.701102, 0.564712, 1)

    if "Pale_Cedar" in self.pencil_type: #E1E0AA 
        node.inputs[0].default_value = (0.752942, 0.745404, 0.401978, 1)

    if "Green_Shadow" in self.pencil_type: #9CB490
        node.inputs[0].default_value = (0.332452, 0.456411, 0.278894, 1)

    if "Crag_Green" in self.pencil_type: #B0C388
        node.inputs[0].default_value = (0.434154, 0.545725, 0.246201, 1)
    
    if "Olive_Earth" in self.pencil_type: #6C784D
        node.inputs[0].default_value = (0.14996, 0.187821, 0.0742136, 1)
    
    if "Warm_Earth" in self.pencil_type: #A48452 
        node.inputs[0].default_value = (0.371238, 0.23074, 0.0843762, 1)
    
    if "Brown_Ochre" in self.pencil_type: #DCAB58 
        node.inputs[0].default_value = (0.715694, 0.40724, 0.0975874, 1)
    
    if "Wheat" in self.pencil_type: #FBF3C7  
        node.inputs[0].default_value = (0.964686, 0.896269, 0.571125, 1)
    
    if "Yellow_Ochre" in self.pencil_type: #FED86A 
        node.inputs[0].default_value = (0.991102, 0.686685, 0.144129, 1)

    if "Sepia_Red" in self.pencil_type: #8B695B
        node.inputs[0].default_value = (0.258183, 0.141263, 0.104617, 1)

    if "Mars_Orange" in self.pencil_type: #FC6636
        node.inputs[0].default_value = (0.973445, 0.132868, 0.0368895, 1)

    if "Sanguine" in self.pencil_type: #DB4529
        node.inputs[0].default_value = (0.708376, 0.0595112, 0.0221739, 1)

    if "Venetian_Red" in self.pencil_type: #AC5B45
        node.inputs[0].default_value = (0.412543, 0.104617, 0.0595112, 1)

    if "Terracotta" in self.pencil_type: #C55E4B
        node.inputs[0].default_value = (0.558341, 0.111932, 0.0703601, 1)

    if "Mars_Violet" in self.pencil_type: #AA7C7F
        node.inputs[0].default_value = (0.401978, 0.201556, 0.212231, 1)

    if "Ruby_Earth" in self.pencil_type: #9F514F
        node.inputs[0].default_value = (0.346704, 0.0822827, 0.0781874, 1)

    if "Chocolate" in self.pencil_type: #474441
        node.inputs[0].default_value = (0.06301, 0.0578054, 0.0528607, 1)

    if "Ivory_Black" in self.pencil_type: #192223
        node.inputs[0].default_value = (0.00972122, 0.0159963, 0.0168074, 1)

    if "Warm_Gray" in self.pencil_type: #C9BD9A 
        node.inputs[0].default_value = (0.584078, 0.508881, 0.323143, 1)

    if "Cool_Gray" in self.pencil_type: #BAC5AC
        node.inputs[0].default_value = (0.491021, 0.558341, 0.412543, 1)


    # GRAPHITINT COLORS #
    if "Port" in self.pencil_type: #A95658
        node.inputs[0].default_value = (0.396755, 0.093059, 0.0975874, 1)

    if "Juniper" in self.pencil_type: #946683
        node.inputs[0].default_value = (0.296138, 0.132868, 0.226966, 1)

    if "Aubergine" in self.pencil_type: #5F4877
        node.inputs[0].default_value = (0.114435, 0.0648033, 0.184475, 1)

    if "Dark_Indigo" in self.pencil_type: #2C3A4F
        node.inputs[0].default_value = (0.0251869, 0.0423114, 0.0781874, 1)

    if "Shadow" in self.pencil_type: #23525F
        node.inputs[0].default_value = (0.0168074, 0.0843762, 0.114435, 1)

    if "Steel_Blue" in self.pencil_type: #325A60
        node.inputs[0].default_value = (0.031896, 0.102242, 0.116971, 1)

    if "Ocean_Blue" in self.pencil_type: #1D4B73
        node.inputs[0].default_value = (0.0122865, 0.0703601, 0.171441, 1)

    if "Slate_Green" in self.pencil_type: #235E51
        node.inputs[0].default_value = (0.0168074, 0.111932, 0.0822827, 1)

    if "Meadow" in self.pencil_type: #3F4A2F
        node.inputs[0].default_value = (0.0497066, 0.0684782, 0.028426, 1)

    if "Ivy" in self.pencil_type: #5F6D30
        node.inputs[0].default_value = (0.114435, 0.152926, 0.0295568, 1)

    if "Sage" in self.pencil_type: #6A5228
        node.inputs[0].default_value = (0.144129, 0.0843762, 0.021219, 1)

    if "Chestnut" in self.pencil_type: #602A23
        node.inputs[0].default_value = (0.116971, 0.0231534, 0.0168074, 1)

    if "Russet" in self.pencil_type: #613A26
        node.inputs[0].default_value = (0.119538, 0.0423114, 0.0193824, 1)

    if "Cool_Brown" in self.pencil_type: #47472B
        node.inputs[0].default_value = (0.06301, 0.06301, 0.0241576, 1)

    if "Cocoa" in self.pencil_type: #633829
        node.inputs[0].default_value = (0.124772, 0.0395462, 0.0221739, 1)

    if "Autumn_Brown" in self.pencil_type: #5D352C
        node.inputs[0].default_value = (0.109462, 0.0356013, 0.0251869, 1)

    if "Storm" in self.pencil_type: #332D26
        node.inputs[0].default_value = (0.0331048, 0.0262412, 0.0193824, 1)

    if "Warm_Gray" in self.pencil_type: #373635
        node.inputs[0].default_value = (0.0382044, 0.0368895, 0.0356013, 1)

    if "Midnight_Black" in self.pencil_type: #272B23
        node.inputs[0].default_value = (0.0202886, 0.0241576, 0.0168074, 1)

    if "Mountain_Gray" in self.pencil_type: #535249
        node.inputs[0].default_value = (0.0865005, 0.0843762, 0.0666259, 1)

    if "Mountain_Blue" in self.pencil_type: #535249
        node.inputs[0].default_value = (0.063, 0.122, 0.109, 1)

    if "Cloud_Gray" in self.pencil_type: #65726A
        node.inputs[0].default_value = (0.130137, 0.168269, 0.144129, 1)

    if "Cool_Gray" in self.pencil_type: #2B4648
        node.inputs[0].default_value = (0.0241576, 0.0612461, 0.0648033, 1)


    # TINTED CHARCOAL COLORS #
    if "Sand" in self.pencil_type: #E2B35B
        node.inputs[0].default_value = (0.760525, 0.450786, 0.104617, 1)

    if "Burnt_Orange" in self.pencil_type: #D88135
        node.inputs[0].default_value = (0.686685, 0.219526, 0.0356013, 1)

    if "Sunset_Pink" in self.pencil_type: #E39774
        node.inputs[0].default_value = (0.768151, 0.309469, 0.174647, 1)

    if "Glowing_Embers" in self.pencil_type: #6D5E4A
        node.inputs[0].default_value = (0.152926, 0.111932, 0.0684782, 1)

    if "Heather_Mist" in self.pencil_type: #8A776A
        node.inputs[0].default_value = (0.254152, 0.184475, 0.144129, 1)

    if "Burnt_Embers" in self.pencil_type: #6F645C
        node.inputs[0].default_value = (0.158961, 0.127438, 0.107023, 1)

    if "Lavender" in self.pencil_type: #57454A
        node.inputs[0].default_value = (0.0953075, 0.0595112, 0.0684782, 1)

    if "Thistle" in self.pencil_type: #5D5859
        node.inputs[0].default_value = (0.109462, 0.0975874, 0.0998987, 1)

    if "Bilberry" in self.pencil_type: #455560
        node.inputs[0].default_value = (0.0595112, 0.0908417, 0.116971, 1)
    
    if "Elderberry" in self.pencil_type: #425968             
        node.inputs[0].default_value = (0.0544803, 0.0998987, 0.138432, 1)
    
    if "Moutain_blue" in self.pencil_type: #48635E
        node.inputs[0].default_value = (0.0648033, 0.124772, 0.111932, 1)

    if "Ocean_Deep" in self.pencil_type: #3B4444
        node.inputs[0].default_value = (0.043735, 0.0578054, 0.0578054, 1)

    if "Slate" in self.pencil_type: #415151
        node.inputs[0].default_value = (0.0528607, 0.0822827, 0.0822827, 1)

    if "Forest_Pine" in self.pencil_type: #4D6656
        node.inputs[0].default_value = (0.0742136, 0.132868, 0.093059, 1)

    if "Green_Moss" in self.pencil_type: #6E735A
        node.inputs[0].default_value = (0.155926, 0.171441, 0.102242, 1)

    if "Dark_Moss" in self.pencil_type: #63654A
        node.inputs[0].default_value = (0.124772, 0.130137, 0.0684782, 1)

    if "Driftwood" in self.pencil_type: #232518
        node.inputs[0].default_value = (0.0168074, 0.0185002, 0.00913406, 1)

    if "Peat" in self.pencil_type: #474332
        node.inputs[0].default_value = (0.06301, 0.0561285, 0.031896, 1)

    if "Burnt_Earth" in self.pencil_type: #363325
        node.inputs[0].default_value = (0.0368895, 0.0331048, 0.0185002, 1)

    if "Natural" in self.pencil_type: #515446
        node.inputs[0].default_value = (0.0822827, 0.0886556, 0.0612461, 1)

    if "Charcoal_Light" in self.pencil_type: #45483B
        node.inputs[0].default_value = (0.0595112, 0.0648033, 0.043735, 1)

    if "Charcoal_Medium" in self.pencil_type: #2B2D23
        node.inputs[0].default_value = (0.0241576, 0.0262412, 0.0168074, 1)

    if "Charcoal_Dark" in self.pencil_type: #1E211B
        node.inputs[0].default_value = (0.012983, 0.0152085, 0.0109601, 1)

    if "Charcoal_Black" in self.pencil_type: #1E211B
        node.inputs[0].default_value = (0.005, 0.005, 0.005, 1)


    # WATER COLORS #
    if "Zinc_Yellow" in self.pencil_type: #F6EB81
        node.inputs[0].default_value = (0.921582, 0.83077, 0.219526, 1)

    if "Lemon_Cadmium" in self.pencil_type: #F7EB82
        node.inputs[0].default_value = (0.930111, 0.83077, 0.223228, 1)

    if "Gold" in self.pencil_type: #FDDD59
        node.inputs[0].default_value = (0.982251, 0.723055, 0.0998987, 1)

    if "Primrose_Yellow" in self.pencil_type: #F7EFA2
        node.inputs[0].default_value = (0.930111, 0.863157, 0.361307, 1)

    if "Straw_Yellow" in self.pencil_type: #F9ED90
        node.inputs[0].default_value = (0.947307, 0.846873, 0.278894, 1)

    if "Deep_Cadmium" in self.pencil_type: #FBE968
        node.inputs[0].default_value = (0.964686, 0.814847, 0.138432, 1)

    if "Naples_Yellow" in self.pencil_type: #FDDA5A
        node.inputs[0].default_value = (0.982251, 0.701102, 0.102242, 1)

    if "Middle_Chrome" in self.pencil_type: #FFBD43
        node.inputs[0].default_value = (1, 0.508881, 0.0561285, 1)

    if "Deep_Chrome" in self.pencil_type: #FFB24E
        node.inputs[0].default_value = (1, 0.445201, 0.0761854, 1)

    if "Orange_Chrome" in self.pencil_type: #FF9D44
        node.inputs[0].default_value = (1, 0.337164, 0.0578054, 1)

    if "Spectrum_Orange" in self.pencil_type: #FF7C3D
        node.inputs[0].default_value = (1, 0.201556, 0.0466651, 1)

    if "Scarlet_Lake" in self.pencil_type: #FF673A
        node.inputs[0].default_value = (1, 0.135633, 0.0423114, 1)

    if "Pale_Vermilion" in self.pencil_type: #FF7E56
        node.inputs[0].default_value = (1, 0.208637, 0.093059, 1)

    if "Geranium_Lake" in self.pencil_type: #FF5E45
        node.inputs[0].default_value = (1, 0.111932, 0.0595112, 1)

    if "Flesh_Pink" in self.pencil_type: #FCF5D6
        node.inputs[0].default_value = (0.973445, 0.913099, 0.672443, 1)

    if "Pink_Madder_Lake" in self.pencil_type: #FE918B
        node.inputs[0].default_value = (0.991102, 0.283149, 0.258183, 1)

    if "Rose_Pink" in self.pencil_type: #FCD6E4
        node.inputs[0].default_value = (0.973445, 0.672443, 0.775822, 1)
    
    if "Madder_Carmine" in self.pencil_type: #F24234
        node.inputs[0].default_value = (0.887923, 0.0544803, 0.0343398, 1)
    
    if "Crimson_Lake" in self.pencil_type: #F53B2D
        node.inputs[0].default_value = (0.913099, 0.043735, 0.0262412, 1)

    if "Rose_Madder_Lake" in self.pencil_type: #F7465F
        node.inputs[0].default_value = (0.930111, 0.0612461, 0.114435, 1)

    if "Magenta" in self.pencil_type: #C55DA9
        node.inputs[0].default_value = (0.558341, 0.109462, 0.396755, 1)

    if "Imperial_Purple" in self.pencil_type: #4D3178
        node.inputs[0].default_value = (0.0742136, 0.0307135, 0.187821, 1)

    if "Red_Violet_Lake" in self.pencil_type: #9674AA
        node.inputs[0].default_value = (0.304987, 0.174647, 0.401978, 1)

    if "Dark_Violet" in self.pencil_type: #323688
        node.inputs[0].default_value = (0.031896, 0.0368895, 0.246201, 1)

    if "Light_Violet" in self.pencil_type: #AAA6D2
        node.inputs[0].default_value = (0.401978, 0.381326, 0.64448, 1)

    if "Blue_Violet_Lake" in self.pencil_type: #6C94CC
        node.inputs[0].default_value = (0.14996, 0.296138, 0.603827, 1)

    if "Delft_Blue" in self.pencil_type: #1F2E78
        node.inputs[0].default_value = (0.0137021, 0.0273209, 0.187821, 1)

    if "Ultramarine" in self.pencil_type: #214DA4
        node.inputs[0].default_value = (0.0152085, 0.0742136, 0.371238, 1)

    if "Smalt_Blue" in self.pencil_type: #4FA5D8
        node.inputs[0].default_value = (0.0781874, 0.376262, 0.686685, 1)

    if "Cobald_Blue" in self.pencil_type: #116AB7
        node.inputs[0].default_value = (0.00560539, 0.144129, 0.473531, 1)

    if "Spectrum_Blue" in self.pencil_type: #337EC3
        node.inputs[0].default_value = (0.0331048, 0.208637, 0.545725, 1)

    if "Light_Blue" in self.pencil_type: #30B2E3
        node.inputs[0].default_value = (0.0295568, 0.445201, 0.768151, 1)

    if "Sky_Blue" in self.pencil_type: #A1E3EA
        node.inputs[0].default_value = (0.3564, 0.768151, 0.822786, 1)

    if "Prussian_Blue" in self.pencil_type: #173E93
        node.inputs[0].default_value = (0.00856813, 0.0481718, 0.291771, 1)

    if "Indigo" in self.pencil_type: #1F3459
        node.inputs[0].default_value = (0.0137021, 0.0343398, 0.0998987, 1)

    if "Oriental_Blue" in self.pencil_type: #268ACB
        node.inputs[0].default_value = (0.0193824, 0.254152, 0.597202, 1)

    if "Kingfisher" in self.pencil_type: #1AA9DD
        node.inputs[0].default_value = (0.0103298, 0.396755, 0.723055, 1)

    if "Turquoise_Blue" in self.pencil_type: #97E0E5
        node.inputs[0].default_value = (0.309469, 0.745404, 0.783538, 1)

    if "Turquoise_Green" in self.pencil_type: #96DDD6
        node.inputs[0].default_value = (0.304987, 0.723055, 0.672443, 1)

    if "Jade_Green" in self.pencil_type: #38C3B9
        node.inputs[0].default_value = (0.0395462, 0.545725, 0.48515, 1)

    if "Juniper_Green" in self.pencil_type: #288A6D
        node.inputs[0].default_value = (0.021219, 0.254152, 0.152926, 1)

    if "Bottle_Green" in self.pencil_type: #1D8B63
        node.inputs[0].default_value = (0.0122865, 0.258183, 0.124772, 1)

    if "Water_Green" in self.pencil_type: #B1E1BC
        node.inputs[0].default_value = (0.439657, 0.752942, 0.502886, 1)

    if "Mineral_Green" in self.pencil_type: #1C8D49
        node.inputs[0].default_value = (0.0116122, 0.266356, 0.0666259, 1)

    if "Emerald_Green" in self.pencil_type: #47BD69
        node.inputs[0].default_value = (0.06301, 0.508881, 0.141263, 1)

    if "Grass_Green" in self.pencil_type: #82CB6B
        node.inputs[0].default_value = (0.223228, 0.597202, 0.147027, 1)

    if "May_Green" in self.pencil_type: #A1D265
        node.inputs[0].default_value = (0.3564, 0.64448, 0.130137, 1)

    if "Sap_Green" in self.pencil_type: #288747
        node.inputs[0].default_value = (0.021219, 0.242281, 0.06301, 1)

    if "Cedar_Green" in self.pencil_type: #3C703A
        node.inputs[0].default_value = (0.0451862, 0.162029, 0.0423114, 1)

    if "Olive_Green" in self.pencil_type: #84993F
        node.inputs[0].default_value = (0.23074, 0.318547, 0.0497066, 1)

    if "Bronze" in self.pencil_type: #836A30
        node.inputs[0].default_value = (0.226966, 0.144129, 0.0295568, 1)

    if "Sepia" in self.pencil_type: #5C5232
        node.inputs[0].default_value = (0.107023, 0.0843762, 0.031896, 1)

    if "Burnt_Umber" in self.pencil_type: #281E1B
        node.inputs[0].default_value = (0.021219, 0.012983, 0.0109601, 1)

    if "Vandyke_Brown" in self.pencil_type: #7D5834
        node.inputs[0].default_value = (0.205079, 0.0975874, 0.0343398, 1)

    if "Raw_Umber" in self.pencil_type: #CA8B34
        node.inputs[0].default_value = (0.590619, 0.258183, 0.0343398, 1)

    if "Brown_Ochre" in self.pencil_type: #D99E3B
        node.inputs[0].default_value = (0.693872, 0.341914, 0.043735, 1)

    if "Raw_Sienna" in self.pencil_type: #FEC44D
        node.inputs[0].default_value = (0.991102, 0.552011, 0.0742136, 1)

    if "Golden_Brown" in self.pencil_type: #F39733
        node.inputs[0].default_value = (0.896269, 0.309469, 0.0331048, 1)

    if "Burnt_Yellow_Ochre" in self.pencil_type: #FD9D3A
        node.inputs[0].default_value = (0.982251, 0.337164, 0.0423114, 1)

    if "Copper_Beach" in self.pencil_type: #89442C
        node.inputs[0].default_value = (0.250158, 0.0578054, 0.0251869, 1)

    if "Burnt_Sienna" in self.pencil_type: #FE993C
        name_color = 'Burnt_Sienna'
        node.inputs[0].default_value = (0.991102, 0.318547, 0.0451862, 1)

    if "Venetia_Red" in self.pencil_type: #B14C2D
        node.inputs[0].default_value = (0.439657, 0.0722718, 0.0262412, 1)
    
    if "Terracotta" in self.pencil_type: #F96733
        node.inputs[0].default_value = (0.947307, 0.135633, 0.0331048, 1)
    
    if "Burnt_Carmine" in self.pencil_type: #FE782E
        node.inputs[0].default_value = (0.991102, 0.187821, 0.0273209, 1)

    if "Chocolate" in self.pencil_type: #25201E
        node.inputs[0].default_value = (0.0185002, 0.0144438, 0.012983, 1)

    if "Ivory_Black" in self.pencil_type: #171E1C
        node.inputs[0].default_value = (0.00856813, 0.012983, 0.0116122, 1)

    if "Blue_Gray" in self.pencil_type: #17597B
        node.inputs[0].default_value = (0.00856813, 0.0998987, 0.198069, 1)

    if "Gun_Metal" in self.pencil_type: #587484
        node.inputs[0].default_value = (0.0975874, 0.174647, 0.23074, 1)

    if "French_Gray" in self.pencil_type: #A4A992
        node.inputs[0].default_value = (0.371238, 0.396755, 0.287441, 1)

    if "Silver_Gray" in self.pencil_type: #C9E4E0
        node.inputs[0].default_value = (0.584078, 0.775822, 0.745404, 1)


    # INKTENSE COLORS #
    if "Sherbert_Lemon" in self.pencil_type: #EBE982
        node.inputs[0].default_value = (0.83077, 0.814847, 0.223228, 1)

    if "Sun_Yellow" in self.pencil_type: #FEF083
        node.inputs[0].default_value = (0.991102, 0.871367, 0.226966, 1)

    if "Cadmium_Yellow" in self.pencil_type: #FDE47D
        node.inputs[0].default_value = (0.982251, 0.775822, 0.205079, 1)

    if "Silician_Yellow" in self.pencil_type: #F5CB8F
        node.inputs[0].default_value = (0.913099, 0.597202, 0.274677, 1)

    if "Golden_Yellow" in self.pencil_type: #F4AD6C
        node.inputs[0].default_value = (0.904661, 0.417885, 0.14996, 1)

    if "Sienna_Gold" in self.pencil_type: #E79167
        node.inputs[0].default_value = (0.799103, 0.283149, 0.135633, 1)

    if "Cadmium_Orange" in self.pencil_type: #F09062
        node.inputs[0].default_value = (0.871367, 0.278894, 0.122139, 1)

    if "Burnt_Orange" in self.pencil_type: #B76D54
        node.inputs[0].default_value = (0.473531, 0.152926, 0.0886556, 1)

    if "Tangerine" in self.pencil_type: #EA7C5C
        node.inputs[0].default_value = (0.822786, 0.201556, 0.107023, 1)

    if "Mid_Vermilion" in self.pencil_type: #D97768
        node.inputs[0].default_value = (0.693872, 0.184475, 0.138432, 1)

    if "Scarlet_Pink" in self.pencil_type: #E26956
        node.inputs[0].default_value = (0.760525, 0.141263, 0.093059, 1)

    if "Poppy_Red" in self.pencil_type: #D85B4E
        node.inputs[0].default_value = (0.686685, 0.104617, 0.0761854, 1)

    if "Hot_Red" in self.pencil_type: #C8554D
        node.inputs[0].default_value = (0.577581, 0.0908417, 0.0742136, 1)

    if "Chilli_Red" in self.pencil_type: #A1524F
        node.inputs[0].default_value = (0.3564, 0.0843762, 0.0781874, 1)

    if "Cherry" in self.pencil_type: #B05350
        node.inputs[0].default_value = (0.434154, 0.0865005, 0.0802198, 1)

    if "Carmine_Pink" in self.pencil_type: #B65658
        node.inputs[0].default_value = (0.467784, 0.093059, 0.0975874, 1)

    if "Crimson" in self.pencil_type: #9C4E53
        node.inputs[0].default_value = (0.332452, 0.0761854, 0.0865005, 1)

    if "Shiraz" in self.pencil_type: #574749
        node.inputs[0].default_value = (0.0953075, 0.06301, 0.0666259, 1)

    if "Red_Violet" in self.pencil_type: #814E5F
        node.inputs[0].default_value = (0.219526, 0.0761854, 0.114435, 1)

    if "Fuchsia" in self.pencil_type: #B85A75
        node.inputs[0].default_value = (0.47932, 0.102242, 0.177888, 1)

    if "Deep_Rose" in self.pencil_type: #8F4B5E
        node.inputs[0].default_value = (0.274677, 0.0703601, 0.111932, 1)

    if "Thistle" in self.pencil_type: #855B7F
        node.inputs[0].default_value = (0.234551, 0.104617, 0.212231, 1)

    if "Dusky_Purple" in self.pencil_type: #3E424A
        node.inputs[0].default_value = (0.0481718, 0.0544803, 0.0684782, 1)

    if "Mauve" in self.pencil_type: #514967
        name_color = 'Mauve'
        node.inputs[0].default_value = (0.0822827, 0.0666259, 0.135633, 1)

    if "Dark_Purple" in self.pencil_type: #504966
        node.inputs[0].default_value = (0.0802198, 0.0666259, 0.132868, 1)

    if "Deep_Violet" in self.pencil_type: #494F67
        node.inputs[0].default_value = (0.0666259, 0.0781874, 0.135633, 1)

    if "Violet" in self.pencil_type: #4D5578
        node.inputs[0].default_value = (0.0742136, 0.0908417, 0.187821, 1)

    if "Lagoon" in self.pencil_type: #414A71
        node.inputs[0].default_value = (0.0528607, 0.0684782, 0.165132, 1)

    if "Peacock_Blue" in self.pencil_type: #3A4877
        node.inputs[0].default_value = (0.0423114, 0.0648033, 0.184475, 1)

    if "Navy_Blue" in self.pencil_type: #405067
        node.inputs[0].default_value = (0.0512695, 0.0802198, 0.135633, 1)

    if "Iron_Blue" in self.pencil_type: #405067
        node.inputs[0].default_value = (0.0512695, 0.0802198, 0.135633, 1)

    if "Deep_Blue" in self.pencil_type: #3C518E
        node.inputs[0].default_value = (0.0451862, 0.0822827, 0.270498, 1)

    if "Iris_Blue" in self.pencil_type: #5E8CC8
        node.inputs[0].default_value = (0.111932, 0.262251, 0.577581, 1)

    if "Bright_Blue" in self.pencil_type: #4D6AA7
        node.inputs[0].default_value = (0.0742136, 0.144129, 0.386429, 1)

    if "Deep_Indigo" in self.pencil_type: #3C4C5D
        node.inputs[0].default_value = (0.0451862, 0.0722718, 0.109462, 1)

    if "Dark_Aquamarine" in self.pencil_type: #34517F
        node.inputs[0].default_value = (0.0343398, 0.0822827, 0.212231, 1)

    if "Turquoise" in self.pencil_type: #51A1C2
        node.inputs[0].default_value = (0.0822827, 0.3564, 0.53948, 1)

    if "Green_Aquamarine" in self.pencil_type: #3E658A
        node.inputs[0].default_value = (0.0481718, 0.130137, 0.254152, 1)

    if "Mallard_Green" in self.pencil_type: #477E8F
        node.inputs[0].default_value = (0.06301, 0.208637, 0.274677, 1)

    if "Teal_Green" in self.pencil_type: #478489
        node.inputs[0].default_value = (0.06301, 0.23074, 0.250158, 1)

    if "Iron_Green" in self.pencil_type: #374C59
        node.inputs[0].default_value = (0.0382044, 0.0722718, 0.0998987, 1)

    if "Ionian_Green" in self.pencil_type: #3C5352
        node.inputs[0].default_value = (0.0451862, 0.0865005, 0.0843762, 1)

    if "Vivid_Green" in self.pencil_type: #518D77
        node.inputs[0].default_value = (0.0822827, 0.266356, 0.184475, 1)

    if "Apple_Green" in self.pencil_type: #7FBA69
        node.inputs[0].default_value = (0.212231, 0.491021, 0.141263, 1)

    if "Field_Green" in self.pencil_type: #496A56
        node.inputs[0].default_value = (0.0666259, 0.144129, 0.093059, 1)

    if "Beech_Green" in self.pencil_type: #3D5853
        node.inputs[0].default_value = (0.0466651, 0.0975874, 0.0865005, 1)

    if "Hookers_Green" in self.pencil_type: #4E7B5D
        node.inputs[0].default_value = (0.0761854, 0.198069, 0.109462, 1)

    if "Felt_Green" in self.pencil_type: #496A56
        node.inputs[0].default_value = (0.0666259, 0.144129, 0.093059, 1)

    if "Light_Olive" in self.pencil_type: #4D5B55
        node.inputs[0].default_value = (0.0742136, 0.104617, 0.0908417, 1)

    if "Spring_Green" in self.pencil_type: #6B8765
        node.inputs[0].default_value = (0.147027, 0.242281, 0.130137, 1)

    if "Fern" in self.pencil_type: #819065
        node.inputs[0].default_value = (0.219526, 0.278894, 0.130137, 1)

    if "Leaf_Green" in self.pencil_type: #545D56
        node.inputs[0].default_value = (0.0886556, 0.109462, 0.093059, 1)

    if "Mustard" in self.pencil_type: #B69066
        node.inputs[0].default_value = (0.467784, 0.278894, 0.132868, 1)

    if "Amber" in self.pencil_type: #8C7560
        node.inputs[0].default_value = (0.262251, 0.177888, 0.116971, 1)

    if "Tan" in self.pencil_type: #947A63
        node.inputs[0].default_value = (0.296138, 0.194618, 0.124772, 1)

    if "Oak" in self.pencil_type: #5E625F
        node.inputs[0].default_value = (0.111932, 0.122139, 0.114435, 1)

    if "Saddle_Brown" in self.pencil_type: #836C61
        node.inputs[0].default_value = (0.226966, 0.14996, 0.119538, 1)

    if "Baked_Earth" in self.pencil_type: #A36C58
        node.inputs[0].default_value = (0.366253, 0.14996, 0.0975874, 1)

    if "Willow" in self.pencil_type: #866556
        node.inputs[0].default_value = (0.238398, 0.130137, 0.093059, 1)

    if "Oxide_Red" in self.pencil_type: #7A524E
        node.inputs[0].default_value = (0.194618, 0.0843762, 0.0761854, 1)

    if "Madder_Brown" in self.pencil_type: #504A4B
        node.inputs[0].default_value = (0.0802198, 0.0684782, 0.0703601, 1)

    if "Dark_Chocolate" in self.pencil_type: #474C50
        node.inputs[0].default_value = (0.06301, 0.0722718, 0.0802198, 1)

    if "Bark" in self.pencil_type: #A56E5A
        node.inputs[0].default_value = (0.376262, 0.155926, 0.102242, 1)

    if "Sepia_Ink" in self.pencil_type: #434E50
        node.inputs[0].default_value = (0.0561285, 0.0761854, 0.0802198, 1)

    if "Indian_Ink" in self.pencil_type: #454F54
        node.inputs[0].default_value = (0.0595112, 0.0781874, 0.0886556, 1)

    if "Chinese_Ink" in self.pencil_type: #344146
        node.inputs[0].default_value = (0.0343398, 0.0528607, 0.0612461, 1)

    if "Charcoal_Gray" in self.pencil_type: #445157
        node.inputs[0].default_value = (0.0578054, 0.0822827, 0.0953075, 1)

    if "Paynes_Gray" in self.pencil_type: #414F5E
        node.inputs[0].default_value = (0.0528607, 0.0781874, 0.111932, 1)

    if "Neutral_Gray" in self.pencil_type: #3E4B50
        node.inputs[0].default_value = (0.0481718, 0.0703601, 0.0802198, 1)

    if "Ink_Black" in self.pencil_type: #39454B
        node.inputs[0].default_value = (0.0409152, 0.0595112, 0.0703601, 1)


    # CONTRAST COLORS #
    if "Blacken" in self.pencil_type: #1D1D1D
        node.inputs[0].default_value = (0.012286, 0.012286, 0.012286, 1)

    if "Dark_Slate" in self.pencil_type: #363636
        node.inputs[0].default_value = (0.036889, 0.036889, 0.036889, 1)

    if "Silver" in self.pencil_type: #D0D0D0
        node.inputs[0].default_value = (0.630757, 0.630757, 0.630757, 1)

