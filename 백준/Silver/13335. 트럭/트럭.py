from functools import reduce
import sys
input = sys.stdin.readline

N, W, L = map(int, input().split())
truck = list(map(int, input().split()))

result = 0
bridge = [0] * W

while (len(bridge)):
  bridge.pop(0)
  if (len(truck)):
    sumBridge = reduce(lambda a, b: a + b, bridge, 0)
    if (sumBridge + truck[0] <= L):
      bridge.append(truck.pop(0))
    else:
      bridge.append(0)
  result += 1

print(result)