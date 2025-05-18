import sys
input = sys.stdin.readline

N = int(input())
MOD = 1_000_000

def multiply(X, Y):
  return [[(X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % MOD, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % MOD], [(X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % MOD, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % MOD]]

def power(X, N):
  if N == 1:
    return X
  elif N % 2 == 0:
    return power(multiply(X, X), N // 2)
  else:
    return multiply(X, power(multiply(X, X), (N - 1) // 2))

def fibonacci(N):
  if N == 0:
    return 0
  elif N == 1:
    return 1
  
  F = [[1, 1], [1, 0]]
  result = power(F, N - 1)
  return result[0][0]

print(fibonacci(N) % MOD)