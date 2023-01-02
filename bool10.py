from math import sqrt


def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    n = sqrt(a)
    return n % (int(n)) == 0


print(main(623))
