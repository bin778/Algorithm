import sys
input = sys.stdin.readline

N = int(input())
NGE = list(map(int, input().split()))
result = [-1] * N
stack = []

for i in range(N):
  while stack and NGE[stack[-1]] < NGE[i]:
    result[stack.pop()] = NGE[i]
  stack.append(i)

print(*result)