array= [5,0,-1,-8]
n=len(array)
x = -8
left = 0
right = n-1
count = 0
while True:
    mid = (left+right)//2
    print(mid)
    count = count+1
    print("Step:", count)
    if array[mid] == x:
        print("Found at ",mid)
        break
    if x > array[mid]:
        right = mid -1
    else:
        left = mid + 1

    if left > right:
        print("element not found")  
        break
