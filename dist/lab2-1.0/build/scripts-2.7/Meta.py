class MyMetaClass(type):
    def __new__(cls, name, bases, clsdict):
        filename = clsdict['filename']
        with open(filename, 'r+') as fl:
            for line in fl:
                st = line.split()
                clsdict[st[0]] = st[1]
        del clsdict['filename']
        return super(MyMetaClass, cls).__new__(cls, name, bases, clsdict)


class Pup():
    __metaclass__ = MyMetaClass
    filename = 'args.txt'
    deep = 5
 
if __name__ == "__main__":
    pup = Pup()
    pupa = Pup()
    print(dir(pup))
    print pup.deep
    print pupa.deep
    print pup.color