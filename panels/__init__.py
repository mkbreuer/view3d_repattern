
import bpy
from ..utilities.utils import get_prefs

from .main_panel import RTS_PT_RePattern_Panel
from .sub_image import RTS_PT_Repattern_Color_Management


panels = (
    RTS_PT_RePattern_Panel,
    RTS_PT_Repattern_Color_Management,
)

def update_panel(self, context):
    prefs = get_prefs()
    message = "Updating Panel has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            if prefs is not None:
                panel.bl_category = prefs.panel_type.category
            bpy.utils.register_class(panel)

    except Exception as e:
        #print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        self.report({'INFO'}, __name__, message, e) 
        pass
