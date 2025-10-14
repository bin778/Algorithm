import sys
input = sys.stdin.readline

def largestArea(heights):
  stack = []
  result = 0

  for i, h in enumerate(heights + [0]):
    while stack and heights[stack[-1]] >= h:
      height = heights[stack.pop()]
      width = i if not stack else i - stack[-1] - 1
      result = max(result, height * width)
    stack.append(i)

  return result

while True:
  line = input().split()
  N = int(line[0]) 
  if (N == 0): break
  heights = [int(x) for x in line[1:]] 
  print(largestArea(heights))