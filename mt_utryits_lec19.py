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





    L1 = [2,5,1]
    L2 = ["blobfish", "crazyant", "parafox"]
    animals = make_animals(L1, L2)
    print(animals)     # note this prints a list of animal objects
    for i in animals:  # this prints the indivdual animals
        print(i)

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


