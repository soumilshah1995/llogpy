from llogpy import logMethod,logClass


@logClass
class A(object):
    def __init__(self):
        pass

    def method(self):
        print(" I am a method ")


    def clsmethod(cls):
        print(" i am a class method ")


if __name__ == "__main__":
    obj = A()
    obj.method()
    obj.clsmethod()
