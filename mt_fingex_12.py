# mt_fingex_12

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    ct = 0
    for i in nums_list :
        if i*i in nums_list:
            ct +=1
        
    return ct

   
print(count_sqrts([3,4,2,1,9,25])) # prints 3

