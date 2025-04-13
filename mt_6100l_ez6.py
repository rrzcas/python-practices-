#mt_6100l_ez6

# Assume you are given an integer 0 \<= N \<= 1000. Write a piece of Python code that uses 
# bisection search to guess N. The code prints two lines: count: with how many guesses it
# took to find N, and answer: with the value of N. Hints: If the halfway value is exactly in 
# between two integers, choose the smaller one. 
N= 9

high = 1001
low = 0 
mid= (high+low)/2

ct=0

while mid != N :
    mid= (high+low)/2
    ct+=1

    if mid > N :
        high=mid+1
    elif mid < N :
        low = mid-1
    else:

     print(f'so the secret number is {N} and comp guessed for {ct} times')
     break


 