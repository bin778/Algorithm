from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
letter = list(input().rstrip().split())
letter.sort()

for pw in combinations(letter, L):
  consonant = 0
  gather = 0

  for i in pw:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
      gather += 1
    else:
      consonant += 1
  
  if gather >= 1 and consonant >= 2:
    print(*list(pw), sep="")