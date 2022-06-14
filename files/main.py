input_file = "c:/Users/admin/python/learn-py/files/users.txt"

my_file = open(input_file,mode='r',encoding='utf-8')

#print(my_file.read())

#for line in my_file:
    #print("Hello " + line.strip())

#for num,line in enumerate(my_file, 1):
    #print("Line: " + str(num) + " - " +  "User: " + line.strip())

for num,line in enumerate(my_file, 1):
    if "Benzema" in line:
        print("Line: " + str(num) + " - " +  "User: " + line.strip())


#----------------------------------------------------------------------
password_to_look = "rrr"

input_file_pass = "c:/Users/admin/python/learn-py/files/passwords.txt"
output_file_pass = "c:/Users/admin/python/learn-py/files/my_passwords.txt"

my_file = open(input_file_pass,mode='r',encoding='utf-8')

my_file_1 = open(output_file_pass,mode='w',encoding='utf-8')  # перезапись файла. Для добавления - mode='a'

for num,line in enumerate(my_file, 1):
    if password_to_look in line:
        print("Line: " + str(num) + " - " +  "User: " + line.strip())
        my_file_1.write("Find password: " + line)


my_file.close()
my_file_1.close()

