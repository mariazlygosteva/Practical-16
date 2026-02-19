def task5() -> None:
    '''
    Reads an integer n from standard input.
    Prints all prime numbers from 2 to n-1 (inclusive) as a space-separated string.
    If n <= 2, prints an empty line.
    '''
    limit = int(input())
    if limit <= 2:
        print()
        return
    candidates = set(range(2, limit))
    for current in range(2, int(limit ** 0.5) + 1):
        if current in candidates:
            candidates -= set(range(current * current, limit, current))
    print(' '.join(map(str, sorted(candidates))))
