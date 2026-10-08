"""Corey Schafer, Python OOP Tutorial 3: classmethods and staticmethods.
Video: https://www.youtube.com/watch?v=rq8cL2XMM5M

Run (from learning-lab/):  python drill/oop/oop3_class_static_methods.py

Steps (code along with the video):
  Step 2. Fill in set_raise_amt(cls, amount): set cls.raise_amt to amount.
          Call Employee.set_raise_amt(1.05), then print the three raise_amt values.
          Question: why did ALL of them change this time (unlike OOP 2 Step 5)?
  Step 3. Alternative constructor: add a @classmethod from_string(cls, emp_str)
          that splits "John-Doe-70000" on "-" and returns cls(first, last, pay).
          Create emp_3 with it and print emp_3.email.
          Question: why return cls(...) instead of Employee(...)?
  Step 4. Add a @staticmethod is_workday(day) that returns False for Saturday
          and Sunday, True otherwise. Test it with datetime.date(2026, 10, 10).
          Question: why is this a staticmethod (it uses neither self nor cls)?
"""

import datetime

# Python OOP
class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)
# Employee.raise_amt = 1.05 both are same but we are using class method to set the raise amount

emp_str_1 = 'John-Doe-70000'  
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# alternative constructor: class method
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email, new_emp_1.pay)
                                


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)



my_date = datetime.date(2026, 10, 10)
print(Employee.is_workday(my_date))  # False

