def task3() -> None:
    '''
    Reads a line of space-separated sweets (the ones the user has),
    then reads an integer n, and n lines of space-separated sweets that friends have.
    Prints the number of sweets that the user has but none of the friends have.
    '''
    sweet = set(input().split())
    n = int(input())
    friends = set()
    for i in range(n):
        friends |= set(input().split())
    only_sweet = sweet - friends
    print(len(only_sweet))