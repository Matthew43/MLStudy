# -*- coding: utf-8 -*-
# @File    : p_7zip.py
# @Author  : Matthew Liu
# @Time    : 2017/6/8 16:42

import os
import sys
import subprocess


def p_7zip(argv, zip=r'D:\Program Files\7-Zip\7z.exe'):
    root = argv
    for rt, dirs, files in os.walk(root):
        for file in files:
            if not(file.endswith('zip') or file.endswith('7z') or file.endswith('rar')):
                file_path = os.path.join(rt, file)
                ps = subprocess.Popen(
                    [zip, 'a', '-t7z', '-mx=5',
                     os.path.join(rt, os.path.splitext(file)[0] + '.7z'),
                     '-p123456', '-mhe', file_path, '-ms', '-mmt'], executable=zip)
                if ps.wait() == 0:
                    os.remove(file_path)

if __name__ == '__main__':
    p_7zip(sys.argv[1])
