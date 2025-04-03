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
        
        


class InvalidInputYearRange(Exception):
    """Invalid input year range"""
    def __init__(self):
        self.message = "Endind year is lesser than starting year"
        super().__init__(self.message)
#catch abcd as str and desimal as hw , invalid input 
class NegativeYear(Exception):
    """Negative year provided"""
    def __init__(self):
        self.message = "Year input is negative"
        super().__init__(self.message)

class AttackException(Exception):
    """Attack Attack Attack !!!"""
    def __init__(self):
        self.message = "Terminating as this seems to be a resource wasting attack"
        super().__init__(self.message)


def isLeapYear(year : int) -> bool: 
    return True if year % 4 == 0  else False


def takeInput():
    valid_inputs_recieved = False
    attack = False
    while (not valid_inputs_recieved and not attack) :
        try:
            starting_yr=int(input('starting from:'))
            ending_yr=int(input('ending at:'))
            if starting_yr < 0 or ending_yr < 0:
                raise NegativeYear()
            if starting_yr > ending_yr :
                raise InvalidInputYearRange()
            valid_inputs_recieved = True
        except Exception as e:
            if (isinstance(e, NegativeYear)):
                print ("This in an attack")
                attack = True
                raise AttackException()
            else:
                print (e.message)    
                print("Please try again")    
        
    return starting_yr, ending_yr

def countLeapYears(starting_yr, ending_yr) -> int:
    count = 0
    for i in range(starting_yr, ending_yr):
        if (isLeapYear( i)):
            count+=1
    return count

def main():
    try:
        starting_yr, ending_yr = takeInput()
        count = countLeapYears(starting_yr, ending_yr)
        print("No. of leap years between " , starting_yr, " and ", ending_yr, " is: ", count)  
    except Exception as e:
        print ("Execution failed with exception: ", e)

main()

#bisection method for cube root
# assuming for all +ve cubes , error w/in epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube
ct=0

guess = (high + low ) / 2.0


#while high - low > epsilon :
while abs(guess ** 3 - cube )> epsilon :
    ct+=1

    print(ct)
    if guess ** 3 > cube :
        high = guess
        print(f"higher now : guess is {guess}")
    elif guess **3  < cube :
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

