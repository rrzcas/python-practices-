#console_history

x=1
y=2

# 1. swap value of x and y
temp = y
y = x
x = temp 
print(x , y)
# 2. input word in sentence
ans1 = input('1.pls input what ur goood at :')
if ans1 is None :
 quit()
print('i can ', ans1 , 'better than u!')
print((ans1+" ")*5)

#2.2 secret number 
s_num= 9
user_guess=input('2.what do u think the secret num will be ?')
if user_guess.strip() == "":
 quit()
ug_int=int(user_guess)
print( ' ur guess is ', ug_int== s_num )
if ug_int > s_num:
 
 print('too high , try again')
elif ug_int < s_num:
  print('too low , try again')

#3.

uage=int(input( 'how old r u??'))
if uage < 18 :
 print('ur a teen')
if uage == 18 and uage <65:
 print('ur an adult')
if uage >= 65 :
 print('ur a senior')

#  4. lost in the woods
#2 times right - print sad face b4 inptting next
# lcount=0
# rcount=0
# while True :
#  uchoise=input('where should i go..')
 
#  if uchoise.strip()=='left' :
#     print ('still lost , where to go next..')
#     lcount += 1
#     if lcount >= 2:
#       print(':(')
    
#  elif uchoise.strip()=='right' :
#     rcount+= 1
#     if rcount == 3 :
#       print('3 straight rights ! otta da woods !')
#       quit()
#  else:
#    print(' pls gimme a valid direction order')
#    quit()

#mini factorial calculator
#9*8*7*6*5*4*3*2*1

#Counting down
ufac=int(input('which number to be factorial this time?'))

count=ufac-1
while count > 0 :
    ufac=ufac*count
    count=count-1
print(ufac)

#Counting up

ufac=int(input('which number to be factorial this time?'))
count=1
ans=ufac
while ans> count:
    ufac=count*ufac
    count=count+1

print(ufac)

#printing start , and end-including sum
start=int(input('starts at:'))
end=int(input('ends at:'))
sum=0
for i in range(start,end+1):
 sum+=i 
print(sum)

#counts how many even number is in range , using for loop & break 
scstart=int(input('in range starts at ?'))
scend=int(input('in range ends at ?'))

ce=0
if scstart % 2 == 0:
    ce += 1

for i in range(scstart,scend+1,2) :
    ce+=1

print(ce)

#counts how many even number is in range , using for loop - improved version
sdstart=int(input('in range starts at ?'))
sdend=int(input('in range ends at ?'))
sdstep=int(input('step ?'))

ce=0

for i in range(sdstart,sdend+1,sdstep) :
    if i%2 == 0:
        ce+=1
print(ce)


#counts how many uniqe letters in string
s='kfccfkkfcccccvvggbb'
count=0
seen=[]
for i in s:
 if i not in seen:
     seen.append(i)
     print(seen)
     count+=1
print(count)

#checking if secret num is in range, prints staement only once using bool
secret_num = 9
fda=False
for i in range (1,11):
    if i == secret_num  :
        fda= True

if fda == True :
    print('fd')
else :
    print('not fd ')
        
        


#bisection method for cube root
# assuming for all +ve cubes , error w/in epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube
ct=0

guess = (high + low ) / 2.0


#while high - low > epsilon :
while abs(guess ** 2 - cube )> epsilon :
    ct+=1

    print(ct)
    if guess ** 2 > cube :
        high = guess
        print(f"higher now : guess is {guess}")
    elif guess **2  < cube :
        low = guess
        print(f"lower now : guess is {guess}")
    

    else:
        print (f"the final guess will be {guess } used {ct} times guesses")
        quit()
    guess = (high + low ) / 2.0

# LA6-Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to
# guess N. he code prints two ines: count: with how many guesses it took to find N, and answer: with the
# vaue of N. Hints: If the hafway vaue is exact y in between two integers, choose the smaer one

N=829
count=0
guess=0
high=1000
low = 0
guess = (high + low )/2
while guess != N :
    count+=1
    if guess < N :
        low = guess
    if guess > N :
        high = guess
    guess = (high + low )/2

print(f"so comp has guessed {count } times , the guessed ans will be {guess}")

#use fx for testing if a int is tiangular int (ie if its a number thats add of sum of continues int , eg 1+2+3..+k)
def is_triangular(n):
    """ n is an int > 0 
        Returns True if n is triangular, i.e. equals a continued
        summation of natural numbers (1+2+3+...+k) 
    """
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return True
    return False
print(is_triangular(6))


    #  "'"
    #  n is an int > 2
    #      epsilon is a positive number < 1
    #  Returns how many integers have a square root within epsilon of n 

# def is_squareroot (n, epsilon) :
#     low = 0
#     high = n
#     ct=0
#     guess = (high + low ) / 2.0


#     while abs(guess ** 2 - n )> epsilon :
#         ct += 1

#         if guess ** 2 > n :
#             high = guess
#         elif guess ** 2  < n :
#             low = guess
#         guess = (high + low ) / 2.0
#     return(guess)

#fx for finding sqrt using bisection mthd. v
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low) /2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) /2.0
    return ans 

def count_nums_with_sqrt_close_to (n  , epsilon) :
    count = 0
    sqrt=bisection_root()
    for i in range (n**3):
        if abs(n-sqrt)< epsilon:
            count+=1
    return count 


print(count_nums_with_sqrt_close_to(10),0.1)

def func_a():
    print (' inside func_a')
def func_b (y) :
    print ('inside func_b')
    return y
def func_c (f, z) :
    print ('inside func_c')
    return f (z)
print (func_a())
print (5 + func_b (2))
print (func_c (func_b, 3))
# * criteria is a func that takes in a number and returns a bool
# * n is an int


# Returns how many ints from 0 to n (inclusive) match
# the criteria (i.e. return True when run with criteria)

def is_even(x):
    return x%2 == 0

def apply (criteria, n) :
    count = 0

    for i in range (n + 1):
        if criteria(i):# == True :
            count += 1
    return count


how_many=apply(is_even,10)
print(how_many)


def char_counts (s) :

# s is a string of lowercase chars

# Return a tuple where the first element is the

# number of vowels in s and the second element

# is the number of consonants in s 
    vowels=('a','e','i','o','u')
    con_ct=0
    vw_ct=0

    for i in s :
        if i not in vowels :
            con_ct+=1
        if i in vowels :
            vw_ct+=1
    return (vw_ct,con_ct)
print(char_counts('anab'))

def sum_and_prod (L) :
# Lis a list of numbers
# Return a tuple where the first value is the sum of all
# elements in L and the second value is the product of 
# all elements in L
 sum=0
 prod=1
 for i in L:
    sum+= i
 for i in L:
   prod *= i 
 return(sum,prod)
print(sum_and_prod([1,2,3,4,5]))

def make_ordered_ap_list (n) :

# n is a positive int
# Returns a ap_list containing all ints in order from 0 to n (inclusive)
 ap_list=[]
 for i in range(n+1):
  
  ap_list.append(i)
 return ap_list 
print(make_ordered_ap_list(10))


def remove_elem (L, e) :
# L is a list
# Returns a new list with elements in the same order as L
# but without any elements equal to e.
 new_L=[]
 for i in range(len(L)) :
    if L[i]!= e:
        new_L.append(L[i])
 return new_L


L = [1,2,2,2]
print (remove_elem (L, 2) ) # prints [1]

def count_words (sen) :
#  sen is a string representing a sentence
# Returns how many words are in a ( i.e. a word is a 
# sequence of characters between spaces.
#b how many words r there , seperated by space
 ct = 0 
 lsen=sen.split(' ')

 print(lsen)
 for i in lsen:
    ct+=1
 return ct
print(count_words ("Hello it's me") )



def sort_words (sen) :
    ''' sen is a string representing a sentence
    Returns a list containing all the words in sen 
    but sorted in alphabetical order. '''
    spsen=sen.split(' ')
    spsen.sort()
    return spsen
 
print (sort_words ("look at this photograph") )

# This one is similar to remove_elem from lec10 except that remove_elem 
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    """ 
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    # your code here
    Lnew=L[:]
    L.clear()

    for i in range(len(Lnew)):
       if e != Lnew[i] :
           L.append(Lnew[i])
    



L=[1,1,2,2,3,3,3,44]
print(remove_all (L,2))
print(L)

# This one is similar to remove_elem from lec10 except that remove_elem 
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    """ 
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    # your code here
    Lnew=L[:]

    for i in range(len(Lnew)) :
        if e == Lnew[i] :
            L.remove(e)
                



L=[1,1,2,2,3,3,3,44]
print(remove_all (L,2))
print(L)


