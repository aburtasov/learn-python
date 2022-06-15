import re

mytext = "Vasya 1983 , fsfewfwefew, Kolya,,ffdsfs" \
    "fsdfsdfsf, 2423523, Andrey, ggggg"


"""
\d = any digit 0-9
\D = any non digit
\w = any alphabet symbol (A-Z, a-z)
\W = any non alphabet symbol
\s = breakspace
\S = non breakspace

[0-9]{3} = \d\d\d
[A-Z][a-z]+
\w+\.\w+
"""
textlookfor_digits = r"\d\d\d"
textlookfor = r"Andrey"
textlookfor_symbols = r"\w{5}"

allresult = re.findall(textlookfor,mytext)
allresult2 = re.findall(textlookfor_digits,mytext)
allresult3 = re.findall(textlookfor_symbols,mytext)
print(allresult,allresult2,allresult3)