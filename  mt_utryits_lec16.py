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



# Q2. If we evaluate mult_recur(3,4), how many times is the 
# procedure mult_recur called (including initial call)?
# Hint: add a print inside the function!

# or use print: count hpow many prints are printed out by hand (official ans)
def mult_recur(a,b):
    
    mult_recur.ct +=1
    if b == 0:
        return 0
    else:
        return a + mult_recur(a,b-1) 
mult_recur.ct = 0

print(mult_recur(3,4))
print(mult_recur.ct)


# Q3. Calculate a+b recursively. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add(a, b):
    """ Uses recursion to calculate a+b as adding
    a to 1, b times. """
    # your code here
    if a==0:
        return b
    else :
        return 1+(add(a-1,b))
    
    
print(add(3,4))   # prints 7



# Q4. Calculate a+b recursively by 1's. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add_by_ones(a, b):
    """ Uses recursion to calculate a+b as adding
    1, a times then adding 1, b times. """
    # your code here
    if a ==0 :
        return b
    if b == 0 :
        return a 
    else :
        return add_by_ones(1,a-1)+add_by_ones(b-1,1)

print(add_by_ones(3,4))   # prints 7