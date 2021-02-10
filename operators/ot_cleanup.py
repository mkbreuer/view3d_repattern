import bpy
from bpy import *
from bpy.props import *

from ..utilities.utils import get_prefs


# OPERATOR # 
def draw_cutout_operator(clean_props, context):

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')  
    bpy.ops.mesh.select_all(action='SELECT')
    
    if clean_props.cutout_reso == "32px":       
        bpy.ops.mesh.bisect(plane_co=(0, -1.5625, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-1.5625, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 1.5625, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(1.5625, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "64px":       
        bpy.ops.mesh.bisect(plane_co=(0, -3.125, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-3.125, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 3.125, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(3.125, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "128px":       
        bpy.ops.mesh.bisect(plane_co=(0, -6.25, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-6.25, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 6.25, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT') 
        bpy.ops.mesh.bisect(plane_co=(6.25, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "256px":       
        bpy.ops.mesh.bisect(plane_co=(0, -12.5, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-12.5, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 12.5, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(12.5, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "512px":       
        bpy.ops.mesh.bisect(plane_co=(0, -25, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-25, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 25, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(25, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "1024px":       
        bpy.ops.mesh.bisect(plane_co=(0, -50, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-50, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 50, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(50, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "2048px":       
        bpy.ops.mesh.bisect(plane_co=(0, -100, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-100, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 100, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(100, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "4096px":       
        bpy.ops.mesh.bisect(plane_co=(0, -200, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-200, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, 200, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT') 
        bpy.ops.mesh.bisect(plane_co=(200, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    if clean_props.cutout_reso == "custom":       
        bpy.ops.mesh.bisect(plane_co=(0, -clean_props.custom_cutout, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(-clean_props.custom_cutout, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(plane_co=(0, clean_props.custom_cutout, 0), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)
        bpy.ops.mesh.select_all(action='SELECT') 
        bpy.ops.mesh.bisect(plane_co=(clean_props.custom_cutout, 0, 0), plane_no=(1, 0, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=0, xend=0, ystart=0, yend=0)

    bpy.ops.mesh.select_all(action='SELECT')       
    bpy.ops.mesh.normals_make_consistent() 

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
   
    if clean_props.cutout_edit == False:   
        bpy.ops.object.mode_set(mode='EDIT')

       
class RTS_OT_RePattern_Cutout_Center(bpy.types.Operator):
    """does: convert to mesh > merged wrap around > cutout center"""
    bl_idname = "rts_ot.repattern_cutout_center"
    bl_label = "CutOut"
    bl_options = {'REGISTER', 'UNDO'}


    def draw(self, context):
        layout = self.layout
        
        prefs = get_prefs()
        clean_props = prefs.clean_type

        col = layout.column(align=True)
        box = col.box().column(align=True)             

        row = box.row(align=True)  
        row.label(text='CutOut Size')         
        row.prop(clean_props, 'cutout_reso', text='')         
     
        if clean_props.cutout_reso == 'custom':
           
            box.separator()
            
            row = box.row(align=True)        
            row.prop(clean_props, 'custom_cutout')          
             
        box.separator()
  
        row = box.row(align=True)         
        row.prop(clean_props, 'cutout_edit')    

        box.separator()


    def execute(self, context):   
 
        prefs = get_prefs()
        clean_props = prefs.clean_type 
 
        bpy.ops.object.mode_set(mode='OBJECT')            

        bpy.ops.object.select_linked(type='OBDATA')      
        if len(bpy.context.selected_objects) == 1:        

            if context.mode == ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]:      
                bpy.ops.object.editmode_toggle()                        
            else:
                pass   
    
            if context.mode == "EDIT_MESH":
                draw_cutout_operator(clean_props, context)

            else:       
                draw_cutout_operator(clean_props, context)    
                bpy.ops.object.editmode_toggle() 

            self.report({'INFO'}, "CutOut Center!")            
        else:
            self.report({'INFO'}, "Merge Instances first!")            

        return {'FINISHED'}







# OPERATOR # 
def draw_cleanup_operator(clean_props, context):

    if context.mode == "EDIT_MESH":
        pass          
    else:      
        bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.mesh.select_all(action='DESELECT')                               
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    obj = bpy.context.object 
    mat = obj.matrix_world
  
    for v in obj.data.vertices:
        
       # Multiply world matrix of the object 
       # with coordinate for global coordinate
        co = mat @ v.co

        if clean_props.cleanup_reso == "32px":       

            if co.x > 1.5626:
                v.select = True                      
            
            elif co.x < -1.5626:
                v.select = True  

            elif co.y > 1.5626: 
                v.select = True                  
            
            elif co.y < -1.5626: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 1.5626:             
                    v.select = True                   
                    
                elif co.z < -1.5626:             
                    v.select = True  

        if clean_props.cleanup_reso == "64px":       

            if co.x > 3.1251:
                v.select = True                      
            
            elif co.x < -3.1251:
                v.select = True  

            elif co.y > 3.1251: 
                v.select = True                  
            
            elif co.y < -3.1251: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 3.1251:             
                    v.select = True                   
                    
                elif co.z < -3.1251:             
                    v.select = True  

        if clean_props.cleanup_reso == "128px":       

            if co.x > 6.2501:
                v.select = True                      
            
            elif co.x < -6.2501:
                v.select = True  

            elif co.y > 6.2501: 
                v.select = True                  
            
            elif co.y < -6.2501: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 6.2501:             
                    v.select = True                   
                    
                elif co.z < -6.2501:             
                    v.select = True  

        if clean_props.cleanup_reso == "256px":       

            if co.x > 12.501:
                v.select = True                      
            
            elif co.x < -12.501:
                v.select = True  

            elif co.y > 12.501: 
                v.select = True                  
            
            elif co.y < -12.501: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 12.501:             
                    v.select = True                   
                    
                elif co.z < -12.501:             
                    v.select = True  

        if clean_props.cleanup_reso == "512px":       

            if co.x > 25.001:
                v.select = True                      
            
            elif co.x < -25.001:
                v.select = True  

            elif co.y > 25.001: 
                v.select = True                  
            
            elif co.y < -25.001: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 25.001:             
                    v.select = True                   
                    
                elif co.z < -25.001:             
                    v.select = True  

        if clean_props.cleanup_reso == "1024px":       
            
            if co.x > 50.001:
                v.select = True                      
            
            elif co.x < -50.001:
                v.select = True  

            elif co.y > 50.001: 
                v.select = True                  
            
            elif co.y < -50.001: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 50.001:             
                    v.select = True                   
                    
                elif co.z < -50.001:             
                    v.select = True     

        if clean_props.cleanup_reso == "2048px":       
          
            if co.x > 100.001:
                v.select = True                      
            
            elif co.x < -100.001:
                v.select = True  

            elif co.y > 100.001: 
                v.select = True                  
            
            elif co.y < -100.001: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 100.001:             
                    v.select = True                   
                    
                elif co.z < -100.001:             
                    v.select = True  

        if clean_props.cleanup_reso == "4096px":       

            if co.x > 200.001:
                v.select = True                      
            
            elif co.x < -200.001:
                v.select = True  

            elif co.y > 200.001: 
                v.select = True                  
            
            elif co.y < -200.001: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > 200.001:             
                    v.select = True                   
                    
                elif co.z < -200.001:             
                    v.select = True  

        
        if clean_props.cleanup_reso == "custom":       

            if co.x > clean_props.custom_cleanup + 0.001:
                v.select = True                      
            
            elif co.x < -clean_props.custom_cleanup + -0.001:
                v.select = True  

            elif co.y > clean_props.custom_cleanup + 0.001: 
                v.select = True                  
            
            elif co.y < -clean_props.custom_cleanup + -0.001: 
                v.select = True   
           
            if clean_props.cleanup_3D == True: 

                if co.z > clean_props.custom_cleanup + 0.001:             
                    v.select = True                   
                    
                elif co.z < -clean_props.custom_cleanup + -0.001:             
                    v.select = True  

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.delete(type='VERT')
  
    if clean_props.cleanup_edit == True:      
        bpy.ops.object.mode_set(mode='OBJECT') 
    else:
        pass  



class RTS_OT_RePattern_CleanUp_Outside(bpy.types.Operator):
    """remove vertices around the center: xy (2D) or xyz (3D)"""
    bl_idname = "rts_ot.repattern_cleanup_pattern"
    bl_label = "CleanUp"
    bl_options = {'REGISTER', 'UNDO'}
    

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align=True)

        box = col.box().column(align=True)             

        row = box.row(align=True)  
        row.label(text='Cleanup Size')        
        row.prop(clean_props, 'cleanup_reso')       

        box.separator()
        
        row = box.row(align=True)         
        row.prop(clean_props, 'cleanup_3D')       
     
        if clean_props.cleanup_reso == 'custom':
           
            box.separator()
            
            row = box.row(align=True)        
            row.prop(clean_props, 'custom_cleanup')          
             
        box.separator()
  
        row = box.row(align=True)         
        row.prop(clean_props, 'cleanup_edit')    

        box.separator()


    def execute(self, context):   
        
        prefs = get_prefs()
        clean_props = prefs.clean_type     

        if context.mode == "EDIT_MESH":
            
            bpy.ops.object.editmode_toggle() 
            
            bpy.ops.object.select_linked(type='OBDATA')      
            if len(bpy.context.selected_objects) == 1:
                bpy.ops.object.editmode_toggle()           
          
                draw_cleanup_operator(clean_props, context)          

                self.report({'INFO'}, "CleanUp around Center!")   
            else:
                self.report({'INFO'}, "Merge Instances first!")            
       
        else:       
                  
            bpy.ops.object.select_linked(type='OBDATA')      
            if len(bpy.context.selected_objects) == 1:

                draw_cleanup_operator(clean_props, context)      
                bpy.ops.object.editmode_toggle() 
                
                self.report({'INFO'}, "CleanUp around Center!")              
            else:
                self.report({'INFO'}, "Merge Instances first!")            
       
        return {'FINISHED'}


