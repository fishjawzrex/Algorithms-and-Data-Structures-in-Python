#towers of hanoi

def toh(n,a,b,c):
    if n==1:
        print("move " + str(a) + " to " + str(c))
    else:
        toh(n-1,a,c,b)
        toh(1,a,b,c)
        toh(n-1,b,a,c)

print(toh(3, 'a', 'b', 'c'))
        
 