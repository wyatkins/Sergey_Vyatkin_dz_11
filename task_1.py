#!/usr/bin/env python3

class Date:
    __date: str

    def __init__(self, date: str) -> None:
        self.__date = date

    @staticmethod
    def is_valid(date: str):

        day: int
        month: int
        year: int

        try:
            day, month, year = Date.split_to_numb(date)
        except:
            return False

        if not 1 <= month <= 12:
            return False

        if not 0 <= year:
            return False

        if not 1 <= day <= 31:
            return False

        # test over 30
        if month in [4, 6, 9, 11] and day == 31:
            return False

        # test February
        if (
                month == 2 and
                day == 29 and
                year % 4 != 0 and
                year % 100 != 0 and
                year % 400 != 0
        ):
            return False

        return True

    @classmethod
    def split_to_numb(cls, date: str):
        try:
            return(list(map(int, date.split("-"))))
        except:
            raise ValueError("can't split by integer")