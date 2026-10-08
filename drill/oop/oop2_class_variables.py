"""Corey Schafer, Python OOP Tutorial 2: Class Variables.
Video: https://www.youtube.com/watch?v=BJ-VvGyQxho

Run (from learning-lab/):  python drill/oop/oop2_class_variables.py

Key idea:
  instance variable -> set in __init__ as self.x, different for each object (first, pay)
  class variable    -> set in the class body, shared by ALL objects (raise_amount)
  Lookup order for self.x: the instance first, then the class (first match wins).
"""


class Employee:
    # Class variables: defined in the class body, outside any method.
    raise_amount = 1.04   # same raise for every employee
    num_of_emps = 0       # counts how many employees were created

    def __init__(self, first, last, pay):
        # Instance variables: each employee has their own.
        self.first = first
        self.last = last
        self.pay = pay
        # Use the CLASS name: the count belongs to the company, not to one employee.
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def email(self):
        return f"{self.first}.{self.last}@company.com"

    def apply_raise(self):
        # self.raise_amount: Python looks on the instance first, then the class.
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


if __name__ == "__main__":
    emp_1 = Employee("Corey", "Schafer", 50000)
    emp_2 = Employee("Test", "User", 60000)

    # Step 2: a method that changes the object's state
    print("Step 2: pay before/after raise")
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)                      # 52000

    # Step 4: one class variable, read three ways
    print("\nStep 4: where does raise_amount live?")
    print(Employee.raise_amount)          # 1.04
    print(emp_1.raise_amount)             # 1.04 (found on the class)
    print(emp_2.raise_amount)             # 1.04 (found on the class)
    print(emp_1.__dict__)                 # no raise_amount here: it's on the class

    # Step 5: setting it on ONE instance creates a new instance variable
    print("\nStep 5: emp_1.raise_amount = 1.05")
    emp_1.raise_amount = 1.05
    print(Employee.raise_amount)          # 1.04 (class unchanged)
    print(emp_1.raise_amount)             # 1.05 (emp_1's own copy wins)
    print(emp_2.raise_amount)             # 1.04 (still reads the class)
    print(emp_1.__dict__)                 # now raise_amount IS here

    # Step 6: a class variable as a shared counter
    print("\nStep 6: number of employees")
    print(Employee.num_of_emps)           # 2