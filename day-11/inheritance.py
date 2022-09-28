class Pet: # General Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont't know what I say")

class Cat(Pet): #Specific Class -> will inherit from Pet Class
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am {self.color}")

class Dog(Pet): #Specific Class
    def speak(self): # Overriding method from the upper class
        print("bark")

class Fish(Pet):
    pass


p = Pet("Millie", 10)
p.show()
p.speak()
c = Cat("Flurry", 29, 'black')
c.show()
c.speak()
d = Dog("Bill", 30)
d.show()
d.speak()

f = Fish("Dory", 0)
f.show()
f.speak()