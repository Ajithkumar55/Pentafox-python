import random
l=["s1","s2","s3","s4","s5"]
l1=[]
for i in range(5):
    a=random.sample(l,5)
    if a not in l1:
      l1.append(a)
for i in range(5):
    for j in range(5):
        print(l1[i][j],end=" ")
    print() 