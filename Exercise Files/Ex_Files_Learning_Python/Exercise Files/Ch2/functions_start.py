#
# Example file for working with functions
#

# define a basic function
def fun1():
    print("I am a Function")

# function that takes arguments
def fun2(arg1, arg2):
    print(arg1,"",arg2)

# function that returns a value
def cube(x):
    return x*x*x 

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result =  result + x
    return result
# fun1()
# print(fun1())
# print(fun1)

# fun2(10,20)
# print(fun2(10,20))
# print(cube(3))

print(power(2))
print(power(2,3))
print(power(x = 3, num=2))

print(multi_add(4,5,10,4))