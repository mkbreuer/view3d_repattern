import bpy
import string

from ..materials.mat_utils import *
from ..utilities.utils import get_prefs


class RTS_OT_RePattern_Hex_Export(bpy.types.Operator):
    bl_idname = "rts_ot.textools_hex_export"
    bl_label = "Hex Export"
    bl_description = "Export current hex color palette to clipboard"

    def execute(self, context):
        prefs = get_prefs()
        mat_prefs = prefs.mat_type
        
        hex_colors = []
        for i in range(mat_prefs.color_ID_count):
            color = getattr(mat_prefs, "color_ID_color_{}".format(i))
            hex_colors.append(color_to_hex(color))

        bpy.context.window_manager.clipboard = ", ".join(hex_colors)
        
        bpy.ops.rts.OT_report_message('INVOKE_DEFAULT', message="{}x hex colors copied to clipboard".format(len(hex_colors)))   
        return {'FINISHED'}


class RTS_OT_RePattern_Hex_Import(bpy.types.Operator):
    bl_idname = "rts_ot.textools_hex_import"
    bl_label = "Hex Import"
    bl_description = "Import hex colors from the clipboard as current color palette"

    def execute(self, context):
        prefs = get_prefs()
        mat_prefs = prefs.mat_type
 
        # clipboard hex strings
        hex_strings = bpy.context.window_manager.clipboard.split(',')

        for i in range(len(hex_strings)):
            hex_strings[i] = hex_strings[i].strip().strip('#')
            if len(hex_strings[i]) != 6 or not all(c in string.hexdigits for c in hex_strings[i]):
                # incorrect format
                self.report({'ERROR_INVALID_INPUT'}, "Incorrect hex format '{}' use a #RRGGBB pattern".format(hex_strings[i]))
                return
            else:
                name = "color_ID_color_{}".format(i)
                if hasattr(mat_prefs, name):
                    # color Index exists
                    color = hex_to_color( hex_strings[i] )
                    setattr(mat_prefs, name, color)
                else:
                    # more colors imported than supported
                    self.report({'ERROR_INVALID_INPUT'}, "Only {}x colors have been imported instead of {}x".format(i,len(hex_strings)))
                    return
        
        # set number of colors
        mat_prefs.color_ID_count = len(hex_strings)

        bpy.ops.rts.OT_report_message('INVOKE_DEFAULT', message="{}x colors imported from clipboard".format( len(hex_strings) ))
        return {'FINISHED'}


