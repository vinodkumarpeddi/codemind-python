n = int(input())
a = map(int, input().split())
sum = 0
for i in a:
    if i % 2 == 0:
        sum += i
print(sum)