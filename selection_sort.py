n=int(input("enter list size" ))
a=[]
for i in range(n):
    val=int(input("enter number"))
    a.append(val)
    print("unsorted list is")
    print(a)
for i in range (n-1):
        min=i
        for j in range (i+1, n):
            if a[j] < a[min]:
                min=j
            a[i],a[min]=a[min],a[i]
            print("sorted list is")
            print(a)
            
            