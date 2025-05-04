# mt_utryits_lec18

# 1.
class Coordinate(object):
    """ A coordinate made up of an x and y value """
def __init__(self, x, y):
    """ Sets the x and y values """
    self.x = x
    self.y = y
def distance(self, other):
    """ Returns the euclidean distance between two Coordinate objects """
    x_diff_sq = (self.x-other.x)**2
    y_diff_sq = (self.y-other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
def to_origin(self):
    """ always sets self.x and self.y to 0,0 """
    self.x = 0
    self.y = 0
def __str__(self):
    """ Returns a string representation of self """
    return "<" + str(self.x) + "," + str(self.y) + ">"# Add code to the init method to check that 
# * the type of center is a Coordinate obj and 
# * the type of radius is an int. 
# If either are not these types, raise a ValueError.

# utry:
class Circle(object):
    def __init__(self, center, radius):

        self.center = center
        self.radius = radius
        if type(center) != Coordinate:
            raise ValueError
        if type(radius) != int:
            raise ValueError
# center = Coordinate(2, 2)
# my_circle = Circle(center, 2)   # no error

# my_circle = Circle(2, 2)    # raises ValueError
# my_circle = Circle(center, 'two')  # raises ValueError
# 2. Implement the missing get_inverse and invert methods below
class SimpleFraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def get_inverse(self):
        """ Returns a float representing 1/self """
        # your code here
        return float(self.denom/self.num)
        
    def invert(self):
        """ Sets self's numerator to its denominator and vice versa.
            Returns None. """
        # your code here
        (self.num , self.denom)=(self.denom, self.num)
        return self
        
f1 = SimpleFraction(3,4)
print(f1.num, f1.denom)   # prints 3 4 
print(f1.get_inverse())   # prints 1.33333333 (note this one returns value)
f1.invert()               # acts on data attributes internally, no return
print(f1.num, f1.denom)   # prints 4 3 
#3.
# Modify the str method to represent the Fraction as just the 
# numerator, when the denominator is 1. Otherwise its representation 
# is the numerator then a / then the denominator, as before
class Fraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of self """
        # modify this
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + "/" + str(self.denom)

 
a = Fraction(1,4)
b = Fraction(3,1)
print(a)     # prints 1/4
print(b)     # prints 3

#4.
# Modify the code to return a Fraction object when denominator is 1
class Fraction(object):
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def reduce(self):
        def gcd(n, d):
            while d != 0:
                (d, n) = (n%d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1:
            # modify this
            return Fraction(self.num, 1)
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num/greatest_common_divisor)
            bottom = int(self.denom/greatest_common_divisor)
            return Fraction(top, bottom)
    def __str__(self):
        """ Returns a string representation of self """
        # Note this is not the version with the numerator 
        # only when the denomiator is 1
        return str(self.num) + "/" + str(self.denom)
    
f1 = Fraction(5,1)
f1r = f1.reduce()
# print(f1r)          # prints 5/1 not 5
# print(type(f1r))    # prints <class '__main__.Fraction'>
