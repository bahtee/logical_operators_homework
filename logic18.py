def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a % 10 
    x2 = a % 100
    x2 = x2 // 10
    x3 = a % 1000
    x3 = x3 // 100
    x4 = a % 10000
    x4 = x4 // 1000
    x5 = a // 10000
    
    return x5 < x4 < x3 < x2 < x1
print(main(12347))
    