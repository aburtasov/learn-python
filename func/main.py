#------------------------------------
def print_hello():
    """Print Hello and return Hello string"""
    print("Hello,World!")
    return "Hello!"
    
    
hello = print_hello()

print(hello)


print("=================")

def hello_func(name):
    print("Hello, " + name)
    
    
hello_func("Andrey")

print("=================")

def summa(x, y):
    print(x + y)

summa(10,20)

print("=================")

def summa2(x,y):
    s = x + y
    return s

sum = summa2(11,22)
print(sum)

print("=================")


def factorial(x):
    """Calculate Factorial of number X"""
    ans = 1
    for i in range(1,x + 1):
        ans = ans * i
    
    return ans


for x in range(1,10):
    print(str(x) + "!\t = " + str(factorial(x)))