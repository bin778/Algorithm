import sys
input = sys.stdin.readline

N = int(input())

serial = []
for i in range(N):
  str = input().strip()
  serial.append(str)

def sum_of_digits(s):
  return sum(int(char) for char in s if char.isdigit())

serial.sort(key=lambda x: (len(x), sum_of_digits(x), x))
print(*serial, sep="\n")