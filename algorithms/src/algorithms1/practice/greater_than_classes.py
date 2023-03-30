
from abc import ABC

class Person(ABC):
    age:int
    name: str



if __name__ == "main":

    p1 = Person()
    p1.age =34
    p1.name = "luis"
    print(p1)