#learning split
problems = 'broke, pale, short, nerdy'
print(problems)
print()

l=problems.split(", ")
print(l)

print()
#l2 =problems.split("short")
#print(l2)

print()

#learning join
joined = ' and '.join(l)

print(joined)
print()

csv = ','.join(l)
print(csv)