str = 'zhang jia lu'

# for char in str:
#     print(char)

# 改变字符串，需要扫描字符串时间复杂度是O(n)
str2 = str.replace('z','Z')   
print(str)
print(str2)


str = '0123456789'
l = []
for n in range(0,9):
    l.append(str[n])
print(l)

# 将每个元素按照指定的格式连接起来
sss = '***'
l = sss.join(l)

print(l)

# 字符串格式化
logging_string = 'hello,my name is {} and i am {} years old.'.format('zjl',14,'zyq')
print(logging_string)

