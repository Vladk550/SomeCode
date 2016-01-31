import collections


class DefDict(dict):

    # def __init__(self, *args, **kwargs):
    #     dict.__init__(self, *args, **kwargs)
    #
    # def __getitem__(self, item):
    #     try:
    #         return dict.__getitem__(self, item)
    #     except:
    #         return self.__missing__(item)

    def __missing__(self, item):
        self[item] = DefDict()
        return self[item]


if __name__ == "__main__":
    dct = DefDict()
    dct['a'] = 1
    dct['b']['c'] = 2
    print dct
    print dct['v']
    print dct