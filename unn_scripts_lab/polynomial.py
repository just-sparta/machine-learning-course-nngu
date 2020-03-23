class Polynomial(object):

    def __init__(self, *coeffs):

        self.coefficients = []
        if isinstance(coeffs[0], (list, )):
            if not coeffs:
                self.coefficients = [0]
            else:
                for el in coeffs[0]:
                    if not isinstance(el, (int, float)):
                        raise ValueError('Incorrect polynomial parameters: Please enter int or float')
                else:
                    self.coefficients = coeffs[0]
        elif isinstance(coeffs[0], (Polynomial, )):
            self.coefficients = [c for c in coeffs[0].coefficients]
        else:
            for el in coeffs:
                if not isinstance(el, (int, float)):
                    raise ValueError('Incorrect polynomial parameters: Please enter int or float')
            self.coefficients = [c for c in coeffs]

        if self.coefficients:
            while len(self.coefficients) > 1 and self.coefficients[0] == 0:
                self.coefficients.pop(0)

    def is_empty(self):
        return len(self.coefficients) == 0

    def __repr__(self):
        return "Polynomial" + str(self.coefficients)

    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res

    @property
    def degree(self):
        return len(self.coefficients) - 1

    def __eq__(self, other):
        if isinstance(other, (int, float)) and self.degree == 0:
            return self.coefficients[0] == other
        elif isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        elif isinstance(other, str):
            return str(self) == other
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        res = []
        if isinstance(other, (int, float)):
            if self.coefficients:
                res = self.coefficients[:]
                res[-1] += other
            else:
                res = other
        elif isinstance(other, Polynomial):
            if self.degree > other.degree:
                res = self.coefficients[:]
                for i in range(0, other.degree + 1, 1):
                    res[self.degree - other.degree + i] += other.coefficients[i]
            else:
                res = other.coefficients[:]
                for i in range(0, self.degree + 1, 1):
                    res[other.degree - self.degree + i] += self.coefficients[i]
        else:
            raise TypeError('Adding: Incorrect functional arguments')

        return Polynomial(*res)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Polynomial([-coeff for coeff in self.coefficients])

    def __sub__(self, other):
        if isinstance(other, (int, float, Polynomial)):
            return self.__add__(-other)
        else:
            raise TypeError('Subtracting: Incorrect functional arguments')

    def __rsub__(self, other):
        return (self.__neg__()).__add__(other)

    def derivative(self):
        derived_coeffs = []
        exponent = len(self.coefficients) - 1
        for i in range(len(self.coefficients) - 1):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent -= 1
        return Polynomial(*derived_coeffs)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Polynomial([coeff * other for coeff in self.coefficients])
        elif isinstance(other, Polynomial):
            res = [0] * (self.degree + other.degree + 1)
            for self_pow, self_coeff in enumerate(self.coefficients):
                for arg_pow, arg_coeff in enumerate(other.coefficients):
                    res[self_pow + arg_pow] += self_coeff * arg_coeff
        else:
            raise TypeError('Multiplication: Incorrect functional arguments')
        return Polynomial(*res)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        res = ""
        res += str(self.coefficients[0]) + "x^" + str(self.degree)
        for i in range(1, len(self.coefficients) - 1):
            coeff = self.coefficients[i]
            if coeff < 0:
                res += " - " + str(-coeff) + "x^" + str(self.degree - i)
            else:
                res += " + " + str(coeff) + "x^" + str(self.degree - i)

        if self.coefficients[-1] < 0:
            res += " - " + str(-self.coefficients[-1])
        else:
            res += " + " + str(self.coefficients[-1])

        return res.replace('^1', '').replace('1x', 'x')


def main():
    print('Profit')


if __name__ == "__main__":
    main()
