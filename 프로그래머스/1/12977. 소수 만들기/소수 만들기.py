import math

# 소수 구하는 함수
def isPrime(N):
    if N < 2: return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0: 
            return False
    return True;

def solution(nums):
    result = 0
    num = []
    
    # 자연수 만들기
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                num.append(nums[i] + nums[j] + nums[k])
    
    # 소수 판별하기
    for i in range(0, len(num)):
        if (isPrime(num[i])):
            result += 1
    
    return result