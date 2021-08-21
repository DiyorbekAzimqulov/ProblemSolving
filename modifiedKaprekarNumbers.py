# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
def is_karpekar(n):
    """
        defines wheter given number is karpekar number or not.
    """ 
    n_square = n**2
    len_of_n = len(str(n))
    l = str(n_square)[-(len_of_n):]
    r = str(n_square)[:-(len_of_n)]
    if r == '':
        r = 0
    if (int(l) + int(r) == n):
        return True
    return False

def kaprekarNumbers(p, q):
    # Write your code here
    interval = list(range(p, q+1))
    result = ''
    for i in interval:
        if is_karpekar(i):
            result += str(i) + ' '
    
    if result == '':
        print("INVALID RANGE ")
    else:
        print(result)
kaprekarNumbers(1, 100)