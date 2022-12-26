def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """

    x = a < 0
    y = b < 0    
    return x or y 
print(main(3,8))    