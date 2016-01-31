import types


class LinearFunction(object):

    def __init__(self, *args):
        self.coef = args

    def __add__(self, other):
        if not isinstance(other, LinearFunction):
            raise TypeError("Input argument is not LinearFunction")
        if len(self.coef) == len(other.coef):
            return LinearFunction(*[self.coef[i] + other.coef[i] for i in xrange(len(self.coef))])
        elif len(self.coef) < len(other.coef):
            res = [self.coef[i] + other.coef[i] for i in xrange(len(self.coef))] + list(other.coef[len(self.coef):])
            return LinearFunction(*res)
        else:
            res = [self.coef[i] + other.coef[i] for i in xrange(len(other.coef))] + list(self.coef[len(other.coef):])
            return LinearFunction(*res)

    def __call__(self, *args):
        if len(args) == len(self.coef) - 1:
            return self.coef[0] + sum([args[i]*self.coef[i+1] for i in xrange(len(self.coef)-1)])
        else:
            raise ValueError("Number of arguments is not equals number of dimentions")

    def __mul__(self, other):
        if isinstance(other, types.IntType) or isinstance(other, types.LongType)or isinstance(other, types.FloatType):
            return LinearFunction(*[c * other for c in self.coef])
        elif type(other) == LinearFunction:
            res = LinearFunction(self.coef[0])
            for i in xrange(len(self.coef)-1):
                res = res.__add__(LinearFunction(*[self.coef[i+1]*other.coef[k] for k in xrange(len(other.coef))]))
            return res
        else:
            raise TypeError("Input argument is not LinearFunction or numeric type")

    def __eq__(self, other):
        if isinstance(other, LinearFunction):
            if len(other.coef) == len(self.coef):
                return all([self.coef[i] == other.coef[i] for i in xrange(len(other.coef))])
        return False

    def __str__(self):
        res = '{}'.format(self.coef[0])
        for i in xrange(len(self.coef)-1):
            if self.coef[i+1] < 0:
                res += '{}x{}'.format(self.coef[i+1], i+1)
            else:
                res += '+{}x{}'.format(self.coef[i+1], i+1)
        return res



if __name__ == "__main__":
    f = LinearFunction(1, 2)
    g = LinearFunction(1, 2, -3,+3)

    print f, g
    print f + g
    print f(1)
    print f*2
    print f*g
    print g
    print g(1,2,2)
