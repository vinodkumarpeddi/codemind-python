for a in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in l:
            print(i)