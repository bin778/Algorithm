import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
result = float('inf')

start = 0
end = 0
numSum = 0

while start < N:
  if numSum < S and end < N:
    numSum += num[end]
    end += 1
  else:
    if numSum >= S:
      result = min(result, end - start)
    numSum -= num[start]
    start += 1

if result == float('inf'): print(0)
else: print(result)