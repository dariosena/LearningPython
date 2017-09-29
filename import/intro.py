import sys

sys.path.append('../my_modules')

# import my_module as mm
from my_module import find_index, test
# from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

print(test)

print(sys.path)
