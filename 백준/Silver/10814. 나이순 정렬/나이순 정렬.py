N = int(input())
result = []
for _ in range(N):
    age, name = input().split()
    result.append([int(age), name])

for i in sorted(result, key = lambda x : x[0]):
    print(i[0], i[1])