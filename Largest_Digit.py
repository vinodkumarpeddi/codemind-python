n = int(input())
str_n = str(n)
for i in range (len(str_n)) :
    lst = []
    for j in str_n :
        lst.append(int(j))
        maxi = max(lst)
print(maxi)