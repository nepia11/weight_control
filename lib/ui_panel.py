# Copyright 2022 nepia11.
# SPDX-License-Identifier: GPL-3.0-only

import bpy
from logging import getLogger
from .ops_weight_control import NWC_OT_WeightControl, get_vertex_groups_from_selected


class NWC_PT_WeightControlPanel(bpy.types.Panel):
    """ """

    bl_label = "weight control panel"
    bl_idname = "NWC_PT_WeightControlPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        layout.label(text="weight control")
        layout.operator(NWC_OT_WeightControl.bl_idname)
        result = str(get_vertex_groups_from_selected(context.object))
        layout.label(text=result)


classes = [NWC_PT_WeightControlPanel]

# tools = []


def register():
    for c in classes:
        bpy.utils.register_class(c)
    # for t in tools:
    #     bpy.utils.register_tool(t)

    bpy.types.Scene.nwa_asset_id = bpy.props.StringProperty(default="asset_id")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    # for t in tools:
    #     bpy.utils.unregister_tool(t)
    del bpy.types.Scene.nwa_asset_id
