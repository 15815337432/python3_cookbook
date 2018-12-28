#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

Curdir = os.getcwd()
Tagfile = os.path.join(Curdir,'Tagfile.text')

if not os.path.exists(Tagfile):
    with open('Tagfile.text','wt',encoding=sys.getdefaultencoding()) as f:
        print("这是新创建的文件",file=f)
        f.write('下面的是测试')
else:
    print('File already exists')
