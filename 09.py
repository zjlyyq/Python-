# 闭包的概念以及用法:闭包就是返回函数的函数
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是 exponent_of 函数

square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方 
# square
# 输出
# <function __main__.nth_power.<locals>.exponent(base)>

# cube
# 输出
# <function __main__.nth_power.<locals>.exponent(base)>

print(square(2))  # 计算 2 的平方
print(cube(2)) # 计算 2 的立方
# 输出
# 4 # 2^2
# 8 # 2^3
