

#Instructions: Replace variables indicated by "Template" with modifier specific variable names

#Template replacements:
#   Need Four Variables - 
#       function label          (bl_label)
#       functionName            (camelcase describing what modifier does)
#       function category?       (bl_category - currently set to 'Object' like in init - should it be function name for side panel?)
#       functionname            (lowercase function name for operator)






import bpy

class nbt_PT_Panel(bpy.types.Panel):

    """Creates a Panel in the N-Panel of the 3D viewport"""
    bl_label = "Spin!" #Template: Replace with string that describes what node will do - gets written above button
    bl_idname = "OBJECT_PT_ducky" #Template: Replace with node_name (lower case with space underline)
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Spin' #Template - Replace with Node Name - this is N-panel side bar label

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        obj = context.object
        box = layout.box()
        box.scale_y = 4
        active_obj = context.view_layer.objects.active

        try:
            active_obj.modifiers['GeoNode']
            box.operator("object.undo_ducky", text="UNDO") #template: Replace with undo_node_name
        except:
            box.operator("object.apply_ducky", text="APPLY") #template: Replace with undo_node_name