#mt_fingex_9
def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    sum=0
    ct=0
    for i in range(tA) :
            sum += tA[i] *tB[j]  
            ct+=1

    return (ct,sum)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)
