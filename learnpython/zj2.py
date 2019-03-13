#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#声明使用的是utf-8编码，避免文档中的中文在被解释器解释时出现乱码

print("learning makes me happy!")
print("i don't konw what's the reason.")
print("learnjava merged to master.")

name = input('please enter your name: ')
print('hello,', name)


n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print('''n...f...s1...s2...s3...s4''')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print("Miciael's value = ",d['Michael'])

if 'Thomas' in d :
    print('exist')
else:
    print('not exist')



from my_abspack import my_abs
print(my_abs(-456))


import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100,100,60,math.pi/6)
print(x, y)

r = move(100,100,60,math.pi/6)
print(r) #返回一个tuple

def quadratic(a,b,c):
    r1=((0-b)+math.sqrt(b*b-4*a*c))/(2*a)
    r2=((0-b)-math.sqrt(b*b-4*a*c))/(2*a)
    return r1, r2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#测试代码
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([3,5,'x','y']))
print(add_end)
print(add_end)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#往可变参数里面传入元素（可变参数允许传入0，任意多个参数）
print(calc(3,4,5))
#已经有一个名为nums的tuple，nums如何使用可变参数的函数
nums = [1, 2, 3]
print(calc(*nums))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))

# 预期结果：name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}





