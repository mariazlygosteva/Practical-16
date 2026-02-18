from itertools import combinations

def task8() -> None:
    '''
    Reads a line of space-separated integers, extracts unique numbers,
    sorts them, and prints all possible subsets (including the empty subset).
    Each subset is printed on a separate line with elements separated by spaces.
    '''
    nums = sorted(set(map(int, input().split())))
    for i in range(len(nums) + 1):
        for comb in combinations(nums, i):
            print(' '.join(map(str, comb)))