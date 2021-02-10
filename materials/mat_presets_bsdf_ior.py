import bpy
from ..utilities.utils import get_prefs

def mat_presets_bsdf_ior(self, node):     

    if self.mat_ior_values == 'ior001':  
        node.inputs[14].default_value = 1.360
    if self.mat_ior_values == 'ior002': 
         node.inputs[14].default_value = 1.491
    if self.mat_ior_values == 'ior003':  
        node.inputs[14].default_value = 1.618
    if self.mat_ior_values == 'ior004':  
        node.inputs[14].default_value = 1.550
    if self.mat_ior_values == 'ior005':  
        node.inputs[14].default_value = 1.547
    if self.mat_ior_values == 'ior006':  
        node.inputs[14].default_value = 1.540
    if self.mat_ior_values == 'ior007':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior008':  
        node.inputs[14].default_value = 1.329
    if self.mat_ior_values == 'ior009':  
        node.inputs[14].default_value = 1.360
    if self.mat_ior_values == 'ior010':  
        node.inputs[14].default_value = 1.329
    if self.mat_ior_values == 'ior011':  
        node.inputs[14].default_value = 1.750
    if self.mat_ior_values == 'ior012':  
        node.inputs[14].default_value = 1.244
    if self.mat_ior_values == 'ior013':  
        node.inputs[14].default_value = 1.244
    if self.mat_ior_values == 'ior014':  
        node.inputs[14].default_value = 2.700
    if self.mat_ior_values == 'ior015':  
        node.inputs[14].default_value = 1.665
    if self.mat_ior_values == 'ior016': 
        node.inputs[14].default_value = 1.543
    if self.mat_ior_values == 'ior017':  
        node.inputs[14].default_value = 1.611
    if self.mat_ior_values == 'ior018':  
        node.inputs[14].default_value = 1.544
    if self.mat_ior_values == 'ior019':  
        node.inputs[14].default_value = 1.600
    if self.mat_ior_values == 'ior020':  
        node.inputs[14].default_value = 2.920
    if self.mat_ior_values == 'ior021': 
        node.inputs[14].default_value = 2.490
    if self.mat_ior_values == 'ior022':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior023':  
        node.inputs[14].default_value = 1.571
    if self.mat_ior_values == 'ior024':  
        node.inputs[14].default_value = 1.426
    if self.mat_ior_values == 'ior025':  
        node.inputs[14].default_value = 1.536
    if self.mat_ior_values == 'ior026':  
        node.inputs[14].default_value = 1.567
    if self.mat_ior_values == 'ior027':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior028':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior029':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior030':  
        node.inputs[14].default_value = 1.635
    if self.mat_ior_values == 'ior031':  
        node.inputs[14].default_value = 1.574
    if self.mat_ior_values == 'ior032':  
        node.inputs[14].default_value = 1.689
    if self.mat_ior_values == 'ior033':  
        node.inputs[14].default_value = 1.675
    if self.mat_ior_values == 'ior034':  
        node.inputs[14].default_value = 1.730 
    if self.mat_ior_values == 'ior035':  
        node.inputs[14].default_value = 1.636
    if self.mat_ior_values == 'ior036':  
        node.inputs[14].default_value = 1.684
    if self.mat_ior_values == 'ior037':  
        node.inputs[14].default_value = 1.345
    if self.mat_ior_values == 'ior038':  
        node.inputs[14].default_value = 1.757
    if self.mat_ior_values == 'ior039':  
        node.inputs[14].default_value = 1.501
    if self.mat_ior_values == 'ior040':  
        node.inputs[14].default_value = 1.635
    if self.mat_ior_values == 'ior041':  
        node.inputs[14].default_value = 1.579
    if self.mat_ior_values == 'ior042': 
        node.inputs[14].default_value = 1.553
    if self.mat_ior_values == 'ior043':  
        node.inputs[14].default_value = 1.446
    if self.mat_ior_values == 'ior044':  
        node.inputs[14].default_value = 1.603
    if self.mat_ior_values == 'ior045':  
        node.inputs[14].default_value = 1.661
    if self.mat_ior_values == 'ior046':  
        node.inputs[14].default_value = 1.180
    if self.mat_ior_values == 'ior047':  
        node.inputs[14].default_value = 1.567 
    if self.mat_ior_values == 'ior048':  
        node.inputs[14].default_value = 1.486
    if self.mat_ior_values == 'ior049':  
        node.inputs[14].default_value = 1.573
    if self.mat_ior_values == 'ior050':  
        node.inputs[14].default_value = 1.491
    if self.mat_ior_values == 'ior051':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior052':  
        node.inputs[14].default_value = 1.628
    if self.mat_ior_values == 'ior053':  
        node.inputs[14].default_value = 1.460
    if self.mat_ior_values == 'ior054':  
        node.inputs[14].default_value = 1.340
    if self.mat_ior_values == 'ior055':  
        node.inputs[14].default_value = 1.997
    if self.mat_ior_values == 'ior056':  
        node.inputs[14].default_value = 1.622
    if self.mat_ior_values == 'ior057':  
        node.inputs[14].default_value = 1.804
    if self.mat_ior_values == 'ior058':  
        node.inputs[14].default_value = 1.770
    if self.mat_ior_values == 'ior059':  
        node.inputs[14].default_value = 1.549
    if self.mat_ior_values == 'ior060':  
        node.inputs[14].default_value = 1.510
    if self.mat_ior_values == 'ior061':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior062':  
        node.inputs[14].default_value = 1.001
    if self.mat_ior_values == 'ior063':  
        node.inputs[14].default_value = 1.385
    if self.mat_ior_values == 'ior064':  
        node.inputs[14].default_value = 2.400
    if self.mat_ior_values == 'ior065':  
        node.inputs[14].default_value = 2.420
    if self.mat_ior_values == 'ior066':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior067':  
        node.inputs[14].default_value = 2.310
    if self.mat_ior_values == 'ior068':  
        node.inputs[14].default_value = 2.970
    if self.mat_ior_values == 'ior069':  
        node.inputs[14].default_value = 2.705
    if self.mat_ior_values == 'ior070':  
        node.inputs[14].default_value = 1.745
    if self.mat_ior_values == 'ior071':  
        node.inputs[14].default_value = 1.500
    if self.mat_ior_values == 'ior072':  
        node.inputs[14].default_value = 1.534
    if self.mat_ior_values == 'ior073':  
        node.inputs[14].default_value = 3.020
    if self.mat_ior_values == 'ior074':  
        node.inputs[14].default_value = 1.532
    if self.mat_ior_values == 'ior075':  
        node.inputs[14].default_value = 1.293
    if self.mat_ior_values == 'ior076':  
        node.inputs[14].default_value = 1.625
    if self.mat_ior_values == 'ior077':  
        node.inputs[14].default_value = 1.724
    if self.mat_ior_values == 'ior078':  
        node.inputs[14].default_value = 1.740
    if self.mat_ior_values == 'ior079':  
        node.inputs[14].default_value = 1.970
    if self.mat_ior_values == 'ior080':  
        node.inputs[14].default_value = 1.710
    if self.mat_ior_values == 'ior081':  
        node.inputs[14].default_value = 1.586
    if self.mat_ior_values == 'ior082':  
        node.inputs[14].default_value = 1.765
    if self.mat_ior_values == 'ior083':  
        node.inputs[14].default_value = 2.705
    if self.mat_ior_values == 'ior084':  
        node.inputs[14].default_value = 1.486
    if self.mat_ior_values == 'ior085':  
        node.inputs[14].default_value = 1.540
    if self.mat_ior_values == 'ior086':  
        node.inputs[14].default_value = 1.766
    if self.mat_ior_values == 'ior087':  
        node.inputs[14].default_value = 1.351
    if self.mat_ior_values == 'ior088':  
        node.inputs[14].default_value = 2.310
    if self.mat_ior_values == 'ior089':  
        node.inputs[14].default_value = 2.160
    if self.mat_ior_values == 'ior090':  
        node.inputs[14].default_value = 1.620
    if self.mat_ior_values == 'ior091':  
        node.inputs[14].default_value = 1.520
    if self.mat_ior_values == 'ior092':  
        node.inputs[14].default_value = 1.338
    if self.mat_ior_values == 'ior093':  
        node.inputs[14].default_value = 1.750
    if self.mat_ior_values == 'ior094':  
        node.inputs[14].default_value = 2.000
    if self.mat_ior_values == 'ior095':  
        node.inputs[14].default_value = 2.165
    if self.mat_ior_values == 'ior096':  
        node.inputs[14].default_value = 2.850 
    if self.mat_ior_values == 'ior097':  
        node.inputs[14].default_value = 1.634
    if self.mat_ior_values == 'ior098':  
        node.inputs[14].default_value = 2.418
    if self.mat_ior_values == 'ior099':  
        node.inputs[14].default_value = 1.680
    if self.mat_ior_values == 'ior100':  
        node.inputs[14].default_value = 1.503
    if self.mat_ior_values == 'ior101':  
        node.inputs[14].default_value = 1.686 
    if self.mat_ior_values == 'ior102':  
        node.inputs[14].default_value = 1.660
    if self.mat_ior_values == 'ior103':  
        node.inputs[14].default_value = 1.600
    if self.mat_ior_values == 'ior104':  
        node.inputs[14].default_value = 1.532
    if self.mat_ior_values == 'ior105':  
        node.inputs[14].default_value = 1.583
    if self.mat_ior_values == 'ior106':  
        node.inputs[14].default_value = 1.586
    if self.mat_ior_values == 'ior107':  
        node.inputs[14].default_value = 1.561
    if self.mat_ior_values == 'ior108':  
        node.inputs[14].default_value = 1.568
    if self.mat_ior_values == 'ior109':  
        node.inputs[14].default_value = 1.663
    if self.mat_ior_values == 'ior110':  
        node.inputs[14].default_value = 1.733
    if self.mat_ior_values == 'ior111':  
        node.inputs[14].default_value = 1.360
    if self.mat_ior_values == 'ior112':  
        node.inputs[14].default_value = 1.360
    if self.mat_ior_values == 'ior113':  
        node.inputs[14].default_value = 1.652
    if self.mat_ior_values == 'ior114':  
        node.inputs[14].default_value = 1.330
    if self.mat_ior_values == 'ior115':  
        node.inputs[14].default_value = 1.380
    if self.mat_ior_values == 'ior116':  
        node.inputs[14].default_value = 1.410
    if self.mat_ior_values == 'ior117':  
        node.inputs[14].default_value = 1.340
    if self.mat_ior_values == 'ior118':  
        node.inputs[14].default_value = 2.409
    if self.mat_ior_values == 'ior119':  
        node.inputs[14].default_value = 1.532
    if self.mat_ior_values == 'ior120':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior121':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior122':  
        node.inputs[14].default_value = 1.565
    if self.mat_ior_values == 'ior123':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior124':  
        node.inputs[14].default_value = 1.539
    if self.mat_ior_values == 'ior125':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior126':  
        node.inputs[14].default_value = 1.724
    if self.mat_ior_values == 'ior127':  
        node.inputs[14].default_value = 1.610
    if self.mat_ior_values == 'ior128':  
        node.inputs[14].default_value = 1.433
    if self.mat_ior_values == 'ior129':  
        node.inputs[14].default_value = 1.560
    if self.mat_ior_values == 'ior130':  
        node.inputs[14].default_value = 1.434
    if self.mat_ior_values == 'ior131':  
        node.inputs[14].default_value = 1.470
    if self.mat_ior_values == 'ior132':  
        node.inputs[14].default_value = 1.460 
    if self.mat_ior_values == 'ior133':  
        node.inputs[14].default_value = 3.927
    if self.mat_ior_values == 'ior134':  
        node.inputs[14].default_value = 3.500
    if self.mat_ior_values == 'ior135':  
        node.inputs[14].default_value = 1.760
    if self.mat_ior_values == 'ior136':  
        node.inputs[14].default_value = 1.790
    if self.mat_ior_values == 'ior137':  
        node.inputs[14].default_value = 1.820
    if self.mat_ior_values == 'ior138':  
        node.inputs[14].default_value = 1.890
    if self.mat_ior_values == 'ior139':  
        node.inputs[14].default_value = 1.760
    if self.mat_ior_values == 'ior140':  
        node.inputs[14].default_value = 1.745
    if self.mat_ior_values == 'ior141':  
        node.inputs[14].default_value = 1.795
    if self.mat_ior_values == 'ior142':  
        node.inputs[14].default_value = 1.745
    if self.mat_ior_values == 'ior143':  
        node.inputs[14].default_value = 1.755
    if self.mat_ior_values == 'ior144': 
        node.inputs[14].default_value = 1.810
    if self.mat_ior_values == 'ior145':  
        node.inputs[14].default_value = 1.742
    if self.mat_ior_values == 'ior146':  
        node.inputs[14].default_value = 1.805
    if self.mat_ior_values == 'ior147':  
        node.inputs[14].default_value = 1.517
    if self.mat_ior_values == 'ior148':  
        node.inputs[14].default_value = 1.500
    if self.mat_ior_values == 'ior149':  
        node.inputs[14].default_value = 1.489
    if self.mat_ior_values == 'ior150':  
        node.inputs[14].default_value = 2.040
    if self.mat_ior_values == 'ior151': 
        node.inputs[14].default_value = 1.520
    if self.mat_ior_values == 'ior152':  
        node.inputs[14].default_value = 1.517
    if self.mat_ior_values == 'ior153':  
        node.inputs[14].default_value = 1.569
    if self.mat_ior_values == 'ior154':  
        node.inputs[14].default_value = 1.669
    if self.mat_ior_values == 'ior155':  
        node.inputs[14].default_value = 1.805
    if self.mat_ior_values == 'ior156':  
        node.inputs[14].default_value = 1.660
    if self.mat_ior_values == 'ior157':  
        node.inputs[14].default_value = 1.890
    if self.mat_ior_values == 'ior158':  
        node.inputs[14].default_value = 1.655
    if self.mat_ior_values == 'ior159':  
        node.inputs[14].default_value = 1.800
    if self.mat_ior_values == 'ior160':  
        node.inputs[14].default_value = 1.580
    if self.mat_ior_values == 'ior161':  
        node.inputs[14].default_value = 1.627
    if self.mat_ior_values == 'ior162':  
        node.inputs[14].default_value = 1.459
    if self.mat_ior_values == 'ior163':  
        ode.inputs[14].default_value = 1.474
    if self.mat_ior_values == 'ior164':  
        node.inputs[14].default_value = 1.473
    if self.mat_ior_values == 'ior165':  
        node.inputs[14].default_value = 1.473
    if self.mat_ior_values == 'ior166':  
        node.inputs[14].default_value = 0.470
    if self.mat_ior_values == 'ior167':  
        node.inputs[14].default_value = 1.519
    if self.mat_ior_values == 'ior168':  
        node.inputs[14].default_value = 1.559
    if self.mat_ior_values == 'ior169':  
        node.inputs[14].default_value = 1.497
    if self.mat_ior_values == 'ior170':  
        node.inputs[14].default_value = 1.502
    if self.mat_ior_values == 'ior171':  
        node.inputs[14].default_value = 1.890
    if self.mat_ior_values == 'ior172':  
        node.inputs[14].default_value = 1.650
    if self.mat_ior_values == 'ior173':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior174':  
        node.inputs[14].default_value = 2.940
    if self.mat_ior_values == 'ior175':  
        node.inputs[14].default_value = 1.614
    if self.mat_ior_values == 'ior176':  
        node.inputs[14].default_value = 1.655
    if self.mat_ior_values == 'ior177':  
        node.inputs[14].default_value = 1.504
    if self.mat_ior_values == 'ior178':  
        node.inputs[14].default_value = 1.494
    if self.mat_ior_values == 'ior179':  
        node.inputs[14].default_value = 1.484
    if self.mat_ior_values == 'ior180':  
        node.inputs[14].default_value = 1.586
    if self.mat_ior_values == 'ior181':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior182':  
        node.inputs[14].default_value = 1.097
    if self.mat_ior_values == 'ior183':  
        node.inputs[14].default_value = 1.670  
    if self.mat_ior_values == 'ior184':  
        node.inputs[14].default_value = 1.309
    if self.mat_ior_values == 'ior185':  
        node.inputs[14].default_value = 1.713
    if self.mat_ior_values == 'ior186':  
        node.inputs[14].default_value = 3.340
    if self.mat_ior_values == 'ior187':  
        node.inputs[14].default_value = 1.550
    if self.mat_ior_values == 'ior188':  
        node.inputs[14].default_value = 2.950
    if self.mat_ior_values == 'ior189':  
        node.inputs[14].default_value = 1.540 
    if self.mat_ior_values == 'ior190':  
        node.inputs[14].default_value = 1.653
    if self.mat_ior_values == 'ior191':  
        node.inputs[14].default_value = 1.620
    if self.mat_ior_values == 'ior192':  
        node.inputs[14].default_value = 1.665
    if self.mat_ior_values == 'ior193':  
        node.inputs[14].default_value = 1.540
    if self.mat_ior_values == 'ior194':  
        node.inputs[14].default_value = 1.660  
    if self.mat_ior_values == 'ior195':  
        node.inputs[14].default_value = 1.665
    if self.mat_ior_values == 'ior196':  
        node.inputs[14].default_value = 1.668
    if self.mat_ior_values == 'ior197':  
        node.inputs[14].default_value = 1.715 
    if self.mat_ior_values == 'ior198':  
        node.inputs[14].default_value = 1.566
    if self.mat_ior_values == 'ior199':  
        node.inputs[14].default_value = 1.500
    if self.mat_ior_values == 'ior200':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior201':  
        node.inputs[14].default_value = 1.615
    if self.mat_ior_values == 'ior202':  
        node.inputs[14].default_value = 2.010
    if self.mat_ior_values == 'ior203':  
        node.inputs[14].default_value = 1.782
    if self.mat_ior_values == 'ior204':  
        node.inputs[14].default_value = 1.509
    if self.mat_ior_values == 'ior205':  
        node.inputs[14].default_value = 1.575
    if self.mat_ior_values == 'ior206':  
        node.inputs[14].default_value = 1.200
    if self.mat_ior_values == 'ior207':  
        node.inputs[14].default_value = 1.333
    if self.mat_ior_values == 'ior208':  
        node.inputs[14].default_value = 1.495 
    if self.mat_ior_values == 'ior209':  
        node.inputs[14].default_value = 1.515
    if self.mat_ior_values == 'ior210':  
        node.inputs[14].default_value = 1.655
    if self.mat_ior_values == 'ior211':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior212':  
        node.inputs[14].default_value = 1.620
    if self.mat_ior_values == 'ior213':  
        node.inputs[14].default_value = 1.329
    if self.mat_ior_values == 'ior214':  
        node.inputs[14].default_value = 1.350
    if self.mat_ior_values == 'ior215':  
        node.inputs[14].default_value = 2.675
    if self.mat_ior_values == 'ior216':  
        node.inputs[14].default_value = 1.500
    if self.mat_ior_values == 'ior217':  
        node.inputs[14].default_value = 1.522
    if self.mat_ior_values == 'ior218':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior219':  
        node.inputs[14].default_value = 1.535
    if self.mat_ior_values == 'ior220':  
        node.inputs[14].default_value = 1.590
    if self.mat_ior_values == 'ior221':  
        node.inputs[14].default_value = 1.650 
    if self.mat_ior_values == 'ior222': 
        node.inputs[14].default_value = 1.480
    if self.mat_ior_values == 'ior223':  
        node.inputs[14].default_value = 1.600
    if self.mat_ior_values == 'ior224':  
        node.inputs[14].default_value = 1.080
    if self.mat_ior_values == 'ior225':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior226':  
        node.inputs[14].default_value = 1.205
    if self.mat_ior_values == 'ior227':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior228':  
        node.inputs[14].default_value = 1.495
    if self.mat_ior_values == 'ior229':  
        node.inputs[14].default_value = 1.536
    if self.mat_ior_values == 'ior230':  
        node.inputs[14].default_value = 1.535
    if self.mat_ior_values == 'ior231':  
        node.inputs[14].default_value = 1.481
    if self.mat_ior_values == 'ior232':  
        node.inputs[14].default_value = 1.482
    if self.mat_ior_values == 'ior233':  
        node.inputs[14].default_value = 1.473
    if self.mat_ior_values == 'ior234':  
        node.inputs[14].default_value = 1.466
    if self.mat_ior_values == 'ior235':  
        node.inputs[14].default_value = 1.470
    if self.mat_ior_values == 'ior236':  
        node.inputs[14].default_value = 1.670
    if self.mat_ior_values == 'ior237':  
        node.inputs[14].default_value = 1.486
    if self.mat_ior_values == 'ior238':  
        node.inputs[14].default_value = 1.486
    if self.mat_ior_values == 'ior239':  
        node.inputs[14].default_value = 1.450
    if self.mat_ior_values == 'ior240':  
        node.inputs[14].default_value = 1.450
    if self.mat_ior_values == 'ior241':  
        node.inputs[14].default_value = 1.445
    if self.mat_ior_values == 'ior242':  
        node.inputs[14].default_value = 1.450
    if self.mat_ior_values == 'ior243':  
        node.inputs[14].default_value = 1.566
    if self.mat_ior_values == 'ior244':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior245':  
        node.inputs[14].default_value = 1.221  
    if self.mat_ior_values == 'ior246':  
        node.inputs[14].default_value = 1.766
    if self.mat_ior_values == 'ior247':  
        node.inputs[14].default_value = 1.787
    if self.mat_ior_values == 'ior248':  
        node.inputs[14].default_value = 1.610
    if self.mat_ior_values == 'ior249':  
        node.inputs[14].default_value = 1.740
    if self.mat_ior_values == 'ior250':  
        node.inputs[14].default_value = 1.525
    if self.mat_ior_values == 'ior251':  
        node.inputs[14].default_value = 1.575
    if self.mat_ior_values == 'ior252':  
        node.inputs[14].default_value = 1.502
    if self.mat_ior_values == 'ior253':  
        node.inputs[14].default_value = 1.570
    if self.mat_ior_values == 'ior254':  
        node.inputs[14].default_value = 1.650
    if self.mat_ior_values == 'ior255':  
        node.inputs[14].default_value = 2.117
    if self.mat_ior_values == 'ior256':  
        node.inputs[14].default_value = 1.460
    if self.mat_ior_values == 'ior257':  
        node.inputs[14].default_value = 2.330
    if self.mat_ior_values == 'ior258':  
        node.inputs[14].default_value = 1.500
    if self.mat_ior_values == 'ior259':  
        node.inputs[14].default_value = 1.490
    if self.mat_ior_values == 'ior260':  
        node.inputs[14].default_value = 1.584
    if self.mat_ior_values == 'ior261':  
        node.inputs[14].default_value = 1.550
    if self.mat_ior_values == 'ior262':  
        node.inputs[14].default_value = 1.540
    if self.mat_ior_values == 'ior263':  
        node.inputs[14].default_value = 1.540
    if self.mat_ior_values == 'ior264':  
        node.inputs[14].default_value = 1.610
    if self.mat_ior_values == 'ior265':  
        node.inputs[14].default_value = 2.790
    if self.mat_ior_values == 'ior266':  
        node.inputs[14].default_value = 1.840
    if self.mat_ior_values == 'ior267':  
        node.inputs[14].default_value = 1.810
    if self.mat_ior_values == 'ior268':  
        node.inputs[14].default_value = 1.740
    if self.mat_ior_values == 'ior269':  
        node.inputs[14].default_value = 1.594
    if self.mat_ior_values == 'ior270':  
        node.inputs[14].default_value = 1.458  
    if self.mat_ior_values == 'ior271':  
        node.inputs[14].default_value = 1.690
    if self.mat_ior_values == 'ior272':  
        node.inputs[14].default_value = 1.600
    if self.mat_ior_values == 'ior273':  
        node.inputs[14].default_value = 1.735
    if self.mat_ior_values == 'ior274':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior275':  
        node.inputs[14].default_value = 1.519
    if self.mat_ior_values == 'ior276':  
        node.inputs[14].default_value = 1.768
    if self.mat_ior_values == 'ior277':  
        node.inputs[14].default_value = 1.361
    if self.mat_ior_values == 'ior278':  
        node.inputs[14].default_value = 2.620 
    if self.mat_ior_values == 'ior279':  
        node.inputs[14].default_value = 1.544
    if self.mat_ior_values == 'ior280':  
        node.inputs[14].default_value = 1.522
    if self.mat_ior_values == 'ior291':  
        node.inputs[14].default_value = 1.768
    if self.mat_ior_values == 'ior292':  
        node.inputs[14].default_value = 1.766
    if self.mat_ior_values == 'ior293':  
        node.inputs[14].default_value = 1.540
    if self.mat_ior_values == 'ior294':  
        node.inputs[14].default_value = 1.555
    if self.mat_ior_values == 'ior295':  
        node.inputs[14].default_value = 1.920
    if self.mat_ior_values == 'ior296':  
        node.inputs[14].default_value = 2.920
    if self.mat_ior_values == 'ior297':  
        node.inputs[14].default_value = 1.560
    if self.mat_ior_values == 'ior298':  
        node.inputs[14].default_value = 1.362
    if self.mat_ior_values == 'ior299':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior290':  
        node.inputs[14].default_value = 1.510
    if self.mat_ior_values == 'ior291':  
        node.inputs[14].default_value = 4.130
    if self.mat_ior_values == 'ior292':  
        node.inputs[14].default_value = 1.658
    if self.mat_ior_values == 'ior293':  
        node.inputs[14].default_value = 0.765
    if self.mat_ior_values == 'ior294':  
        node.inputs[14].default_value = 1.699
    if self.mat_ior_values == 'ior295':  
        node.inputs[14].default_value = 1.608
    if self.mat_ior_values == 'ior296':  
        node.inputs[14].default_value = 1.621
    if self.mat_ior_values == 'ior297':  
        node.inputs[14].default_value = 1.483
    if self.mat_ior_values == 'ior298':  
        node.inputs[14].default_value = 1.594
    if self.mat_ior_values == 'ior299':  
        node.inputs[14].default_value = 1.780
    if self.mat_ior_values == 'ior300':  
        node.inputs[14].default_value = 2.368
    if self.mat_ior_values == 'ior301':  
        node.inputs[14].default_value = 1.885
    if self.mat_ior_values == 'ior302':  
        node.inputs[14].default_value = 1.715
    if self.mat_ior_values == 'ior303':  
        node.inputs[14].default_value = 1.730
    if self.mat_ior_values == 'ior304':  
        node.inputs[14].default_value = 1.722
    if self.mat_ior_values == 'ior305':  
        node.inputs[14].default_value = 1.650
    if self.mat_ior_values == 'ior306':  
        node.inputs[14].default_value = 1.767
    if self.mat_ior_values == 'ior307':  
        node.inputs[14].default_value = 1.739
    if self.mat_ior_values == 'ior308':  
        node.inputs[14].default_value = 1.539
    if self.mat_ior_values == 'ior309':  
        node.inputs[14].default_value = 2.500
    if self.mat_ior_values == 'ior310':  
        node.inputs[14].default_value = 1.520
    if self.mat_ior_values == 'ior311':  
        node.inputs[14].default_value = 2.410
    if self.mat_ior_values == 'ior312':  
        node.inputs[14].default_value = 1.595
    if self.mat_ior_values == 'ior313':  
        node.inputs[14].default_value = 1.519
    if self.mat_ior_values == 'ior314':  
        node.inputs[14].default_value = 1.380
    if self.mat_ior_values == 'ior315': 
        node.inputs[14].default_value = 1.490
    if self.mat_ior_values == 'ior316':  
        node.inputs[14].default_value = 1.960
    if self.mat_ior_values == 'ior317':  
        node.inputs[14].default_value = 1.730 
    if self.mat_ior_values == 'ior318':  
        node.inputs[14].default_value = 1.720
    if self.mat_ior_values == 'ior319':  
        node.inputs[14].default_value = 2.240
    if self.mat_ior_values == 'ior320':  
        node.inputs[14].default_value = 1.696
    if self.mat_ior_values == 'ior321':  
        node.inputs[14].default_value = 1.365
    if self.mat_ior_values == 'ior322':  
        node.inputs[14].default_value = 1.530
    if self.mat_ior_values == 'ior323':  
        node.inputs[14].default_value = 1.544
    if self.mat_ior_values == 'ior324':  
        node.inputs[14].default_value = 2.106
    if self.mat_ior_values == 'ior325':  
        node.inputs[14].default_value = 2.160
    if self.mat_ior_values == 'ior326':  
        node.inputs[14].default_value = 1.617
    if self.mat_ior_values == 'ior327':  
        node.inputs[14].default_value = 1.610
    if self.mat_ior_values == 'ior328':  
        node.inputs[14].default_value = 1.625
    if self.mat_ior_values == 'ior329':  
        node.inputs[14].default_value = 1.620
    if self.mat_ior_values == 'ior330':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior331':  
        node.inputs[14].default_value = 1.620
    if self.mat_ior_values == 'ior332':  
        node.inputs[14].default_value = 1.629
    if self.mat_ior_values == 'ior333':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior334':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior335':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior336':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior337':  
        node.inputs[14].default_value = 1.625
    if self.mat_ior_values == 'ior338':  
        node.inputs[14].default_value = 1.600
    if self.mat_ior_values == 'ior339':  
        node.inputs[14].default_value = 1.496
    if self.mat_ior_values == 'ior340':  
        node.inputs[14].default_value = 1.472
    if self.mat_ior_values == 'ior341':  
        node.inputs[14].default_value = 1.630
    if self.mat_ior_values == 'ior342':  
        node.inputs[14].default_value = 1.490
    if self.mat_ior_values == 'ior343':  
        node.inputs[14].default_value = 1.870
    if self.mat_ior_values == 'ior344':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior345':  
        node.inputs[14].default_value = 1.550
    if self.mat_ior_values == 'ior346':  
        node.inputs[14].default_value = 1.580
    if self.mat_ior_values == 'ior347':  
        node.inputs[14].default_value = 1.363
    if self.mat_ior_values == 'ior348':  
        node.inputs[14].default_value = 1.590
    if self.mat_ior_values == 'ior349':  
        node.inputs[14].default_value = 1.333
    if self.mat_ior_values == 'ior350':  
        node.inputs[14].default_value = 1.318
    if self.mat_ior_values == 'ior351':  
        node.inputs[14].default_value = 1.333
    if self.mat_ior_values == 'ior352':  
        node.inputs[14].default_value = 1.000
    if self.mat_ior_values == 'ior353':  
        node.inputs[14].default_value = 1.325
    if self.mat_ior_values == 'ior354':  
        node.inputs[14].default_value = 1.310
    if self.mat_ior_values == 'ior355':  
        node.inputs[14].default_value = 1.356
    if self.mat_ior_values == 'ior356':  
        node.inputs[14].default_value = 2.300   
    if self.mat_ior_values == 'ior357':  
        node.inputs[14].default_value = 1.517
    if self.mat_ior_values == 'ior358':  
        node.inputs[14].default_value = 2.010
    if self.mat_ior_values == 'ior359':  
        node.inputs[14].default_value = 1.875
    if self.mat_ior_values == 'ior360':  
        node.inputs[14].default_value = 1.960
    if self.mat_ior_values == 'ior361':  
        node.inputs[14].default_value = 1.800
    if self.mat_ior_values == 'ior362':  
        node.inputs[14].default_value = 2.192 
    if self.mat_ior_values == 'ior000':  
        node.inputs[14].default_value = self.mat_ior

