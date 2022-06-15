import re

filename = "c:/Users/admin/python/learn-py/regexpr/emails.txt"
resulfile = "c:/Users/admin/python/learn-py/regexpr/result.txt"
myfile = open(filename,mode='r',encoding='Latin-1')
resultfile = open(resulfile,mode='w',encoding='Latin-1')
mytext = myfile.read()

lookfor = r"\w-.+@\w+"

results = re.findall(lookfor,mytext)

for item in results:
    print(item)
    resultfile.write(item)