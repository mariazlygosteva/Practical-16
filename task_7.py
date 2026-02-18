from itertools import permutations

def task7() -> None:
    '''
    Reads a line of space-separated integers, sorts them,
    and prints all possible permutations of the numbers.
    Each permutation is printed on a separate line,
    with numbers separated by spaces.
    '''
    numbers = list(map(int, input().split()))
    numbers.sort()
    for perm in permutations(numbers):
        print(' '.join(map(str, perm)))