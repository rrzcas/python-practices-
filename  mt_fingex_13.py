# mt_fingex_13
def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here
    lengthct=0
    for i in L:
        if type(i) == str :
            lengthct+= len(i)
        if type(i) == list :
            for j in i :
                lengthct += len(j)

        else:
            raise ValueError("List must only contain strings or sublists")
        
    return lengthct
    


# Examples:
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError

        
