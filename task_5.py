def task5() -> None:
    '''
    Reads an integer n from standard input.
    Prints all prime numbers from 2 to n-1 (inclusive) as a space-separated string.
    If n <= 2, prints an empty line.
    '''
    n = int(input())
    if n <= 2:
        print()
        return
    primes = set(range(2, n))
    for i in range(2, int(n ** 0.5) + 1):
        if i in primes:
            primes -= set(range(i * i, n, i))
    print(' '.join(map(str, sorted(primes))))