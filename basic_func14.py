from math import floor
def main(a, b):
    '''find the floor division of a and b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    i = floor(a/b)
    return i
print(main(11 , 2))

