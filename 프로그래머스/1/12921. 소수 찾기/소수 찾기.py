import math

# 소수 구하는 함수
def isPrime(N):
    if N < 2: return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0: 
            return False
    return True;

def solution(n):
    result = 0
    for i in range(1, n + 1):
        if (isPrime(i)): result += 1

    return result