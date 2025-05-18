import sys
input = sys.stdin.readline

K = int(input())
N = int(input())

def mono_digital(K, num):
  cal = [[] for _ in range(9)]
  chk = set()

  for i in range(1, 9):
    val = int(str(K) * i)
    if val == num:
      return i
    cal[i] = [val]
    chk.add(val)

  chk.add(0)

  for i in range(2, 9):
    for j in range(1, i):
      k = i - j
      for a in cal[j]:
        for b in cal[k]:
          opers = [a + b, abs(a - b), a * b, a // b, b // a]
          for oper in opers:
            if oper in chk:
              continue
            elif oper == num:
              return i
            cal[i].append(oper)
            chk.add(oper)
  
  return "NO"

for _ in range(N):
  num = int(input())
  print(mono_digital(K, num))