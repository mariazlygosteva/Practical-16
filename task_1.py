def task1() -> None:
    '''
    Reads a line of integers and a separate integer x from standard input.
    Prints 'YES' if x appears at least twice in the list of integers,
    otherwise prints 'NO'.
    '''
    sequence = list(map(int, input().split()))
    digit = int(input())
    seen_once, duplicates = set(), set()
    for number in sequence:
        if number in seen_once:
            duplicates.add(number)
        else:
            seen_once.add(number)
    print('YES' if digit in duplicates else 'NO')
