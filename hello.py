# python hello world
'''python 多行注释方式：3个单引号或者是双引号;
'''
# 解决python3打印显示中文问题;

# encode:utf-8 使用io和sys模块中文无法显示问题
# import io
# import sys
import time
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
print('你好世界:',time.time())
