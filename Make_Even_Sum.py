def evensum(arr,n):
    even_count=odd_count=0
    
    for i in range(n):
        if arr[i]%2==0:
            even_count+=1
        else:
            odd_count+=1
    if odd_count%2==0:
        return True
    else:
        return False
n=int(input())
arr=list(map(int,input().split()))
if evensum(arr,n):
    print("1")
else:
    print("0")