class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class Popa(object):
    __metaclass__ = Singleton
    size = 24

if __name__ == "__main__":
    a = Popa()
    a.size = 32
    b = Popa()
    print b.size