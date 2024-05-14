def fact(n):
    if n==0:
        result = 1
    else:
        result = n * fact(n-1)
    return result
       
n = int(input("enter the number : "))
print("factorial=",fact(n))
