import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

num.sort()
min = float('inf')
res1, res2, res3 = 0, 0, 0

for i in range(len(num) - 2):
  start, end = i + 1, len(num) - 1

  while start < end:
    sum = num[i] + num[start] + num[end]

    if abs(sum) < min:
      min = abs(sum)
      res1 = num[i]
      res2 = num[start]
      res3 = num[end]
    
    if sum > 0:
      end -= 1
    else:
      start += 1

print(res1, res2, res3)
