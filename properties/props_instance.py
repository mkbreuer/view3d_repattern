import bpy

from bpy.props import StringProperty, EnumProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, BoolVectorProperty
from ..utilities.units import get_current_units, bu_to_unit, unit_to_bu

# RP: WRAP PRIMITIVES AND INSTANCES # 
class PropsGroup_Instance(bpy.types.PropertyGroup):
  
    collapse_toggle : BoolProperty(name="Close Collections", description="close all collections", default=False)   
    collapse_parent : BoolProperty(name="Parent Collections", description="parent to scene or under child collections", default=False)   
    purge_data : BoolProperty(name="",  description="purge unused after deleting objects from collection", default=True) 
    lock_instances : BoolProperty(name="NoSelect",  description="restrict viewport selection for instances", default=True)   
    wired_instances : BoolProperty(name="Wired",  description="set display draw type: wire", default=True)   
    parent_instances : BoolProperty(name="Parent",  description="parent wrap around instances to center field", default=False)  
    editmode_toggle : BoolProperty(name="Editmode", description="toggle to editmode", default=True)   
    uvmap_toggle : BoolProperty(name="UV Map", description="create uv map", default=False)   

    # INSTANCES #
    
    use_custom_name : BoolProperty(name="Use Custom Name",  description="on/off", default=False, options={'SKIP_SAVE'})   
    tp_name_prefix : StringProperty(name="Name", default="Wrap_")       
    tp_name_object : StringProperty(name="Name", default="Instance")
    tp_name_suffix : StringProperty(name="Name", default="_Center")     
  
    use_custom_wrap : BoolProperty(name="Use Custom Wrap",  description="on/off", default=False, options={'SKIP_SAVE'})   
    tp_wrap_prefix : StringProperty(name="Name", default="Wrap_")       
    tp_wrap_object : StringProperty(name="Name", default="Instance")
    tp_wrap_suffix : StringProperty(name="Name", default="_Grid")     

    use_custom_group : BoolProperty(name="Use Custom Name",  description="on/off", default=False, options={'SKIP_SAVE'})    
    tp_group_prefix : StringProperty(name="Name", default="Wrap_")       
    tp_group_name : StringProperty(name="Name", default="Instance")
    tp_group_suffix : StringProperty(name="Name", default="_Group")  
 
    wrap_instances : BoolProperty(name="Wrap",  description="switch to wrap around primitiv or selected", default=False)  

    tp_geom_result : EnumProperty( 
       items = [("32px",    "0.313m", "32px/26dpi/0.313m",  "", 1),
                ("64px",    "0.625m", "64px/26dpi/0.625m",  "", 2), 
                ("128px",   "0.125m", "128px/26dpi/0.125m", "", 3), 
                ("256px",   "0.25m",  "256px/26dpi/0.25m",  "", 4), 
                ("512px",   "0.5m",   "512px/26dpi/0.5m",   "", 5), 
                ("1024px",  "1m",     "1024px/26dpi/1m",    "", 6), 
                ("2048px",  "2m",     "2048px/26dpi/2m",    "", 7), 
                ("4096px",  "4m",     "4096px/26dpi/4m",    "", 8)],
               name = "Size",  
               default = "1024px",  
               description=" ")   


    # BOUND TO #
    bounds_to_all : BoolProperty(name="To View", description=" ", default=False)   
    make_link : BoolProperty(name="Make Link", description=" ", default=False)   

    # GEOMETRY TYPE #
    typ_geometry : EnumProperty(
        items=[("typ_custom"  ,"Custom" ,"custom"    ),
               ("typ_curve"   ,"Curve"  ,"circle"    ),
               ("typ_ico"     ,"Ico"    ,"ico sphere"),
               ("typ_sphere"  ,"Sphere" ,"uv sphere" ),
               ("typ_torus"   ,"Torus"  ,"torus"     ),
               ("typ_circle"  ,"Circle" ,"circle"    ),
               ("typ_cone"    ,"Cone"   ,"cone"      ),
               ("typ_cylinder","Tube"   ,"cylinder"  ),
               ("typ_cube"    ,"Cube"   ,"cube / box"),
               ("typ_grid"    ,"Grid"   ,"grid plane")],
               name = "",
               default = "typ_cube",    
               description = "choose geometry for bounding")

    # MESH TYPE #  
    typ_mesh : EnumProperty(
        items=[("typ_00"    ,"Shaded"      ,"solid mesh"                ),
               ("typ_01"    ,"Shade off"   ,"transparent mesh"          ),
               ("typ_02"    ,"Wire only"   ,"wired mesh > delete faces" )],
               name = "",
               default = "typ_00",    
               description = "change typ of the mesh")
    
    # CURVE TYPE #  
    typ_curve : EnumProperty(
      items = [("POLY",   "Poly",   ""),
               ("BEZIER", "Beziér", ""),                       
               ("NURBS",  "Nurbs",  "")], 
               name = "Curve Type",
               default = "BEZIER",
               description="")
   
    use_handles : BoolProperty(name="Use Handles", description=" ", default=False)   

    # GRID #
    bounds_grid_subdivX : IntProperty(name="X-Loops", description="set vertices value",  min=2, max=100, default=0, step=1)
    bounds_grid_subdivY : IntProperty(name="Y-Loops", description="set vertices value",  min=2, max=100, default=0, step=1)
    bounds_grid_size : FloatProperty(name="Size", description="set vertices value", default=10.0, min=0.01, max=100)            

    # CUBE #
    bounds_cube_radius : FloatProperty(name="Radius", default=0.1, min=0.01, max=100, description="xyz scaling")
    

    # BOX (CUBE ALTERNATIVE) #
    scale : FloatVectorProperty(name="Scale", default=(0.1, 0.1, 0.1), subtype='TRANSLATION', description="xyz scaling" )
    rotation : FloatVectorProperty(name="Rotation", subtype='EULER')
    location : FloatVectorProperty(name="Location", subtype='TRANSLATION')
    rotation : FloatVectorProperty(name="Rotation",subtype='EULER')
    layers : BoolVectorProperty(name="Layers", size=20, subtype='LAYER', options={'HIDDEN', 'SKIP_SAVE'}) 
            
    # CIRCLE #
    bounds_circle_amount : IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bounds_circle_radius : FloatProperty(name="Radius", description="set vertices value", default=0.1, min=0.01, max=100)

    # CYLINDER #
    bounds_cylinder_amount : IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bounds_cylinder_radius : FloatProperty(name="Radius", description="set vertices value", default=0.1, min=0.01, max=100)
    bounds_cylinder_depth : FloatProperty(name="Depth", description="set depth value", default=0.1, min=0.01, max=100)

    # CONE #
    bounds_cone_amount : IntProperty(name="Verts", description="vertices value",  min=3, max=80, default=12)
    bounds_cone_radius_1 : FloatProperty(name="Bottom", description="set bottom value",  min=0.01, max=100, default=10)
    bounds_cone_radius_2 : FloatProperty(name="Top", description="set top value",  min=0.01, max=100, default=0.1)
    bounds_cone_depth : FloatProperty(name="Depth", description="set depth value",  min=1, max=100, default=10)

    # TORUS #
    bounds_torus_segments_1 : IntProperty(name="Major Segments", description="set value",  min=1, max=100, default=51) 
    bounds_torus_segments_2 : IntProperty(name="Minor Segments", description="set value",  min=1, max=100, default=15)
    bounds_torus_size_1 : FloatProperty(name="Major Radius", description="set value", default=1.13, min=0.01, max=1000)
    bounds_torus_size_2 : FloatProperty(name="Minor Radius", description="set value", default=0.78, min=0.01, max=1000)
    bounds_torus_dimension : EnumProperty(
                                         items = [("MAJOR_MINOR", "Major/Minor",       ""),                      
                                                  ("EXT_INT",     "Exterior/Interior", "")], 
                                                  name = "Dimension", default = "MAJOR_MINOR", description="")

    # SPHERE #
    bounds_sphere_segments : IntProperty(name="Segments",  description="set value", min=1, max=100, default=32) 
    bounds_sphere_ring : IntProperty(name="Rings",  description="set value",  min=1, max=100, default=16) 
    bounds_sphere_size : FloatProperty(name="Size",  description="set value", default=0.1, min=0.01, max=100) 
   
    # ICO #
    bounds_ico_subdiv : IntProperty(name="Subdiv",  description="set value", min=1, max=5, default=2) 
    bounds_ico_size : FloatProperty(name="Size",  description="set value", default=0.1, min=0.01, max=100) 

    # CURVE  #
    bounds_curve_radius : FloatProperty(name="Radius",  default=0.1, min=0.01, max=100, description="xyz scaling")

    # curve: shape
    bounds_curve_type : EnumProperty(items = [("2D", "2D", ""), 
                                              ("3D", "3D", "")], 
                                     name = "Shape Type", default = "3D", description="")

    bounds_curve_twist : EnumProperty(items = [("Z_UP",    "Z-Up",    ""), 
                                               ("MINIMUM", "Minimum", ""), 
                                               ("TANGET",  "Tanget",  "")], 
                                      name = "Twist Method", default = "MINIMUM", description="tilt calculation for 3d curves")
                                      
    bounds_curve_smooth : FloatProperty(name="Smooth",  description="twist smooth", default=0.00, min=0.00, max=100.00) 

    bounds_curve_fill : EnumProperty(items = [("FULL",  "Full",  ""), 
                                              ("BACK",  "Back",  ""), 
                                              ("FRONT", "Front", ""), 
                                              ("HALF",  "Half",  "")], 
                                      name = "Fill Mode", default = "FULL", description="mode of filling curve")
                                      
    bounds_curve_deformed : BoolProperty(name="Fill Deformed", description=" ", default=True)   
    bounds_curve_use_radius : BoolProperty(name="Radius", description=" ", default=True)   
    bounds_curve_stretch : BoolProperty(name="Stretch", description=" ", default=False)   
    bounds_curve_clamp : BoolProperty(name="Bounds Clamp", description=" ", default=False)   
   
    # curve: geometry
    bounds_curve_geom_offset : FloatProperty(name="Offset",  description="set value", default=0.00, min=-0.01, max=0.01) 
    bounds_curve_geom_extrude : FloatProperty(name="Height",  description="set value", default=0.00, min=0.00, max=100.00) 
    bounds_curve_geom_depth : FloatProperty(name="Bevel",  description="set value", default=0.00, min=0.00, max=100.00) 
    bounds_curve_geom_rings : IntProperty(name="Rings",  description="set value", min=0, max=100, default=12) 
    bounds_curve_geom_loops : IntProperty(name="Loops",  description="set value", min=0, max=100, default=4) 

    bounds_curve_geom_start : FloatProperty(name="Start",  description="set value", default=0.00, min=0.00, max=1.00)   
    bounds_curve_geom_end : FloatProperty(name="End",  description="set value", default=0.00, min=0.00, max=1.00)   

    bounds_curve_geom_start_map : EnumProperty(items = [("SPLINE",     "Spline",     ""), 
                                                        ("RESOLUTION", "Resolution", ""), 
                                                        ("SEGMENTS",   "Segments",   "")], 
                                             name = "Mapping Start", default = "RESOLUTION", description="") 

    bounds_curve_geom_end_map : EnumProperty(items = [("SPLINE",     "Spline",     ""), 
                                                      ("RESOLUTION", "Resolution", ""), 
                                                      ("SEGMENTS",   "Segments",   "")], 
                                             name = "Mapping End", default = "RESOLUTION", description="")   

   
    # ADJUSTMENTS #
    align : EnumProperty(
      items = [("WORLD",  "World",  ""),
               ("VIEW",   "View",   ""),                       
               ("CURSOR", "Cursor", "")], 
               name = "Align",
               default = "WORLD",
               description="")

    end_fill_type : EnumProperty(
        items=[("NOTHING"   ,"Nothing"  ,""   ),
               ("NGON"      ,"Ngon"     ,""   ),
               ("TRIFAN"    ,"Triangle" ,""   )],
               name = "Fill Type",
               default = "NGON",    
               description = "change mesh fill type")

    offset_location : FloatVectorProperty(name="Offset", description="offset location", default=(0.0, 0.0, 0.0), subtype='TRANSLATION', size=3, options={'SKIP_SAVE'})
    
    rota_x : FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    rota_y : FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    rota_z : FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)


    tp_geom_rota : EnumProperty( 
        items = [("rota_axis_xy", "xy", "xy horizontal"),
                 ("rota_axis_yz", "yz", "yz vertical"  ), 
                 ("rota_axis_xz", "xz", "xz vertical"  )],
                 name = "Local",  
                 default = "rota_axis_xy",  
                 description="align geometry to an axis")  

    tp_instance_rota : EnumProperty( 
        items = [("rota_axis_xy", "xy", "xy horizontal"),
                 ("rota_axis_yz", "yz", "yz vertical"  ), 
                 ("rota_axis_xz", "xz", "xz vertical"  )],
                 name = "Axis",  
                 default = "rota_axis_xy",  
                 description="align instances to an axis")  

               
    mesh_subdiv_use : BoolProperty(name="Subdivide",  description="activate subdivide", default=False) 
    mesh_subdiv : IntProperty(name="Loops", description="How many?", default=0, min=0, max=20, step=1)                   
    mesh_subdiv_smooth : FloatProperty(name="Value",  description="smooth subdivide", default=0.0, min=0.0, max=1.0)                     
  

    # COLLECTION #    
    rb_collection_name_instance : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_instance : StringProperty(name="Parent", description="create custom group name", default="")
   
    rb_collection_name_clone : StringProperty(name="Name", description="create custom group name", default="")
    rb_collection_name_exist_clone : StringProperty(name="Parent", description="create custom group name", default="")
  