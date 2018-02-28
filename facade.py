

class Facade:
    def __init__(self):
        self._service1 = Service1()
        self._service2 = Service2()

    def calculate(self):
        return self._service1.operation1(5) + \
               self._service1.operation2(4) + \
               Service2.operation1(4) + \
               self._service2.operation2(2)


class Service1:
    def operation1(self, a):
        return a
    def operation2(self, a):
        return a

class Service2:
    @staticmethod
    def operation1(a):
        return a

    def operation2(self, a):
        return a


f = Facade()
print (f.calculate())