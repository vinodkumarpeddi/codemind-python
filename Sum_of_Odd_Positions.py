n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(1, n, 2):
    sum += a[i]
print(sum)