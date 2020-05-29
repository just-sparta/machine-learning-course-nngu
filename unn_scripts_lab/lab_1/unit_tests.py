import unittest
from lab_1 import polynomial


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

    def test_copy_polynom_tuple(self):
        p1 = polynomial.Polynomial(1, 2, -3)
        p2 = polynomial.Polynomial(p1)
        self.assertEqual(p1, p2)

    def test_copy_polynom_edit_coeffs(self):
        p1 = polynomial.Polynomial([1, 2, 4])
        p2 = polynomial.Polynomial(p1)
        p2.coeffs[0] = 100
        self.assertNotEqual(p1, p2)

    def test_neg_polynom(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = p1.__neg__()
        self.assertEqual(p1 * (-1), p2)

    def test_neg_polynom_2(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = -p1
        self.assertEqual(p1 * (-1), p2)

    def test_const_sub_left(self):
        p1 = polynomial.Polynomial([1, 2, 3])
        p2 = 1
        self.assertEqual((p1 - p2).coeffs, [1, 2, 2])

    def test_const_sub_right(self):
        p1 = polynomial.Polynomial([1, 2, 3])
        p2 = 1
        self.assertEqual((p2 - p1).coeffs, [-1, -2, -2])

    def test_derivative(self):
        p1 = polynomial.Polynomial([1, 2, -3])
        p2 = polynomial.Polynomial([2, 2])
        self.assertEqual(p1.derivative(), p2)

    def test_string(self):
        p1 = polynomial.Polynomial([1, 1, 0, 1, 1])
        p2 = p1.__str__()
        self.assertEqual('x^4 + x^3 + x + 1', p2)

    def test_string_zeros(self):
        p1 = polynomial.Polynomial([1, 0, 0, 1, 1])
        p2 = p1.__str__()
        self.assertEqual('x^4 + x + 1', p2)

    def test_string_zeros_2(self):
        p1 = polynomial.Polynomial([1, 1, 0, 0, 0])
        p2 = p1.__str__()
        self.assertEqual('x^4 + x^3', p2)

    def test_string_zeros_3(self):
        p1 = polynomial.Polynomial([1, -1, 0, -1, -1])
        p2 = p1.__str__()
        self.assertEqual('x^4 - x^3 - x - 1', p2)

    def test_string_zeros_4(self):
        p1 = polynomial.Polynomial([0, -1, 0, -1, 0])
        p2 = p1.__str__()
        self.assertEqual('-x^3 - x', p2)

    def test_string_zeros_5(self):
        p1 = polynomial.Polynomial([0, 0, 0, 0, 0])
        p2 = p1.__str__()
        self.assertEqual('0', p2)

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

    def test_add_polynom_null(self):
        p1 = polynomial.Polynomial([0, 0, 1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 + p2, polynomial.Polynomial([1, 3, -1]))

    def test_add_polynom_tuple_null(self):
        p1 = polynomial.Polynomial(0, 0, 1, 2, -3)
        p2 = polynomial.Polynomial(1, 2)
        self.assertEqual(p1 + p2, polynomial.Polynomial(1, 3, -1))

    def test_add_const_null(self):
        p1 = polynomial.Polynomial([0, 0, 1, 2, -3])
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial([1, 2, -2]))

    def test_add_const_tuple_null(self):
        p1 = polynomial.Polynomial(0, 0, 1, 2, -3)
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial(1, 2, -2))

    def test_sub_polynom_null(self):
        p1 = polynomial.Polynomial([0, 0, 1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 - p2, polynomial.Polynomial([1, 1, -5]))

    def test_sub_polynom_tuple_null(self):
        p1 = polynomial.Polynomial(0, 0, 1, 2, -3)
        p2 = polynomial.Polynomial(1, 2)
        self.assertEqual(p1 - p2, polynomial.Polynomial(1, 1, -5))

    def test_sub_const_null(self):
        p1 = polynomial.Polynomial([0, 0, 1, 2, -3])
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial([1, 2, -2]))

    def test_sub_const_tuple_null(self):
        p1 = polynomial.Polynomial(0, 0, 1, 2, -3)
        p2 = 1
        self.assertEqual(p1 + p2, polynomial.Polynomial(1, 2, -2))

    def test_mul_polynom_null(self):
        p1 = polynomial.Polynomial([0, 0, 1, 2, -3])
        p2 = polynomial.Polynomial([1, 2])
        self.assertEqual(p1 * p2, polynomial.Polynomial([1, 4, 1, -6]))

    def test_mul_polynom_tuple_null(self):
        p1 = polynomial.Polynomial(0, 0, 1, 2, -3)
        p2 = polynomial.Polynomial(1, 2)
        self.assertEqual(p1 * p2, polynomial.Polynomial(1, 4, 1, -6))

    def test_mul_const_null(self):
        p1 = polynomial.Polynomial([0, 0, 1, 2, -3])
        p2 = 1
        self.assertEqual(p1 * p2, polynomial.Polynomial([1, 2, -3]))

    def test_can_modify_coefficients(self):
        p1 = polynomial.Polynomial([2, 2, 4])
        p1.coeffs[0] -= 1
        p1.coeffs[1] -= 1
        self.assertEqual(p1, polynomial.Polynomial([1, 1, 4]))

    def test_string_3(self):
        self.assertEqual('-1', str(polynomial.Polynomial([-1])))

    def test_string_3_with_zero(self):
        self.assertEqual('0', str(polynomial.Polynomial([])))

    def test_zero_mul(self):
        p1 = polynomial.Polynomial([1, 4, 5])
        p2 = 0
        self.assertEqual((p2 * p1).coeffs, [0])

    def test_mul_with_empty_polinomial(self):
        p1 = polynomial.Polynomial([])
        p2 = 5
        self.assertEqual((p2 * p1).coeffs, [0])

    def test_coefficients(self):
        coefficients = [1, 1, 3]
        p1 = polynomial.Polynomial(coefficients)
        self.assertEqual(coefficients, p1.coeffs)

    def test_coefficients_tuple(self):
        coefficients = (1, 1, 3)
        p1 = polynomial.Polynomial(coefficients)
        self.assertEqual(list(coefficients), p1.coeffs)


if __name__ == '__main__':
    unittest.main()
