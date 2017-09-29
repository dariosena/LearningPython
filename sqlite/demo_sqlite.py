import sqlite3
from employee import Employee

# In memory
conn = sqlite3.connect(':memory:')

# Save file employee.db
# conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
             first text,
             last text,
             pay integer
             )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_name(lastname):
    with conn:
        c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first':emp.first, 'last':emp.last, 'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last", {'first':emp.first, 'last':emp.last})


emp_1 = Employee('Xiun', 'Jia', '10000')
emp_2 = Employee('Ah Xi', 'Jia', '30000')
emp_3 = Employee('Xiu', 'Ling', '20000')

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

emps = get_emps_name('Jia')
print(emps)

update_pay(emp_2, 55000)
remove_emp(emp_1)

emps = get_emps_name('Jia')
print(emps)


################################################################################
################################################################################

# FIRST FORM
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# SECOND FORM
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_1.first, 'last':emp_1.last, 'pay':emp_1.pay})

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_3.first, 'last':emp_3.last, 'pay':emp_3.pay})

# Danger: SQL INJECTION
c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

c.execute("INSERT INTO employees VALUES ('Emanuel', 'Sena', 48000)")
c.execute("INSERT INTO employees VALUES ('Sophia', 'Sena', 58000)")
#
conn.commit()

c.execute("SELECT * FROM employees WHERE last='Ling'")
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Sena'})
print(c.fetchall())

conn.close()
