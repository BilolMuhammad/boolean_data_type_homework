def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    if a == 0:
        return True
    elif a % (a//1) == 0:
        return True
    else:
        return False


print(main(4.5))
