#recursive code to copute su of squarees of n nubers
def sqsu(n):
    if n==1:
        return 1
    else:
        return (n**2)+sqsu(n-1)
#__ain _ inputs
n=int(input("Enter value of n :"))
print(sqsu(n))
