def gcd_iter(a, b):
    while b:
        a, b = b, a % b
    return a
        

def solution(n, m):
    return [gcd_iter(n, m), int(n * m / gcd_iter(n, m))]