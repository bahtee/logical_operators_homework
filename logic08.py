def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x = a % 2
    x = x ==0
    y = b % 2 
    y = y ==0    
    return x or y 
print(main(4,6)) 
