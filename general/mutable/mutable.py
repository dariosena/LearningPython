
a = 'dario'
print(a)
print('Address of a is: {}'.format(id(a)))

a = 'john'
print(a)
print('Address of a is: {}'.format(id(a)))

# TypeError: 'str' object does not support item assignment
# a[0] = 'C'

a = [1, 2, 3, 4, 5]
print(a)
print('Address of a is: {}'.format(id(a)))

a[0] = 6
print(a)
print('Address of a is: {}'.format(id(a)))

employees = ['Corey', 'John', 'Rick', 'Steve', 'Carl', 'Adam']
output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Address of a is: {}'.format(id(output)))

output += '</ul>'

print(output)
print('\n')
