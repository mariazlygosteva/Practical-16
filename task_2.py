def task2() -> None:
    '''
    Reads an integer n from standard input.
    If n == 0, prints 0 and returns.
    Otherwise reads n lines of space-separated words and prints the number
    of words that appear in every line (the intersection of all lines).
    '''
    n = int(input())
    if n == 0:
        print(0)
        return
    common = set(input().split())
    for i in range(n - 1):
        common &= set(input().split())
    print(len(common))