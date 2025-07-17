import sys
input = sys.stdin.readline

h, w = map(int, input().split())
s = list(map(int, input().split()))
result = 0

for i in range(1, w - 1):
    left = max(s[:i])
    right = max(s[i + 1:])
    if s[i] < left and s[i] < right:
        result += min(left, right) - s[i]

print(result)