def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x1 = n % 10 
    # x2 = n % 100
    # x2 = x2 // 10
    # x = x1 == 0
    # y = x2 == 0

    return x1 > 0
print(main(10011))