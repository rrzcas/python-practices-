# mt_fingex_14.2
def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    # Your code here 
    anslist=[]
    for k , v in d.items():
        if sum(v) >= 0:
            anslist.append(k)
    anslist.sort()
    return anslist
        

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]