def solution(a):
    result = 2
    if len(a) <= 2:
        return len(a)
    
    left_min = [0] * len(a)
    left_min[0] = a[0]
    for i in range(1, len(a)):
        left_min[i] = min(left_min[i - 1], a[i])
    
    right_min = [0] * len(a)
    right_min[len(a) - 1] = a[len(a) - 1]
    for i in range(len(a) - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
    
    for i in range(1, len(a) - 1):
        min_n1 = left_min[i - 1]
        min_n2 = right_min[i + 1]
        if (min_n1 > a[i] or min_n2 > a[i]):
            result += 1
    
    return result