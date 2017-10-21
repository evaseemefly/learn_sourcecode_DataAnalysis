
# coding: utf-8

# # 数据分析中常用的Python技巧

# ## 1. Python常用容器类型
# 1-1 list
# 列表 使用[]
# list类型可以被修改
l = [1, 'a', 2, 'b']
print(type(l))
print('修改前：', l)
'''
<class 'list'>
修改前： [1, 'a', 2, 'b']
'''

# 修改list的内容
l[0] = 3
print('修改后：', l)
''''
修改后： [3, 'a', 2, 'b']
'''

# 末尾添加元素
l.append(4)
print('添加后：', l)
'''
添加后： [3, 'a', 2, 'b', 4]
'''

# 遍历list
print('遍历list(for循环)：')
for item in l:
    print(item)
'''
遍历list(for循环)：
3
a
2
b
4
'''
    
# 通过索引遍历list
print('遍历list(while循环)：')
i = 0
while i != len(l):
    print(l[i])
    i += 1
'''
遍历list(while循环)：
3
a
2
b
4
'''
    
# 列表合并
print('列表合并(+)：', [1, 2] + [3, 4])
'''
列表合并(+)： [1, 2, 3, 4]
'''

# 列表重复
print('列表重复(*)：', [1] * 5)
'''
列表重复(*)： [1, 1, 1, 1, 1]
'''

# 判断元素是否在列表中
print('判断元素存在(in)：', 1 in [1, 2])


# 1-2 tuple
# 元祖 使用()

t = (1, 'a', 2, 'b')
print(type(t))

#元组的内容不能修改，否则会报错
# t[0] = 3 

# 遍历tuple
print('遍历list(for循环)：')
for item in t:
    print(item)
    
# 通过索引遍历tuple
# 与list的遍历方式较为近似
print('遍历tuple(while循环)：')
i = 0
while i != len(t):
    print(t[i])
    i += 1
    
# 解包 unpack
'''
t 本身是(1, 'a', 2, 'b')
解包即相当于 c 就是 取出 第三个位置的对象 也就是 2
解包接收的变量个数需要与元组的长度相同，否则会出错
'''
a, b, c, d = t
print('unpack: ', c)

# 确保unpack接收的变量个数和tuple的长度相同，否则报错
# 经常出现在函数返回值的赋值时
# a, b, c = t


# 1-3 dictionary
'''
使用大括号{}
'''

d = {'小象学院': 'http://www.chinahadoop.cn/',
    '百度': 'https://www.baidu.com/',
    '阿里巴巴': 'https://www.alibaba.com/',
    '腾讯': 'https://www.tencent.com/'}

print('通过key获取value: ', d['小象学院'])

# 遍历key
print('遍历key: ')
for key in d.keys():
    print(key)
    
# 遍历value
print('遍历value: ')
for value in d.values():
    print(value)
    
# 遍历item
print('遍历item: ')
for key, value in d.items():
    print(key + ': ' + value)

# format输出格式
print('format输出格式：')
for key, value in d.items():
    print('{}的网址是{}'.format(key, value))


# 1-3 set

print('创建set:')
my_set = {1, 2, 3}
print(my_set)
my_set = set([1, 2, 3, 2])
print(my_set)

print('添加单个元素:')
my_set.add(3)
print('添加3', my_set)

my_set.add(4)
print('添加4', my_set)

print('添加多个元素：')
my_set.update([4, 5, 6])
print(my_set)


# ## 2. Python字符串操作
# 索引获取数据
s = '数据分析'

print('索引操作：')
print('s[0]: ', s[0])
print('s[0:2]: ', s[0:2])
print('s[-1]: ', s[-1])
print('s[-2:]: ', s[-2:])

print('split分割字符串：')
s2 = 'Python is a widely used high-level programming language for general-purpose programming.'
print(s2.split(' '))


# ## 3. Python日期时间处理

import datetime as dt
import time as tm

#  从1970年1月1日算起
# 从一个指定的起点开始到现在共相差多少秒
print('当前时间：', tm.time())

dt_now = dt.datetime.fromtimestamp(tm.time())
print(dt_now)
print('{}年{}月{}日'.format(dt_now.year, dt_now.month, dt_now.day))

# 日期计算
delta = dt.timedelta(days=100)
print('今天的前100天：', dt.date.today() - delta)
print(dt.date.today() > dt.date.today() - delta)


# ## 4. Python面向对象编程


class Person:
    def __init__(self, name, company='自由职业'):
        self.name = name
        self.company = company
    
    def set_name(self, name):
        self.name = name
        
    def set_company(self, company):
        self.company= company
        
p = Person('小王')
print('{}的职业是{}'.format(p.name, p.company))

p.set_company('数据分析师')
p.set_name('王工')
print('{}的职业是{}'.format(p.name, p.company))


# ## 5. Python map()函数

import math

print('示例1，获取两个列表对应位置上的最小值：')
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
mins = map(min, l1, l2)
print(mins)

# map()函数操作时，直到访问数据时才会执行
# 相当于ef中查询时的延迟加载
for item in mins:
    print(item)

print('示例2，对列表中的元素进行平方根操作：')
# 对L2中的每一个变量进行开平方的操作
squared = map(math.sqrt, l2)
print(squared)
print(list(squared))


# ## 6. 匿名函数 lambda

my_func = lambda a, b, c: a * b
print(my_func)
print(my_func(1, 2, 3))

# 结合map
print('lambda结合map')
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
result = map(lambda x, y: x * 2 + y, l1, l2)
print(list(result))


# ## 7. 列表推导式

print('找出1000内的偶数(for循环)：')
l1 = []
for i in range(1000):
    if i % 2 == 0:
        l1.append(i)
print(l1)

print('找出1000内的偶数(列表推导式)：')
# 注意列表推导式需要加方括号
# exp for x in list if contdition
l2 = [i for i in range(1000) if i % 2 == 0]
print(l2)


# ## 8. Python操作CSV数据文件
import csv
import os
# 此处有问题！！！
with open('grades.csv') as csvfile:
    # 通过csv.DictReader的方式读取打开后的文件
    grades_data = list(csv.DictReader(csvfile))
    
print('记录个数：', len(grades_data))
print('前2条记录：', grades_data[:2])
print('列名：', list(grades_data[0].keys()))

'''
取出所有的assignment1_grade的行数据，转成float类型并求和，最后除总行数
'''
avg_assign1 = sum(float(row['assignment1_grade']) for row in grades_data) / len(grades_data) 
print('assignment1平均分数：', avg_assign1)

# set是集合，不能重复，且是无序的，使用下面这种方式由于通过列表推导式取出的数据中有重复数据，所以使用set()的方式转换后会自动去重
assign1_sub_month = set(row['assignment1_submission'][:7] for row in grades_data)
print(assign1_sub_month)

