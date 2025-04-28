#mt_fingex_17
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        
        # your code here
        self.sradius=radius

    def get_radius(self):# for showing/printing raius out OR to use this function to access radius in other functions
        """ Returns the radius of self """
        # your code here
        return self.sradius

    def set_radius(self, radius):# when there's a change of value of radius using function , use this function to substitute it back to to original function , so it acts like all other radius in this function onwards
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.sradius=radius
        

    def get_area(self):# cal area of circle
        """ Returns the area of self using pi = 3.14 """
        # your code here
        pi=3.14
        return pi*(self.sradius)**2


    def equal(self, c): #see if 2 circle equals
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here
        return c.sradius==self.sradius

    def bigger(self, c): # see which circle's bigger
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        # can raise exeption for invalid input 
        # your code here 
        if c.sradius > self.sradius:
            return c
        elif self.sradius> c.sradius:
            return self
        else:
            return 'equals'
circle1 = Circle(5)
circle2 = Circle(7)

# Test get_radius method
print("Circle 1 radius:", circle1.get_radius())
print("Circle 2 radius:", circle2.get_radius())

# Test get_area method
print("Circle 1 area:", circle1.get_area())
print("Circle 2 area:", circle2.get_area())

# Test set_radius method
circle1.set_radius(10)
print("Circle 1 new radius:", circle1.get_radius())

# Test equal method
print("Are circle1 and circle2 equal?", circle1.equal(circle2))

# Test bigger method
bigger_circle = circle1.bigger(circle2)
print("Bigger circle radius:", bigger_circle.get_radius())