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




