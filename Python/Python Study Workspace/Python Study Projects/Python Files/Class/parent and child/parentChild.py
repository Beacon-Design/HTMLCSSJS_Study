#!/usr/bin/env python3
#coding:utf-8

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Cinstructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Consturctor Called")
        Parent.__init__(self, last_name, eye_color )
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)
        print("Number of toys: " + str(self.number_of_toys))    # Methord Overriding


bill = Parent("Bill", "blue")
print(bill.last_name)

mike = Child("Mike", "Green", 4)
print(mike.last_name)
print(mike.number_of_toys)
mike.show_info()