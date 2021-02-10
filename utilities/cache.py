import bpy

# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    rts = bpy.context.window_manager.rp_props_repattern
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(rts, key))


# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    rts = bpy.context.window_manager.rp_props_repattern
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(rts, key, getattr(self, key))
