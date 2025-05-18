import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start, end, result = 1, house[0] + house[-1], 0

while start <= end:
  mid = (start + end) // 2
  
  cnt = 1
  prevHouse = house[0]
  for i in range(1, N):
    if house[i] - prevHouse >= mid:
      cnt += 1
      prevHouse = house[i]
  
  if cnt >= C:
    result = max(result, mid)
    start = mid + 1
  else:
    end = mid - 1

print(result)