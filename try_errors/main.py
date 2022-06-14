import sys

filename = "c:/Users/admin/python/learn-py/files/userrewrwes.txt"

while True:

   try:
     print("Inside Try")
     myfile = open(filename,mode='r',encoding='utf-8')
   
     print(myfile.read())
   except Exception:
    print("Inside Except")
    print("Error Found")
    print(sys.exc_info()[1])
    filename = input("Enter correct filename: ")
    # sys.exit()
   else:
      print("Inside Else")
      print(myfile.read())
      sys.exit()
   finally:
      print("Inside finally")


print("=====================")


 