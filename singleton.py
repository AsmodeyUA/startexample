class Singleton1(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("Here")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton1, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __new__(mcs, *args, **kwargs):
        print("HereN")
        return super().__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("HereI")
        super().__init__(*args, **kwargs)


#Python3
class MyClass(metaclass=Singleton1):
    def __init__(self):
        print("II")
        super().__init__()

    def __new__(cls):
        print("NN")
        return super().__new__(cls)


class Singleton():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance,Singleton):
            cls._instance = super(Singleton, cls).__new__(cls, *args,**kwargs)
        return cls._instance



def main():
    a = MyClass()
    b = MyClass()
    print(a)
    print(b)
    a.g=7
    print(a.g)
    print(b.g)
    c=MyClass()
    print(c)
    print(c.g)


if __name__ == "__main__":
    main()

