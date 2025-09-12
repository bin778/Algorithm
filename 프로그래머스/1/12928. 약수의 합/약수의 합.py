import math

def solution(n):
    root = int(math.sqrt(n))
    result = 0
    
    for i in range(1, root + 1):
        if (n % i == 0):
            result += i
            if (n / i != i):
                result += int(n / i)
    
    return result