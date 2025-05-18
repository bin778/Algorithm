import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [list(map(int, input().strip())) for _ in range(N)]
min_num = min(N, M)

for k in range(min_num, -1, -1):
  for i in range(N - k):
    for j in range(M - k):
      if num[i][j] == num[i + k][j] == num[i][j + k] == num[i + k][j + k]:
        print((k + 1) * (k + 1))
        exit()