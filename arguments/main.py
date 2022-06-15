import os
import sys

print("Hello")

print(sys.argv)

print(sys.argv[1:])

#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

#-----------------------------------
x = len(sys.argv)

if x > 1 :
    if sys.argv[1] == "?":
        print("Help requested!")
    print("Arguments: " + str(sys.argv[1:]))
else:
    print("No arguments!")

#----------------------------------

os.system("dir > test.txt")

# os.mkdir("mydir")
# sys.exit(1)