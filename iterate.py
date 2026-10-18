
s=0
a=[1,2,3,4,5,6,7,8,9,10]
m=a[0]
for i in range(0,len(a)):
    b=+a[i]
    s=s+b
    if a[i]>m:
        m=a[i]
    print(a[i])
print(s,m)