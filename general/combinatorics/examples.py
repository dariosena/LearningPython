import itertools

my_list = [1, 2, 3, 4, 5, 6]

combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

print([result for result in combinations if sum(result) == 10])

word = 'sample'
my_letters = 'plmeas'

permutations = itertools.permutations(my_letters, 6)
count = 0

for p in permutations:
    if ''.join(p) == word:
        print('Number of no matches: {}'.format(count))
        print('Match!')
        break
    else:
        count += 1
