#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

import tempfile


def external_mergesort(file_name):
    fl = open(file_name, 'r+')
    n = 0
    while fl.readline():
        n += 1
    res = tempfile.TemporaryFile('r+')
    fl.seek(0)
    rd = fl.read()
    f = False
    res.write(rd)
    res.seek(0)
    while n > 1:
        fl_new1 = tempfile.TemporaryFile('r+')
        fl_new2 = tempfile.TemporaryFile('r+')

        for i in xrange(n):
            if i % 2 == 0:
                fl_new1.write(res.readline())
            else:
                fl_new2.write(res.readline())
        if n % 2 != 0:
            f = True

        fl_new1.seek(0)
        fl_new2.seek(0)

        res = tempfile.TemporaryFile('r+')
        n //= 2
        j = n

        while j > 0:
            a = list(map(lambda x: int(x), fl_new1.readline().split()))
            b = list(map(lambda x: int(x), fl_new2.readline().split()))
            l, r = 0, 0

            while l < len(a) and r < len(b):
                if a[l] < b[r]:
                    res.write(str(a[l]) + ' ')
                    l += 1

                else:
                    res.write(str(b[r]) + ' ')
                    r += 1

            while l < len(a):
                res.write(str(a[l]) + ' ')
                l += 1

            while r < len(b):
                res.write(str(b[r]) + ' ')
                r += 1
            res.write('\n')
            j -= 1
        if f:
            res.write(fl_new1.readline())
            f = False
            n += 1
        res.seek(0)

    res.seek(0)
    new = open('res.txt', 'w')
    for i in xrange(n):
        new.write(res.readline() + '\n')


if __name__ == "__main__":
    external_mergesort('numbers.txt')
