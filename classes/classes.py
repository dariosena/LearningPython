class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee {:d}.".format(Employee.empCount))

    def displayEmployee(self):
        print("Name : {0}, Salary: {1}.".format(self.name, self.salary))


emp1 = Employee("fayaz", 3000)
emp2 = Employee("kha", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print("total Employees: {:d}".format(Employee.empCount))
