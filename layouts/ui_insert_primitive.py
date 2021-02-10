import bpy
from ..utilities.utils import get_prefs
from ..icons.general import get_icon_id_general


def draw_primitive_ui(self, context):    
    layout = self.layout.column(align=True)     
    layout.operator_context = 'INVOKE_REGION_WIN'
    layout.operator_context = 'INVOKE_AREA'   

    prefs = get_prefs()
    addon_prefs = prefs.panel_type
    global_props = prefs.panel_type 

  
    if context.mode == 'OBJECT': 
     
        row = layout.row(align=True)             
        row.alignment = 'CENTER' 
        row.scale_x = 1.1         
        row.scale_y = 1.2         
   
        row.menu("TOPBAR_MT_file_import", text="", icon="IMPORT")
        row.menu("TOPBAR_MT_file_export", text="", icon="EXPORT") 
      
        row.separator()
              
        row.menu("VIEW3D_MT_mesh_add", text="", icon='OUTLINER_DATA_MESH')              
        row.menu("VIEW3D_MT_curve_add", text="" , icon='OUTLINER_DATA_CURVE')
        row.menu("VIEW3D_MT_surface_add", text="", icon='OUTLINER_DATA_SURFACE')
        row.menu("VIEW3D_MT_metaball_add", text="", icon="OUTLINER_DATA_META")         
        #row.operator("object.text_add", text="", icon="OUTLINER_DATA_FONT")      
   
        row.separator()      
        
        row.menu("VIEW3D_MT_image_add", text="", icon='IMAGE_BACKGROUND')  
        row.operator_context = 'INVOKE_AREA'
        row.operator("wm.append", text="", icon='APPEND_BLEND') 
                 

 
    if context.mode == 'EDIT_MESH': 

        row = layout.row(align=True) 
        row.alignment = 'CENTER'               
        row.scale_x = 1.2         
        row.scale_y = 1.2 
             
        row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')        
        row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
        row.operator("mesh.primitive_grid_add", text="", icon='MESH_GRID') 
        row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')   
        row.operator("mesh.primitive_circle_add", text="", icon='MESH_CIRCLE')
      
        row = layout.row(align=True) 
        row.alignment = 'CENTER' 
        row.scale_x = 1.2         
        row.scale_y = 1.2          

        row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER') 
        row.operator("mesh.primitive_cone_add", text="", icon='MESH_CONE')                                       
        row.operator("mesh.primitive_torus_add", text="", icon='MESH_TORUS')
        row.operator("mesh.primitive_ico_sphere_add", text="", icon='MESH_ICOSPHERE')
        row.operator("mesh.primitive_monkey_add", text="", icon='MESH_MONKEY')    


    if context.mode == 'EDIT_CURVE': 

        row = layout.row(align=True) 
        row.alignment = 'CENTER' 
        row.scale_x = 1.2         
        row.scale_y = 1.2   
        row.operator("curve.primitive_bezier_curve_add", text="", icon='CURVE_BEZCURVE')
        row.operator("curve.primitive_bezier_circle_add", text="", icon='CURVE_BEZCIRCLE')
        row.operator("curve.primitive_nurbs_curve_add", text="", icon='CURVE_NCURVE')
        row.operator("curve.primitive_nurbs_circle_add", text="", icon='CURVE_NCIRCLE')
        row.operator("curve.primitive_nurbs_path_add", text="", icon='CURVE_PATH')    
       
#        row.prop(panel_prefs, "tp_create_category_draw", text="Draw", icon='MOD_CURVE')
#       
#        if panel_prefs.tp_create_category_draw == True:  
#            draw_cdraw_ui(self, context, layout)  


    if context.mode == 'EDIT_SURFACE':

        row = layout.row(align=True) 
        row.alignment = 'CENTER'
        row.scale_x = 1.2         
        row.scale_y = 1.2                         
        row.operator("surface.primitive_nurbs_surface_curve_add", text="", icon='SURFACE_NCURVE') 
        row.operator("surface.primitive_nurbs_surface_circle_add", text="", icon='SURFACE_NCIRCLE')
        row.operator("surface.primitive_nurbs_surface_surface_add", text="", icon='SURFACE_NSURFACE')
        row.operator("surface.primitive_nurbs_surface_cylinder_add", text="", icon='SURFACE_NCYLINDER')
        row.operator("surface.primitive_nurbs_surface_sphere_add", text="", icon='SURFACE_NSPHERE')
        row.operator("surface.primitive_nurbs_surface_torus_add", text="", icon='SURFACE_NTORUS')   


    if context.mode == 'EDIT_METABALL':   
    
        row = layout.row(align=True)   
        row.alignment = 'CENTER'  
        row.scale_x = 1.2         
        row.scale_y = 1.2                        
        row.operator("object.metaball_add", text="", icon='META_BALL').type = "BALL"
        row.operator("object.metaball_add", text="", icon='META_CAPSULE').type = "CAPSULE"
        row.operator("object.metaball_add", text="", icon='META_PLANE').type = "PLANE"
        row.operator("object.metaball_add", text="", icon='META_ELLIPSOID').type = "ELLIPSOID"                
        row.operator("object.metaball_add", text="", icon='META_CUBE').type = "CUBE"         
         
         
    if context.mode == 'EDIT_ARMATURE': 
     
        row = layout.row(align=True) 
        row.alignment = 'CENTER' 
        row.scale_x = 1.2         
        row.scale_y = 1.2                                
        row.operator("armature.bone_primitive_add", text="Single Bone", icon="BONE_DATA")         
        
      
