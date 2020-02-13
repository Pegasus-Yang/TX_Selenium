# Author:Pegasus-Yang
# Time:2020/1/5 20:27
import os


def get_abs_path(file_path):
    """通过相对路径获取对应的绝对路径"""
    return os.path.abspath(file_path)
