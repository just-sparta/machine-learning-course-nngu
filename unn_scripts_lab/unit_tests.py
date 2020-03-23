import unittest
import polynomial


class TestPolynomial(unittest.TestCase):

    def test_add_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 + p2, polynomial.Polynomial([1, 3, -1]))

    def test_add_polynom_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = polynomial.Polynomial(1, 2)
        self.assertEqual(p1 + p2, polynomial.Polynomial(1, 3, -1))

    def test_add_const(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial([1, 2, -2]))

    def test_add_const_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial(1, 2, -2))

    def test_sub_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 - p2, polynomial.Polynomial([1, 1, -5]))

    def test_sub_polynom_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = polynomial.Polynomial(1, 2)
        self.assertEqual(p1 - p2, polynomial.Polynomial(1, 1, -5))

    def test_sub_const(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial([1, 2, -2]))

    def test_sub_const_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial(1, 2, -2))

    def test_mul_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 * p2, polynomial.Polynomial([1, 4, 1, -6]))

    def test_mul_polynom_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = polynomial.Polynomial(1, 2)
        self.assertEqual(p1 * p2, polynomial.Polynomial(1, 4, 1, -6))

    def test_mul_const(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = 1
        self.assertEqual(p1 * p2, polynomial.Polynomial([1, 2, -3]))

    def test_mul_const_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = 1
        self.assertEqual(p1 * p2, polynomial.Polynomial(1, 2, -3))

    def test_non_eq_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 == p2, False)

    def test_eq_polynom(self):
        p1 = polynomial.Polynomial([1, 2])
        p2 = polynomial.Polynomial([1, 2])
        self.assertFalse(p1 != p2)

    def test_eq_const(self):
        p1 = polynomial.Polynomial([1])
        p2 = 1
        self.assertEqual(p1, p2)

    def test_copy_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial(p1)
        self.assertEqual(p1, p2)

    def test_neg_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = p1.__neg__()
        self.assertEqual(p1 * (-1), p2)

    def test_derivative(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial([2, 2])
        self.assertEqual(p1.derivative(), p2)

    def test_string(self):
        p1 = polynomial.Polynomial([1, 1, 1, 1, 1])
        p2 = p1.__str__()
        self.assertEqual('x^4 + x^3 + x^2 + x + 1', p2)

    def test_string_tuple(self):
        p1 = polynomial.Polynomial(1, 1, 1, 1, 1)
        p2 = p1.__str__()
        self.assertEqual('x^4 + x^3 + x^2 + x + 1', p2)

    def test_string_2(self):
        p1 = polynomial.Polynomial([5, 5, -5, -5, 1])
        p2 = p1.__str__()
        self.assertEqual('5x^4 + 5x^3 - 5x^2 - 5x + 1', p2)

    def test_string_2_tuple(self):
        p1 = polynomial.Polynomial(5, 5, -5, -5, 1)
        p2 = p1.__str__()
        self.assertEqual('5x^4 + 5x^3 - 5x^2 - 5x + 1', p2)


if __name__ == '__main__':
    unittest.main()
