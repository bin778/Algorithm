import sys, itertools
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
result_max = 0

numPr = itertools.permutations(num, N)

for arr in numPr:
  result = 0
  for i in range(0, len(arr) - 1):
    result += abs(arr[i] - arr[i + 1])
  result_max = max(result_max, result)

print(result_max)