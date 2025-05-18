import sys
input = sys.stdin.readline

N = int(input())
color = []

for _ in range(N):
  R, G, B = map(int, input().split())
  color.append([R, G, B])

for i in range(1, N):
  color[i][0] += min(color[i - 1][1], color[i - 1][2])
  color[i][1] += min(color[i - 1][0], color[i - 1][2])
  color[i][2] += min(color[i - 1][0], color[i - 1][1])

print(min(color[-1]))