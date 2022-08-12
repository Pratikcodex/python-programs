import re

text = "a Random string  pratikrajcpr@website.com  YOURNAME@company.net"

pattern = re.compile("[a-zA-Z0-9,]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

#result = pattern.search(text)#only search for first function

result = pattern.findall(text)
print(result)



