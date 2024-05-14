n  = int(input("enter list size"))
a = []
for i in range(n):
    val = int(input("enter number"))
    a.append(val)
    print("unsorted list is:")
    print(a)
    
for i in range (n):
    swapped=False
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swapped=True
    if not swapped:
        break
    print("sorted list is:")
    print(a)
    