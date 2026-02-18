def task6() -> None:
    '''
    Prints all three-digit numbers 'hod' from 100 to 333 (inclusive)
    such that the number 'mat = hod * 3' uses exactly the same six digits
    as 'hod' and 'mat' combined, with all six digits being distinct.
    Output format: hod+hod+hod=mat
    '''
    for hod in range(100, 334):
        mat = hod * 3
        digits = str(hod) + str(mat)
        if len(set(digits)) == 6:
            print(f'{hod}+{hod}+{hod}={mat}')