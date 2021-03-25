ar=list(map(int,input().split(",")))
b=int(input())
c=0
c1=0
f=0
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        s=ar[i]+ar[j]
        if(b==s):
            f=1
            c=ar[i]
            c1=ar[j]
            break
    
        n=0
    if (f==1):
        break
if (f==1):
    print(c,",",c1)
else:
    print("No Pairs found")