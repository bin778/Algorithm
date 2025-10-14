import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]
stack = []
result = 0

for i, h in enumerate(heights + [0]):
  while stack and heights[stack[-1]] >= h:
    height = heights[stack.pop()]
    width = i if not stack else i - stack[-1] - 1
    result = max(result, height * width)
  stack.append(i)

print(result)