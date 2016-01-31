class Filter:
    def __init__(self, iterable, filter_function):
        self.iterable = iterable
        self.filter_function = filter_function
        self.iter = None

    def __iter__(self):
        #self.iter = iter(self.iterable)
        for elem in self.iterable:
            if self.filter_function(elem):
                yield elem
        #return self

    # def next(self):
    #     elem = next(self.iter)
    #     while not self.filter_function(elem):
    #         elem = next(self.iter)
    #
    #     return elem


if __name__ == "__main__":
    lst = [1, 2, 3, 1, 10]
    fn = lambda x: x > 2
    new = [x for x in Filter(lst, fn)]
    print new