# mt_fingex_15
def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    # Your code here  
    if exp==0 :
        return 1
    elif exp==1 :
        return base
    else:
        return recur_power(base,exp-1)*base



# Examples:
print(recur_power(2,5))  # prints 32