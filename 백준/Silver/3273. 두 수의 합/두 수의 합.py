import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()

def two_pointer(a, x):
    result = 0
    left, right = 0, len(a) - 1
    while left < right:
        cur_sum = a[left] + a[right]
        if cur_sum == x:
            result += 1
            left += 1
        elif cur_sum < x:
            left += 1
        else:
            right -= 1
    return result

print(two_pointer(a, x))