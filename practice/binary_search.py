#  EXERCISE 4 : Implement Binary search technique
def bin_ser(a,n,key): # FUNCTION DEFINITION
    beg = 0
    end= n - 1
    flag = 0
    while beg <= end and flag == 0:
        mid = ( beg + end ) // 2
        if ( key == a[mid]) :
            flag = 1
            pos = mid + 1
        if key > a[mid]:
            beg = mid + 1
        if key < a[mid]:
            end = mid - 1
    if flag == 1:
        print("Number found at position ",pos)
    else:
        print("Number not found")

# __main()__

n = int(input("Input List size "))
a = []
for i in range(n):
    val = int(input("Enter Number "))
    a.append(val)
print("The Input List is ")
print(a)
key = int(input("Enter the search key "))
bin_ser(a,n,key)
