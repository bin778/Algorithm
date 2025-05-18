import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

if N <= 2:
  print(len(num))
else:
  start, result = 0, 2
  freq = defaultdict(int)

  for end in range(N):
    freq[num[end]] += 1
  
    while len(freq) >= 3:
      freq[num[start]] -= 1
      if freq[num[start]] == 0:
        del freq[num[start]]
      start += 1
    result = max(result, end - start + 1)
  print(result)