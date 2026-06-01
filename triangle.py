def is_triangle(a, b, c):
    """
    Check if three values can form a valid triangle.
    A valid triangle requires:
    1. All sides must be positive numbers
    2. The sum of any two sides must be greater than the third side
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)
