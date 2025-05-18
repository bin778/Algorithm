import sys
input = sys.stdin.readline

quiz = [[i + 1, int(input())] for i in range(8)]
quiz.sort(key=lambda x: x[1])

sum = 0
idx = set()

for i in range(3, len(quiz)):
  sum += quiz[i][1]
  idx.add(quiz[i][0])

print(sum)
print(*idx)