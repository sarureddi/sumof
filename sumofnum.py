s=int(input())
a=list(map(int,input().split()))
r=0
for u in range(0,s):
    for k in range(0,u):
        if a[k]<a[u]:
            r=r+a[k]
print(r)  
