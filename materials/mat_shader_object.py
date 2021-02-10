import bpy
from bpy.props import *

from ..utilities.utils import get_prefs
from ..layouts.ui_material_draw_panel import mat_props_draw_panel
from .mat_utils import *

import random as rand

class RTS_OT_Repattern_Shader_Object(bpy.types.Operator):
    """enable object colour on all selected objects"""
    bl_idname = "rts_ot.repattern_shader_object"
    bl_label = "Object Colour"
    bl_options = {'REGISTER', 'UNDO'}         
    
    mode : StringProperty(default="", description="change if operation with a string", options={'HIDDEN'})  

    def draw(self, context):
        layout = self.layout.column(align=True)
        box = layout.box().column(align=True)          
        mat_props_draw_panel(layout, box)

    def execute(self, context):
        prefs = get_prefs()
        mat_prefs = prefs.mat_type

        # store active # 
        view_layer = bpy.context.view_layer  
        target = view_layer.objects.active 

        selected = bpy.context.selected_objects             
        obj_list = [obj for obj in selected]
        if not obj_list:  
            self.report({'INFO'}, "No Selection!")  
            return {'CANCELLED'}    
        else:  

            # CONTRAST
                
            if "gray_00" in self.mode: add_color = hex_to_rgb_new(0x000000)      
            if "gray_20" in self.mode: add_color = hex_to_rgb_new(0x333333)         
            if "gray_40" in self.mode: add_color = hex_to_rgb_new(0x666666)         
            if "gray_50" in self.mode: add_color = hex_to_rgb_new(0x7F7F7F)         
            if "gray_60" in self.mode: add_color = hex_to_rgb_new(0x999999)         
            if "gray_80" in self.mode: add_color = hex_to_rgb_new(0xCCCCCC)                
            if "gray_10" in self.mode: add_color = hex_to_rgb_new(0xFFFFFF)      


            # RED COLORS #

            if "0x601600" in self.mode: add_color = hex_to_rgb_new(0x601600)       
            if "0x861900" in self.mode: add_color = hex_to_rgb_new(0x861900)       
            if "0xb41b00" in self.mode: add_color = hex_to_rgb_new(0xb41b00)        
            if "0xd21c00" in self.mode: add_color = hex_to_rgb_new(0xd21c00)       
            if "0xef1f00" in self.mode: add_color = hex_to_rgb_new(0xef1f00)         
            if "0xee3d1a" in self.mode: add_color = hex_to_rgb_new(0xee3d1a)      
            if "0xf05d42" in self.mode: add_color = hex_to_rgb_new(0xf05d42)      
            if "0xf1826a" in self.mode: add_color = hex_to_rgb_new(0xf1826a)      
            if "0xf4aa97" in self.mode: add_color = hex_to_rgb_new(0xf4aa97)      
            if "0xf8d4c2" in self.mode: add_color = hex_to_rgb_new(0xf8d4c2)      
            if "0x600000" in self.mode: add_color = hex_to_rgb_new(0x600000)         
            if "0x870000" in self.mode: add_color = hex_to_rgb_new(0x870000)      
            if "0xb20000" in self.mode: add_color = hex_to_rgb_new(0xb20000)        
            if "0xcf0000" in self.mode: add_color = hex_to_rgb_new(0xcf0000)       
            if "0xec0000" in self.mode: add_color = hex_to_rgb_new(0xec0000)       
            if "0xee1a1f" in self.mode: add_color = hex_to_rgb_new(0xee1a1f)      
            if "0xef3e44" in self.mode: add_color = hex_to_rgb_new(0xef3e44)      
            if "0xf0686f" in self.mode: add_color = hex_to_rgb_new(0xf0686f)      
            if "0xef9394" in self.mode: add_color = hex_to_rgb_new(0xef9394)      
            if "0xf7c8cb" in self.mode: add_color = hex_to_rgb_new(0xf7c8cb)             
            if "0x550020" in self.mode: add_color = hex_to_rgb_new(0x550020)         
            if "0x750027" in self.mode: add_color = hex_to_rgb_new(0x750027)      
            if "0x9a002e" in self.mode: add_color = hex_to_rgb_new(0x9a002e)        
            if "0xb30033" in self.mode: add_color = hex_to_rgb_new(0xb30033)       
            if "0xce003b" in self.mode: add_color = hex_to_rgb_new(0xce003b)       
            if "0xd51252" in self.mode: add_color = hex_to_rgb_new(0xd51252)      
            if "0xdc3670" in self.mode: add_color = hex_to_rgb_new(0xdc3670)      
            if "0xe05d8e" in self.mode: add_color = hex_to_rgb_new(0xe05d8e)      
            if "0xde91af" in self.mode: add_color = hex_to_rgb_new(0xde91af)      
            if "0xefc2d3" in self.mode: add_color = hex_to_rgb_new(0xefc2d3)      
            if "0x490031" in self.mode: add_color = hex_to_rgb_new(0x490031)       
            if "0x640040" in self.mode: add_color = hex_to_rgb_new(0x640040)       
            if "0x83004f" in self.mode: add_color = hex_to_rgb_new(0x83004f)        
            if "0x970056" in self.mode: add_color = hex_to_rgb_new(0x970056)       
            if "0xac0069" in self.mode: add_color = hex_to_rgb_new(0xac0069)         
            if "0xb51380" in self.mode: add_color = hex_to_rgb_new(0xb51380)      
            if "0xc02e93" in self.mode: add_color = hex_to_rgb_new(0xc02e93)      
            if "0xcf57ac" in self.mode: add_color = hex_to_rgb_new(0xcf57ac)      
            if "0xdb85c6" in self.mode: add_color = hex_to_rgb_new(0xdb85c6)      
            if "0xecbbdc" in self.mode: add_color = hex_to_rgb_new(0xecbbdc)            
            if "0x410048" in self.mode: add_color = hex_to_rgb_new(0x410048)         
            if "0x580061" in self.mode: add_color = hex_to_rgb_new(0x580061)      
            if "0x70007f" in self.mode: add_color = hex_to_rgb_new(0x70007f)        
            if "0x830093" in self.mode: add_color = hex_to_rgb_new(0x830093)       
            if "0x9500a7" in self.mode: add_color = hex_to_rgb_new(0x9500a7)       
            if "0xa600ae" in self.mode: add_color = hex_to_rgb_new(0xa600ae)      
            if "0xb42cc2" in self.mode: add_color = hex_to_rgb_new(0xb42cc2)      
            if "0xc450d1" in self.mode: add_color = hex_to_rgb_new(0xc450d1)      
            if "0xd481e4" in self.mode: add_color = hex_to_rgb_new(0xd481e4)      
            if "0xecb5f8" in self.mode: add_color = hex_to_rgb_new(0xecb5f8)               
            if "0x250041" in self.mode: add_color = hex_to_rgb_new(0x250041)         
            if "0x300056" in self.mode: add_color = hex_to_rgb_new(0x300056)      
            if "0x3d0070" in self.mode: add_color = hex_to_rgb_new(0x3d0070)        
            if "0x430082" in self.mode: add_color = hex_to_rgb_new(0x430082)       
            if "0x490090" in self.mode: add_color = hex_to_rgb_new(0x490090)       
            if "0x5d00a6" in self.mode: add_color = hex_to_rgb_new(0x5d00a6)      
            if "0x752baf" in self.mode: add_color = hex_to_rgb_new(0x752baf)      
            if "0x8c52c6" in self.mode: add_color = hex_to_rgb_new(0x8c52c6)      
            if "0xad7dd7" in self.mode: add_color = hex_to_rgb_new(0xad7dd7)      
            if "0xd4b5f0" in self.mode: add_color = hex_to_rgb_new(0xd4b5f0)      


            # BLUE COLORS #     

            if "0x160042" in self.mode: add_color = hex_to_rgb_new(0x160042)       
            if "0x1b005a" in self.mode: add_color = hex_to_rgb_new(0x1b005a)      
            if "0x1e0075" in self.mode: add_color = hex_to_rgb_new(0x1e0075)      
            if "0x200084" in self.mode: add_color = hex_to_rgb_new(0x200084)      
            if "0x220098" in self.mode: add_color = hex_to_rgb_new(0x220098)       
            if "0x3300a4" in self.mode: add_color = hex_to_rgb_new(0x3300a4)       
            if "0x4c2bbb" in self.mode: add_color = hex_to_rgb_new(0x4c2bbb)       
            if "0x6d51ca" in self.mode: add_color = hex_to_rgb_new(0x6d51ca)       
            if "0x957fd9" in self.mode: add_color = hex_to_rgb_new(0x957fd9)       
            if "0xc7b9f1" in self.mode: add_color = hex_to_rgb_new(0xc7b9f1)          
            if "0x060642" in self.mode: add_color = hex_to_rgb_new(0x060642) 
            if "0x0B0058" in self.mode: add_color = hex_to_rgb_new(0x0B0058)      
            if "0x0B0072" in self.mode: add_color = hex_to_rgb_new(0x0b0072)      
            if "0x0b0088" in self.mode: add_color = hex_to_rgb_new(0x0b0088)      
            if "0x0c009a" in self.mode: add_color = hex_to_rgb_new(0x0c009a)      
            if "0x1d1dad" in self.mode: add_color = hex_to_rgb_new(0x1d1dad)      
            if "0x373bbb" in self.mode: add_color = hex_to_rgb_new(0x373bbb)      
            if "0x5b5ccd" in self.mode: add_color = hex_to_rgb_new(0x5b5ccd)      
            if "0x8286df" in self.mode: add_color = hex_to_rgb_new(0x8286df)      
            if "0xb9c0f0" in self.mode: add_color = hex_to_rgb_new(0xb9c0f0)          
            if "0x0d1944" in self.mode: add_color = hex_to_rgb_new(0x0d1944)       
            if "0x111d60" in self.mode: add_color = hex_to_rgb_new(0x111d60)      
            if "0x11227a" in self.mode: add_color = hex_to_rgb_new(0x11227a)      
            if "0x14268d" in self.mode: add_color = hex_to_rgb_new(0x14268d)      
            if "0x1729a6" in self.mode: add_color = hex_to_rgb_new(0x1729a6)       
            if "0x233dae" in self.mode: add_color = hex_to_rgb_new(0x233dae)       
            if "0x3c57bd" in self.mode: add_color = hex_to_rgb_new(0x3c57bd)       
            if "0x5b76cb" in self.mode: add_color = hex_to_rgb_new(0x5b76cb)       
            if "0x899dda" in self.mode: add_color = hex_to_rgb_new(0x899dda)       
            if "0xb5cbf4" in self.mode: add_color = hex_to_rgb_new(0xb5cbf4)           
            if "0x112649" in self.mode: add_color = hex_to_rgb_new(0x112649) 
            if "0x153063" in self.mode: add_color = hex_to_rgb_new(0x153063)      
            if "0x193b80" in self.mode: add_color = hex_to_rgb_new(0x193b80)      
            if "0x1c438f" in self.mode: add_color = hex_to_rgb_new(0x1c438f)      
            if "0x1d4ba4" in self.mode: add_color = hex_to_rgb_new(0x1d4ba4)      
            if "0x2b5faf" in self.mode: add_color = hex_to_rgb_new(0x2b5faf)      
            if "0x4176c2" in self.mode: add_color = hex_to_rgb_new(0x4176c2)      
            if "0x5e91d9" in self.mode: add_color = hex_to_rgb_new(0x5e91d9)      
            if "0x8bb3e3" in self.mode: add_color = hex_to_rgb_new(0x8bb3e3)      
            if "0xc1d3ef" in self.mode: add_color = hex_to_rgb_new(0xc1d3ef)           
            if "0x162f4a" in self.mode: add_color = hex_to_rgb_new(0x162f4a)       
            if "0x193e66" in self.mode: add_color = hex_to_rgb_new(0x193e66)      
            if "0x204f86" in self.mode: add_color = hex_to_rgb_new(0x204f86)      
            if "0x205c96" in self.mode: add_color = hex_to_rgb_new(0x205c96)      
            if "0x226aac" in self.mode: add_color = hex_to_rgb_new(0x226aac)       
            if "0x327bbd" in self.mode: add_color = hex_to_rgb_new(0x327bbd)       
            if "0x4690c8" in self.mode: add_color = hex_to_rgb_new(0x4690c8)       
            if "0x65aad1" in self.mode: add_color = hex_to_rgb_new(0x65aad1)       
            if "0x90c0e2" in self.mode: add_color = hex_to_rgb_new(0x90c0e2)       
            if "0xc2def5" in self.mode: add_color = hex_to_rgb_new(0xc2def5)           
            if "0x193d4e" in self.mode: add_color = hex_to_rgb_new(0x193d4e) 
            if "0x21546c" in self.mode: add_color = hex_to_rgb_new(0x21546c)      
            if "0x266c8b" in self.mode: add_color = hex_to_rgb_new(0x266c8b)      
            if "0x2a7da4" in self.mode: add_color = hex_to_rgb_new(0x2a7da4)      
            if "0x2e8bb7" in self.mode: add_color = hex_to_rgb_new(0x2e8bb7)      
            if "0x3b9fc4" in self.mode: add_color = hex_to_rgb_new(0x3b9fc4)      
            if "0x4dadce" in self.mode: add_color = hex_to_rgb_new(0x4dadce)      
            if "0x6bc0de" in self.mode: add_color = hex_to_rgb_new(0x6bc0de)      
            if "0x93d0e7" in self.mode: add_color = hex_to_rgb_new(0x93d0e7)      
            if "0xc2edf0" in self.mode: add_color = hex_to_rgb_new(0xc2edf0)      



            # GREEN COLORS #

            if "0x1c4927" in self.mode: add_color = hex_to_rgb_new(0x1c4927)  
            if "0x246533" in self.mode: add_color = hex_to_rgb_new(0x246533)  
            if "0x2c8240" in self.mode: add_color = hex_to_rgb_new(0x2c8240)  
            if "0x319845" in self.mode: add_color = hex_to_rgb_new(0x319845)  
            if "0x36aa4e" in self.mode: add_color = hex_to_rgb_new(0x36aa4e)  
            if "0x3fbb61" in self.mode: add_color = hex_to_rgb_new(0x3fbb61)  
            if "0x53c47e" in self.mode: add_color = hex_to_rgb_new(0x53c47e)  
            if "0x6dd598" in self.mode: add_color = hex_to_rgb_new(0x6dd598)  
            if "0x93e2b5" in self.mode: add_color = hex_to_rgb_new(0x93e2b5)  
            if "0xc2efd8" in self.mode: add_color = hex_to_rgb_new(0xc2efd8)    
            if "0x1c4500" in self.mode: add_color = hex_to_rgb_new(0x1c4500)      
            if "0x225d00" in self.mode: add_color = hex_to_rgb_new(0x225d00)      
            if "0x2a7900" in self.mode: add_color = hex_to_rgb_new(0x2a7900)        
            if "0x308e00" in self.mode: add_color = hex_to_rgb_new(0x308e00)        
            if "0x359f00" in self.mode: add_color = hex_to_rgb_new(0x359f00)       
            if "0x40ae00" in self.mode: add_color = hex_to_rgb_new(0x40ae00)      
            if "0x54bf2a" in self.mode: add_color = hex_to_rgb_new(0x54bf2a)      
            if "0x6ed252" in self.mode: add_color = hex_to_rgb_new(0x6ed252)      
            if "0x98da8a" in self.mode: add_color = hex_to_rgb_new(0x98da8a)      
            if "0xc0efbb" in self.mode: add_color = hex_to_rgb_new(0xc0efbb)         
            if "0x264a00" in self.mode: add_color = hex_to_rgb_new(0x264a00)       
            if "0x336600" in self.mode: add_color = hex_to_rgb_new(0x336600)      
            if "0x3e8400" in self.mode: add_color = hex_to_rgb_new(0x3e8400)      
            if "0x479800" in self.mode: add_color = hex_to_rgb_new(0x479800)      
            if "0x4eaf00" in self.mode: add_color = hex_to_rgb_new(0x4eaf00)       
            if "0x5fbd00" in self.mode: add_color = hex_to_rgb_new(0x5fbd00)       
            if "0x78c62a" in self.mode: add_color = hex_to_rgb_new(0x78c62a)       
            if "0x95d45c" in self.mode: add_color = hex_to_rgb_new(0x95d45c)       
            if "0xb4e27e" in self.mode: add_color = hex_to_rgb_new(0xb4e27e)       
            if "0xd4efc0" in self.mode: add_color = hex_to_rgb_new(0xd4efc0)   
            if "0x3a5000" in self.mode: add_color = hex_to_rgb_new(0x3a5000)      
            if "0x4e6f00" in self.mode: add_color = hex_to_rgb_new(0x4e6f00)      
            if "0x629100" in self.mode: add_color = hex_to_rgb_new(0x629100)        
            if "0x71a600" in self.mode: add_color = hex_to_rgb_new(0x71a600)        
            if "0x80bf00" in self.mode: add_color = hex_to_rgb_new(0x80bf00)       
            if "0x91cd00" in self.mode: add_color = hex_to_rgb_new(0x91cd00)      
            if "0xa4d32d" in self.mode: add_color = hex_to_rgb_new(0xa4d32d)      
            if "0xb5da56" in self.mode: add_color = hex_to_rgb_new(0xb5da56)      
            if "0xcdee82" in self.mode: add_color = hex_to_rgb_new(0xcdee82)      
            if "0xe2f7b3" in self.mode: add_color = hex_to_rgb_new(0xe2f7b3)       
            if "0x5e6b00" in self.mode: add_color = hex_to_rgb_new(0x5e6b00)       
            if "0x788600" in self.mode: add_color = hex_to_rgb_new(0x788600)      
            if "0x9eb000" in self.mode: add_color = hex_to_rgb_new(0x9eb000)      
            if "0xbdd400" in self.mode: add_color = hex_to_rgb_new(0xbdd400)      
            if "0xd1ed00" in self.mode: add_color = hex_to_rgb_new(0xd1ed00)       
            if "0xe1f400" in self.mode: add_color = hex_to_rgb_new(0xe1f400)       
            if "0xdef22d" in self.mode: add_color = hex_to_rgb_new(0xdef22d)       
            if "0xe5f65a" in self.mode: add_color = hex_to_rgb_new(0xe5f65a)       
            if "0xeef98b" in self.mode: add_color = hex_to_rgb_new(0xeef98b)       
            if "0xf6fdc6" in self.mode: add_color = hex_to_rgb_new(0xf6fdc6)   
            if "0x676800" in self.mode: add_color = hex_to_rgb_new(0x676800)      
            if "0x939300" in self.mode: add_color = hex_to_rgb_new(0x939300)      
            if "0xc0c200" in self.mode: add_color = hex_to_rgb_new(0xc0c200)        
            if "0xeaee00" in self.mode: add_color = hex_to_rgb_new(0xeaee00)        
            if "0xffff00" in self.mode: add_color = hex_to_rgb_new(0xffff00)       
            if "0xfffe00" in self.mode: add_color = hex_to_rgb_new(0xfffe00)      
            if "0xfefe30" in self.mode: add_color = hex_to_rgb_new(0xfefe30)      
            if "0xfefe5a" in self.mode: add_color = hex_to_rgb_new(0xfefe5a)      
            if "0xfffe8d" in self.mode: add_color = hex_to_rgb_new(0xfffe8d)      
            if "0xfefdc9" in self.mode: add_color = hex_to_rgb_new(0xfefdc9)      


            # BROWN COLORS #

            if "0x612700" in self.mode: add_color = hex_to_rgb_new(0x612700)       
            if "0x883000" in self.mode: add_color = hex_to_rgb_new(0x883000)             
            if "0xb53c00" in self.mode: add_color = hex_to_rgb_new(0xb53c00)      
            if "0xd14500" in self.mode: add_color = hex_to_rgb_new(0xd14500)       
            if "0xf04c00" in self.mode: add_color = hex_to_rgb_new(0xf04c00)        
            if "0xf16618" in self.mode: add_color = hex_to_rgb_new(0xf16618)      
            if "0xf0803c" in self.mode: add_color = hex_to_rgb_new(0xf0803c)      
            if "0xf29c6f" in self.mode: add_color = hex_to_rgb_new(0xf29c6f)      
            if "0xf6bd94" in self.mode: add_color = hex_to_rgb_new(0xf6bd94)      
            if "0xfee3d0" in self.mode: add_color = hex_to_rgb_new(0xfee3d0)           
            if "0x602f00" in self.mode: add_color = hex_to_rgb_new(0x602f00)      
            if "0x873e00" in self.mode: add_color = hex_to_rgb_new(0x873e00)      
            if "0xb24f00" in self.mode: add_color = hex_to_rgb_new(0xb24f00)      
            if "0xd45800" in self.mode: add_color = hex_to_rgb_new(0xd45800)       
            if "0xf06300" in self.mode: add_color = hex_to_rgb_new(0xf06300)      
            if "0xf47a19" in self.mode: add_color = hex_to_rgb_new(0xf47a19)      
            if "0xf6943a" in self.mode: add_color = hex_to_rgb_new(0xf6943a)      
            if "0xf1ad65" in self.mode: add_color = hex_to_rgb_new(0xf1ad65)      
            if "0xf6c798" in self.mode: add_color = hex_to_rgb_new(0xf6c798)      
            if "0xfae3c4" in self.mode: add_color = hex_to_rgb_new(0xfae3c4)          
            if "0x633900" in self.mode: add_color = hex_to_rgb_new(0x633900)       
            if "0x8c4c00" in self.mode: add_color = hex_to_rgb_new(0x8c4c00)             
            if "0xb76100" in self.mode: add_color = hex_to_rgb_new(0xb76100)      
            if "0xcf7000" in self.mode: add_color = hex_to_rgb_new(0xcf7000)       
            if "0xf17900" in self.mode: add_color = hex_to_rgb_new(0xf17900)        
            if "0xf48e00" in self.mode: add_color = hex_to_rgb_new(0xf48e00)      
            if "0xf5a637" in self.mode: add_color = hex_to_rgb_new(0xf5a637)      
            if "0xf7bb67" in self.mode: add_color = hex_to_rgb_new(0xf7bb67)      
            if "0xf9d19a" in self.mode: add_color = hex_to_rgb_new(0xf9d19a)      
            if "0xfde7c9" in self.mode: add_color = hex_to_rgb_new(0xfde7c9)            
            if "0x614400" in self.mode: add_color = hex_to_rgb_new(0x614400)      
            if "0x8a5c00" in self.mode: add_color = hex_to_rgb_new(0x8a5c00)      
            if "0xb57800" in self.mode: add_color = hex_to_rgb_new(0xb57800)      
            if "0xd68a00" in self.mode: add_color = hex_to_rgb_new(0xd68a00)       
            if "0xf59a00" in self.mode: add_color = hex_to_rgb_new(0xf59a00)      
            if "0xf4ad00" in self.mode: add_color = hex_to_rgb_new(0xf4ad00)      
            if "0xf8bf38" in self.mode: add_color = hex_to_rgb_new(0xf8bf38)      
            if "0xf9cb63" in self.mode: add_color = hex_to_rgb_new(0xf9cb63)      
            if "0xf9da9a" in self.mode: add_color = hex_to_rgb_new(0xf9da9a)      
            if "0xfdebc7" in self.mode: add_color = hex_to_rgb_new(0xfdebc7)          
            if "0x655100" in self.mode: add_color = hex_to_rgb_new(0x655100)       
            if "0x8f7000" in self.mode: add_color = hex_to_rgb_new(0x8f7000)             
            if "0xbd9100" in self.mode: add_color = hex_to_rgb_new(0xbd9100)      
            if "0xd9a400" in self.mode: add_color = hex_to_rgb_new(0xd9a400)       
            if "0xf7bd00" in self.mode: add_color = hex_to_rgb_new(0xf7bd00)        
            if "0xf8ca00" in self.mode: add_color = hex_to_rgb_new(0xf8ca00)      
            if "0xf9d338" in self.mode: add_color = hex_to_rgb_new(0xf9d338)      
            if "0xf8de64" in self.mode: add_color = hex_to_rgb_new(0xf8de64)      
            if "0xfde791" in self.mode: add_color = hex_to_rgb_new(0xfde791)      
            if "0xfdf4c8" in self.mode: add_color = hex_to_rgb_new(0xfdf4c8)            
            if "0x685f00" in self.mode: add_color = hex_to_rgb_new(0x685f00)      
            if "0x938700" in self.mode: add_color = hex_to_rgb_new(0x938700)      
            if "0xbdb200" in self.mode: add_color = hex_to_rgb_new(0xbdb200)      
            if "0xf1e200" in self.mode: add_color = hex_to_rgb_new(0xf1e200)       
            if "0xfcec00" in self.mode: add_color = hex_to_rgb_new(0xfcec00)      
            if "0xfcf022" in self.mode: add_color = hex_to_rgb_new(0xfcf022)      
            if "0xfdf133" in self.mode: add_color = hex_to_rgb_new(0xfdf133)      
            if "0xfef870" in self.mode: add_color = hex_to_rgb_new(0xfef870)      
            if "0xfef78f" in self.mode: add_color = hex_to_rgb_new(0xfef78f)      
            if "0xfdfcc2" in self.mode: add_color = hex_to_rgb_new(0xfdfcc2)
            
            for obj in selected:
                view_layer.objects.active = obj
                bpy.context.space_data.shading.color_type = 'OBJECT'
 
                if mat_prefs.mat_random_object == False:            
                    bpy.context.object.color = add_color 
                    
                    self.report({'INFO'}, 'Object Color!')                             
                
                else:
                    #https://stackoverflow.com/questions/64955774/attributeerror-builtin-function-or-method-object-has-no-attribute-randint
                    # r = random.randint( 0, 255)
                    # AttributeError: 'builtin_function_or_method' object has no attribute 'randint'
                    # solve: import random as rand

                    r = rand.randint(0, 255)
                    g = rand.randint(0, 255)
                    b = rand.randint(0, 255)
                    add_color = (r/255, g/255, b/255,  1)
                    bpy.context.object.color = add_color

                    self.report({'INFO'}, 'Random Object Color!') 


        # reload active #     
        view_layer.objects.active = target
        return {'FINISHED'}   


