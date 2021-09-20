import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):

    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""

    valid_triangles = [
        (1, 1, 1),
        (3, 4, 5),
        (3, 4, 6),
        (8, 10, 12),
        (100, 101, 200),
        (0.9, 1.0, 1.1)
    ]
    not_valid_triangles = [
        (21, 10, 10),
        (2, 1, 1),
        (6, 10, 4),
        (6, 20, 4)
    ]
    def test_valid_triangle(self):
        for a, b, c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue(is_triangle(a, b, c), msg)

    def test_not_triangle(self):
        for a, b, c in self.not_valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertFalse(is_triangle(a, b, c), msg)

    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""
        with self.assertRaises(ValueError):
            b2 = is_triangle( 1, 0, 2)
            b1 = is_triangle(-1, 2, 2)

        with self.assertRaises(ValueError):
            b2 = is_triangle( 1, 0, 2)
            b1 = is_triangle( 1, -1, 2)

        with self.assertRaises(ValueError):
            b2 = is_triangle( 1, 2,  0)
            b1 = is_triangle(1, 2, -1)
        with self.assertRaises(ValueError):
            b2 = is_triangle( 0, 0, 0)
            b1 = is_triangle(-1, -1, -1)
    def test_c_greater_than_other(self):
        self.assertFalse(is_triangle(10, 10, 21))
        self.assertFalse(is_triangle(10, 11, 24))