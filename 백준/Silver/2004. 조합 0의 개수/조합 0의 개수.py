import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def countFact(N, factor):
  count = 0
  while N >= factor:
    count += N // factor
    N //= factor
  return count
  
def countnCm(N, M):
  count_2 = countFact(N, 2) - countFact(M, 2) - countFact(N - M, 2)
  count_5 = countFact(N, 5) - countFact(M, 5) - countFact(N - M, 5)
  return min(count_2, count_5)

print(countnCm(N, M))