class Demo:
    def __init__(self):
        self._x = 0
    @property
    def x(self):
        print("Estoy en get")
        return self._x
    @x.setter
    def x(self, value):
        print("Estoy en set")
        self._x = value
    @x.deleter
    def x(self):
        del self._x
        
obj = Demo()
obj.x = 10
print(obj.x)


"""class A:
    def __init__(self, x, y, z):
        self.varX = x
        self._varY = y
        self.__varZ = z
    def demo(self):
        return f"ESTOY en A: x: {self.varX} -- y:{self._varY} --- z:{self.__varZ}"
class B(A):
    def __init__(self):
        super().__init__("x", "y", "z")
    def demo(self):
        return(super().demo())
        #return f"ESTOY en B: x: {super.varX} -- y:{super._varY} --- z:{super.__varZ}"
objB = B()
print(objB.demo())"""



"""class A():
    def __init__(self,n):
        self.n = n
    def funcion1(self):
        return ("Hola")

class B():
    def __init__(self,n):
        self.n = n
    def funcion1(self):
        return ("Chau")

class C():
    def __init__(self,n):
        self.n = n
    def funcion1(self):
         return ("Hasta la vista!")
    def saludo(self):
        #x = self.funcion1()
        x = super().funcion1()
        print(x)

class D(B, A, C):
    def __init__(self,a,b,c,d):
        A.__init__(self,a)
        B.__init__(self,b)
        C.__init__(self,c)
        self.n = d
    def funcion1(self):
         return ("Hasta la vista!")
    def saludo(self):
        #x = self.funcion1()
        x = super().funcion1()
        print(x)
    def giveN():
        a = super.n
        return(a)


objD = D("a","b","c","d")
print(objD.n)
"""