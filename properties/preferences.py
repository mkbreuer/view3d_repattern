import bpy
from ..utilities.utils import get_name, get_prefs, get_path
from bpy.props import * #PointerProperty, EnumProperty

# updater ops import, all setup in this file
from .. import addon_updater_ops

from .props_panel import PropsGroup_Panel, draw_props_panel
from .props_keys import PropsGroup_Keys, draw_props_keys
from .props_camera import PropsGroup_Camera
from .props_clean import PropsGroup_Clean
from .props_clone import PropsGroup_Clone
from .props_curve import PropsGroup_Curve
from .props_coll import PropsGroup_Collection
from .props_cutout import PropsGroup_Cutout
from .props_grid import PropsGroup_Grid
from .props_info import draw_props_info
from .props_insert import PropsGroup_Insert
from .props_instance import PropsGroup_Instance
from .props_light import PropsGroup_Light
from .props_material import PropsGroup_Material, draw_props_mat
from .props_modif import PropsGroup_Modifier
from .props_origin import PropsGroup_Origin
from .props_render import PropsGroup_Render
from .props_transform import PropsGroup_Transform
from .props_url import draw_props_url


@addon_updater_ops.make_annotations
class AddonPrefs_RePattern(bpy.types.AddonPreferences):
    path = get_path()
    bl_idname = get_name() #addon_name
    #bl_idname = __package__

    # Property Groups 
    panel_type: PointerProperty(type=PropsGroup_Panel)
    keymap_type: PointerProperty(type=PropsGroup_Keys) 
    camera_type: PointerProperty(type=PropsGroup_Camera) 
    clean_type: PointerProperty(type=PropsGroup_Clean) 
    clone_type: PointerProperty(type=PropsGroup_Clone) 
    curve_type: PointerProperty(type=PropsGroup_Curve) 
    coll_type: PointerProperty(type=PropsGroup_Collection) 
    cutout_type: PointerProperty(type=PropsGroup_Cutout) 
    grid_type: PointerProperty(type=PropsGroup_Grid) 
    insert_type: PointerProperty(type=PropsGroup_Insert) 
    instance_type: PointerProperty(type=PropsGroup_Instance) 
    light_type: PointerProperty(type=PropsGroup_Light) 
    mat_type: PointerProperty(type=PropsGroup_Material) 
    modif_type: PointerProperty(type=PropsGroup_Modifier) 
    origin_type: PointerProperty(type=PropsGroup_Origin) 
    render_type: PointerProperty(type=PropsGroup_Render) 
    transform_type: PointerProperty(type=PropsGroup_Transform) 

    # Theme Tabs
    prefs_tabs : EnumProperty(
        items=(('info',   "Updater",     "Updater"),
               ('ui',     "Layout",      "Layout"),
               #('keys',   "Keymap",      "Keymap"),
               ('url',    "URLs",        "URLs")),
        default='info')

    #----------------------------

    # ADDON UPDATER #

    auto_check_update : BoolProperty(name = "Auto-check for Update", description = "If enabled, auto-check for updates using an interval", default = False)
    updater_intrval_months : IntProperty(name='Months', description = "Number of months between checking for updates", default=0, min=0)
    updater_intrval_days : IntProperty(name='Days', description = "Number of days between checking for updates", default=7, min=0, max=31)
    updater_intrval_hours : IntProperty(name='Hours', description = "Number of hours between checking for updates", default=0, min=0, max=23)
    updater_intrval_minutes : IntProperty(name='Minutes', description = "Number of minutes between checking for updates", default=0, min=0, max=59)

    #----------------------------

    def draw(self, context):
        layout = self.layout.column(align=True)
        
        prefs = get_prefs() 

        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
               
        # General Info
        if self.prefs_tabs == 'info': 
            addon_updater_ops.update_settings_ui(self, context)
        
        # Layout
        if self.prefs_tabs == 'ui':           
            box = layout.box()
            draw_props_panel(prefs, box)  
            draw_props_mat(prefs, box)  

        # # Keymaps
        # if self.prefs_tabs == 'keys':
        #     box = layout.box()
        #     draw_props_keys(prefs, box)

        # URL
        if self.prefs_tabs == 'url':
            box = layout.box()
            draw_props_url(self, box)

