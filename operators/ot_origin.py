import bpy, mathutils
from bpy import *
from bpy.props import *
from mathutils import Vector, Matrix

from ..utilities.utils import get_prefs
 

class RTS_OT_RePattern_Origin_BBox(bpy.types.Operator):  
    bl_idname = "rts_ot.repattern_bbox_origin"  
    bl_label = "BBox Origin"  
    bl_options = {'REGISTER', 'UNDO'} 

    box_level : EnumProperty(
        items=[("top"     ,"Top"     ,"constraint XY-Axis / plus Z-Axis"),
               ("middle"  ,"Middle"  ,"constraint XY-Axis / zero Z-Axis"),
               ("bottom"  ,"Bottom"  ,"constraint XY-Axis / minus Z-Axis")],
               name = " ",
               default = "middle")


    origin_location : EnumProperty( 
        items = [("center",         "center",  "center",    "BLANK1", 0),
                ("minus_y",         "--y",     "--y",       "BLANK1", 1), 
                ("minus_y_minus_x", "--y--x",  "--y--x",    "BLANK1", 2), 
                ("minus_x",         "--x",     "--x",       "BLANK1", 3), 
                ("plus_y_minus_x",  "+y--x",   "+y--x",     "BLANK1", 4), 
                ("plus_y",          "+y",      "+y",        "BLANK1", 5), 
                ("plus_y_plus_x",   "+y+x",    "+y+x",      "BLANK1", 6), 
                ("plus_x",          "+x",      "+x",        "BLANK1", 7),
                ("minus_y_plus_x",  "--x",     "--x",       "BLANK1", 8)],
                name = "bbox origin",  
                default = "center",  
                description=" ")   

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(align=True)              
        box.separator() 
        
        row = box.row(align=True) 
        row.prop(self, 'box_level') 

        box.separator() 

        row = box.row(align=True) 
        row.prop(self, 'origin_location') 

        box.separator() 


    def execute(self, context):
        prefs = get_prefs()
        origin_prefs = prefs.origin_type   
        
        # store active # 
        target = bpy.context.view_layer.objects.active    
        
        for ob in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = ob 

            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)             
                          
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
                
            # reload active #     
            bpy.context.view_layer.objects.active = target


        for o in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = o                 

            init=0

            # TOP +Z #
            if self.box_level == 'top' or origin_prefs.box_level == 'top':    
                           
                if self.origin_location == 'center' or origin_prefs.origin_location == 'center':     
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.z
                             init=1
                         elif x.co.z<a:
                             a=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.z+=a
                                     
                    o.location.z-=a    
                        
               
                if self.origin_location == 'minus_y' or origin_prefs.origin_location == 'minus_y':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.z+=c 
                                     
                    o.location.y+=b 
                    o.location.z-=c                        


                if self.origin_location == 'minus_y_minus_x' or origin_prefs.origin_location == 'minus_y_minus_x':           
                          
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.z+=c
                         x.co.x-=a
                         
                    o.location.y+=b 
                    o.location.z-=c  
                    o.location.x+=a        
                    

                if self.origin_location == 'minus_x' or origin_prefs.origin_location == 'minus_x':
               
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.x-=a
                         x.co.z+=c 
                                     
                    o.location.x+=a 
                    o.location.z-=c                 
                                    
                    
                if self.origin_location == 'plus_y_minus_x' or origin_prefs.origin_location == 'plus_y_minus_x':
                   
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z

                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.z+=c
                         x.co.x-=a

                    o.location.y-=b 
                    o.location.z-=c
                    o.location.x+=a          
                    
             
                if self.origin_location == 'plus_y' or origin_prefs.origin_location == 'plus_y':
                   
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.z+=c 
                                     
                    o.location.y-=b 
                    o.location.z-=c  

                if self.origin_location == 'plus_y_plus_x' or origin_prefs.origin_location == 'plus_y_plus_x':  
                  
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.z+=c
                         x.co.x+=a

                    o.location.y-=b
                    o.location.z-=c
                    o.location.x-=a          
                    
                         
                if self.origin_location == 'plus_x' or origin_prefs.origin_location == 'plus_x':
                   
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.x+=a
                         x.co.z+=c 
                                     
                    o.location.x-=a 
                    o.location.z-=c                   


                if self.origin_location == 'minus_y_plus_x' or origin_prefs.origin_location == 'minus_y_plus_x':

                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.z+=c
                         x.co.x+=a
                         
                    o.location.y+=b
                    o.location.z-=c  
                    o.location.x-=a                    



            # MIDDLE #
            if self.box_level == 'middle' or origin_prefs.box_level == 'middle':    
                           
                if self.origin_location == 'center' or origin_prefs.origin_location == 'center':     
                    
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                                       
               
                if self.origin_location == 'minus_y' or origin_prefs.origin_location == 'minus_y':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.y
                             init=1
                         elif x.co.y<a:
                             a=x.co.y
                             
                    for x in o.data.vertices:
                         x.co.y-=a
                                     
                    o.location.y+=a    
                    
              
                if self.origin_location == 'minus_y_minus_x' or origin_prefs.origin_location == 'minus_y_minus_x':           
                   
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.x-=a 
                                     
                    o.location.y+=b 
                    o.location.x+=a                             
            

                if self.origin_location == 'minus_x' or origin_prefs.origin_location == 'minus_x':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             init=1
                         elif x.co.x<a:
                             a=x.co.x
                             
                    for x in o.data.vertices:
                         x.co.x-=a
                                     
                    o.location.x+=a                   
                                    
                    
                if self.origin_location == 'plus_y_minus_x' or origin_prefs.origin_location == 'plus_y_minus_x':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.x-=a 
                                     
                    o.location.y-=b 
                    o.location.x+=a  
             

                if self.origin_location == 'plus_y' or origin_prefs.origin_location == 'plus_y':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.y
                             init=1
                         elif x.co.y<a:
                             a=x.co.y
                             
                    for x in o.data.vertices:
                         x.co.y+=a
                                     
                    o.location.y-=a  


                if self.origin_location == 'plus_y_plus_x' or origin_prefs.origin_location == 'plus_y_plus_x':  
         
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.x+=a 
                                     
                    o.location.y-=b 
                    o.location.x-=a   
                                    
                         
                if self.origin_location == 'plus_x' or origin_prefs.origin_location == 'plus_x':
                
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             init=1
                         elif x.co.x<a:
                             a=x.co.x
                             
                    for x in o.data.vertices:
                         x.co.x+=a
                                     
                    o.location.x-=a                     


                if self.origin_location == 'minus_y_plus_x' or origin_prefs.origin_location == 'minus_y_plus_x':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.x+=a 
                                     
                    o.location.y+=b 
                    o.location.x-=a                   





            # BOTTOM -Z #
            if self.box_level == 'bottom' or origin_prefs.box_level == 'bottom':    
                           
                if self.origin_location == 'center' or origin_prefs.origin_location == 'center':     
                   
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.z
                             init=1
                         elif x.co.z<a:
                             a=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.z-=a
                                     
                    o.location.z+=a           
               
               
                if self.origin_location == 'minus_y' or origin_prefs.origin_location == 'minus_y':

                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.z-=c 
                                     
                    o.location.y+=b 
                    o.location.z+=c              
                    
              
                if self.origin_location == 'minus_y_minus_x' or origin_prefs.origin_location == 'minus_y_minus_x':           
                          
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.z-=c
                         x.co.x-=a
                         
                    o.location.y+=b
                    o.location.z+=c 
                    o.location.x+=a              


                if self.origin_location == 'minus_x' or origin_prefs.origin_location == 'minus_x':
               
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.x-=a
                         x.co.z-=c 
                                     
                    o.location.x+=a 
                    o.location.z+=c                 
                                    
                    
                if self.origin_location == 'plus_y_minus_x' or origin_prefs.origin_location == 'plus_y_minus_x':
                 
                    for x in o.data.vertices:
                         if init==0:            
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.z-=c
                         x.co.x-=a
                         
                    o.location.y-=b 
                    o.location.z+=c  
                    o.location.x+=a  
             

                if self.origin_location == 'plus_y' or origin_prefs.origin_location == 'plus_y':
                    
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.z-=c 
                                     
                    o.location.y-=b 
                    o.location.z+=c  


                if self.origin_location == 'plus_y_plus_x' or origin_prefs.origin_location == 'plus_y_plus_x':  
         
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y+=b
                         x.co.z-=c
                         x.co.x+=a
                         
                    o.location.y-=b 
                    o.location.z+=c  
                    o.location.x-=a                       
                         

                if self.origin_location == 'plus_x' or origin_prefs.origin_location == 'plus_x':
                                  
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.x+=a
                         x.co.z-=c
                                     
                    o.location.x-=a 
                    o.location.z+=c 


                if self.origin_location == 'minus_y_plus_x' or origin_prefs.origin_location == 'minus_y_plus_x':
                 
                    for x in o.data.vertices:
                         if init==0:
                             a=x.co.x
                             b=x.co.y
                             c=x.co.z

                             init=1
                         
                         elif x.co.x < a:
                             a=x.co.x
                             
                         elif x.co.y < b:
                             b=x.co.y
                         
                         elif x.co.z < c:
                             c=x.co.z
                             
                    for x in o.data.vertices:
                         x.co.y-=b
                         x.co.z-=c
                         x.co.x+=a
                         
                    o.location.y+=b 
                    o.location.z+=c  
                    o.location.x-=a              
                     
        # reload active #     
        bpy.context.view_layer.objects.active = target
        
        return {'FINISHED'}







def origin_cursor_function(loc_x, loc_y, loc_z, loc_offset):
    # snippet from advanced align by Lell, Anfeo               

    sel_obj = bpy.context.selected_objects
    act_obj = bpy.context.view_layer.objects.active  
    
    global ref_co

    def move_pivot(obj):
        me = obj.data                
        vec_ref_co = Vector(ref_co)       
       
        offset = vec_ref_co - obj.location  
       
        offset_x = [offset[0] + loc_offset[0], 0, 0]
        offset_y = [0, offset[1] + loc_offset[1], 0]
        offset_z = [0, 0, offset[2] + loc_offset[2]]   
        
        def movement(vec):
            obj_mtx = obj.matrix_world.copy()
            # find pivot displacement vector
            move_pivot = Vector(vec)
             
            # move pivot point = object location
            pivot = obj.location
            pivot += move_pivot         
            
            nm = obj_mtx.inverted() @ Matrix.Translation(-move_pivot) * obj_mtx

            # move mesh 
            me.transform(nm) 
            
        if loc_x: 
            movement(offset_x)
       
        if loc_y:
            movement(offset_y)   
       
        if loc_z:
            movement(offset_z)

    ref_co = bpy.context.scene.cursor.location  
    move_pivot(act_obj)
   
    for obj in sel_obj:   
        move_pivot(obj)           

                    

class RTS_OT_RePattern_Origin_Cursor_Align(bpy.types.Operator):
    """align origin to cursor"""
    bl_idname = "rts_ot.repattern_origin_cursor_align"
    bl_label = "Origin Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    loc_x : BoolProperty (name = "Align to X axis", default= False, description= "Enable X axis alignment")
    loc_y : BoolProperty (name = "Align to Y axis", default= False, description= "Enable Y axis alignment")                               
    loc_z : BoolProperty (name = "Align to Z axis", default= False, description= "Enable Z axis alignment")

    loc_offset : FloatVectorProperty(name="Location Offset", description="Offset for location align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)       

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(align=True)              
        box.separator()      
        
        row = box.row()
        row.prop(self, 'active_too')    

        box.separator()      
     
        row = box.row(align=True)
        row.prop(self, "loc_x", text="X")       
        row.prop(self, "loc_y", text="Y") 
        row.prop(self, "loc_z", text="Z")
       
        box.separator()              
        
        row = box.row()   
        row.prop(self, 'loc_offset', text='')     
       
        box.separator()    

    def execute(self, context):
        origin_cursor_function(self.loc_x, self.loc_y, self.loc_z, self.loc_offset)                     
        return {'FINISHED'} 
    
