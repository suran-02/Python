#class example
class Dog:
    species = "Siberian Husky"
    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = Dog("Prince",2)
print("Name: " + dog1.name)
print("Age: " + str(dog1.age) + "y")
print("Species: "+dog1.species)

#Encapsulation
class BankAcc:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

acc = BankAcc(1000)
acc.deposit(4230)
print(acc.get_balance())

#Abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

c = Car()
c.start()
b = Bike()
b.start()

#Inheritance
#Single Inheritance
##Parent Class
class Person:
    def __init__(self,name,id_no):
        self.name = name
        self.id_no = id_no

    def display(self):
        print(f"Name: {self.name}, ID: {self.id_no}")

##creating an instance of Person
person = Person("Alice",101)
person.display()

##Child Class
class Employee(Person):
    def print_message(self):
        print("Employee class called")

##creating an instance of Employee
emp = Employee("Bob",102)
emp.display() #Calling the inherited method
emp.print_message() #Calling the child class method

#Multiple Inheritance:

class Mother:
  last_name_1 = "Nath"
class Father:
  last_name_2 = "Roy"

class Child(Mother,Father):
  last_name = Mother.last_name_1 + " " + Father.last_name_2
  def show_last_name(self):
      print(self.last_name)

c= Child()
c.show_last_name()


#Polymorphism

class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
#polymorphic behaviour
animals = [Dog(),Cat(),Animal()]
for a in animals:
    print(a.sound())

#Another example of Polymorphism

class UPI:
    def pay(self):
        print("Paying with UPI")


class Card:
    def pay(self):
        print("Paying with Card")


class Cash:
    def pay(self):
        print("Paying with Cash")


payments = [UPI(), Card(), Cash()]

for p in payments:
    p.pay()