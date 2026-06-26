arry=[7,4,6,-2,8]

n = len(arry)
for i in range(n):
    min_index = i

    if min_index < i+1:
       continue
   
arry[i],arry[min_index] = arry[min_index],arry[i]

print(arry)


