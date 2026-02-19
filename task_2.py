def task2() -> None:
    '''
    Reads an integer n from standard input.
    If n == 0, prints 0 and returns.
    Otherwise reads n lines of space-separated words and prints the number
    of words that appear in every line (the intersection of all lines).
    '''
    num_lines = int(input())
    if num_lines == 0:
        print(0)
        return
    courses = set(input().split())
    for i in range(num_lines - 1):
        courses &= set(input().split())
    print(len(courses))
