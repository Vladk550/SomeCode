import math


class n_vector(object):
    def __init__(self, *coords):
        self._vector = coords
        self._dimensions = len(coords)

    def __add__(self, other):
        if type(other) == n_vector and len(self._vector) == len(other):
            new = [self._vector[i] + other[i] for i in xrange(self._dimensions)]
            return n_vector(*new)
        else:
            raise ValueError("Dimensions of vectors isn't equal")

    def __sub__(self, other):
        if type(other) == n_vector and len(self._vector) == len(other):
            new = [self._vector[i] - other[i] for i in xrange(self._dimensions)]
            return n_vector(*new)
        else:
            raise ValueError("Dimensions of vectors isn't equal")

    def mul_const(self, const):
        if isinstance(const, (int, float, long)):
            return n_vector(*[self._vector[i] * const for i in xrange(self._dimensions)])  # &&&&&????????????
        else:
            raise TypeError("Argument should be int, float, long")

    def __mul__(self, other):
        if type(other) == n_vector and len(self._vector) == len(other):
            return sum([self._vector[i] * other[i] for i in xrange(self._dimensions)])
        else:
            raise ValueError("Dimensions of vectors isn't equal")

    def __eq__(self, other):
        if type(other) == n_vector and len(self._vector) == len(other):
            return False not in [self._vector[i] == other[i] for i in xrange(self._dimensions)]
        else:
            return False

    def __len__(self):
        return self._dimensions

    def len(self):
        return math.sqrt(sum([i ** 2 for i in self._vector]))

    def __getitem__(self, item):
        return self._vector[item]

    def __str__(self):
        return str(self._vector)


if __name__ == "__main__":
    a = n_vector(1, 2, 3)
    b = n_vector(1, 2, 3)
    print a, b
    print a + b
    print a - b
    print a.mul_const(2)
    print a * b
    print a == b
    print a.len()
    print a[1]
    print len(a)
    print n_vector.__dict__
