import re

text = "a Random string."

pattern = re.compile("a Random string")

result = pattern.search(text)

print(result)

wolla = "A bug in the House"

pattern = re.compile("[ABC]")

result2 = pattern.search(wolla)

print(result2)



text2 = "Random546 string."

pattern = re.compile("[a-zA-Z0-9]+")

result3 = pattern.search(text2)

print(result3)


