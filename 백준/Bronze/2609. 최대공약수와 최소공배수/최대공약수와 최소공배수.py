import sys
input = sys.stdin.readline

gcd = 0
n, m = map(int, input().split())

for i in range(1, m + 1):
  if (n % i == 0 and m % i == 0): gcd = i

print(gcd, int(n * m / gcd))