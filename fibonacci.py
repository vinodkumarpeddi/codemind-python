n = int(input())
a = 0
b = 1
if n == 1:
    print(a)
elif n == 2:
    print(a, b, end = " ")
else:
    for i in range (n):
        print(a, end = " ")
        c = a + b
        a = b
        b = c