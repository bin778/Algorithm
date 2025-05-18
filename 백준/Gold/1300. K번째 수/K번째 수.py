import sys
input = sys.stdin.readline

N = int(input())
k = int(input())
left, right = 1, k
result = 0

def getCnt(mid, N):
  cnt = 0
  for x in range(1, N + 1):
    cnt += min(N, mid // x)
  return cnt

while left <= right:
  mid = (left + right) // 2
  cnt = getCnt(mid, N)

  if cnt < k:
    left = mid + 1
  else:
    result = mid
    right = mid - 1

print(result)   