import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

num.sort()
start, end = 0, N - 1
res1, res2 = float('-inf'), float('inf')
min = float('inf')

while start < end:
  sum = num[start] + num[end]

  if abs(sum) < min:
    min = abs(sum)
    res1 = num[start]
    res2 = num[end]
  
  if sum > 0:
    end -= 1
  else:
    start += 1

print(res1, res2)