class Person:
    number_of_people = 0 #class attribute

    def __init__(self, name):
        self.name = name
        Person.add_person() #call the class method

    # accessible from Class based
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("roms")
p2 = Person("joy")

print(Person.number_of_people_())