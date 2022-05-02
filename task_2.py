#!/usr/bin/env python3

class MyZeroDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input("input a: "))
        b = float(input("input b: "))
    except:
        print("incorrect input")
        exit(1)

    try:
        if b == 0:
            raise MyZeroDiv("We try div by zero")
        print(f"All is ok {a}/{b} = {a/b}")
    except MyZeroDiv as ex:
        print(ex)