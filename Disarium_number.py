n = int(input())
str_n = str(n)
sum = 0
for i in range(len(str_n)):
    sum += int(str_n[i]) ** (i + 1)
if n == sum:
    print("True")
else:
    print("False")