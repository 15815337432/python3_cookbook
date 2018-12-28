#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys


print(sys.getdefaultencoding())
# 获取当前问价
curDir = os.getcwd()
print('curDir：当前的路径：',curDir)

# 返回文件下的单纯路径
script_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
print(script_path)

# # Read the entire file as a single string
# with open(os.path.join(curDir,'somefile.text'),'rt',encoding= sys.getdefaultencoding()) as f:
#     data = f.read()
#     f.close()
# print(data)

# somefile.text
with open(os.path.join(script_path,'somefile.text'),'rt') as f:
    for line in f:
        # 遇到空行就结束
        print(line.strip('\n'))



# Write chunk of text data 编写文本数据块              wt模式文件内容存在则清楚掉并且覆盖掉
# with open(os.path.join(curDir,'somefile.text'),'wt') as f:
#     f.write("python是全世界最好的语言")

# with open(os.path.join(curDir,'somefile.text'),'wt') as f:
#     print(line,file=f)
#     print(line2,file=f)

# 使用with给被使用的的文件创造一个上下文环境，但是with控制块结束时，文件会自动关闭





