# Copyright 2022 nepia11.
# SPDX-License-Identifier: GPL-3.0-only

import importlib
from logging import getLogger, StreamHandler, Formatter, handlers, DEBUG
import sys
import bpy
import os
import datetime


# アドオン情報
bl_info = {
    "name": "weight_control",
    "author": "nepia",
    "version": (0, 1, 0),
    "blender": (3, 1, 0),
    "location": "VIEW3D/UI/Item",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh",
}

# インポートするモジュール
module_names = ["ops_weight_control", "ui_panel"]


def setup_logger(log_folder: str, modname=__name__):
    """loggerの設定をする"""
    logger = getLogger(modname)
    logger.setLevel(DEBUG)
    # log重複回避　https://nigimitama.hatenablog.jp/entry/2021/01/27/084458
    if not logger.hasHandlers():
        sh = StreamHandler()
        sh.setLevel(DEBUG)
        formatter = Formatter("NWA: %(name)s - %(levelname)s - %(message)s")
        sh.setFormatter(formatter)
        logger.addHandler(sh)
        fh = handlers.RotatingFileHandler(log_folder, maxBytes=500000, backupCount=2)
        fh.setLevel(DEBUG)
        fh_formatter = Formatter(
            "%(asctime)s - %(filename)s - %(name)s"
            " - %(lineno)d - %(levelname)s - %(message)s"
        )
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)
    return logger


# log周りの設定
scripts_dir = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(scripts_dir, "log", f"{datetime.date.today()}.log")
logger = setup_logger(log_folder, modname=__name__)
logger.debug("hello")


# サブモジュールのインポート
namespace = {}
for name in module_names:
    fullname = "{}.{}.{}".format(__package__, "lib", name)
    # if "bpy" in locals():
    if fullname in sys.modules:
        namespace[name] = importlib.reload(sys.modules[fullname])
    else:
        namespace[name] = importlib.import_module(fullname)
logger.debug(namespace)


def register():
    for module in namespace.values():
        module.register()


def unregister():
    for module in namespace.values():
        module.unregister()


if __name__ == "__main__":
    register()
