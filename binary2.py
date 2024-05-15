def bin_ser(array, target):  # FUNCTION DEFINITION
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# __main()__
n = int(input("Input List size: "))
a = []
for i in range(n):
    val = int(input("Enter Number: "))
    a.append(val)
a.sort()  # Binary search requires a sorted array
print("The Input List is:")
print(a)
key = int(input("Enter the search key: "))
pos = bin_ser(a, key)
if pos != -1:
    print("Number found at position:", pos)
else:
    print("Number not found")
