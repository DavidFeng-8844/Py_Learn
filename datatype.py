#In python 3, there are 3 types of number data type: int, float, complex
#Reverse a string
def reverse(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]
    opt = ' '.join(inputwords)
    return opt

# Path: type.py
#The difference betweeen type() and isinstance() is that type() does not consider the inheritance, while isinstance() does.
class Parent:
    pass
class Child(Parent):
    pass

child_obj = Child()

print(type(child_obj))  # 输出：<class '__main__.Child'>
print(isinstance(child_obj, Child))  # 输出：True
print(issubclass(Child, Parent))  # 输出：True
var1 = 18
var2 = 44
print(var1.__add__(var2))  # 输出：62

#List
list = ['M','a','r','y']
str = 'I Like Mary'
input = str
print(list[0:3:2])
print(list[-1:0:-2])
rvr =reverse(input)
print(rvr)

#In python Tuple is a immutable sequence of python objects
#String can be seen as a special tuple

#Set
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素

# 使用大括号 {} 来创建空字典
emptyDict = {}
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

myDict = dict({1:"Mary",2:"Like",3:"I"})
# 打印字典
print(myDict)
# 查看字典的数量
print("Length:",len(myDict))
# 查看类型
print(type(myDict))

    
#列表推导式：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
'''name.upper()列表生成元素表达式，可以是有返回值的函数
for name in names迭代names将name传入name.upper 表达式中
'''
print(new_names)

#字典推导式：
#d = {key:value for (key,value) in iterable}
#集合推导式：
s = {x for x in 'abracadabra' if x not in 'abc'}
#生成器推导式：
g = (x**2 for x in range(10))
#元组推导式：
t = tuple(x**2 for x in range(10))

#函数
def printme(str):
    print(str)
    return
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


#For loop
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")