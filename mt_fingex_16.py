#mt_fingex_16
def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Your code here
    #aligned return type : int
    if len(L)== 1:
        if type(L[0])!= list:
            return [L[0]]   
        else:
            return flatten(L[0])  
    else:
        if type(L[0])!= list:
            return [L[0]]+flatten(L[1:])
        else:
            return flatten(L[0])+flatten(L[1:])

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5] 