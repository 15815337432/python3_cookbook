#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 使用其他分隔符或行终止符打印

# 想使用print()函数输出数据，但是像改变丰富符，或者行尾符
print('MVP',50,91.5)

print('MVP',50,91.5,sep=',')

print('MVP',50,91.5,sep=',',end='!!\n')

# 使用end参数也可以在输出中禁止换行
for i in range(5):
    print(i)


for i in range(5):
    print(i,end=' ')

# 当你想使用非空格分隔符输出数据的时候，给print()函数传递一个sep参数是最简单的方式。有时候可以采用 str.join()来完成同样的方式
print(','.join(('MVP','50','91.5')))

row = ('MVP','50','91.5')
print(*row,sep=',')