import Field


class ModelCreator(type):
    def __call__(cls, *args, **kwargs):
        obj = super(ModelCreator, cls).__call__(*args)
        for (k, v) in kwargs.items():
            if not hasattr(obj, k):
                raise KeyError("{} field doesn't exist".format(k))
            attr = getattr(obj, k)
            if issubclass(attr.__class__, Field.Field):
                if not issubclass(v.__class__, attr.get_type()):
                    raise TypeError("Type of input value is not subclass of {}".format(attr.get_type()))
            setattr(obj, k, v)
        return obj


class Model(object):
    __metaclass__ = ModelCreator
    name = Field.StringField()
    num = Field.NumField()
    pip = 1


if __name__ == "__main__":
    model1 = Model(name="lala", pip=2)
    model2 = Model(name='popa')
    model3 = Model(num=5)
    model4=Model(name="lola",pop=3)

    print model1.pip, model4.pop, model3.name.default
