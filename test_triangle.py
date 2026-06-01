import unittest
from triangle import is_triangle


class TestIsTriangle(unittest.TestCase):

    # --- Valid triangles ---

    def test_equilateral_triangle(self):
        """All three sides equal"""
        self.assertTrue(is_triangle(5, 5, 5))

    def test_isosceles_triangle(self):
        """Two sides equal"""
        self.assertTrue(is_triangle(5, 5, 3))

    def test_scalene_triangle(self):
        """All sides different"""
        self.assertTrue(is_triangle(3, 4, 5))
        
    def test_large_valid_triangle(self):
    """Fixed: 1000,999,1 is degenerate; use 1000,999,2"""
    self.assertTrue(is_triangle(1000, 999, 2))
   
    def test_float_valid_triangle(self):
        """Float sides"""
        self.assertTrue(is_triangle(1.5, 2.5, 3.0))

    def test_minimum_valid_triangle(self):
        """Smallest reasonable valid triangle"""
        self.assertTrue(is_triangle(1, 1, 1))

    # --- Invalid triangles: degenerate (collinear) ---

    def test_degenerate_sum_equals_third(self):
        """Sum of two sides equals the third (degenerate triangle)"""
        self.assertFalse(is_triangle(1, 2, 3))

    def test_degenerate_reversed(self):
        """Degenerate case with different ordering"""
        self.assertFalse(is_triangle(3, 1, 2))

    def test_degenerate_all_same_check(self):
        """Another degenerate case"""
        self.assertFalse(is_triangle(5, 5, 10))

    # --- Invalid triangles: one side too long ---

    def test_one_side_too_long(self):
        """One side exceeds sum of other two"""
        self.assertFalse(is_triangle(1, 2, 10))

    def test_one_side_too_long_reordered(self):
        """Same case, different order"""
        self.assertFalse(is_triangle(10, 1, 2))

    def test_very_large_third_side(self):
        """Third side much larger"""
        self.assertFalse(is_triangle(1, 1, 100))

    # --- Invalid triangles: non-positive sides ---

    def test_zero_side(self):
        """A side of zero is invalid"""
        self.assertFalse(is_triangle(0, 4, 5))

    def test_negative_side(self):
        """A negative side is invalid"""
        self.assertFalse(is_triangle(-3, 4, 5))

    def test_all_zeros(self):
        """All zeros"""
        self.assertFalse(is_triangle(0, 0, 0))

    def test_all_negative(self):
        """All negative values"""
        self.assertFalse(is_triangle(-1, -2, -3))

    def test_two_zero_sides(self):
        """Two sides are zero"""
        self.assertFalse(is_triangle(0, 0, 5))

    # --- Float edge cases ---

    def test_float_degenerate(self):
        """Float degenerate case"""
        self.assertFalse(is_triangle(0.5, 0.5, 1.0))

    def test_float_invalid(self):
        """Float invalid triangle"""
        self.assertFalse(is_triangle(0.1, 0.2, 0.4))


if __name__ == '__main__':
    unittest.main()
