'''THIS IS A CODE TO IMPLEMENT THE BISECTION SEARCH
OF A SORTED LIST '''

def bisearch1(L, e):
    #this takes in a list and some other item and checks to see
    #if this element is included in the list
    if len(L)==0:
        return False
    elif len(L)==1:
        return L[0]==e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisearch1(L[:half], e)
        else:
            return bisearch1(L[half:],e)
          
          
j = [1, 2, 3, 4, 5, 6 , 7]
print(bisearch1(j, 4))