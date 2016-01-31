import math

class MyXrange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.end = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            if args[2] == 0:
                raise ValueError("Step can't be zero")
            self.step = args[2]

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError()
        i = self.start + item * self.step
        return i

    def __iter__(self):
        i = 0
        while i < len(self):
            yield self.__getitem__(i)
            i += 1

    def __len__(self):
        return int(math.fabs((self.end - self.start)//self.step))


if __name__ == "__main__":
    xrng = MyXrange(10, 2, 1)

    for i in xrng:
        print '{}'.format(i)
