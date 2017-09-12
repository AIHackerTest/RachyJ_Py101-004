## Animal is-a object, a base class
class Animal(object):
    ## a placeholder when a statement is required syntactically, but no code needs to be executed
    pass

## Dog is a class, inherit Animal
class Dog(Animal):
    def __init__(self, name):
        ## dog has a name
        self.name = name
        print("The dog name is %s" % name)

## cat is a class, inherit Animal
class Cat(Animal):
    def __init__(self, name):
        ## cat has a name
        self.name = name
        print("The cat name is %s" % name)

## person is a base class
class Person(object):
    def __init__(self, name):
        ## person has a name
        self.name = name

        ## set the default value to None
        self.pet = None
        print("The name of the person is %s" % name)
        #print("He/She has a pet %s" % name.pet)

## empoyee is a type of person
class Employee(Person):
    def __init__(self, name, salary):
        ## run the init method of its parent class - Person
        super(Employee, self).__init__(name)
        ##
        self.salary = salary
        print("%s earns how much each year" % name)
        print(salary)

## fish is an object
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## halibut is a fish
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")


## Mary's pet is satan
mary.pet = satan

print("He/She has a pet %s" % mary.pet.name)

## frank is an employee with salary 120000
frank = Employee("Frank", 120000)

## frank has a rover as pet
frank.pet = rover

print("He/She has a pet %s" % frank.pet.name)

## flipper is a kind of fish
flipper = Fish()

## crouse is a kind of Salmon
crouse = Salmon()

## harry is a kind of halibut
harry = Halibut()
