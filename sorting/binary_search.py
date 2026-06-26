# Binery Sort for desending order

array= [8,5,3,0,-1,-7,-8,-9]
n=len(array)
x = 8
left = 0
right = n-1
count = 0
while True:
    mid = (left+right)//2
    print(mid)
    count = count+1
    print("Step:", count)
    if array[mid] == x:
        print("Found")
        break
    if x > array[mid]:
        right = mid -1
    else:
        left = mid + 1

    if left > right:
        print("element not found")  
        break
