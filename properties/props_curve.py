import bpy
from bpy.props import BoolProperty, IntProperty, FloatVectorProperty, FloatProperty, EnumProperty


class PropsGroup_Curve(bpy.types.PropertyGroup):

    radius : FloatProperty(name="Radius",  description=" ", default=10, min=0.01, max=1000)
    depth : FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring : IntProperty(name="Ring",  description=" ", min=0, max=100, default=12) 
    nring : IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop : IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 
    offset : FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height : FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)
    wire : BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    
    convert : BoolProperty(name="Convert to Mesh",  description=" ", default=False, options={'SKIP_SAVE'})   

    curve_type : EnumProperty(
        items=[("tp_bezier"     ,"Bezier Curve"     ,"Bezier Curve"),
               ("tp_circle"     ,"Circle Curve"     ,"Circle Curve"),
               ("tp_nurbs"      ,"Nurbs Curve"      ,"Nurbs Curve"),
               ("tp_ncircle"    ,"Nurbs Circle"     ,"Nurbs Circle")],
               name = "Type",
               default = "tp_bezier",    
               description = "add geometry")

    # MATERIAL #
    add_mat : BoolProperty(name="Add Material",  description="add material and enable object color", default=False)        
    add_random : BoolProperty(name="Add Random",  description="add random material", default=False, options={'SKIP_SAVE'})    
    add_objmat : BoolProperty(name="Add Material",  description="add material", default=False, options={'SKIP_SAVE'})    
    add_color : FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor : FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    remesh : BoolProperty(name="Remesh",  description="remesh for curve extrude", default=True, options={'SKIP_SAVE'})    
