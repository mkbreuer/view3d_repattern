import bpy


from .preferences import AddonPrefs_RePattern
from .props_camera import PropsGroup_Camera
from .props_clean import PropsGroup_Clean
from .props_clone import PropsGroup_Clone
from .props_coll import PropsGroup_Collection
from .props_curve import PropsGroup_Curve
from .props_cutout import PropsGroup_Cutout
from .props_grid import PropsGroup_Grid
from .props_insert import PropsGroup_Insert
from .props_instance import PropsGroup_Instance
from .props_keys import PropsGroup_Keys
from .props_light import PropsGroup_Light
from .props_material import PropsGroup_Material
from .props_modif import PropsGroup_Modifier
from .props_origin import PropsGroup_Origin
from .props_panel import PropsGroup_Panel
from .props_render import PropsGroup_Render
from .props_transform import PropsGroup_Transform

classes = (
    PropsGroup_Camera,
    PropsGroup_Clean,
    PropsGroup_Clone,
    PropsGroup_Collection,
    PropsGroup_Curve,
    PropsGroup_Cutout,
    PropsGroup_Grid,
    PropsGroup_Insert,
    PropsGroup_Instance,
    PropsGroup_Keys,
    PropsGroup_Light,
    PropsGroup_Material,
    PropsGroup_Modifier,
    PropsGroup_Origin,
    PropsGroup_Panel,
    PropsGroup_Render,
    PropsGroup_Transform,
    AddonPrefs_RePattern,    
)

def register_properties():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    bpy.types.WindowManager.rp_props_repattern = bpy.props.PointerProperty(type = PropsGroup_Material)


def unregister_properties():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.WindowManager.rp_props_repattern