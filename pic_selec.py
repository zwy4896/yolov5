#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
File        :pic_selec.py
Description : 
Date        :2021/08/13 13:19:23
Author      :Wuyang Zhang
'''


from shutil import copyfile
import os
import shutil
home = os.environ['HOME']


def pic_select(path: str, ch: str, dst_path: str = None) -> None:
    """
    Desc:

    Args:

    Returns:

    """

    for root, dir, files in os.walk(path):
        if root.split('/')[-1] != 'CH2':
            continue
        for file in files:
            if '.bmp' in file:
                # if int(file.split('.')[0].split('_')[-1]) in ch:
                print(file)
                copyfile(os.path.join(root, file), os.path.join(
                    home, 'share/DATASET/train/CH2/imgs', root.split('/')[-2]+'-'+file))


if __name__ == '__main__':
    ch = [2, 6, 10, 14]
    pic_select(os.path.join(home, 'share/nas/dataset/H70/raw_data'), ch)
