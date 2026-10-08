"""Corey Schafer, Python OOP Tutorial 6: Property Decorators, plus the 4 pillars.
Video: https://www.youtube.com/watch?v=jCzT9XFZ5bw

Run (from learning-lab/):  python drill/oop/oop6_property_and_pillars.py

Part A: Encapsulation with @property (code along with the video)
  Step 1. Make an Employee class with first, last and email set in __init__.
          Change emp_1.first = 'Jim' and print emp_1.email.
          Question: why is the email now wrong?
  Step 2. Turn email into a @property, so emp_1.email (no brackets) always
          uses the current first and last.
  Step 3. Add a fullname @property with a @fullname.setter that splits
          "Corey Schafer" into first and last.
          Then add a @fullname.deleter that sets first and last to None.
  Step 4. Add __repr__ returning "Employee('first', 'last')". Print a list
          of two employees and check it uses __repr__.

Part B: Abstraction + polymorphism (not in the video, ~10 min)
  Step 5. from abc import ABC, abstractmethod.
          Make class Shape(ABC) with an @abstractmethod area(self).
          Try Shape() and read the error.
          Question: why can't you create a Shape?
  Step 6. Make Circle(radius) and Square(side), both subclasses of Shape,
          each with its own area().
  Step 7. Loop over [Circle(1), Square(2)] and print shape.area() for each.
          Question: which pillar is this, and why?
"""
from abc import ABC, abstractmethod
from turtle import shape

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def __repr__(self):
        # !r uses repr(): strings get quotes, None stays None
        return f"Employee({self.first!r}, {self.last!r})"
    
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
        def __init__(self, radius):
                self.radius = radius
        
        def area(self):
                return 3.14 * self.radius ** 2

class Square(Shape):
        def __init__(self, side):
                self.side = side

        def area(self):
                return self.side ** 2

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Corey", "Schafer")

# emp_1.first = "Jim"
emp_1.fullname = 'corey schafer'

print(emp_1.first)
print(emp_1.email)  

print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
print([emp_1, emp_2])  

# Shape()  # This will raise an error because Shape is abstract

print([shape.area() for shape in [Circle(1), Square(2)]])  # This will print the area of each shape