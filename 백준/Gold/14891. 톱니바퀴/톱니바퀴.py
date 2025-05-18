from collections import deque
import sys
input = sys.stdin.readline

# 톱니바퀴 상태 입력하기(N극은 0, S극은 1)
cogwheels = [deque(map(int, input().strip())) for _ in range(4)]

# 회전 횟수
K = int(input())

operator = [list(map(int, input().split())) for _ in range(K)]

# 명령어에 따라 톱니바퀴를 회전시킴
for op in operator:
  # num: 회전시킬 톱니바퀴 번호, dir: 회전시킬 방향(1은 시계방향, -1은 반시계방향)
  num = op[0]
  dir = op[1]

  if num == 1:
    if cogwheels[0][2] != cogwheels[1][6]:
      if cogwheels[1][2] != cogwheels[2][6]:
        if cogwheels[2][2] != cogwheels[3][6]:
          cogwheels[3].rotate(-dir)
        cogwheels[2].rotate(dir)
      cogwheels[1].rotate(-dir)
    cogwheels[0].rotate(dir)
  elif num == 2:
    if cogwheels[0][2] != cogwheels[1][6] and cogwheels[1][2] != cogwheels[2][6]:
      if cogwheels[2][2] != cogwheels[3][6]:
        cogwheels[3].rotate(dir)
      cogwheels[0].rotate(-dir)
      cogwheels[2].rotate(-dir)
    elif cogwheels[1][2] != cogwheels[2][6]:
      if cogwheels[2][2] != cogwheels[3][6]:
        cogwheels[3].rotate(dir)
      cogwheels[2].rotate(-dir)
    elif cogwheels[0][2] != cogwheels[1][6]:
      cogwheels[0].rotate(-dir)
    cogwheels[1].rotate(dir)
  elif num == 3:
    if cogwheels[1][2] != cogwheels[2][6] and cogwheels[2][2] != cogwheels[3][6]:
      if cogwheels[0][2] != cogwheels[1][6]:
        cogwheels[0].rotate(dir)
      cogwheels[1].rotate(-dir)
      cogwheels[3].rotate(-dir)
    elif cogwheels[1][2] != cogwheels[2][6]:
      if cogwheels[0][2] != cogwheels[1][6]:
        cogwheels[0].rotate(dir)
      cogwheels[1].rotate(-dir)
    elif cogwheels[2][2] != cogwheels[3][6]:
      cogwheels[3].rotate(-dir)
    cogwheels[2].rotate(dir)
  elif num == 4:
    if cogwheels[2][2] != cogwheels[3][6]:
      if cogwheels[1][2] != cogwheels[2][6]:
        if cogwheels[0][2] != cogwheels[1][6]:
          cogwheels[0].rotate(-dir)
        cogwheels[1].rotate(dir)
      cogwheels[2].rotate(-dir)
    cogwheels[3].rotate(dir)

# 결과 점수
result = 0
for i in range(4):
  if cogwheels[i][0] == 1:
    result += (2 ** i)

print(result)