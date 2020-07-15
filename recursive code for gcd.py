#Srecursive code to compute G.C.D.  of two number
def gcd(a,b):
    if (b==0):
        return a                #base case
    else:
        return gcd(b,a%b)       #recursive case
#main inputs for  programme
x=int(input("Enter first number:-"))
y=int(input("Enter second number:- "))
output=gcd(x,y)
print("GCD of ",x,"and",y,"is:",output)
