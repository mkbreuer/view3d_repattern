import bpy
from bpy import *
from bpy.props import *
import random

from ..utilities.utils import get_prefs


class RTS_OT_RePattern_Curve_Beveled(bpy.types.Operator):
    """create curve with bevel extrusion"""
    bl_idname = "rts_ot.beveled_curve"
    bl_label = "Add beveled Curve"
    bl_options = {'REGISTER', 'UNDO'}


    def draw(self, context):      
        layout = self.layout
        
        prefs = get_prefs()
        curve_props = prefs.curve_type
       
        col = layout.column(align=True)

        box = col.box().column(align=True)             

        row = box.column(align=True)  
        row.prop(curve_props, 'curve_type')  
        
        row.separator()
        
        row.prop(curve_props, 'radius')

        box.separator()        
       
        row = box.row(align=True)                                                                                                                                                                                                                    
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(curve_props, 'depth')
 
        if curve_props.wire == True:
            row.prop(curve_props, 'wire', "", icon = 'MESH_PLANE')              
        else:                       
           row.prop(curve_props, 'wire', "", icon = 'MESH_GRID') 
                    
        row = box.row(align=True)
        row.prop(curve_props, 'ring')  
        row.prop(curve_props, 'loop')

        row = box.row(align=True)
        row.prop(curve_props, 'offset')  
        row.prop(precurve_propsfs, 'height')
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(align=True)
            row.prop(curve_props, 'nring')        
     

        box.separator()

        row = box.row(align=True) 
        row.prop(curve_props, "add_mat", text ="")                    
        row.label(text="Color:") 
     
        row.prop(curve_props, "add_objmat", text ="", icon="GROUP_VCOL")
        if curve_props.add_random == False:                   
            if curve_props.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(curve_props, "add_cyclcolor", text ="")        
                else:
                    row.prop(curve_props, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")  
        else:            
            if curve_props.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(curve_props, "add_cyclcolor", text ="")        
                else:
                    row.prop(curve_props, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")              

        row.prop(curve_props, "add_random", text ="", icon="FILE_REFRESH")

       
        box.separator()



    def execute(self, context):

        prefs = get_prefs()
        curve_props = prefs.curve_type
 
        scene = bpy.context.scene
        
        if curve_props.curve_type == "tp_bezier":   
            bpy.ops.curve.primitive_bezier_curve_add(radius=curve_props.radius)

        if curve_props.curve_type == "tp_circle":   
            bpy.ops.curve.primitive_bezier_circle_add(radius=curve_props.radius)        
       
        if curve_props.curve_type == "tp_nurbs":   
            bpy.ops.curve.primitive_nurbs_curve_add(radius=curve_props.radius)

            bpy.context.object.data.splines[0].order_u = curve_props.nring

        if curve_props.curve_type == "tp_ncircle":   
            bpy.ops.curve.primitive_nurbs_circle_add(radius=curve_props.radius)     

            bpy.context.object.data.splines[0].order_u = curve_props.nring

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)        

        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = curve_props.loop
        bpy.context.object.data.resolution_u = curve_props.ring
        bpy.context.object.data.bevel_depth = curve_props.depth
        bpy.context.object.data.offset = curve_props.offset
        bpy.context.object.data.extrude = curve_props.height
            

        # add material with enabled object color
        for i in range(curve_props.add_mat):

            active = bpy.context.active_object
            # Get material
            mat = bpy.data.materials.get("Mat_Lathe")
            if mat is None:
                # create material
                mat = bpy.data.materials.new(name="Mat_Lathe")
            else:
                bpy.ops.object.material_slot_remove()
                mat = bpy.data.materials.new(name="Mat_Lathe")
                     
            # Assign it to object
            if len(active.data.materials):
                # assign to 1st material slot
                active.data.materials[0] = mat
            else:
                # no slots
                active.data.materials.append(mat)
                        


            # toggle random
            if curve_props.add_random == False:            
                                
                # toggle color target
                if curve_props.add_objmat == False: 
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        mat.diffuse_color = (curve_props.add_cyclcolor)                        
                    else:
                        mat.use_object_color = True
                        bpy.context.object.color = (curve_props.add_color)
                else:                    
                    # regular material
                    pass
                       
            else: 
                
                # toggle color target
                if curve_props.add_objmat == False:   
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            mat.diffuse_color = RGB                       
                    else:
                        mat.use_object_color = True
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            bpy.context.object.color = RGB
               
                else:        
                    # regular material    
                    if bpy.context.scene.render.engine == 'CYCLES':
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        for i in range(3):
                            node.inputs['Color'].default_value[i] *= random.random()             
                    else:
                        for i in range(3):
                            mat.diffuse_color[i] *= random.random()   


        if curve_props.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False  
     
        return {'FINISHED'}
    
    

class RTS_OT_RePattern_Curve_Wire(bpy.types.Operator):
    """Add wired Curve"""
    bl_idname = "rts_ot.wired_curve"
    bl_label = "Add wired Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        active_wire = bpy.context.object.show_wire 

        if active_wire == True:
            bpy.context.object.show_wire = False             
        else:                       
            bpy.context.object.show_wire = True

        return {'FINISHED'}



class RTS_OT_RePattern_Curve_Bevel(bpy.types.Operator):
    """Bevel Setup"""
    bl_idname = "rts_ot.bevel_set"
    bl_label = "Bevel Extrusion"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}    
    
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=350)


    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'     
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box().column(align=True)         
        
        if context.mode == 'OBJECT': 
            row = box.row(align=True)
            row.label("", icon='MOD_CURVE') 
            row.prop(context.scene, "curve_type", text="") 
            row.operator("rts_ot.beveled_curve", text="Add Curve")                          
                           
            box.separator()
        
        row = box.row(align=True)                                                                                                                                                                                                            
        
        active_wire = bpy.context.object.show_wire 
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
        
        if active_wire == True:
            row.operator("rts_ot.wire_off", "", icon = 'MESH_PLANE')              
        else:                       
            row.operator("rts_ot.wire_on", "", icon = 'MESH_GRID') 
                    
        row = box.row(align=True)
        row.prop(context.object.data, "resolution_u", text="Rings")          
        row.prop(context.object.data, "bevel_resolution", text="Loops")

        row = box.row(align=True)
        row.prop(context.object.data, "offset")
        row.prop(context.object.data, "extrude","Height")
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(align=True)
            row.prop(context.object.data.splines.active, "order_u", text="U Order")

        box.separator() 

        row = box.row(align=True)
        row.prop(context.object.data, "fill_mode", text="")   
        active_bevel = bpy.context.object.data.bevel_depth            
        if active_bevel == 0.0:              
            row.operator("rts_ot.enable_bevel", text="Bevel on", icon='MOD_WARP')
        else:   
            row.operator("rts_ot.enable_bevel", text="Bevel off", icon='MOD_WARP')      
            
        box.separator() 

    def check(self, context):
        return True



class RTS_OT_RePattern_Curve_Purge(bpy.types.Operator):
    '''Purge orphaned curve'''
    bl_idname="purge.unused_curve_data"
    bl_label="Purge Mesh"
    
    def execute(self, context):

        target_coll = eval("bpy.data.curves")
        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}



class RTS_OT_RePattern_Curve_Enable_Bevel(bpy.types.Operator):
    """toggle curve bevel extrusion"""
    bl_idname = "rts_ot.enable_bevel"
    bl_label = "Add enable Bevel"
    bl_options = {'REGISTER', 'UNDO'}

    depth : FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring : IntProperty(name="Ring",  description=" ", min=0, max=100, default=12) 
    nring : IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop : IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 

    offset : FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height : FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    wire : BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})   


    def draw(self, context):
        layout = self.layout
        
        prefs = get_prefs()
        curve_props = prefs.curve_type

        col = layout.column(align=True)

        box = col.box().column(align=True)                     
       
        row = box.row(align=True)                                                                                                                                                                                                                    
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(curve_props, 'depth')
 
        if curve_props.wire == True:
            row.prop(curve_props, 'wire', "", icon = 'MESH_PLANE')              
        else:                       
           row.prop(curve_props, 'wire', "", icon = 'MESH_GRID') 
                    
        row = box.row(align=True)
        row.prop(curve_props, 'ring')  
        row.prop(curve_props, 'loop')

        row = box.row(align=True)
        row.prop(curve_props, 'offset')  
        row.prop(curve_props, 'height')
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(align=True)
            row.prop(curve_props, 'nring')
     
        box.separator()


    def execute(self, context):
         
        prefs = get_prefs()
        curve_props = prefs.curve_type

        active_bevel = bpy.context.object.data.bevel_depth
      
        if active_bevel == 0.0:              
            bpy.context.object.data.fill_mode = 'FULL'
            bpy.context.object.data.bevel_resolution = curve_props.loop

            bpy.context.object.data.bevel_depth = curve_props.depth
            bpy.context.object.data.offset = curve_props.offset
            bpy.context.object.data.extrude = curve_props.height 

            if context.object.data.splines.active.type == 'NURBS':            
                bpy.context.object.data.splines[0].order_u = curve_props.nring            
            else:
                bpy.context.object.data.resolution_u = curve_props.ring

        else:                   
            bpy.context.object.data.fill_mode = 'HALF'
            #bpy.context.object.data.bevel_resolution = 0
            #bpy.context.object.data.resolution_u = 0
            bpy.context.object.data.bevel_depth = 0.0
            bpy.context.object.data.extrude = 0
            bpy.context.object.data.offset = 0
    
        if curve_props.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False 

        return {'FINISHED'}



class RTS_OT_RePattern_Curve_Quader(bpy.types.Operator):
    """select 2 vertices  on circle and execute"""
    bl_idname = "rts_ot.quader_curve"
    bl_label = "A full Bevel Quader Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='TOGGLE')
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.curve.cyclic_toggle()   

        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_depth = 1.5
        bpy.context.object.data.bevel_resolution = 6
        bpy.context.object.show_wire = True

        return {'FINISHED'} 
    


class RTS_OT_RePattern_Curve_Half_Circle(bpy.types.Operator):
    """select start-point on circle and execute"""
    bl_idname = "rts_ot.half_curve"
    bl_label = "A full Bevel Quader CircleCurve"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        bpy.ops.curve.surfsk_first_points()
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.cyclic_toggle()
        
        bpy.context.object.data.fill_mode = 'FULL'            
        bpy.context.object.data.bevel_depth = 1.5
        bpy.context.object.data.bevel_resolution = 6
        bpy.context.object.show_wire = True

        return {'FINISHED'}




class RTS_OT_RePattern_Curve_Convert_to_Mesh(bpy.types.Operator):
    """convert, get origin, remove doubles, recalculate, remesh"""
    bl_idname = "rts_ot.convert_mesh"
    bl_label = "Convert to Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        prefs = get_prefs()
        curve_props = prefs.curve_type

        bpy.ops.object.mode_set(mode = 'OBJECT')
            
        bpy.ops.object.convert(target='MESH')                  
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        bpy.ops.object.mode_set(mode='EDIT')  

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.normals_make_consistent()

        bpy.ops.object.mode_set(mode = 'OBJECT')

        # from sculpt remesh 
        for i in range(curve_props.remesh):                         
            bpy.ops.rts_ot.remesh(remeshDepthInt=4, remeshSubdivisions=1, remeshPreserveShape=True)

        return {'FINISHED'}
                
  
        
class RTS_OT_RePattern_Curve_Lathe(bpy.types.Operator):
    """draw a screw curve to 3d cursor"""
    bl_idname = "rts_ot.curve_lathe"
    bl_label = "Curve Lathe"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return hasattr(bpy.types, "CURVE_OT_draw")
    
    def execute(self, context):

        prefs = get_prefs()
        curve_props = prefs.curve_type

        scene = bpy.context.scene

        add_mat = curve_props.add_mat
        add_objmat = curve_props.add_objmat  
        add_random = curve_props.add_random
        add_color = curve_props.add_color
        add_cyclcolor = curve_props.add_cyclcolor
     
        obj = context.object 
        if obj:
            active = context.active_object if context.object is not None else None
            if active :
                bpy.context.scene.obj1 = active.name
                    
            bpy.ops.object.mode_set(mode = 'OBJECT')
                
            # add curve          
            bpy.ops.curve.primitive_bezier_curve_add(view_align=True) 
            
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.curve.select_all(action='SELECT')            
            bpy.ops.curve.delete(type='VERT')
            bpy.context.object.data.show_normal_face = False

            # add screw modifier to curve           
            bpy.ops.object.modifier_add(type='SCREW')
            bpy.context.object.modifiers["Screw"].steps = 40
            bpy.context.object.modifiers["Screw"].use_normal_flip = False            
            bpy.context.object.modifiers["Screw"].use_smooth_shade = True
            
            if active:
                bpy.context.object.modifiers["Screw"].object = active

        else:          
            # add curve            
            bpy.ops.curve.primitive_bezier_curve_add(view_align=True) 
           
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.curve.select_all(action='SELECT')            
            bpy.ops.curve.delete(type='VERT')
            bpy.context.object.data.show_normal_face = False

            # add screw modifier to curve           
            bpy.ops.object.modifier_add(type='SCREW')
            bpy.context.object.modifiers["Screw"].steps = 40
            bpy.context.object.modifiers["Screw"].use_normal_flip = False          
            bpy.context.object.modifiers["Screw"].use_smooth_shade = True

        
        bpy.ops.object.mode_set(mode = 'OBJECT')            
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


        # add material with enabled object color
        for i in range(add_mat):

            active = bpy.context.active_object
            # Get material
            mat = bpy.data.materials.get("Mat_Lathe")
            if mat is None:
                # create material
                mat = bpy.data.materials.new(name="Mat_Lathe")
            else:
                bpy.ops.object.material_slot_remove()
                mat = bpy.data.materials.new(name="Mat_Lathe")
                     
            # Assign it to object
            if len(active.data.materials):
                # assign to 1st material slot
                active.data.materials[0] = mat
            else:
                # no slots
                active.data.materials.append(mat)
                        
            if add_random == False:                            
                if add_objmat == False: 
                    if bpy.context.scene.render.engine == 'CYCLES':
                        mat.diffuse_color = (add_cyclcolor)                        
                    else:
                        mat.use_object_color = True
                        bpy.context.object.color = (add_color)
                else:
                     pass                    
            else: 
                if bpy.context.scene.render.engine == 'CYCLES':
                    node=mat.node_tree.nodes['Diffuse BSDF']
                    for i in range(3):
                        node.inputs['Color'].default_value[i] *= random.random()             
                else:
                    for i in range(3):
                        mat.diffuse_color[i] *= random.random()   


        # go to edit and draw curve
        bpy.ops.object.mode_set(mode = 'EDIT')        
        bpy.ops.curve.draw('INVOKE_DEFAULT')

        return {"FINISHED"}




class RTS_OT_RePattern_Curve_Origin_Start(bpy.types.Operator):
    """Origin to curve start point / objectmode"""
    bl_idname = "rts_ot.origin_start_point"
    bl_label = "Origin to Start Point"
            
    def execute(self, context):
        blCurve = context.active_object
        blSpline = blCurve.data.splines[0]
      
        newOrigin = blCurve.matrix_world * blSpline.bezier_points[0].co
    
        origOrigin = bpy.context.scene.cursor_location.copy()

        bpy.context.scene.cursor_location = newOrigin
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor_location = origOrigin

        return {'FINISHED'}




class RTS_OT_RePattern_Curve_Extrude(bpy.types.Operator):
    """create 2d bevel extrude on curve"""
    bl_idname = "rts_ot.curve_extrude"
    bl_label = "Curve Extrude"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context):      
        layout = self.layout
       
        prefs = get_prefs()
        curve_props = prefs.curve_type

        col = layout.column(align=True)
        box = col.box().column(align=True)             

        box.separator()        
       
        row = box.row(align=True)                                                                                                                                                                                                                    
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(curve_props, 'depth')
 
        if curve_props.wire == True:
            row.prop(curve_props, 'wire', "", icon = 'MESH_PLANE')              
        else:                       
           row.prop(curve_props, 'wire', "", icon = 'MESH_GRID') 
                    
        row = box.row(align=True)
        row.prop(curve_props, 'ring')  
        row.prop(curve_props, 'loop')

        row = box.row(align=True)
        row.prop(securve_propslf, 'offset')  
        row.prop(curve_props, 'height')
    
        box.separator()
                    
        row = box.row(align=True) 
        row.prop(curve_props, "add_mat", text ="")                    
        row.label(text="Color:") 
     
        row.prop(curve_props, "add_objmat", text ="", icon="GROUP_VCOL")
        if curve_props.add_random == False:                   
            if curve_props.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(curve_props, "add_cyclcolor", text ="")        
                else:
                    row.prop(curve_props, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")  
        else:
            row.prop(context.object.active_material, "diffuse_color", text="")
       
        row.prop(curve_props, "add_random", text ="", icon="FILE_REFRESH")
       
        box.separator()


    def execute(self, context):
       
        prefs = get_prefs()
        curve_props = prefs.curve_type
 
        # add material
        for i in range(curve_props.add_mat):
            bpy.ops.object.mode_set(mode = 'OBJECT')
           
            # Get material
            active = bpy.context.active_object
            mat = bpy.data.materials.get("Mat_Lathe")
            if mat is None:
                # create material
                mat = bpy.data.materials.new(name="Mat_Lathe")
            else:
                bpy.ops.object.material_slot_remove()
                mat = bpy.data.materials.new(name="Mat_Lathe")
                     
            # Assign it to object
            if len(active.data.materials):
                # assign to 1st material slot
                active.data.materials[0] = mat
            else:
                # no slots
                active.data.materials.append(mat)
                        

            # toggle random
            if curve_props.add_random == False:            
                                
                # toggle color target
                if curve_props.add_objmat == False: 
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        mat.diffuse_color = (curve_props.add_cyclcolor)                        
                    else:
                        mat.use_object_color = True
                        bpy.context.object.color = (curve_props.add_color)
                else:                                      
                    # regular material
                    pass
          
            else: 
                
                # toggle color target
                if curve_props.add_objmat == False:   
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            mat.diffuse_color = RGB                       
                    else:
                        mat.use_object_color = True
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            bpy.context.object.color = RGB
               
                else:        
                    # regular material    
                    if bpy.context.scene.render.engine == 'CYCLES':
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        for i in range(3):
                            node.inputs['Color'].default_value[i] *= random.random()             
                    else:
                        for i in range(3):
                            mat.diffuse_color[i] *= random.random()   


        # curve extrude    
        if bpy.context.object.mode == "OBJECT":               
            bpy.ops.object.mode_set(mode = 'EDIT')
        
        if bpy.context.object.data.splines.active.use_cyclic_u == True:         
            pass
        else:
            bpy.ops.curve.cyclic_toggle()

        bpy.context.object.data.dimensions = '2D'
        bpy.context.object.data.fill_mode = 'BOTH'
        bpy.context.object.data.bevel_depth = curve_props.depth
        bpy.context.object.data.bevel_resolution = curve_props.ring         
        bpy.context.object.data.resolution_u = curve_props.loop
        bpy.context.object.data.offset = curve_props.offset            
        bpy.context.object.data.extrude = curve_props.height           
        

        # wire visibility
        if curve_props.wire == True:
            bpy.context.object.show_axis = True
            bpy.context.object.show_wire = True            
        else:
            bpy.context.object.show_axis = False
            bpy.context.object.show_wire = False 
                  
        return {"FINISHED"}




















