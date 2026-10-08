"""Dataclasses: a class that writes __init__, __repr__ and __eq__ for you.
Read: https://docs.python.org/3/library/dataclasses.html (first example + field() only)

Run (from learning-lab/):  python drill/oop/dataclasses_basics.py

Steps:
  Step 1. Write a normal class Point with __init__(self, x, y) only.
          Print Point(1, 2) and Point(1, 2) == Point(1, 2).
          Question: what do you see, and why is the == result surprising?
  Step 2. Write the same thing as a dataclass:
              from dataclasses import dataclass
              @dataclass
              class Point2: x and y with type hints (x: int, y: int)
          Print Point2(1, 2) and Point2(1, 2) == Point2(1, 2).
          Question: which three methods did @dataclass write for you?
  Step 3. Make an Employee dataclass: first: str, last: str, pay: int = 50000.
          Add a normal method email(self) and a @property fullname.
          Question: can a dataclass still have methods and properties?
  Step 4. Add skills: list[str] with a default of an empty list.
          Try "skills: list[str] = []" first and read the error.
          Then fix it with field(default_factory=list).
          Question: which OOP 4 trap is Python protecting you from?
  Step 5. Use @dataclass(frozen=True) on Point2 and try p.x = 10.
          Question: what happens, and when would you want that?
"""
from dataclasses import dataclass, field
import string
import random
from unicodedata import name

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass(frozen=True)  # makes data immutable (read-only)
class Person:
    name: str
    address: str
    active: bool = True
    email_address: list[str] = field(default_factory=list) 
    id: str = field(init=False, default_factory=generate_id) 
    _search_string: str = field(init=False)

    def __post_init__(self) -> None:
        # frozen blocks self.x = ..., so set it directly (standard idiom for frozen dataclasses)
        object.__setattr__(self, "_search_string", f"{self.name} {self.address} {self.email_address}")

    
def main() -> None:
    person = Person(name = "John Doe", address = "123 Main St")
#     person.name = 'kise'  # This will raise an error because the dataclass is frozen
    print(person.__repr__())
    print(person.__eq__(Person(name = "John Doe", address = "123 Main St")))

if __name__ == "__main__":
   main()