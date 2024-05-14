n = int(input("Input List size "))
a = []
for i in range(n):
    val = int(input("Enter Number "))
    a.append(val)
print("The Input List is ")
print(a)
key = int(input("Input Key element "))
flag = 0
for i in range(n):
    if a[i] == key:
        flag=1
        pos=i
        break   
if flag == 1:
    print("Element found at position:",pos,"and Search is successful")
else:
    print("Element not found and Search is Unsuccessful")