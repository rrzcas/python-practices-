#mt_athomes_19
#mt_utryits_lec19

class Animal(object):
    def __init__(self, age , name=None):
        self.age = age
        self.name = name
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname


    # Write a function that meets this spec.
    def make_animals(L1, L2):
        """ L1 is a list if ints and L2 is a list of str
            L1 and L2 have the same length
        Creates a list of Animals the same length as L1 and L2.
        An animal object at index i has the age and name
        corresponding to the same index in L1 and L2, respectively. """
        # your code here
        L3=[]
        for i in range(len(L1)):
            age = L1[i]
            name = L2[i]
            a = Animal(age)
            a.set_name(name)
            L3.append(a)
        return L3





    # L1 = [2,5,1]
    # L2 = ["blobfish", "crazyant", "parafox"]
    # animals = make_animals(L1, L2)
    # print(animals)     # note this prints a list of animal objects
    # for i in animals:  # this prints the indivdual animals
    #     print(i)

#mt_utryits_lec19

class Animal():
    def __init__(self, age , name=None):
        self.age = age
        self.name = name
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def speak(self):
        print("hello")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)



    # Write a function that meets this spec.
    def make_animals(L1, L2):
        """ L1 is a list if ints and L2 is a list of str
            L1 and L2 have the same length
        Creates a list of Animals the same length as L1 and L2.
        An animal object at index i has the age and name
        corresponding to the same index in L1 and L2, respectively. """
        # your code here
        L3=[]
        for i in range(len(L1)):
            age = L1[i]
            name = L2[i]
            a = Animal(age)
            a.set_name(name)
            L3.append(a)
        return L3
# 2. Write the function according to this spec
    def make_pets(d):
        """ d is a dict mapping a Person obj to a Cat obj
        Prints, on each line, the name of a person, 
        a colon, and the name of that person's cat """
        # your code here
        for person, cat in d.items():
            print(f"{person.get_name()}: {cat.get_name()}")



p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")

#1st utry printouts
# L1 = [2,5,1]
# L2 = ["blobfish", "crazyant", "parafox"]
# animals = make_animals(L1, L2)
# print(animals)     # note this prints a list of animal objects
# for i in animals:  # this prints the indivdual animals
#     print(i)

d = {p1:c1, p2:c2}
Cat.make_pets(d)  # prints ana:furball(/n)james:fluffsphere


#  at home --

# Write the class Employee as a subclass of Person
class Employee(Person):
    """ An Employee contains an extra data attribute, salary as an int """
    def __init__(self, name, age):
        """ initializes self as a Person with a salary data attribute, initially 0 """
        Person.__init__(self,name, age)
        self.name=name
        self.age=age
        self.salary = 0
        self.list_track = [0] 
        
    def get_salary(self):
        """ returns self's salary """
        return self.salary # get = return self 
    def set_salary(self, s):
        """ s is an int
        Sets self's salary data attribute to s """
        self.salary= s
        self.list_track.append(s) #  hinted at past salaries list
    def salary_change(self, n):
        """ n is an int (positive or negative)
        Adds n to self's salary. If the result is negative, sets 
        self's salary to 0. Otherwise sets self's salary to the new value. """
        if self.salary + n < 0 :
            self.salary = 0

        else:
            self.salary += n 
        self.list_track.append(self.salary)

    def has_friends(self):
        """ Returns True if self's friend list is empty and False otherwise """
        return len(self.friends)!= 0
    def past_salaries_list(self):
        """ Keeps track of all salaries self has had in the order they've changed. 
        i.e. whenever the salary changes, keep track of it.
        Hint: you may need to add an additional data attribute to Employee.
        Returns a copy of the list of all salaries self has had, in order. """
        return self.list_track.copy()
        
    def past_salary_freq(self):
        """ Returns a dictionary where the key is a salary number and the 
        value is how many times self's salary has changed to that number. """
        fdict={}
        for i in self.list_track:
            if i in fdict:
                fdict[i] += 1
            else:
                fdict[i] = 1
        return fdict



# For example:
e = Employee("ana", 35)
print(e.get_salary())   # prints 0
e.set_salary(1000)
print(e.get_salary())   # prints 1000
e.salary_change(2000)
print(e.get_salary())   # prints 3000
e.salary_change(-50000)
print(e.get_salary())   # prints 0
print(e.has_friends())  # prints False
e.add_friend("bob")
print(e.has_friends())  # prints True
print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
print(e.past_salary_freq())  # prints {0: 2, 1000: 1, 3000: 1}
# Write a function that meets this specification
def counts(L):
    """ L is a list of Employee and Person objects 
    Returns a tuple of a count of:
      * how many Person objects are in L
      * how many Employee objects are in L 
      * the number of unique names among Employee and Person objects """
    pass

# For example:
# make employees and people
# L = []
# L.append(Person('ana',8))
# L.append(Person('bob',25))
# L.append(Employee('ana',35))
# L.append(Employee('cara',18))
# L.append(Employee('dan',53))
# # call function
# print(counts(L))    # prints (2,3,4)