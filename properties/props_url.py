import bpy


# Layout AddonPrefs
def draw_props_url(self, layout):

    layout.label(text='WEB-Links!',  icon='URL')

    # Tools
    box = layout.box().column(align=True)   
    box.separator() 

    row = box.column(align=False)          
    row.operator("wm.url_open", text="blenderartist").url = "https://blenderartists.org/t/addon-tileable-pattern"
    row.operator("wm.url_open", text="GitHub").url = "https://github.com/mkbreuer/view3d_repattern"

    box.separator()
