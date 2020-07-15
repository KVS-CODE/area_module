#recursive code to compute G.C.D.  of three numbers
def gcd(a,b,c):
    if (b==0 or a==0 or c==0):      #bace case 
        return a
    else:
        return gcd(c,(b%c),(a%b))       #recursive case
        print(output)
#main inputs of programme
x=int(input("Enter first number"))
y=int(input("Enter second number: "))
z=int(input("Enter second number: "))

output=gcd(x,y,z)
print("GCD of ",x,',',y,"and",z,"is:",output)
