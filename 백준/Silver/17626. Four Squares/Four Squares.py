import math

def min_squares(n):
    # n이 0이면 0 리턴
    if n == 0:
        return 0
    
    # n이 1개의 제곱수로 표현되는 경우
    if int(math.sqrt(n)) ** 2 == n:
        return 1
    
    # n이 2개의 제곱수로 표현되는지 확인
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i ** 2)) ** 2 == n - i ** 2:
            return 2
    
    # n이 3개의 제곱수로 표현되는지 확인 (라그랑주 사제법칙에 의해 4개는 마지막 옵션)
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4
    
    return 3

n = int(input())
print(min_squares(n))