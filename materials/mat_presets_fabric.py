import bpy


def mat_presets_fabric(self, mat):
    

    if "Custom" in self.fabric_type: 
       add_color = self.mat_color


    # CONTRAST COLORS #
    if "Slate" in self.fabric_type: #363636
        add_color = (0.036889, 0.036889, 0.036889, 1)

    if "Silver" in self.fabric_type: #D0D0D0
        add_color = (0.630757, 0.630757, 0.630757, 1)

    if "White" in self.fabric_type:   
        add_color = (1, 1, 1, 1)
                
    if "Gray80" in self.fabric_type:                  
        add_color = (0.603827, 0.603827, 0.603827, 1)

    if "Gray60" in self.fabric_type:                  
        add_color = (0.318547, 0.318547, 0.318547, 1)      
    
    if "Gray50" in self.fabric_type:                  
        add_color = (0.214041, 0.214041, 0.214041, 1)

    if "Gray40" in self.fabric_type:                  
        add_color = (0.132868, 0.132868, 0.132868, 1)  

    if "Gray20" in self.fabric_type:                  
        add_color = (0.0331048, 0.0331048, 0.0331048, 1)

    if "Black" in self.fabric_type:    
        add_color = (0, 0, 0, 1)


    # GREEN COLORS #
    if "Darkgreen" in self.fabric_type: #003A2E  
        add_color = (0, 0.0423114, 0.0273209, 1)   

    if "Hunter" in self.fabric_type: #0A5348 
        add_color = (0.00303527, 0.0865005, 0.0648033, 1) 

    if "Thyme" in self.fabric_type: #475B40 
        add_color = (0.06301, 0.104617, 0.0512695, 1) 
    
    if "Grass_1" in self.fabric_type: #648906
        add_color = (0.127438, 0.250158, 0.00182116, 1) 

    if "Lightgreen" in self.fabric_type: # LIGHTGREEN #62A807 
        add_color = (0.122139, 0.391572, 0.00212469, 1)    

    if "Ino_1" in self.fabric_type: #797E07
        add_color = (0.186706, 0.208637, 0.001518, 1)

    if "Ino_2" in self.fabric_type: #BFD40C
        add_color = (0.520996, 0.658375, 0.003669, 1)
    
    if "Grass_2" in self.fabric_type: #ADC861
        add_color = (0.417885, 0.577581, 0.119538, 1) 
    
    if "Salvia" in self.fabric_type: #CCDFA8 
        add_color = (0.603827, 0.737911, 0.391572, 1) 
    
    if "Pistachio" in self.fabric_type: #C9EE84 
        add_color = (0.584078, 0.854993, 0.23074, 1) 
    
    if "Limette" in self.fabric_type: #E1F6BE 
        add_color = (0.752942, 0.921582, 0.514918, 1) 
    
    if "Lemon" in self.fabric_type: #E6ED6B 
        add_color = (0.791298, 0.846873, 0.147027, 1) 


    # BLUE COLORS #
    if "Bluedark" in self.fabric_type: #1A2131
        add_color = (0.010330, 0.015209, 0.030713, 1) 

    if "Darknavy" in self.fabric_type: #1A2835
        add_color = (0.010330, 0.021219, 0.035601, 1)

    if "Darkroyal_blue_2" in self.fabric_type: #1B1B65
        add_color = (0.010960, 0.010960, 0.130137, 1)

    if "Royal_blue" in self.fabric_type:  #252E8D
        add_color = (0.018500, 0.027321, 0.266356, 1)

    if "Darkroyal_blue_1" in self.fabric_type: #03257C
        add_color = (0.000911, 0.018500, 0.201556, 1)

    if "Blue" in self.fabric_type: #1A7ED0
        add_color = (0.0103298, 0.208637, 0.630757, 1)

    if "Ice" in self.fabric_type: #C2DBE2
        add_color = (0.539480, 0.708376, 0.760525, 1)

    if "Mint" in self.fabric_type:  #7CD0AC
        add_color = (0.201556, 0.630757, 0.412543, 1)

    if "Lightblue" in self.fabric_type: #64C7E6
        add_color = (0.127438, 0.571125, 0.791298, 1)

    if "Grapes" in self.fabric_type:  #3C1742 
        add_color = (0.045186, 0.008568, 0.054480, 1) 

    if "Lightplum" in self.fabric_type: #D263AF
        add_color = (0.644480, 0.124772, 0.428691, 1)

    if "Lilac" in self.fabric_type:#C99CD7
        add_color = (0.584078, 0.332452, 0.679543, 1)


    # BROWN COLORS #
    if "Chocolate" in self.fabric_type: #1F1812
        add_color = (0.013702, 0.009134, 0.006049, 1)

    if "Basalt" in self.fabric_type: #3E3A2E
        add_color = (0.048172, 0.042311, 0.027321, 1)

    if "Morel" in self.fabric_type:  #47301E
        add_color = (0.063010, 0.029557, 0.012983, 1)

    if "Brown" in self.fabric_type:  #5D4529
        add_color = (0.109462, 0.059511, 0.022174, 1)

    if "Noisette" in self.fabric_type: #854F33
        add_color = (0.234551, 0.078187, 0.033105, 1)

    if "Hazelnunt" in self.fabric_type: #C3AA81
        add_color = (0.545725, 0.401978, 0.219526, 1)

    if "Beige" in self.fabric_type: #DFC78B
        add_color = (0.737911, 0.571125, 0.258183, 1)

    if "Champanger" in self.fabric_type: #E6D8B5
        add_color = (0.791298, 0.686685, 0.462077, 1)

    if "Ivory" in self.fabric_type: #EBEBDF
        add_color = (0.830770, 0.830770, 0.737911, 1)

    if "Burgund" in self.fabric_type: #5C0017
        add_color = (0.107023, 0.000000, 0.008568, 1)

    if "Chestnut" in self.fabric_type: #872719
        add_color = (0.242281, 0.020289, 0.009721, 1)

    if "Caramell" in self.fabric_type: #F0AD30
        add_color = (0.871367, 0.417885, 0.0295568, 1)


    # RED COLORS #
    if "Red" in self.fabric_type: #A40410
        add_color = (0.371238, 0.001214, 0.005182, 1)

    if "Scarlet" in self.fabric_type: #E10102
        add_color = (0.752942, 0.000304, 0.000607, 1)

    if "Raspberry" in self.fabric_type: #CF1368
        add_color = (0.623960, 0.006512, 0.138432, 1)

    if "Fuchsia" in self.fabric_type: #B04267
        add_color = (0.434154, 0.054480, 0.135633, 1)

    if "Watermelone" in self.fabric_type: #F56E75
        add_color = (0.913099, 0.155926, 0.177888, 1)

    if "Orange" in self.fabric_type: #FF7D45
        add_color = (1.000000, 0.205079, 0.059511, 1)

    if "Orangered" in self.fabric_type: #FF5B35
        add_color = (1.000000, 0.104617, 0.035601, 1)

    if "Cayenne" in self.fabric_type: #D05833
        add_color = (0.630757, 0.097587, 0.033105, 1)

    if "Peach" in self.fabric_type: #FDD3BB
        add_color = (0.982251, 0.651406, 0.496933, 1)

    if "Rose" in self.fabric_type:  #E5C0C8
        add_color = (0.783538, 0.527115, 0.577581, 1)

    if "Blossom" in self.fabric_type: #EDD6E0
        add_color = (0.846873, 0.672443, 0.745404, 1)

    if "Perlrosa" in self.fabric_type: #FFEBF0
        add_color = (1.000000, 0.830770, 0.871367, 1)


    # YELLOW COLORS #
    if "Mustard" in self.fabric_type: #D9AE2B
        add_color = (0.693872, 0.423268, 0.024158, 1)

    if "Gold" in self.fabric_type: #D1B665
        add_color = (0.637597, 0.467784, 0.130137, 1)

    if "Yelloworange" in self.fabric_type: #FCB333
        add_color = (0.973445, 0.450786, 0.033105, 1)

    if "Corn" in self.fabric_type: #F6C449
        add_color = (0.921582, 0.552011, 0.066626, 1)

    if "Bumblebee" in self.fabric_type: #F4D90C
        add_color = (0.904661, 0.693872, 0.003677, 1)

    if "Sungold" in self.fabric_type: #FBD206
        add_color = (0.964686, 0.644480, 0.001821, 1)

    if "Daffoldil" in self.fabric_type: #FBDE04
        add_color = (0.964686, 0.730461, 0.001214, 1)

    if "Canary" in self.fabric_type: #FCEE45
        add_color = (0.973445, 0.854993, 0.059511, 1)

    if "Lemongrass" in self.fabric_type: #F6FE77
        add_color = (0.921582, 0.991102, 0.184475, 1)

    if "Banana" in self.fabric_type: #F9EE84
        add_color = (0.947307, 0.854993, 0.230740, 1)

    if "Vanille" in self.fabric_type: #EDE6A2
        add_color = (0.846873, 0.791298, 0.361307, 1)

    if "Creme" in self.fabric_type: #FAF9C9
        add_color = (0.955973, 0.947307, 0.584078, 1)

    if "Custom" not in self.fabric_type:
        mat.diffuse_color = add_color


