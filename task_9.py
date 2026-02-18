from itertools import combinations

def task9() -> None:
    '''
    Reads a line of space-separated integers and an integer k from standard input.
    Prints all subsets of size k from the unique sorted numbers.
    Each subset is printed on a separate line with elements separated by spaces.
    If k is out of range (k < 0 or k > number of unique numbers), prints nothing.
    '''
    numbers = list(map(int, input().split()))
    k = int(input())
    nums = sorted(set(numbers))
    if k < 0 or k > len(nums):
        return
    for comb in combinations(nums, k):
        print(' '.join(map(str, comb)))