def task1() -> None:
    '''
    Reads a line of integers and a separate integer x from standard input.
    Prints 'YES' if x appears at least twice in the list of integers,
    otherwise prints 'NO'.
    '''
    a = list(map(int, input().split()))
    x = int(input())
    s, d = set(), set()
    for i in a:
        if i in s:
            d.add(i)
        else:
            s.add(i)
    print('YES' if x in d else 'NO')