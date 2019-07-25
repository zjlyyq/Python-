# 遍历字典

dic = {
    'name': '张嘉璐',
    'age': 23,
}

# 字典只有键值是可迭代的
for key in dic:
    print(key)

# 迭代字典的值
for value in dic.values():
    print(value)

# 迭代字典的键值对
for item in dic.items():
    print('key:{},value:{}\n'.format(item[0],item[1]))


# 循环和条件判断复用
x = [1,-1,3,2,0,8,5]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)
y2 = [value * 2 + 5 for value in x if value > 0]
print(y2)
