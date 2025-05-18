import sys
input = sys.stdin.readline

N = int(input())
amount = list(map(int, input().split()))
M = int(input())

def Parametric(amount, start, end, M):
  while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for i in amount:
      if i > mid:
        total += mid
      else:
        total += i
        
    if total <= M:
      start = mid + 1
    else:
      end = mid - 1

  return end

start, end = 0, max(amount)
print(Parametric(amount, start, end, M))