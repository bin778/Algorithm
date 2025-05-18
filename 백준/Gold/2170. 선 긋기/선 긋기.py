import sys
input = sys.stdin.readline

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort()

L, R = line[0][0], line[0][1]
result = 0

for i in range(1, N):
  if line[i][0] > R:
    result += (R - L)
    L, R = line[i][0], line[i][1]
  else:
    R = max(R, line[i][1])

print(result + (R - L))