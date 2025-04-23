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

## Write a list comprehension expression that uses a list named L.
# It makes a new list whose elements are the middle 
# character of strings whose length is 3. 

# If L = ['abc', 'm', 'p', 'xyz', '123', 57]
# It makes ['b', 'y', '2']

# method using function

def newlist_of3rd_sym(L):
    newL=[]
    for i in L :
        if type(i) == str  and  len(i)== 3 :
            newL.append(i[1])
    return newL 
L = ['abc', 'm', 'p', 'xyz', '123', 57]
# print(newlist_of3rd_sym(L))

# one-liner method
newL=[ i[1] for i in L if type(i) == str  and  len(i)== 3]
print(newL)
# print([e[1] for e in L if len(e)==3 and type(e)==str])
###################################

def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    # your code her
    # challenge: write this with list comprehension! - e**2 for e in L if e%2 != 0
    # newL=[ i[1] for i in L if type(i) == str  and  len(i)== 3]

    # assert len(Lnum)!=0 and len(Ldenom)!=0 and len(Lnum) ==len(Ldenom) 
    assert len(Lnum)!=0 and len(Ldenom)!=0 , ' list is empty^o^'
    assert len(Lnum) ==len(Ldenom)  , 'lengths of lists given are different '

    try :
            ret_L= [ Lnum[i] / Ldenom[i] for i in range(len(Lnum))  ]
    except  ZeroDivisionError:
       print('zero dv error')
       raise ZeroDivisionError  ('cant divide by Zero^^')
      


    
# # For example:
# L1 = [4,5,6]
# L2 = [1,2,3]    
# print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

# L1 = [4,5,6]
# L2 = [1,0,3]    
# print(pairwise_div(L1, L2))  # raises a ValueError

# to run after introducing assertions
# L1 = [4,5,6,7,8]
# L2 = [1,8,3]    
# print(pairwise_div(L1, L2))  # raises an AssertionError

L1 = []
L2 = []    
print(pairwise_div(L1, L2))  # raises an AssertionError

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
    for i in range(len(L)) :
        assert type( L[i]) == str or type(L[i]) == list , 'errror,1'
        for j in range(len(L[i]([j]))):
            assert type (L[i][j]) == str ,'error,2'
   
        sumof_listL_str =[len(L[i]) for i in range(len(L)) + len(L[i][j]) for j in range(len(i)) ]

    # newL=[ i[1] for i in L if type(i) == str  and  len(i)== 3]

    return sumof_listL_str
    

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError

def find_grades(idict, inputted_name):
    """ grades is a dict mapping student names (str) to grades (str)
        students is a list of student names 
    Returns a list containing the grades for students (in the same order) """
    # your code here
    newlist=[]
    for i in inputted_name :
        newlist.append(idict[i])
    return newlist
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']””


#utry lec 14 - dictionaries

def find_in_L(Ld, k):
    """ L is a list of dicts
        k is an int
    Returns True if k is a key in any dicts of L and False otherwise """
    # your code here
    RES=False
    
    for sfdict in Ld :
        if k in sfdict:
            RES= True
    
    return RES




  
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1, d2, d3], 2))  # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False

########################################################

def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    # your code here
    ct=0
    for k, v in d.items():
        if k == v :
            ct+=1
    return ct


d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2

my_d = {
    'Ana': {'mq': [10], 'ps': [10, 10]},
    'Bob': {'ps': [7, 8], 'mq': [8]},
    'Eric': {'mq': [3], 'ps': [0]}
}
def get_average (data, what) :
    all_data = []
    for stud in data.keys () :
    # INSERT LINE HERE\
    # CHOICE A:
        all_data = all_data + data[stud][what]
        
        # returns a list of int 
    # CHOICE B:
        # all_data.append(data [stud][what])
        # print('adlist',all_data)

        #returns int inside a list of list ,as all data is a list
    print('stud',stud)
    print('adlist',all_data)

    print(get_average(my_d,'mq'))
    return sum (all_data) /len (all_data)


def power_while2(n, p):
    ans=1
    flag=False
    if p < 0:
        flag=True
        p=abs(p)
    
    if p == 0:
        return 1

    while p > 0 :
        ans=ans*n
        p-=1
    if flag:
        ans= 1/(ans)
    return ans


print(power_while2(-8,-3))


# utry_lec15_recursion
# Calculate n**p recursively by writing this function

def power_recur1(n, p):
    if p==0 :
        return 1
    elif p==1 :
        return n
    else:
        return power_recur1(n,p-1)*n

print(power_recur1(2,3))  # prints 8










