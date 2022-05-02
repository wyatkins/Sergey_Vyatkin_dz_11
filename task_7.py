from math import e, sqrt

class Complex:
    __real: float
    __img: float

    @property
    def real(self):
        return self.__real

    @property
    def img(self):
        return self.__img

    @real.setter
    def real(self, new_real):
        if new_real.__class__ is int or new_real.__class__ is float:
            self.__real = new_real
        else:
            raise ValueError(f"{new_real.__class__} can't be real")

    @img.setter
    def img(self, new_img):
        if new_img.__class__ is int or new_img.__class__ is float:
            self.__img = new_img
        else:
            raise ValueError(f"{new_img.__class__} can't be img")

    def __init__(self, __real: float = 0, __img: float = 0) -> None:
        self.__real = __real
        self.__img = __img

    def __str__(self) -> str:
        return f"{self.__real}{' + ' if self.__img >= 0 else ' - '}{'{'}{abs(self.__img)}{'}'}"

    def __add__(self, other):
        return self.__add__sub__(other, func=lambda x, y: x + y)

    def __sub__(self, other):
        return self.__add__sub__(other, func=lambda x, y: x - y)

    def __iadd__(self, other):
        result = self.__add__sub__(other, func=lambda x, y: x + y)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __isub__(self, other):
        result = self.__add__sub__(other, func=lambda x, y: x - y)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __imul__(self, other):
        result = self.__mul__(other)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __itruediv__(self, other):
        result = self.__mul__(other)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __bool__(self):
        return self.__img != 0 and self.__real != 0

    def __mul__(self, other):
        if other.__class__ is int or other.__class__ is float:
            return Complex(__real=self.__real * other, __img=self.__img * other)
        elif other.__class__ is Complex:
            return Complex(
                __real=self.__real * other.__real - self.__img * other.__img,
                __img=self.__real * other.__real + self.__img * other.__img
            )
        else:
            raise ValueError(f"No implement __add__ with {other.__class__}")

    def __truediv__(self, other):
        if other.__class__ is int or other.__class__ is float:
            return self / Complex(other)
        elif other.__class__ is Complex:
            div = other.__real ** 2 + other.__img ** 2
            return Complex(
                __real=(self.__real * other.__real + self.__img * other.__img) / div,
                __img=(self.__img * other.__real - self.__real * other.__img) / div
            )
        else:
            raise ValueError(f"No implement __add__ with {other.__class__}")

    def __abs__(self):
        return sqrt(self.__real ** 2 + self.__img ** 2)

    def __add__sub__(self, other, func):
        if other.__class__ is int or other.__class__ is float:
            return Complex(__real=func(self.__real, other), __img=self.__img)
        elif other.__class__ is Complex:
            return Complex(__real=func(self.__real, other.__real), __img=func(self.__img, other.__img))
        else:
            raise ValueError(f"No implement __add__ with {other.__class__}")