import math # Problema arreglado
from typeguard import typechecked
from math_fun import *


"""
Clase para crear números complejos y puntos polares
"""

class Numero_Complejo:
    @typechecked
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def __add__(self, other):
        if isinstance(other, Numero_Complejo):
            x = self.x + other.x
            y = self.y + other.y
            return Numero_Complejo(x, y)
        elif isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            return Numero_Complejo(x, self.y)

    def __sub__(self, other):
        if isinstance(other, Numero_Complejo):
            x = self.x - other.x
            y = self.y - other.y
            return Numero_Complejo(x, y)
        elif isinstance(other, int) or isinstance(other, float):
            x = self.x - other
            return Numero_Complejo(x, self.y)

    def __mul__(self, other):
        if isinstance(other, Numero_Complejo):
            x = (self.x * other.x) - (self.y * other.y)
            y = (self.x * other.y) + (self.y * other.x)
            return Numero_Complejo(x, y)
        elif isinstance(other, int) or isinstance(other, float):
            return Numero_Complejo(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Numero_Complejo):
            x = ((self.x * other.x) + (self.y * other.y) / (other.x ** 2 + other.y ** 2))
            y = ((self.y * other.x) + (self.x * other.y) / (other.x ** 2 + other.y ** 2))
            return Numero_Complejo(x, y)
        elif isinstance(other, int) or isinstance(other, float):
            return Numero_Complejo(self.x / other, self.y / other)

    def __neg__(self):
        return self * (-1)

    def __invert__(self):
        x = self.x / ((self.x ** 2) + (self.y ** 2))
        y = -self.y / ((self.x ** 2) + (self.y ** 2))
        return Numero_Complejo(x, y)

    def __pow__(self, power, modulo=None):
        n = Numero_Complejo(1, 0)
        if power > 0:
            for i in range(power):
                n *= self
            return n
        elif power < 0:
            n = ~self
            for i in range(abs(power)):
                n *= self
            return n
        elif power == 0:
            return n

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def arg(self):
        return math.degrees(math.atan2(self.y, self.x))

    def conj(self):
        return Numero_Complejo(self.x, -self.y)

    def complejo_polar(self):
        if not isinstance(self, Numero_Complejo):
            raise Exception("Introduce un número complejo")
        else:
            r = abs(self)
            a = self.arg()
            return Punto_Polar(r, a)

    def rad(self, power):
        z = self.complejo_polar()
        r = raiz(z.Distancia, power)
        for k in range(power):
            a = (z.Angulo / power) + (2 * k * 180 / power)
            print(Punto_Polar(r, a))

    def __str__(self):
        if self.x == 0 and self.y != 0:
            if self.x == 0 and self.y == 1:
                return "i"
            elif self.x == 0 and self.y == -1:
                return "-i"
            else:
                return "{}i".format(self.y)
        elif self.x != 0 and self.y == 0:
            return "{}".format(self.x)
        elif self.x == 0 and self.y == 0:
            return "0"
        elif self.y < 0:
            if self.y == -1:
                return "{} - i".format(self.x)
            elif self.y == 1:
                return "{} + i".format(self.x)
            else:
                return "{} - {}i".format(self.x, abs(self.y))
        else:
            if self.y == -1:
                return "{} - i".format(self.x)
            elif self.y == 1:
                return "{} + i".format(self.x)
            else:
                return "{} + {}i".format(self.x, self.y)


class Numero_Real(Numero_Complejo):
    def __init__(self, numero):
        super().__init__(numero, 0)

    def __str__(self):
        return "{}".format(super().__str__())


class Imaginario_Puro(Numero_Complejo):
    def __init__(self, numero):
        super().__init__(0, numero)

    def __str__(self):
        return "{}".format(super().__str__())


class Punto_Polar:
    @typechecked
    def __init__(self, Distancia: float, Angulo: float):
        self.Distancia = Distancia
        Angulo = self.redondeo(Angulo)
        self.Angulo = math.radians(Angulo)

    @property
    def Distancia(self):
        return self.__Distancia

    @property
    def Angulo(self):
        return self.__Angulo

    @Distancia.setter
    def Distancia(self, value):
        self.__Distancia = value

    @Angulo.setter
    def Angulo(self, value):
        self.__Angulo = value

    def redondeo(self, value):
        while value >= 360:
            value -= 360
        if value < 0:
            while value <= -360:
                value += 360
            value = 360 + value
        return value

    def __mul__(self, other):
        r = self.Distancia * other.Distancia
        a = math.degrees(self.Angulo) + math.degrees(other.Angulo)
        return Punto_Polar(r, a)

    def __neg__(self):
        return Punto_Polar(self.Distancia, math.degrees(self.Angulo) + 180)

    def __truediv__(self, other):
        r = self.Distancia / other.Distancia
        a = math.degrees(self.Angulo) - math.degrees(other.Angulo)
        return Punto_Polar(r, a)

    def __pow__(self, power, modulo=None):
        r = 1
        for i in range(power):
            r *= self.Distancia
        a = math.degrees(self.Angulo) * power
        return Punto_Polar(r, a)

    def __abs__(self):
        return self.Distancia

    def __invert__(self):
        z = self.polar_complejo()
        t = ~z
        return t.complejo_polar()

    def Moivre(self, power):
        r = self.Distancia ** power
        a = math.radians(math.degrees(self.Angulo) * power)
        x = math.cos(a)
        y = math.sin(a)
        return Numero_Complejo(r * x, r * y)

    def polar_complejo(self):
        if not isinstance(self, Punto_Polar):
            raise Exception("Introduce un punto polar")
        else:
            if math.degrees(self.Angulo) == 0.0:
                x = self.Distancia * 1
                y = self.Distancia * 0
                return Numero_Complejo(x, y)
            elif math.degrees(self.Angulo) == 90.0:
                x = self.Distancia * 0
                y = self.Distancia * 1
                return Numero_Complejo(x, y)
            elif math.degrees(self.Angulo) == 180.0:
                x = self.Distancia * (-1)
                y = self.Distancia * 0
                return Numero_Complejo(x, y)
            elif math.degrees(self.Angulo) == 270.0:
                x = self.Distancia * 0
                y = self.Distancia * (-1)
                return Numero_Complejo(x, y)
            else:
                x = self.Distancia * math.cos(self.Angulo)
                y = self.Distancia * math.sin(self.Angulo)
                return Numero_Complejo(x, y)

    def __str__(self):
        return "({}, {})".format(self.Distancia, math.degrees(self.Angulo))
