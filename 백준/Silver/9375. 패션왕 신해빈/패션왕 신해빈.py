import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
  n = int(input())
  clothes = []
  clothes_dict = {}
  result = 1

  for i in range(n):
    a, b = input().split()
    clothes.append([a, b])

  for type in clothes:
    if type[1] in list(clothes_dict.keys()):
      clothes_dict[type[1]] += 1
    else:
      clothes_dict[type[1]] = 1

  for type in clothes_dict:
    result *= (clothes_dict.get(type) + 1)
    
  print(result - 1)