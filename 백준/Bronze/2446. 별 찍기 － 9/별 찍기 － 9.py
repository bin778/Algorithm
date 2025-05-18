import sys
input = sys.stdin.readline

n = int(input())

def A1(n, num, str):
  for j in range(num + 1):
    print(str, end="")

def A2(n, num, str):
  for j in range(n - num):
    print(str, end="")

for i in range(n):
  A1(n, i - 1, " ")
  A2(n - 1, i, "*")
  A2(n, i, "*")
  print()
for i in range(n - 1):
  A2(n - 2, i, " ")
  A1(n, i, "*")
  A1(n - 1, i + 1, "*")
  print()