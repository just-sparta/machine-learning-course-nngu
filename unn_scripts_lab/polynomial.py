class Polynomial(object):

    def __init__(self, *coefficients):

        self.coeffs = []
        if isinstance(coefficients[0], (list, )):
            if not coefficients or coefficients == ([], ):
                self.coeffs = [0]
            else:
                for el in coefficients[0]:
                    if not isinstance(el, (int, float)):
                        raise ValueError('Incorrect polynomial parameters: Please enter int or float')
                else:
                    self.coeffs = coefficients[0]
        elif isinstance(coefficients[0], (Polynomial, )):
            self.coeffs = [c for c in coefficients[0].coeffs]
        else:
            if isinstance(coefficients[0], tuple):
                self.coeffs = list(coefficients[0])
                return
            for el in coefficients:
                if not isinstance(el, (int, float)):
                    raise ValueError('Incorrect polynomial parameters: Please enter int or float')
            self.coeffs = [c for c in coefficients]

        if self.coeffs:
            while len(self.coeffs) > 1 and self.coeffs[0] == 0:
                self.coeffs.pop(0)

    def is_empty(self):
        return len(self.coeffs) == 0

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def __call__(self, x):
        res = 0
        for coeff in self.coeffs:
            res = res * x + coeff
        return res

    @property
    def degree(self):
        return len(self.coeffs) - 1

    def __eq__(self, other):
        if isinstance(other, (int, float)) and self.degree == 0:
            return self.coeffs[0] == other
        elif isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        elif isinstance(other, str):
            return str(self) == other
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        res = []
        if isinstance(other, (int, float)):
            if self.coeffs:
                res = self.coeffs[:]
                res[-1] += other
            else:
                res = other
        elif isinstance(other, Polynomial):
            if self.degree > other.degree:
                res = self.coeffs[:]
                for i in range(0, other.degree + 1, 1):
                    res[self.degree - other.degree + i] += other.coeffs[i]
            else:
                res = other.coeffs[:]
                for i in range(0, self.degree + 1, 1):
                    res[other.degree - self.degree + i] += self.coeffs[i]
        else:
            raise TypeError('Adding: Incorrect functional arguments')

        return Polynomial(*res)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Polynomial([-coeff for coeff in self.coeffs])

    def __sub__(self, other):
        if isinstance(other, (int, float, Polynomial)):
            return self.__add__(-other)
        else:
            raise TypeError('Subtracting: Incorrect functional arguments')

    def __rsub__(self, other):
        return (self.__neg__()).__add__(other)

    def derivative(self):
        derived_coeffs = []
        exponent = len(self.coeffs) - 1
        for i in range(len(self.coeffs) - 1):
            derived_coeffs.append(self.coeffs[i] * exponent)
            exponent -= 1
        return Polynomial(*derived_coeffs)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Polynomial([coeff * other for coeff in self.coeffs])
        elif isinstance(other, Polynomial):
            res = [0] * (self.degree + other.degree + 1)
            for self_pow, self_coeff in enumerate(self.coeffs):
                for arg_pow, arg_coeff in enumerate(other.coeffs):
                    res[self_pow + arg_pow] += self_coeff * arg_coeff
        else:
            raise TypeError('Multiplication: Incorrect functional arguments')
        return Polynomial(*res)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        res = ""
        if self.degree == 0:
            return str(self.coeffs[0])
        else:
            first_sign = f"{'-' if self.coeffs[0] < 0 else ''}"
            no_one = f"{'' if abs(self.coeffs[0]) == 1 else abs(self.coeffs[0])}"
            res += first_sign + no_one + "x" + f"{'' if self.degree == 1 else '^' + str(self.degree)}"

            for i in range(1, len(self.coeffs) - 1):
                coeff = self.coeffs[i]
                degree = self.degree - i

                if coeff == 0:
                    continue

                if coeff < 0:
                    res += " - " + f"{'' if abs(coeff) == 1 else abs(coeff)}" + \
                           "x" + f"{'' if degree == 1 else '^' + str(degree)}"
                else:
                    res += " + " + f"{'' if abs(coeff) == 1 else abs(coeff)}" + \
                           "x" + f"{'' if degree == 1 else '^' + str(degree)}"

            if self.coeffs[-1] == 0:
                return res

            if self.coeffs[-1] < 0:
                res += " - " + str(-self.coeffs[-1])
            else:
                res += " + " + str(self.coeffs[-1])

            return res


def main():
    print('Profit')


if __name__ == "__main__":
    main()
