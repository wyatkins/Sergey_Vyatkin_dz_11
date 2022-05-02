#!/usr/bin/env python3

class NoAllNumb(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":

    lst = []
    while True:
        try:
            inp = input()
            if inp == "stop":
                break
            elif not inp.isdigit():
                raise NoAllNumb()
            else:
                lst.append(int(inp))
        except NoAllNumb:
            print("You are input not a number")

    print(*lst)