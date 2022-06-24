# Copyright 2022 nepia11.
# SPDX-License-Identifier: GPL-3.0-only
import bpy
import bmesh
from logging import getLogger

logger = getLogger(__name__)


def get_selected_index(bm: bmesh.types.BMesh):
    selected = [v.index for v in bm.verts if v.select is True]
    return selected


# 選択頂点に含まれる頂点グループを列挙する
def get_vertex_groups_from_selected(obj: bpy.types.Object):
    if isinstance(obj.data, bpy.types.Mesh):
        mesh = obj.data
        # オブジェクトに含まれる頂点グループを取得
        vertex_groups = obj.vertex_groups
        # 選択頂点を取得
        bm = bmesh.from_edit_mesh(obj.data)
        selected_indices = get_selected_index(bm)
        # 選択頂点に含まれる頂点グループインデックスを取得
        # リアルタイムの選択頂点はbmeshからじゃないとうまく行かないっぽいけどvertex groupとかのデータ自体へのアクセスはbpy.dataからのほうがやりやすい

        group_indices: list[int] = []
        verts = bm.verts
        bm.verts.layers.deform.verify()
        for i in selected_indices:
            pass
        group_set = set(group_indices)
        names = [vertex_groups[i].name for i in group_set]
        return names
    else:
        return None


class NWC_OT_WeightControl(bpy.types.Operator):
    """a"""

    bl_idname = "mesh.weight_control"
    bl_label = ""
    bl_description = "operator description"
    bl_options = {"REGISTER", "UNDO"}

    # メニューを実行したときに呼ばれるメソッド
    def execute(self, context):
        # logging
        logger.debug("exec my ops")
        result = get_vertex_groups_from_selected(context.object)
        # infoにメッセージを通知
        self.report({"INFO"}, f"{result}")
        # 正常終了ステータスを返す
        return {"FINISHED"}


classes = [NWC_OT_WeightControl]
tools = []


def register():
    for c in classes:
        bpy.utils.register_class(c)
    for t in tools:
        bpy.utils.register_tool(t)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    for t in tools:
        bpy.utils.unregister_tool(t)
