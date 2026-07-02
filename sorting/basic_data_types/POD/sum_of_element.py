a=[2,7,11,50]
target = 9
d ={}

for i in range(len(a)):
    diff = target - a[i]

    if diff in d:
        print("Target Found")
        print("Indexes:", d[diff], i)
        print("Values:", diff, a[i])
        break

    d[a[i]] = i