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



    

    

