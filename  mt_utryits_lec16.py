# mt_utryits_lec16
# recuirsion on non numerics


# Q1. Memoize the code to find possible scores in basketball
def score_count_wm(x, d):# og code p11
    d = {1:1,2:2,3:3}
    if x in d:
        return d[x]
    else:
        ans =  score_count_wm(x-1,d)+score_count_wm(x-2,d)+score_count_wm(x-3,d)
        d[x]= ans
        return ans
d = {1:1, 2:2, 3:3}
print(score_count_wm(4, d))  # prints 6
# print(score_count(6, d))  # prints 20
# print(score_count(13, d))  # prints 1431

# Q2. 
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or 
    sublists of L and False otherwise. 
    """
    # your code here
    if L==[]:
        return False
    elif type (L[0])== list :
        return e in L[0] or in_list_of_lists_mod(L[1:],e)
    else:
        return L[0]==e or in_list_of_lists_mod(L[1:],e)
test = [[1,2],3,4,5,6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 10))  # prints False




