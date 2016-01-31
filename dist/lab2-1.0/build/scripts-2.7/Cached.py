#!C:\Python27\python.exe
# -*- coding: utf-8 -*-


def cached(function):
    dct = dict()

    def wraper(*args):
        if args in dct:
            return dct[args]
        else:
            res = function(*args)
            dct[args] = res
            return res
    return wraper


@cached
def fibonacci(n):
    a = 0
    b = 1
    while n > 2:
        a, b = b, a+b
        n -= 1
    return b

if __name__ == "__main__":
    print fibonacci(10**3)
    print fibonacci(10**3)
