def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a % 100
    x1 = x % 10
    x2 = x // 10
    x3 = a // 100

    y = x1+x2+x3

    return y %2 != 0
print(main(335))