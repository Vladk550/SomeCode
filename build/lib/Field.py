import types
class Field(object):
    def __init__(self):
        self.default = None

    def get_type(self):
        return type(self.default)


class StringField(Field):
    def __init__(self):
        self.default = ''

    def get_type(self):
        return basestring


class NumField(Field):
    def __init__(self):
        self.default = 0

    def get_type(self):
        return (float, int, long)
