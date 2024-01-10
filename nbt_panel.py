

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
    bl_idname = "OBJECT_PT_spin" #Template: Replace with node_name (lower case with space underline)
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Spin' #Template - Replace with Node Name - this is N-panel side bar label

    

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        obj = context.object
        scene = bpy.context.scene
        screen = bpy.context.screen
        active_obj = context.view_layer.objects.active
    


        row = layout.row()
        try:
            active_obj.modifiers['Turntable_GeoNode']
            row.operator("object.undo_turntable", text="REMOVE WENBO",icon='VIEW_PAN') #template: Replace with undo_node_name
        except:
            row.operator("object.apply_turntable", text="APPLY WENBO",icon='FILE_REFRESH') #template: Replace with undo_node_name

# ______________________________________
        row = layout.row()
        try:
            active_obj.modifiers['Derrk_GeoNode']
            row.operator("object.undo_derrk", text="REMOVE DERRK",icon='VIEW_PAN') #template: Replace with undo_node_name
        except:
            row.operator("object.apply_derrk", text="APPLY DERRK",icon='FILE_REFRESH') #template: Replace with undo_node_name

# ______________________________________
        row = layout.row()

        try:
            active_obj.modifiers['Ducky_GeoNode']
            row.operator("object.undo_ducky", text="REMOVE DUCKY",icon='VIEW_PAN') #template: Replace with undo_node_name
        except:
            row.operator("object.apply_ducky", text="APPLY DUCKY",icon='FILE_REFRESH') #template: Replace with undo_node_name



        box = layout.box()
        box.scale_y = 4
        if not screen.is_animation_playing:
            box.operator("screen.animation_play",text="Play animation")
        else:
            box.operator("screen.animation_play",text="Stop animation")

        
        
        