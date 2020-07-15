#recursive code to compute sum of squares between any two numbers
def sqsum(a,b):
    if a==b:
        return a**2
    elif b>a:
        return  b*b +sqsum(a,(b-1))
    else:
        return a*a + sqsum(b,(a-1))
#__main inputs for programme
x=int(input("Enter number from which you want to calculate sum of square of the numbers :-"))
y=int(input("Enter maximum value at which you want to calculate :-"))
output=sqsum(x,y)
print(output)
