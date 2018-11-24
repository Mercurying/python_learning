# python hello world
'''python 多行注释方式：3个单引号或者是双引号;
'''
'''python 是属于解释性的动态语言 变量声明可以不指定类型
   与java这种静态语言 不同声明变量必须指定变量类型
'''

# 解决python3打印显示中文问题;
# encode:utf-8 使用io和sys模块中文无法显示问题
# import io
# import sys
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# 1.hello world
import time
print('你好世界:', time.time())

from datetime import datetime
now = datetime.now()
print('now Time:', now)
print('now timestamp:',now.timestamp())
print(type(now))


# 2.条件语句
'''形式：
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''
age = 19
if age > 18:
    print('adult')
else:
    print('teenage')

# 3.数据结构 list
classMates = ['Mike', 'Bob', 'xiaoMing', 'daXiong']
# 使用-1索引取出最后元素
print(classMates[-1])
print(len(classMates))
# tuple[元组]类型一定声明就不可变
classRooms = ('classOne', 'classTwo', 'classThree')
# classRooms[0]='editClassOne'
print(classRooms[0])

# 4.循环语句
books = ['降龙十八掌', '六脉神剑', '易筋经', '凌波微步', '葵花宝典']
for book in books:
    print(book)

# 求1~100和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 5.dic 和 set 数据结构
# dic 查询和插入速度快 但是十分占据内存
# list 正好相反
# set类型只能存放不重复的key值，无法存放value值
