def task4() -> None:
    '''
    Reads two lines of space-separated integers, converts each to a set,
    then reads a single integer x. Prints 'YES' if x belongs to both sets
    (i.e., x is in the intersection of the two sets), otherwise prints 'NO'.
    '''
    first_set = set(map(int, input().split()))
    second_set = set(map(int, input().split()))
    number = int(input())
    print('YES' if number in (first_set & second_set) else 'NO')
