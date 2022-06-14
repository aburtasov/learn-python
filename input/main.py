#from email import message
#from itertools import count




name = input("Enter your name: ")

print("Hello, " + name)

#---------------------------------------

num1 = int(input("Enter x: "))
num2 = int(input("Enter y: "))

print("Sum: " + str(num1 + num2))
#---------------------------------------
message = ""
count = 3

while count:
    message = input("Enter Password:  ")
    if message == "secret":
        break
    print("Password Incorrect")
    count = count - 1
    
    
#--------------------------------------

my_list = []

msg = ""

while msg != 'stop'.upper():
    msg = input("Enter new item and STOP to finish: ")
    my_list.append(msg)

print(my_list)