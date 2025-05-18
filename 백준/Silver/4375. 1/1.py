import sys
input = sys.stdin.readline

while True:
  try:
    N = int(input())
    result = 1
    while True:
      if (result % N == 0):
        break
      result = result * 10 + 1
    print(len(str(result)))
  except:
    break