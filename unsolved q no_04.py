#unsolved q no: 04
def star(n):
    if n==0:
        return print("please enter any natural number ")
    else:
        return "*"*n,"\n",star(n-1)
#ain inputs
a=int(input('enter a positive integer'))
print(star(a),sep='\n')
