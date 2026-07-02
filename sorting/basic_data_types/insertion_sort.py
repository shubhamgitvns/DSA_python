a=[22,4,6,7,5]
n = len(a)
for i in range(n-1):

    if a[i] > a[i+1]:
        temp = a[i+1]
        j=i

        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
print(a)    

        