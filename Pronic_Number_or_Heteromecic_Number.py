n = int(input())
flag = False
for i in range(1, n+1):
    if i * (i+1) == n:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")