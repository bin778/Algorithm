import sys
input = sys.stdin.readline

N = int(input())
crd = [list(map(int, input().split())) for _ in range(N)]

a = 0
b = 0

for i in range(N - 1):
  a += (crd[i][0] * crd[i + 1][1])
  b += (crd[i][1] * crd[i + 1][0])

a += (crd[-1][0] * crd[0][1])
b += (crd[-1][1] * crd[0][0])

sum = abs(a - b)
result = sum / 2
print(result)