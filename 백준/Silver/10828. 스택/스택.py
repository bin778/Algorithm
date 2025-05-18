import sys
input = sys.stdin.readline
my_deque = []
test_case = int(input())

for i in range(test_case):
  command = input().split()
  if command[0] == 'push':
    my_deque.append(int(command[1]))
  elif command[0] == 'pop':
    if len(my_deque):
      print(my_deque.pop())
    else: print(-1)
  elif command[0] == 'size':
    print(len(my_deque))
  elif command[0] == 'empty':
    if len(my_deque):
      print(0)
    else: print(1)
  elif command[0] == 'top':
    if len(my_deque):
      print(my_deque[-1])
    else: print(-1)