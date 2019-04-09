#coding = 'utf-8'
# 列表推导式
# a = [x for x in range(1, 101)]

# b = []

# c = []

# 将一个数组[1,2,3,4,5....10] 变为 [[1,2,3], [4,5,6], [7,8,9], ...]
# 1 只能处理这种连续数字
for val in a:
    if val% 3 == 0:
        b.append(val) 
        c.append(b)
        b = []
    else:
        b.append(val) 

print(c)

# 2 快捷 使用广泛
a = range(1, 101)
a = list(a)
b  = [a[x:x+3] for x in range(0, len(a), 3)]
print(b)

# 去重
a = [1,1,2,2,3,4]

b = set(a)

a = list(b)

print(a)


'''
 两个参数交换值
'''
# a = a + b
# b = a - b
# a = a - b


# 随机10个不重复的数
import random
def doing(n):
    a = []
    i = 0
    while i < n:
        num = random.randint(1, n)
        if num not in a:
            a.append(num)
            i += 1
    return a
result = doing(10)
print(result)


# 获取 当前目录下的'.pyc'
import os
pathList = []
for temp in os.walk('.'):
    a = temp[2]
    for pathX in a:
        zIndex  = pathX.rfind('.')
        suffix = pathX[zIndex:]
        if suffix == '.pyc':
            pathList.append(pathX)
print(pathList)