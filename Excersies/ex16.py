n= 76542
rev=0
x=n
while (n>0):
    rev = (rev*10)+n%10
    n = n//10
print(rev)