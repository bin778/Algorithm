N = int(input())
F = int(input())

N //= 100
result = N * 100

for i in range(100):
    if (result % F == 0):
        break
    else:
        result += 1

print("{:02d}".format(result % 100))