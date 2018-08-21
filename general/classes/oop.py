# Python Object-Oriented Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

emp_str_1 = 'Jonh-Doe-70000'
new_emp = Employee.from_string(emp_str_1)
print(new_emp.email)
print(new_emp.pay)

print(emp1.email)
print(emp2.email)

print('{} {}'.format(emp1.first, emp1.last))

print(emp2.fullname())
print(Employee.fullname(emp2))

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)

Employee.set_raise_amount(1.06)
#emp2.raise_amount = 1.06
print(emp2.raise_amount)

# print(Employee.__dict__)

print(Employee.num_of_emps)
