import bpy
from bpy import *
from bpy.props import *

from ..utilities.utils import get_prefs
from ..utilities.utils import lock_object, unlock_object

 
class RTS_OT_RePattern_Modifier_Arrays(bpy.types.Operator):
    """does: scale down by a quarter and add two array modifier"""
    bl_idname = "rts_ot.repattern_modifier_arrays"
    bl_label = "XY Arrays"
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout

        prefs = get_prefs()
        modif_prefs = prefs.modif_type      
        
        col = layout.column(align=True)

        box = col.box().column(align=True)                    
        box.separator()   

        row = box.row(align=True)  
        row.label(text='Array Size')                   
        row.prop(modif_prefs, 'xy_array', text='')         
     
        box.separator() 
       
        row = box.row(align=True)  
        row.label(text='Origin -XY')          
        row.prop(modif_prefs, 'origin_minus_xy', text='') 
     
        box.separator() 
              
        row = box.row(align=True)  
        row.label(text='Array Uncut')  
        row.prop(modif_prefs, 'scale_uncut', text='') 

        if modif_prefs.scale_uncut == True:
            pass                    
        else:            
     
            box.separator() 
       
            row = box.row(align=True)  
            row.label(text='Scale 0.5')  
            row.prop(modif_prefs, 'half_scale', text='') 

        box.separator()
        box.separator()



    def execute(self, context):   
        prefs = get_prefs()
        modif_prefs = prefs.modif_type      

        bpy.context.object.name = "Array_Pattern"   
        
        current_x, current_y, current_z =  bpy.context.scene.cursor.location
        
        if modif_prefs.scale_uncut == True:    

            if modif_prefs.origin_minus_xy == True:    
                bpy.ops.tpc.OT_bbox_origin(box_level='bottom', origin_location='minus_y_minus_x')
       
            if modif_prefs.xy_array == "32px":       
                bpy.context.scene.cursor.location = [-3.125, -3.125, 0]
                
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "64px":       
                bpy.context.scene.cursor.location = [-6.25, -6.25, 0]
                
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "128px":       
                bpy.context.scene.cursor.location = [-12.5, -12.5, 0]            
               
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
      
            if modif_prefs.xy_array == "256px":       
                bpy.context.scene.cursor.location = [-25, -25, 0]            

                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "512px":       
                bpy.context.scene.cursor.location = [-50, -50, 0]            
               
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "1024px":       
                bpy.context.scene.cursor.location = [-100, -100, 0]

                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "2048px":       
                bpy.context.scene.cursor.location = [-200, -200, 0]            
     
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "4096px":       
                bpy.context.scene.cursor.location = [-400, -400, 0]            
               
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    
        else:
        
            if modif_prefs.origin_minus_xy == True:    
                bpy.ops.tpc.OT_bbox_origin(box_level='bottom', origin_location='minus_y_minus_x')
       
            if modif_prefs.xy_array == "32px":       
                bpy.context.scene.cursor.location = [-1.5625, -1.5625, 0]
                
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "64px":       
                bpy.context.scene.cursor.location = [-3.125, -3.125, 0]
                
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "128px":       
                bpy.context.scene.cursor.location = [-6.25, -6.25, 0]            
               
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
      
            if modif_prefs.xy_array == "256px":       
                bpy.context.scene.cursor.location = [-12.5, -12.5, 0]            

                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "512px":       
                bpy.context.scene.cursor.location = [-25, -25, 0]            
               
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "1024px":       
                bpy.context.scene.cursor.location = [-50, -50, 0]

                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "2048px":       
                bpy.context.scene.cursor.location = [-100, -100, 0]            
     
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if modif_prefs.xy_array == "4096px":       
                bpy.context.scene.cursor.location = [-200, -200, 0]            
               
                if modif_prefs.origin_minus_xy == False: 
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                    
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        if modif_prefs.scale_uncut == False:
            if modif_prefs.half_scale == True: 
                bpy.ops.transform.resize(value=(0.5, 0.5, 0.5), constraint_axis=(False, False, False), orient_type='GLOBAL')

        bpy.ops.object.modifier_add(type='ARRAY')      
        bpy.context.object.modifiers["Array"].name = "Array_X"        
        bpy.context.object.modifiers["Array_X"].count = 2        

        bpy.ops.object.modifier_add(type='ARRAY')      
        bpy.context.object.modifiers["Array"].name = "Array_Y"  
        bpy.context.object.modifiers["Array_Y"].count = 2
        bpy.context.object.modifiers["Array_Y"].relative_offset_displace[0] = 0
        bpy.context.object.modifiers["Array_Y"].relative_offset_displace[1] = 1
          
        # restrict transform
        lock_object(self, context)

        #print(self)
        self.report({'INFO'}, "XY Array!")   
        return {'FINISHED'}



class RTS_OT_RePattern_Modifier_Scale(bpy.types.Operator):
    """scale selected to choosen xy dimension"""
    bl_idname = "rts_ot.repattern_array_scale"
    bl_label = "Xy Scale"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):   
        prefs = get_prefs()
        modif_prefs = prefs.modif_type

        # unrestrict transform
        unlock_object(self, context)

        # store and use z dimension value
        current_x, current_y, current_z = bpy.context.object.dimensions

        if modif_prefs.array_scale == "32px":       
            bpy.context.object.dimensions = [3.125, 3.125, current_z]

        if modif_prefs.array_scale == "64px":       
            bpy.context.object.dimensions = [6.25, 6.25, current_z]

        if modif_prefs.array_scale == "128px":       
            bpy.context.object.dimensions = [12.5, 12.5, current_z]
            
        if modif_prefs.array_scale == "256px":       
            bpy.context.object.dimensions = [25, 25, current_z]

        if modif_prefs.array_scale == "512px":       
            bpy.context.object.dimensions = [50, 50, current_z]

        if modif_prefs.array_scale == "1024px":       
            bpy.context.object.dimensions = [100, 100, current_z]

        if modif_prefs.array_scale == "2048px":       
            bpy.context.object.dimensions = [200, 200, current_z]

        if modif_prefs.array_scale == "4096px":       
            bpy.context.object.dimensions = [400, 400, current_z]

        # restrict transform
        lock_object(self, context)

        #print(self)
        self.report({'INFO'}, "XY Scale!")     
        return {'FINISHED'}





class RTS_OT_RePattern_Modifier_Offset(bpy.types.Operator):
    """correct modifier array / add single vertices to offset on x/y/xy axis"""
    bl_idname = "rts_ot.repattern_add_vertices_offset"
    bl_label = "Vert Offset"
    bl_options = {'REGISTER', 'UNDO'} 


    def execute(self, context):   
        prefs = get_prefs()
        modif_prefs = prefs.modif_type

        # unrestrict transform
        unlock_object(self, context)

        if bpy.context.mode == "EDIT_MESH":
            pass
        else:
            bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_loose()
        bpy.ops.mesh.delete_loose()
        bpy.ops.object.editmode_toggle()

        # first vertex to array start
        # second vertex to one or both axis
        
        if modif_prefs.verts_offset == "32px":

            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -0.520833

            if modif_prefs.array_divide == "four":
                divide_value = -0.78125

            if modif_prefs.array_divide == "five":
                divide_value = -0.9375

            if modif_prefs.array_divide == "six":
                divide_value = -1.04167

            if modif_prefs.array_divide == "seven":
                divide_value = -1.11607

            if modif_prefs.array_divide == "eight":
                divide_value = -1.17188

            if modif_prefs.array_divide == "nine":
                divide_value = -1.21528

            if modif_prefs.array_divide == "ten":
                divide_value = -1.25
     
            verts_x = [(-1.5625, -1.5625, 0), (divide_value, -1.5625, 0)]          
            verts_y = [(-1.5625, -1.5625, 0), (-1.5625, divide_value, 0)]   
            verts_xy = [(-1.5625, -1.5625, 0), (divide_value, -1.5625, 0), (-1.5625, divide_value, 0)]   

            
        if modif_prefs.verts_offset == "64px":

            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -1.04167

            if modif_prefs.array_divide == "four":
                divide_value = -1.5625

            if modif_prefs.array_divide == "five":
                divide_value = -1.875

            if modif_prefs.array_divide == "six":
                divide_value = -2.08333

            if modif_prefs.array_divide == "seven":
                divide_value = -2.23214

            if modif_prefs.array_divide == "eight":
                divide_value = -2.34375

            if modif_prefs.array_divide == "nine":
                divide_value = -2.43056

            if modif_prefs.array_divide == "ten":
                divide_value = -2.5
     
            verts_x = [(-3.125, -3.125, 0), (divide_value, -3.125, 0)]          
            verts_y = [(-3.125, -3.125, 0), (-3.125, divide_value, 0)]   
            verts_xy = [(-3.125, -3.125, 0), (divide_value, -3.125, 0), (-3.125, divide_value, 0)]   

        if modif_prefs.verts_offset == "128px":
           
            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -1.04167

            if modif_prefs.array_divide == "four":
                divide_value = -1.5625

            if modif_prefs.array_divide == "five":
                divide_value = -1.875

            if modif_prefs.array_divide == "six":
                divide_value = -2.08333

            if modif_prefs.array_divide == "seven":
                divide_value = -2.23214

            if modif_prefs.array_divide == "eight":
                divide_value = -2.34375

            if modif_prefs.array_divide == "nine":
                divide_value = -2.43056

            if modif_prefs.array_divide == "ten":
                divide_value = -5
     
            verts_x = [(-6.25, -6.25, 0), (divide_value, -6.25, 0)]          
            verts_y = [(-6.25, -6.25, 0), (-6.25, divide_value, 0)]   
            verts_xy = [(-6.25, -6.25, 0), (divide_value, -6.25, 0), (-6.25, divide_value, 0)]   


        if modif_prefs.verts_offset == "256px":
            
            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -2.08333

            if modif_prefs.array_divide == "four":
                divide_value = -3.125

            if modif_prefs.array_divide == "five":
                divide_value = -3.75

            if modif_prefs.array_divide == "six":
                divide_value = -4.16667

            if modif_prefs.array_divide == "seven":
                divide_value = -4.46429

            if modif_prefs.array_divide == "eight":
                divide_value = -4.6875

            if modif_prefs.array_divide == "nine":
                divide_value = -4.86111

            if modif_prefs.array_divide == "ten":
                divide_value = -10
     
            verts_x = [(-12.5, -12.5, 0), (divide_value, -12.5, 0)]          
            verts_y = [(-12.5, -12.5, 0), (-12.5, divide_value, 0)]   
            verts_xy = [(-12.5, -12.5, 0), (divide_value, -12.5, 0), (-12.5, divide_value, 0)]             


        if modif_prefs.verts_offset == "512px":
         
            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -8.33333

            if modif_prefs.array_divide == "four":
                divide_value = -12.5

            if modif_prefs.array_divide == "five":
                divide_value = -15

            if modif_prefs.array_divide == "six":
                divide_value = -16.6667

            if modif_prefs.array_divide == "seven":
                divide_value = -17.8571

            if modif_prefs.array_divide == "eight":
                divide_value = -18.75

            if modif_prefs.array_divide == "nine":
                divide_value = -19.4444

            if modif_prefs.array_divide == "ten":
                divide_value = -20
     
            verts_x = [(-25, -25, 0), (divide_value, -25, 0)]          
            verts_y = [(-25, -25, 0), (-25, divide_value, 0)]   
            verts_xy = [(-25, -25, 0), (divide_value, -25, 0), (-25, divide_value, 0)]          


        if modif_prefs.verts_offset == "1024px":
 
            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -33.33333

            if modif_prefs.array_divide == "four":
                divide_value = -50

            if modif_prefs.array_divide == "five":
                divide_value = -60

            if modif_prefs.array_divide == "six":
                divide_value = -66.6667

            if modif_prefs.array_divide == "seven":
                divide_value = -71.4286

            if modif_prefs.array_divide == "eight":
                divide_value = -75

            if modif_prefs.array_divide == "nine":
                divide_value = -77.7778

            if modif_prefs.array_divide == "ten":
                divide_value = -80 
     
            verts_x = [(-50, -50, 0), (divide_value, -50, 0)]          
            verts_y = [(-50, -50, 0), (-50, divide_value, 0)]   
            verts_xy = [(-50, -50, 0), (divide_value, -50, 0), (-50, divide_value, 0)] 


        if modif_prefs.verts_offset == "2048px":
         
            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -16.66667

            if smodif_prefself.array_divide == "four":
                divide_value = -25

            if modif_prefs.array_divide == "five":
                divide_value = -30

            if modif_prefs.array_divide == "six":
                divide_value = -33.33333

            if modif_prefs.array_divide == "seven":
                divide_value = -35.7143

            if modif_prefs.array_divide == "eight":
                divide_value = -37.5

            if modif_prefs.array_divide == "nine":
                divide_value = -38.8889

            if modif_prefs.array_divide == "ten":
                divide_value = -40 

            verts_x = [(-100, -100, 0), (divide_value, -100, 0)]          
            verts_y = [(-100, -100, 0), (-100, divide_value, 0)]   
            verts_xy = [(-25, -100, 0), (divide_value, -100, 0), (-100, divide_value, 0)]        


        if modif_prefs.verts_offset == "4096px":

            if modif_prefs.array_divide == "two":
                divide_value = 0

            if modif_prefs.array_divide == "three":
                divide_value = -66.6667

            if modif_prefs.array_divide == "four":
                divide_value = -100

            if modif_prefs.array_divide == "five":
                divide_value = -120

            if modif_prefs.array_divide == "six":
                divide_value = -133.33333

            if modif_prefs.array_divide == "seven":
                divide_value = -142.857

            if modif_prefs.array_divide == "eight":
                divide_value = -150

            if modif_prefs.array_divide == "nine":
                divide_value = -155.556

            if modif_prefs.array_divide == "ten":
                divide_value = -160

            verts_x = [(-200, -200, 0), (divide_value, -200, 0)]          
            verts_y = [(-200, -200, 0), (-200, divide_value, 0)]   
            verts_xy = [(-200, -200, 0), (divide_value, -200, 0), (-200, divide_value, 0)]          

                
        mesh_data = bpy.data.meshes.new("vertices")  
               
        if modif_prefs.tp_verts_offset == "tp_verts_x":
            mesh_data.from_pydata(verts_x, [], [])  
 
        if modif_prefs.tp_verts_offset == "tp_verts_y":
            mesh_data.from_pydata(verts_y, [], [])  

        if modif_prefs.tp_verts_offset == "tp_verts_xy":
            mesh_data.from_pydata(verts_xy, [], [])  
        
        mesh_data.update()
        obj = bpy.data.objects.new("offset", mesh_data)  
        bpy.context.collection.objects.link(obj)    
        obj.select_set(True)

        if bpy.context.mode == "EDIT_MESH":
            pass
        else:
            bpy.ops.object.join()

        # restrict transform
        lock_object(self, context)
      
        self.report({'INFO'}, "XY Offset!")               
        return {'FINISHED'}


