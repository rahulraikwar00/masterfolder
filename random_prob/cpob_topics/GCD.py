def gcd(a, b):  
    if a == 0 : 
        return b  
    return gcd(b%a, a) 
a = 3
b = 4
print(b%a)
print("gcd(", a , "," , b, ") = ", gcd(a, b)) 