import itertools

my_list = [1, 2, 3]

print('Combinations of 3 elements of {}:'.format(my_list))
combinations_three = itertools.combinations(my_list, 3)
for c in combinations_three:
    print(c)
print('\n')

print('Combinations of 2 elements of {}:'.format(my_list))
combinations_two = itertools.combinations(my_list, 2)
for c in combinations_two:
    print(c)
print('\n')

print('Permutations of 2 elements of {}:'.format(my_list))
permutations_two = itertools.permutations(my_list, 2)
for p in permutations_two:
    print(p)
print('\n')

print('Permutations of 3 elements of {}:'.format(my_list))
permutations_three = itertools.permutations(my_list, 3)
for p in permutations_three:
    print(p)
print('\n')
