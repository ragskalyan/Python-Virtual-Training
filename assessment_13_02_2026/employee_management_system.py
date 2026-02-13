"""
Employee Management System

Goal: Practice Inheritance and Encapsulation
"""

class Employee:

    def __init__(self, name, base_salary):
        self.__name = name
        self.__base_salary = base_salary


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value):
        self.__base_salary = value

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay()")