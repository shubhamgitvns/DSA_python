# Binery Sort for assending order

array= [30,32,40,66,65,80,90,96]
n=len(array)
x = 40
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
    if x < array[mid]:
        right = mid -1
    else:
        left = mid + 1

    if left > right:
        print("element not found")  
        break
