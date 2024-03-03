class Person:
    def __init__(person, name = "Jeff", age = 25):
        person.name = name
        person.age = age

class Skills:
    def __init__(skills, programming = "programming", communication = "communication"):
        skills.programming = programming
        skills.communication = communication

class Employee(Person,Skills):
    def __init__(employee,name,age,programming,communication):
        Person.__init__(employee,name,age)
        Skills.__init__(employee,programming,communication)

    def background(employee):
        print("Person: ", employee.name, employee.age)
        print("Person: ", employee.programming, employee.communication)

s1 = Employee("Jeff",25,"yeah","nah")
s1.background()