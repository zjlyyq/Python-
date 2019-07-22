import os

myList = [1,2,'hello','world']
myTup1 = (1,2,"name")
myTup2 = ("zjl",'yyq')

# 元组和列表都支持嵌套
myTup3 = (myTup1,("zjl",'yyq'))
print(myList)
print(myTup3)
print(type(myTup3[0]))

# list的内置函数
numList = [1,4,5,2,4,2,99]
print(numList)
sortedList = numList
print(sortedList.sort())
print(sortedList)



# 字典的初始化
d = {'b': 1, 'a': 2, 'c': 10}
print(d['b'])
d_sorted_by_key = sorted(d.items(),key=lambda x: x[0])      #根据字典键升序排序
print(d_sorted_by_key)
d_sorted_by_value = sorted(d.items(),key=lambda x: x[1])    #根据字典值升序排序
print(d_sorted_by_value)
print(d)