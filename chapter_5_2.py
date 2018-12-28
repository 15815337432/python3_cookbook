#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

curDir = os.getcwd();

# 将print输入到一个文件中去

with open(os.path.join(curDir,'somefile.text'),'at',encoding=sys.getdefaultencoding()) as f:
    print('大帅哥', file=f)
