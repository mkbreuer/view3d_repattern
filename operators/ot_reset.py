import bpy

class RTS_OT_RePattern_Reset_3D_View(bpy.types.Operator):
    bl_description = "Resets the 3D view to the blender defaults"
    bl_idname = "rts_ot.reset_view"
    bl_label = "Reset 3D View"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self,context):
       
        bpy.context.area.spaces[0].shading.type = "SOLID"
        bpy.context.area.spaces[0].shading.studiolight_background_alpha = 0
        if bpy.app.version[1] == 83: bpy.context.area.spaces[0].shading.studiolight_background_blur = 0.5
        bpy.context.area.spaces[0].shading.studiolight_intensity = 1
        bpy.context.area.spaces[0].shading.use_scene_lights = False
        bpy.context.area.spaces[0].shading.use_scene_world = False
        bpy.context.area.spaces[0].overlay.show_floor = True
        bpy.context.area.spaces[0].overlay.show_axis_x = True
        bpy.context.area.spaces[0].overlay.show_axis_y = True
        bpy.context.area.spaces[0].overlay.show_axis_z = False
        bpy.context.area.spaces[0].overlay.show_text = True
        bpy.context.area.spaces[0].overlay.show_cursor = True
        bpy.context.area.spaces[0].overlay.show_look_dev = True
        bpy.context.area.spaces[0].overlay.show_annotation = True
        bpy.context.area.spaces[0].overlay.show_extras = True
        bpy.context.area.spaces[0].overlay.show_relationship_lines = True
        bpy.context.area.spaces[0].overlay.show_outline_selected = True
        bpy.context.area.spaces[0].overlay.show_bones = True
        bpy.context.area.spaces[0].overlay.show_motion_paths = True
        bpy.context.area.spaces[0].overlay.show_object_origins = True
        bpy.context.area.spaces[0].overlay.show_wireframes = False
        bpy.context.area.spaces[0].overlay.show_face_orientation = False
       
        return {"FINISHED"}