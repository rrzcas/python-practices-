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


# Q3. 
def my_deepcopy(L):
    """ 
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that 
    contains copies (recursively) of every sublist 
    """
    # your code here
    if L==[]:
        return []
    if len(L)==1:
        if type(L[0])==list:
            return [my_deepcopy(L[0])]
        else:
            return [L[0]]
    else:
        if type(L[0])==list:
            return [my_deepcopy(L[0])]+my_deepcopy(L[1:])
        else:
            return [L[0]]+my_deepcopy(L[1:])


myL = ["abc", ['d'], ['e', ['f', 'g',[['kk']]]]]
my_newL = my_deepcopy(myL)
print(myL)
print(my_newL)
myL[2][1][0] = 1
print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]



# Q4. Here are 3 recursive functions that are incorrectly implemented.
# Debug them to have them do what the specs say.
def f(L):
    """ L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet. """
    if len(L) == 1:
        return L[0]
    else:
        if L[0] > L[len(L)-1]: #b>a
            return f(L[1:])
        else:
            return f(L[0:len(L)-1])            
print(f(['z', 'k', 'b', 'c', 'd','b','a','s','p','l']))  # should print 'a'
print(f([ 'k', 'c', 'a','b']))  # should print 'a'

def g(L, e):
    """ L is list of ints, e is an int
    Returns a count of how many times e occurrs in L  """
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            return(1+g(L[1:], e))
        else:
            return g(L[1:],e)
# print(g([1,2,3,1], 1))     # should print 2
print(g([1,1,2,3,1,1], 1)) # should print 4
print(g([1,1,3,2,2,2,2,2], 2)) # prints 5


def h(L, e):
    """ L is list, e is an int
    Returns a count of how many times e occurrs in L or 
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    if len(L)==1:
        if type(L[0])==list:
            return h(L[0],e)+h(L[1:], e)
        else:
             if L[0]==e:
                return 1
             else:
                 return 0
    else: # len(L[0])>1
        if type(L[0])==list:
            return h(L[0],e)+h(L[1:], e)
        else:
             if L[0]==e:
                return 1+h(L[1:],e)
             else:
                 return h(L[1:],e)
    
print(h([1,2,[1,[1]],1], 1))        # should print 4
print(h([1,2,[3,1,[1,[1]]]], 3))  # should print 1
    
