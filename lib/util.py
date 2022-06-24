# Copyright 2022 nepia11.
# SPDX-License-Identifier: GPL-3.0-only

import random
import string
from logging import getLogger
import bpy

logger = getLogger(__name__)


def random_name(n: int) -> str:
    """引数で指定した桁数のランダムなstrを返す"""
    if n < 0:
        raise ValueError
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def get_selected_index(mesh: bpy.types.Mesh):
    buffer = [False] * len(mesh.vertices)
    mesh.vertices.foreach_get("select", buffer)
    return [i for i, v in enumerate(buffer) if v is True]
