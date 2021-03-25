import random
a=input()
b=a.lower()[::-1]
c=random.choice(a).upper()
print(c+b)