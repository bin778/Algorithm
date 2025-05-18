import sys, itertools
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus_one = 0
zero = 0
one = 0

def ninetree(paper):
  global minus_one, zero, one
  # 2차원에서 1차원으로 변환
  paper2 = list(itertools.chain(*paper))

  # 모든 배열이 -1일 때
  if paper2.count(-1) == len(paper2):
    minus_one += 1
    return
  # 모든 배열이 0일 때
  elif paper2.count(0) == len(paper2):
    zero += 1
    return
  # 모든 배열이 1일 때
  elif paper2.count(1) == len(paper2):
    one += 1
    return
  else:
    # 배열의 크기 계산
    length = len(paper)
    three_quarter = length // 3

    topLeft = []
    topMiddle = []
    topRight = []
    middleLeft = []
    middleMiddle = []
    middleRight = []
    bottomLeft = []
    bottomMiddle = []
    bottomRight = []

    # 배열을 9등분해서 새로운 배열에 추가하기
    for i in range(0, three_quarter):
      topLeft.append(paper[i][0:three_quarter])
      topMiddle.append(paper[i][three_quarter:three_quarter*2])
      topRight.append(paper[i][three_quarter*2:length])
    
    for i in range(three_quarter, three_quarter*2):
      middleLeft.append(paper[i][0:three_quarter])
      middleMiddle.append(paper[i][three_quarter:three_quarter*2])
      middleRight.append(paper[i][three_quarter*2:length])
    
    for i in range(three_quarter*2, length):
      bottomLeft.append(paper[i][0:three_quarter])
      bottomMiddle.append(paper[i][three_quarter:three_quarter*2])
      bottomRight.append(paper[i][three_quarter*2:length])
    
    # 재귀함수를 이용하여 배열의 요소가 -1, 0, 1만 있는 지 확인하기
    ninetree(topLeft)
    ninetree(topMiddle)
    ninetree(topRight)
    ninetree(middleLeft)
    ninetree(middleMiddle)
    ninetree(middleRight)
    ninetree(bottomLeft)
    ninetree(bottomMiddle)
    ninetree(bottomRight)

ninetree(paper)
print(minus_one)
print(zero)
print(one)