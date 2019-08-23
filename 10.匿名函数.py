# 匿名函数
nimin_func = lambda x,y: (x+y)

print(nimin_func(12,12))


# 感觉和闭包类似,但是闭包返回的函数是可以拥有自己的参数的
def bibao(x,y):
    def add(base):
        return x  + y - base
    return add

add_func = bibao(2,3)

print(add_func(2))


print_hello = lambda  :print('Hello world')
print_hello()

# 这句话也太pythonic了吧
print([(lambda x: x*x)(x) for x in range(10)])
# 输出
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

nums = [1,2,3,4,5,6,7,8,9]
squared = map(lambda x: x**2,nums)
print(squared)
