def task4() -> None:
    '''
    Reads two lines of space-separated integers, converts each to a set,
    then reads a single integer x. Prints 'YES' if x belongs to both sets,
    otherwise prints 'NO'.
    '''
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    x = int(input())
    print('YES' if x in set1 and x in set2 else 'NO')