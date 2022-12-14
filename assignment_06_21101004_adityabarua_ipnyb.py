# -*- coding: utf-8 -*-
"""Assignment 06_21101004_AdityaBarua.ipnyb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-DQN0chFclbqlvtgHp-ZtSch9MhTkqIO
"""

#Task-01
class Student:
    ID = 0

    def __init__(self,name,department,age,cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa

    @classmethod
    def from_String(cls,var):
        a = var.split('-')
        return cls(a[0],a[1],a[2],a[3])

    def get_details(self):
        Student.ID += 1
        print("ID:",Student.ID)
        print("Name:",self.name)
        print("Department:",self.department)
        print("Age:",self.age)
        print("CGPA:",self.cgpa)

        
s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()

class A:
    temp = 4
    def __init__(self):
        self.y = self.temp - 2
        self.sum = self.temp + 1
        A.temp -= 2
        self.methodA(3, 4)
    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + (self.temp)
        A.temp += 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
    
class B:
    x = 0
    def __init__(self, b = None):
        self.y, self.temp, self.sum = 5, -5, 2
 
        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
    def methodA(self, m, n):
        x = 2
        self.y = self.y + m + (self.temp)
        self.temp += 1
        x = x + 5 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)

a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1,2)
b2.methodB(3,2)

#Task-02
class Assassin:
    counter = 0

    def __init__(self,name,rate):
        self.name = name
        self.rate = rate 
        Assassin.counter += 1
    @classmethod
    def failureRate(cls,name,rate):
        return cls(name, 100 - rate)
    @classmethod
    def failurePercentage(cls,name,rate):
        return cls(name, 100 - rate)

    def printDetails(self):
        print("Name:",self.name)
        print("Success rate:",self.rate,"%")
        print("Total number of Assassin:",Assassin.counter)

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage('Akabane', 10)
akabane.printDetails()

#Task-03
class Passenger:
    count = 0

    def __init__(self,name):
        self.name = name
        self.basefare = 450
        Passenger.count += 1

    def set_bag_weight(self,weight):
        self.weight = weight
        if self.weight <= 20 :
            self.basefare = 450
        elif self.weight >= 21 and self.weight <= 50 :
             self.basefare += 50
        elif self.weight > 50 :
            self.basefare += 100

    def printDetail(self):
        print("Name:",self.name)
        print("Bus Fare:",self.basefare)
        
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)

#Task-04
class Travel:
    count = 0

    def __init__(self,source,destination):
        self.source = source
        self.destination = destination
        self.time = 1.00
        Travel.count += 1

    def set_time(self,x):
        self.time = x

    def set_source(self,y):
        self.source = y 

    def set_destination(self,z):
        self.destination = z

    def display_travel_info(self):
        time = "{:.2f}".format(self.time)
        return f"Source: {self.source} \n Destination: {self.destination} \n Flight Time: {time}"

print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)

#Task-05
class Employee:
    def __init__(self,name,workingPeriod):
        self.name = name
        self.workingPeriod = workingPeriod

    @classmethod
    def employeeByJoiningYear(cls,name,year):
        workingPeriod = 2021 - year
        return cls(name, workingPeriod)
    @staticmethod
    def experienceCheck(workingPeriod,gender):
        if gender == "male":
            if workingPeriod < 3 :
                return "He not is experienced"
            else:
                return "He is experienced"
        elif gender == "female":
            if workingPeriod < 3 :
                return "She is not experienced"
            else:
                return "She is experienced"

employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))

#Task-06
class Laptop:
    laptopCount = 0
    def __init__(self,name,count):
        self.name = name
        self.count = count
        Laptop.laptopCount += self.count

    @classmethod
    def advantage(cls):
        print('Laptops are portable')

    @classmethod 
    def resetCount(cls):
        Laptop.laptopCount = 0
        return Laptop.laptopCount




lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)

#Task-07
class Cat:
    Number_of_cats = 0
    def __init__(self,color,action):
        self.color = color 
        self.action = action
        Cat.Number_of_cats += 1

    def changeColor(self,newColor):
        self.color = newColor
    def printCat(self):
        print(self.color," cat is ",self.action)

    @classmethod
    def no_parameter(cls):
        return cls("White","sitting")

    @classmethod
    def first_parameter(cls,newColor):
        return cls(newColor,"sitting")
    
    @classmethod
    def second_parameter(cls,newAction):
        return cls("Gray",newAction)

print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)

#Task-08
import math

class Cylinder:
     radius = 5
     height = 18
     def __init__(self,radius,height):
         self.radius = radius
         self.height = height
         print("Default radius=",Cylinder.radius,"and","height=",Cylinder.height)
         print("Updated radius=",self.radius,"and","height=",self.height)

     @staticmethod
     def area(r,h):
        Cylinder.radius = r
        Cylinder.height = h
        area = 2* math.pi*r*r + 2*math.pi*r*h
        print("Area:",area)

     @staticmethod
     def volume(r,h):
        Cylinder.radius = r
        Cylinder.height = h
        volume = math.pi*r*r*h
        print("Volume:",volume)
    
     @classmethod
     def swap(cls,r,h):
        return cls(r,h)

     @classmethod
     def changeFormat(cls,var):
        x = var.split("-")
        return cls(float(x[0]), float(x[1]))


c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)

#Task-09
class Student:
    ts = 0
    bs = 0
    os = 0
    def __init__(self,name,department,varsity = "BRAC"):
        self.name = name
        self.department = department
        self.varsity = varsity
        Student.ts += 1
        if varsity == "BRAC":
            Student.bs += 1
        else:
            Student.os += 1
    @classmethod
    def createStudent(cls,name,department,varsity = "BRAC"):
        return cls(name,department,varsity)

    def individualDetail(self):
        print("name:",self.name)
        print("department:",self.department)
        print("Institution:",self.varsity)

    @classmethod
    def printDetails(cls):
        print("total student:",Student.ts)
        print("BRAC University Student(s)::",Student.bs)
        print("Other Institution Student(s):",Student.os)

Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against DarkArts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()