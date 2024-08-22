class Mammal:
    def walk(self):
        print("Walk!!")

class Dog(Mammal):
    def bark(self):
        print("bark...")
class Cat(Mammal):
    pass

c = Cat()
c.walk()

d = Dog()
d.walk()