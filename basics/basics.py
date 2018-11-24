# python基础语法基础
# 1.调用内部函数
a = abs(-100)
print(a)
maxValue = max(100, -100, 20, 50000000,
               1000000000000000000, 233333333333333333333)
print(maxValue)
strToInt = int('123')
print(strToInt)
intToStr = str(100)
print(intToStr)
strToBool = bool('1')
print(strToBool)


# 2.自定义函数
def my_abs(x):
    if(x > 0):
        return x
    else:
        return -x


print('use my_abs:', my_abs(-100))


def power(x):
    return x * x


print(power(-2))


# 3.递归函数
def recursiveFun(n):
    if n == 1:
        return 1
    return n * recursiveFun(n - 1)


result = recursiveFun(10)
print('recursiveFun:', result)

# 4.高级特性 判断是否可进行迭代
from collections import Iterable
print('Iterable:', isinstance('abc', Iterable))

# 列表生成式
exceptResult = list(range(1, 101))
# exceptResult: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('exceptResult:', exceptResult)

# 生成器generator 可以通过next()进行取出每个元素或者使用for循环遍历对象取出
g = (x * x for x in range(10))
for n in g:
    print('generator element:', n)

# 总结集合数据类型：list tuple dic set str等
# 使用isinstance()判断数据类型

'''凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
'''


# 常见的高级函数
# map
def f(n):
    return n * n

r = map(f, [1, 2, 3, 4])
print('map result:', list(r))


# reduce
from functools import reduce


def add(x, y):
    return x + y


reduceResult = reduce(add, [1, 2, 3, 4, 5, 6])
print('reduceResult:', reduceResult)


# filter
def is_odd(n):
    return n % 2 == 1

filterResult = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('filterResult', list(filterResult))


# sorted  python内置排序函数可对数字字符串进行排序
