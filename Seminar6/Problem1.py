import re

input = "Buna ma cheama Ana si am 35 de ani. Maine implinesc 38"
r = re.compile("[0-9a-zA-Z]+")
result = r.findall(input)
print(result)