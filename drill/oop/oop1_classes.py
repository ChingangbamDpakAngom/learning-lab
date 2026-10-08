"""Corey Schafer, Python OOP Tutorial 1: Classes and Instances.
Video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM

Run (from learning-lab/):  python drill/oop/oop1_classes.py

Steps (code along with the video):
  Step 1. Make an empty class Employee. Create two instances, print both.
          Question: are they different objects?
  Step 2. Add __init__(self, first, last, pay). Save first, last and pay on self,
          and build email as "first.last@company.com".
  Step 3. Add a method fullname(self) that returns "first last".
  Step 4. Call it both ways and compare:
              emp_1.fullname()
              Employee.fullname(emp_1)
          Question: what does that tell you about self?
"""


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
       

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    def who_am_i(self):
        print(f"self is emp_1: {self is emp_1}, self is emp_2: {self is emp_2}")
        

if __name__ == "__main__":
    emp_1 = Employee("Corey", "Schafer", 50000)
    emp_2 = Employee("Test", "User", 60000)

    print(emp_1.email())
    print(emp_2.email())
    print(emp_1.fullname())
    print(emp_2.fullname()) 
    print(Employee.fullname(emp_1))
    print()
    emp_1.who_am_i()