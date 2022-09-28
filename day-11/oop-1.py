# Object Orientated Programming in Python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('bark')
    
    def add_one(self, x):
        return x + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

corgi = Dog("Millie", 20)
corgi.bark()
print(corgi.add_one(10))
print(type(corgi)) #type of millie object
print(corgi.get_name())
print(corgi.get_age())

beagle = Dog("Berlin", 30)
print(beagle.get_name())
print(beagle.get_age())
        

