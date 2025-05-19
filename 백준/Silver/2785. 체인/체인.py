import sys
input = sys.stdin.readline

N = input()
L = list(map(int, input().split()))
result = 0

L.sort()
while len(L) > 1:
  chain = L.pop()
  L[-1] += chain
  result += 1

  L[0] -= 1
  if L[0] == 0:
    L.pop(0)
  
print(result)