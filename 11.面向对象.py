class People:

    # __init__是构造函数，其中self变量代指本身
    def  __init__(self,name,age):
        self.name = name
        # 年龄可是隐私哦，要设置成私有属性，只有我自己才能获取
        self.__age = age
    
    def introduce_self(self):
        print("Hello,I'm  {},and my age is {}!".format(self.name,self.__age))
    

me = People('zjl',12)
me.introduce_self()
print(me.name)
print(me.__age)


'''
Hello,I'm  zjl,and my age is 12!
zjl
Traceback (most recent call last):
  File "/home/zjl/mycode/python_jike/11.面向对象.py", line 16, in <module>
    print(me.__age)
AttributeError: 'People' object has no attribute '__age'
'''
