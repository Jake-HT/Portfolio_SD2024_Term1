import random

class Car:
    make = 'Delicious'
    model = 'Kai'
    year = 2023

    def __init__(car, make,model,year):
        car.make = make
        car.model = model
        car.year = year
        
    def __del__(car):
        print("Successfully scrapped {0} {1} from {2}!".format(car.make,car.model,car.year))

    def start_engine(car):
        rnd = int(random.randrange(1,10))
        print("Attempting to start {0} {1} from {2}...".format(car.make, car.model, car.year))
        if rnd < 8:
            print("Engine has started successfully.")
        else:
            print("The engine has failed to start!")

class Person:
    name = ''
    age = ''

    def __init__(person, name, age):
        person.name = name
        person.age = age

    def __del__(person):
        print("{0} has been dealt with accordingly, boss. They were only {1} years old you know...".format(person.name,person.age))

car1 = Car('Cardinal','Pope',2004)
car2 = Car('Delicious','Kai',2005)
car3 = Car('Remington','Ratrace',1998)

car1.start_engine()
car2.start_engine()
car3.start_engine()

del car1
del car2
del car3

John = Person("John Doe",18)

del John
