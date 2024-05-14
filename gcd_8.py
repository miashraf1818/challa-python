def gcd(a,b):
    if a == 0 :
        return b
    elif b == 0 :
        return a
    else:
        return(gcd(b,a%b))
a = int(input("Enter a "))
b = int(input("Enter b "))
print("The gcd of",a,"and",b,"is",gcd(a,b))

 
