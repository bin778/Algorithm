import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
  x = int(input())
  # x가 0이면
  if x == 0:
    # 배열이 비어있으면 0을 출력한다
    if len(heap) == 0:
      print(0)
    # Heap 배열의 원소가 있으면 가장 작은 값을 제거한다.
    else:
      print(heapq.heappop(heap))
  # x가 자연수라면 Heap 배열에 x를 넣는다
  else: heapq.heappush(heap, x)