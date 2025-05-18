import sys
input = sys.stdin.readline

stick = input()
stack = []
count = 0
result = 0

for i in stick:
  if (i == "("):
    count += 1
    if ("(" not in stack):
      stack.append("(")
  elif (i == ")"):
    count -= 1
    if ("(" in stack):
      stack.pop()
      result += count
    elif (")" not in stack):
      result += 1
  
print(result)