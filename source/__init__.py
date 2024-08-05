import functools

import bpy

from bpy.types import Panel

from ._vendor import filelock, easybpy


@functools.cache
def get_extension_directory():
    extension_directory = bpy.utils.extension_path_user(__package__, path="", create=True)
    return extension_directory


class HelloWorldPanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text=f"filelock version {filelock.__version__}")

        active_object = easybpy.active_object()
        if active_object != None:
            row = layout.row()
            row.label(text=f"Active object: {active_object.name}")

        row = layout.row()
        row.label(text=f"Extension directory: {get_extension_directory()}")


def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
