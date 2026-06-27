a=[1,2,3,6,-5,-9]
min = a[0]
minpos = 0
n=len(a)
for i in range(1,n):
     if a[i]<min: # -5 < 1
        min=a[i]
        minpos=i
        print(a)
    
# print(a)
a[0],a[minpos]=a[minpos],a[0]
print(a)









