#mt_6100l_ex4

# Finger Exercise Lecture 4
# Assume you are given a positive integer variable named N. Write a piece of Python code 
# that finds the cube root of N. The code prints the cube root if N is a perfect cube 
# or it prints error if N is not a perfect cube.
#  Hint: use a loop that increments a counter—you decide when the counter should stop.


#old v - bisection method for cube root ,
# assuming for all +ve cubes , error w/in epsilon

#no nd to use bisection method 
cube = 27
epsilon = 0
low = 0
high = cube
ct=0

guess = (high + low ) / 2.0
#NOWADD check if its perfect cube , prints error msg for non perfect cube

#while high - low > epsilon :
while abs(guess ** 3 - cube )> epsilon :
    ct+=1

    print(ct)
    if guess == cube **(1/3) :
        
        print(f"the given number is a pefect cube ,and the cube root ofr it is :{guess}")
    elif guess**3 > cube :
        high = guess + 1
    elif guess ** 3 < cube :
        low = guess -1 

    else:
        print (f"the final guess will be {guess } used {ct} times guesses")
        quit()
    guess = (high + low ) / 2.0



# Finger Exercise Lecture 5
# Assume you are given a string variable named my_str. Write a piece of Python code that prints out
# a new string containing the even indexed characters of my_str. For example,
#  if my_str = "abcdefg" then your code should print out aceg.

