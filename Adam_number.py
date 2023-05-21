n = int(input())
sq = n * n
str_n = str(n)
rev_n = str_n[::-1]
sq_rev = int(rev_n) ** 2
str_sq_rev = str(sq_rev)
rev_str = str_sq_rev[::-1]
if sq == int(rev_str):
    print("True")
else:
    print("False")