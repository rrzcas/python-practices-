#ita_ex2.1-5

A=[1,0,1,1]
B=[1,1,1,1]

def ADD_BINARY_INTEGERS(Aa, Bb, nnn):
    # pt - Initialize result array C with n+1 zeros (extra space for carry)
    C = [0] * (nnn + 1)
    
    # pt - Initialize carry
    carry = 0
    
    # pt- Process each bit from right to left
  #  range(start, stop, step)
    for i in range(nnn-1, -1, -1):

        # pt - Add bits from A and B and the carry
        total = Aa[i] + Bb[i] + carry
        
        # pt - Store the result bit (either 0 or 1)
        C[i+1] = total % 2  
        
        #pt -  Calculate new carry (0 or 1)
        carry = total // 2
    
    # pt - Store final carry in the most significant position
    C[0] = carry
    
    return C
    
ANS1 = ADD_BINARY_INTEGERS(A, B, len(A))
decimal_ANS1 = int(''.join(map(str, ANS1)), 2) #',2' for transfering base10 to base 2
print(f"Binary result: {''.join(map(str, ANS1))}")
print(f"Decimal result: {decimal_ANS1}")



