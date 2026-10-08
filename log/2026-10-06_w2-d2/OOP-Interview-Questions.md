# OOP Interview Questions (Corey 1–4, 6 + 4 pillars) · Classes, Instances, `self`, `__init__`

Basic questions that people *think* they know, then fumble in interviews.
How to use: read the question, **say your answer out loud**, then open the callout. Mark ✅ / ½ / ❌ below.

Levels: 🟢 screening call · 🟡 technical round · 🔴 follow-up probe

---

> [!question]- Q1 🟢 What's the difference between a class and an instance?
> A class is the **blueprint** (`Employee`). An instance is **one object built from it** (`emp_1`, `emp_2`). One class, many instances, each with its own data.

> [!question]- Q2 🟢 What is `self`?
> The **instance the method was called on**. In `emp_2.email()`, `self` *is* `emp_2`. It is **not** the class. Proof: `self is emp_2` → `True`.

> [!question]- Q3 🟡 Why do `emp_1.fullname()` and `Employee.fullname(emp_1)` give the same result?
> Methods live on the class. `emp_1.fullname()` is shorthand: Python rewrites it to `Employee.fullname(emp_1)` and passes the object in as `self` automatically.

> [!question]- Q4 🟡 What happens if you forget `self` in a method definition? *(most forgotten)*
> `def fullname():` then `emp_1.fullname()` → **`TypeError: fullname() takes 0 positional arguments but 1 was given`**. Python still passes the instance, and there's no parameter to receive it.

> [!question]- Q5 🔴 Is `self` a keyword? *(trick question)*
> **No.** It's only a convention (the first parameter of a method). `def fullname(me):` works. Always use `self` anyway: every Python developer expects it.

> [!question]- Q6 🟡 What does `__init__` do? Is it the constructor? *(trick question)*
> It **initialises** a new object: it sets its starting attributes. Strictly, it's not the constructor: `__new__` creates the object, then `__init__` fills it in. It runs automatically on `Employee("Corey", "Schafer", 50000)` and must return `None`.

> [!question]- Q7 🟡 Attribute or method: how do you choose?
> **Stored data → attribute** (`self.pay`). **Computed from other data → method** (`email()`, `fullname()`), so it stays correct if `first` changes. (Later: `@property` lets a method be read like an attribute.)

> [!question]- Q8 🔴 Two instances with the same values: is `emp_a == emp_b` True? *(most forgotten)*
> **No**, by default. Without `__eq__`, `==` falls back to identity, like `is`: two separate objects are not equal. `@dataclass` adds `__eq__` for you.

> [!question]- Q9 🟢 What does `print(emp_1)` show, and how do you change it?
> Something like `<__main__.Employee object at 0x...>`. Define `__repr__` (for developers) or `__str__` (for users) to control it.

> [!question]- Q10 🔴 Where are instance attributes stored?
> In each object's own dictionary: `emp_1.__dict__` → `{'first': 'Corey', 'last': 'Schafer', 'pay': 50000}`. That's why `emp_1` and `emp_2` don't share data.

## OOP 2 · Class variables

> [!question]- Q11 🟢 Instance variable vs class variable?
> Instance variable: set in `__init__` as `self.x`, one copy **per object** (`first`, `pay`). Class variable: set in the **class body**, outside any method, **shared** by all objects (`raise_amount`).

> [!question]- Q12 🟡 `emp_1.raise_amount` works, but `raise_amount` isn't in `emp_1.__dict__`. Why?
> Attribute lookup checks the **instance first, then the class** (first match wins). It's found on the class.

> [!question]- Q13 🔴 What happens after `emp_1.raise_amount = 1.05`? *(most forgotten)*
> It does **not** change the class. It creates a new **instance** variable on emp_1 that shadows the class one. `Employee.raise_amount` and `emp_2.raise_amount` stay 1.04.

> [!question]- Q14 🟡 Why `Employee.num_of_emps += 1` in `__init__`, not `self.num_of_emps += 1`?
> `self.num_of_emps += 1` reads the class value and then writes a new **instance** variable, so each object gets its own counter stuck at 1. A shared count must be updated through the **class name**.

> [!question]- Q15 🔴 Where must a class variable be defined? *(my own bug)*
> In the class body. `raise_amount = 1.04` inside `__init__` is just a **local variable**: it disappears when `__init__` ends, so `self.raise_amount` raises `AttributeError`.

## OOP 3 · classmethod and staticmethod

**Kid version (school):** class = the school, object = one student. `self` = "me", `cls` = "our school".
Normal method → about **me** ("my homework is done") · `@classmethod` → about **our school** ("the bell now rings at 9", or "a new student joins") · `@staticmethod` → about **neither** ("is Saturday a school day?").

> [!question]- Q16 🟢 When do you use a normal method, a classmethod and a staticmethod?
> Ask what the method needs. **One object's data** (`self`) → normal method. **The class** (`cls`): change shared class variables, or create objects another way → `@classmethod`. **Neither** → `@staticmethod`, a helper grouped in the class (`is_workday(day)`).

> [!question]- Q17 🟡 What is an alternative constructor, and why return `cls(...)` not `Employee(...)`?
> A classmethod that builds an object from another format: `Employee.from_string("John-Doe-70000")`. `cls` is whichever class called it, so `Developer.from_string(...)` returns a Developer. Hard-coding `Employee(...)` breaks subclasses.

> [!question]- Q18 🟡 Why did `Employee.set_raise_amt(1.05)` change emp_1 and emp_2, but `emp_1.raise_amt = 1.05` didn't change emp_2?
> The classmethod changes the **shared** class value; objects without their own copy read it. Assigning through an instance gives **only that object** its own copy.

## OOP 4 · Inheritance + `__repr__`

> [!question]- Q19 🟢 What does `super().__init__(first, last, pay)` save you?
> Re-writing the parent's setup (`self.first = first` …) in every subclass. Write it once in the parent; if the parent changes, every child gets the change.

> [!question]- Q20 🟡 Why does a Developer use `raise_amt = 1.10` but an Employee 1.04?
> Lookup order (the **MRO**): instance → Developer → Employee, first match wins. Developer defines its own, so it **overrides** the parent's. See `Developer.__mro__`.

> [!question]- Q21 🔴 Why `employees=None` and not `employees=[]`? *(classic trap)*
> A default `[]` is created **once**, when `def` runs, so every manager would **share the same list**. Use `None`, then make a fresh `[]` inside.

> [!question]- Q22 🟢 `isinstance` vs `issubclass`?
> `isinstance(mgr_1, Employee)` → is this **object** of that class (or a child)? True. `issubclass(Developer, Employee)` → is this **class** a child of that class? True.

> [!question]- Q23 🟡 `__str__` vs `__repr__`?
> `__str__` = readable, for **users** (`print`). `__repr__` = unambiguous, for **developers** (REPL, lists, logs), ideally `Employee('Corey', 'Schafer', 50000)`. If only one, write `__repr__`: `str()` falls back to it. Kid version: nickname vs passport name.

## OOP 6 · @property + the 4 pillars

> [!question]- Q24 🟢 What are the 4 pillars of OOP? *(asked in almost every OOP round)*
> **Encapsulation**: bundle data + methods, control access (`@property`, `_name`). **Abstraction**: hide details, force a contract (`ABC` + `@abstractmethod`). **Inheritance**: reuse parent code (`super()`). **Polymorphism**: same method, different behaviour (`shape.area()`).

> [!question]- Q25 🟡 Why use `@property` for `email` instead of setting it in `__init__`?
> A value computed in `__init__` is a **snapshot** that goes stale when `first` changes. A property **recomputes on every read**. Kid version: photo vs mirror. With `.setter` / `.deleter` you control writes and deletes too, while callers still use plain attribute syntax.

> [!question]- Q26 🔴 Does Python have private attributes?
> **No true private.** `_pay` = "internal" by convention. `__pay` triggers name mangling (`_Employee__pay`) but is still reachable. Use `@property` to control access.

> [!question]- Q27 🟡 Why can't you create `Shape()` if it has an `@abstractmethod`?
> `TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'`. An abstract class only **promises** the method; each subclass must implement it before it can be created. Kid version: a recipe title with no recipe.

> [!question]- Q28 🟡 Inheritance vs polymorphism?
> Inheritance = **reusing** parent code (`class Circle(Shape)`). Polymorphism = **same call, different behaviour** (the loop calls `.area()` without checking the type). Python also has **duck typing**: if it has the method, it works (`len()` on list, str, dict).

> [!question]- Q29 🟢 How should `__repr__` format values?
> Use `!r`: `f"Employee({self.first!r}, {self.last!r})"` → strings get quotes, `None` stays `None`.

---

**Common mistakes from my own drill:** VS Code auto-imports (`from turtle import shape` appeared by itself: delete unused imports) · use 4 spaces per level · `day.weekday == 5` (no brackets) compares the method itself → always False; use `day.weekday()` · `split('-')` returns strings, so convert `pay` with `int()` · imports go at the top of the file · calling a value like a method (`emp_1.raise_amount()` → `TypeError: 'float' object is not callable`) · calling a method twice changes state twice (`apply_raise` → 52000 then 54080) · unsaved VS Code edits (check for the ● on the tab; turn on Auto Save) · using `first` instead of `self.first` inside a method (it only exists in `__init__`) · thinking `self` is the class · calling a method that doesn't exist yet (`AttributeError`) · Git Bash eats `\` in paths, so use `/`.

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Attempt 1 | | | | | | | | | | | | | | | |
| Attempt 2 | | | | | | | | | | | | | | | |
