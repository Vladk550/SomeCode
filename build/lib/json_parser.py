#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import types
import json

class Kisa():
    def __init__(self):
        self.whose = "My"
        self.colors = [1, 2, 3]
        self.fur = None


class Popa():
    def __init__(self):
        self.popa = "Nice"
        self.size = 32
        self.inds = [1, True, 12]
        self.kisa = Kisa()

    def getSize(self):
        return self.size


def to_json(obj):
    isList = False
    inst = False
    nums = (types.FloatType, types.IntType, types.LongType)
    if isinstance(obj, types.ListType) or isinstance(obj, types.TupleType):
        res = '['
        isList = True
    elif type(obj) in nums:
        res = '{}  '.format(obj)
    elif isinstance(obj, types.StringType):
        res = '"' + obj + '"  '
    elif isinstance(obj, types.DictionaryType):
        inst = True
        dct = obj
        res = '{'
    else:
        inst = True
        dct = obj.__dict__
        res = '{'
    items = []
    if isList:
        items = obj
    elif inst:
        items = dct.keys()
    for attr in items:
        if not isList:
            res += '"{}":'.format(attr)
            item = dct[attr]
        else:
            item = attr
        if isinstance(item, types.BooleanType):
            if item:
                res += 'true'
            else:
                res += 'false'

        elif type(item) in nums:
            res += "{}".format(item)
        elif isinstance(item, types.StringType):
            res += '"{}"'.format(item)
        elif isinstance(item, types.NoneType):
            res += 'null'
        elif isinstance(item, types.ListType):
            res += to_json(item)
        else:
            res += to_json(item)
        res += ', '
    res = res[:len(res) - 2]
    if isList:
        res += ']'
    elif inst:
        res += '}'
    return res

if __name__ == "__main__":
    kisa = Kisa()
    popa = Popa()
    dct = {'a': 1, 'b': 2}
    print to_json(popa)
    print to_json(3)
    print to_json((1,2,3))
    print json.dumps(3)
    print json.dumps((1,2,3))
    print to_json("lala")
    print json.dumps("lalal")
    print json.dumps(dct)
    print to_json(dct)
    print json.loads('"lala"')