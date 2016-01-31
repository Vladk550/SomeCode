import unittest
import MyXrange
import random
import json_parser
import n_vector
from LinearFunction import LinearFunction
from Logger import SomeClass
from def_dict import DefDict
import Meta
import Cached
from Filter import Filter
from from_json import from_json
import types
from Singleton import Singleton
from ModelCreator import ModelCreator
from Field import StringField, NumField
from external_mergesort import external_mergesort

glbl = 15


@Cached.cached
def f(a, b):
    return a + b + glbl


def g(a, b):
    global glbl
    glbl += 1
    return a + b + glbl


class Tests(unittest.TestCase):
    def test_external_mergesort(self):
        nums = [random.randint(-100000, 100000) for _ in range(50)]
        with open('test_numbers.txt', 'w') as f:
            f.writelines('{}\n'.format(num) for num in nums)
        external_mergesort('test_numbers.txt')
        with open('test_numbers.txt', 'r') as f:
            nums.sort()
            self.assertItemsEqual((int(x) for x in f.readlines()), nums)

    def test_json_parser(self):
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

        popa = Popa()
        self.assertEqual(json_parser.to_json(popa),
                         '{"popa":"Nice", "kisa":{"whose":"My", "colors":[1, 2, 3], "fur":null}, "inds":[1, true, 12], "size":32}')
        self.assertEqual(json_parser.to_json(3), "3")

    def test_n_vector(self):
        a = n_vector.n_vector(1, 2, 3)
        b = n_vector.n_vector(1, 2, 3)
        self.assertTrue(a == b)
        self.assertEqual(a + b, n_vector.n_vector(2, 4, 6))
        self.assertEqual(a - b, n_vector.n_vector(0, 0, 0))
        self.assertEqual(a.scal_mul(b), 14)
        self.assertEqual(a.mul_const(2), a + b)
        with self.assertRaises(TypeError):
            a.mul_const("dfsdf")

    def test_LinearFunction(self):
        f = LinearFunction(1, 2)
        g = LinearFunction(1, 2, -3)
        self.assertEqual(f + g, LinearFunction(2, 4, -3))
        self.assertEqual(f * g, LinearFunction(3, 4, -6))
        with self.assertRaises(TypeError):
            f([1, 2, 3])

    def test_Logger(self):
        bl = SomeClass()
        bl.speak("I'm Batman")
        bl.scream("AAAAAAAAAAA")
        self.assertItemsEqual(bl.log, [
            """Method speak was called with lovely arguments ("I'm Batman", 1) I'm speaking. I'm Batman as a result was returned""",
            """Method scream was called with lovely arguments ('AAAAAAAAAAA',) I'm screaming. AAAAAAAAAAA as a result was returned"""])

    def test_def_dict(self):
        dct = DefDict()
        self.assertIsInstance(dct['a']['b']['f'], DefDict)
        with self.assertRaises(TypeError):
            dct[[]] = 0

    def test_meta_args(self):
        with open('test_args.txt', 'w') as f:
            f.write('\n'.join(['name lala', 'age 12']))

        class Pup():
            __metaclass__ = Meta.MyMetaClass
            filename = 'test_args.txt'

        pup = Pup()
        self.assertEqual(pup.name, 'lala')
        with self.assertRaises(AttributeError):
            pup.surname

    def test_cached(self):
        f(1, 1)
        g(1, 1)
        self.assertEqual(f(1, 1), 17)

    def test_MyXrange(self):
        self.assertItemsEqual([1, 2, 3], MyXrange.MyXrange(1, 4))
        with self.assertRaises(Exception):
            MyXrange.MyXrange(1, 4, 0)

    def test_filter(self):
        lst = [1, 2, 3, 1, 10]
        self.assertItemsEqual([x for x in Filter(lst, lambda x: x > 2)], [3, 10])

    def test_from_json(self):
        self.assertIsInstance(from_json('{"popa":"Nice", "kisa":{"whose":"My", "colors":[1, 2, 3], "fur":null}, "inds":[1, true, 12], "size":32}'),
                              types.DictionaryType)
        self.assertEqual(from_json('3'), 3)

    def test_singleton(self):
        class Popa(object):
            __metaclass__ = Singleton
            size = 24

        a = Popa()
        a.size = 32
        b = Popa()
        self.assertEqual(b.size, 32)

    def test_model_creator(self):
        class Model(object):
            __metaclass__ = ModelCreator
            name = StringField()
            num = NumField()

        model1 = Model(name="lala", num=2)

        self.assertEqual(model1.name, "lala")
        self.assertEqual(model1.num, 2)
        with self.assertRaises(TypeError):
            model = Model(name=0)
        with self.assertRaises(KeyError):
            model = Model(lala=1)

if __name__ == "__main__":
    unittest.main()