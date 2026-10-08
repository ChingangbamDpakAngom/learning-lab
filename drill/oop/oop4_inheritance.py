"""Corey Schafer, Python OOP Tutorial 4: Inheritance - Creating Subclasses.
Video: https://www.youtube.com/watch?v=RSl87lqOXDE

Run (from learning-lab/):  python drill/oop/oop4_inheritance.py

Steps (code along with the video):
  Step 1. Copy the Employee class from oop3_class_static_methods.py
          (raise_amt, __init__, fullname, apply_raise, from_string).
  Step 2. Make an empty subclass: class Developer(Employee): pass
          Create dev_1 = Developer('Corey', 'Schafer', 50000) and print dev_1.email.
          Question: Developer has no __init__, so where did email come from?
  Step 3. Give Developer its own raise_amt = 1.10. Apply a raise to dev_1 and
          to an Employee, and compare.
          Question: why does Developer use 1.10 but Employee still uses 1.04?
  Step 4. Give Developer an __init__(self, first, last, pay, prog_lang).
          Use super().__init__(first, last, pay), then set self.prog_lang.
          Question: what does super() save you from writing?
  Step 5. Make class Manager(Employee) with a list of employees and methods
          add_emp, remove_emp and print_emps.
          Tip: use None as the default, never [] (mutable default trap).
  Step 6. Print isinstance(mgr_1, Employee), isinstance(mgr_1, Developer),
          issubclass(Developer, Employee).
  Step 7 (link to OOP 3). Create dev_2 = Developer.from_string('Jane-Doe-90000')
          after Step 2 and print type(dev_2).
          Question: why is it a Developer and not an Employee?
"""


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
     def __init__(self, first, last, pay, employees=None):
          super().__init__(first, last, pay)
          if employees is None:
              self.employees = []
          else:
               self.employees = employees


     def add_emp(self, emp):
         if emp not in self.employees:
          self.employees.append(emp)
     
     def remove_emp(self, emp):
         if emp in self.employees:
          self.employees.remove(emp)

     def print_emps(self):
         for emp in self.employees:
           print('-->', emp.fullname())

if __name__ == "__main__":

        dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
        dev_2 = Developer('Test', 'Employee', 60000, 'java')

        mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

        print(mgr_1.email)

        mgr_1.add_emp(dev_2)
        mgr_1.print_emps()


        print(isinstance(mgr_1, Employee))  # True
        print(isinstance(mgr_1, Developer))  # False
        print(issubclass(Developer, Employee))  # True

        # print(dev_1.email)
        # print(dev_2.email)

        # # print(help(Developer))

        # print(dev_1.pay)
        # dev_1.apply_raise()
        # print(dev_1.pay)  # 52000



