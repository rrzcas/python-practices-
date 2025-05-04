#mt_athomes_18

#Question 1.
# Add a method to the Circle class that allows you to print a Circle object
# (you decide how to best represent it!)
class Circle():
    def __init__(self, radius ,center ):
        self.r=radius
        self.c= center
    def __str__(self):
     """ A Circle's string representation is the radius """
    # your code here
     return f"Circle with radius {self.r} and center ({self.c.x}, {self.c.y})"
    def is_inside(self, point):
        """ Returns True if point is inside self and False otherwise """
        return point.distance(self.center) < self.radius
    
class Coordinate():
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

    
center = Coordinate(2, 2)
my_circle = Circle(5,center)
print(my_circle)
#Question 2.
# Implement a method in Fraction class such that the operator ** works
#print(a**b) # works after you define it on two Fraction objects

class Fraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def __float__(self):
        return self.num/self.denom
    def __pow__ (self,exponential):
        """ num and denom are integers """  
        
        return float(self)**float(exponential)
    def __str__(self):
        """ Returns a string representation of self """
        # modify this
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + "/" + str(self.denom)

 
f1 = Fraction(4,1)
f2 = Fraction(1,2)
print(f1**f2)    # prints 2.0

