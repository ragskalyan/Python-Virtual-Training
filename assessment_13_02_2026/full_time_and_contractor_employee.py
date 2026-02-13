"""
Full time employee class

"""
from assessment_13_02_2026.employee_management_system import Employee


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
        print("Full time Employee Class")

    def calculate_pay(self):
        total = self.base_salary + self.base_salary * 0.25
        return total


class ContractorEmployee(Employee):
    def __init__(self, name, base_salary, hourly_rate):
        super().__init__(name, base_salary)
        print("Contractor Employee Class")
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hourly_rate * self.base_salary





kalyan = FullTimeEmployee(name="kalyan", base_salary=100000)

print(
    kalyan.name,
    kalyan.calculate_pay()
)

thenu = ContractorEmployee(name="thenu", base_salary=500, hourly_rate=50)

print(
    thenu.name,
    thenu.base_salary,
    thenu.calculate_pay()
)




