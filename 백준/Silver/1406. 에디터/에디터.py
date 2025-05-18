import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
N = int(input())

for _ in range(N):
  com = list(input().split())

  if com[0] == 'P':
    left.append(com[1])
  elif com[0] == 'B' and left:
    left.pop()
  elif com[0] == 'L' and left:
    right.append(left.pop())
  elif com[0] == 'D' and right:
    left.append(right.pop())

right.reverse()
print(*left, *right, sep='')