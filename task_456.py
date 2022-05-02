#!/usr/bin/env python3

from abc import ABC


# Exceptions


class StoreExcept(Exception):
    pass


class EmptyStore(StoreExcept):
    pass


class WrongReq(StoreExcept):
    pass


class StrongFilter(StoreExcept):
    pass


# !Exceptions


class Store:
    __ID: int = 0
    __single = None
    __store_lst: list['Equip'] = []

    def __new__(cls):

        if not cls.__single:
            cls.__single = super(Store, cls).__new__(cls)

        return cls.__single

    @classmethod
    def add_equip(cls, *equips: 'Equip'):
        for equip in equips:
            equip.equip_id = cls.__ID
            cls.__ID += 1
            cls.__store_lst.append(equip)
            print(f"add {type(equip)} to store")

    @classmethod
    def filter_equip(cls, flt: 'EquipFilter') -> list['Equip']:

        if len(cls.__store_lst) == 0:
            raise EmptyStore()

        res = filter(lambda x: (type(x) is flt.equip_type), cls.__store_lst)

        # filter free equip
        res = filter(lambda x: x.user == "", res)

        for attr_flt in flt.attr_flts:
            res = filter(attr_flt, res)

        res = list(res)
        length = len(res)

        if length == 0 or length < flt.count:
            raise StrongFilter()

        if flt.count == 0:
            return list(res)

        return res[:flt.count]

    @classmethod
    def applue_req(cls, user_name: str, *equips: 'Equip'):

        for equip in cls.__store_lst:
            if equip in equips:
                equip.user = user_name


class EquipFilter:
    equip_type: 'type'
    count: int = 0
    attr_flts: list = []

    def __init__(self, equip_type, *filts, **kwargs) -> None:
        self.equip_type = equip_type
        self.count = kwargs.get("count", 0)
        self.attr_flts = list(filts)


class Equip(ABC):
    __equip_id: int = -1
    create_by: str = ""
    user: str = ""

    @property
    def equip_id(self):
        return self.__equip_id

    @equip_id.setter
    def equip_id(self, id_):
        if self.__equip_id == -1:
            self.__equip_id = id_


class Printer(Equip):
    ink: bool = False
    print_size: list[str] = []


class Shrader(Equip):
    page_size: list[str] = []


class Scanner(Equip):
    scan_size: list[str] = []


class Copper(Printer, Scanner):
    page_in_try: int = 0


def main():
    store = Store()

    # 3 printers

    p = [Printer() for _ in range(3)]

    p[0].create_by = "Sony"
    p[0].ink = True
    p[0].print_size.append("A4")
    p[0].print_size.append("A3")

    p[1].create_by = "Epson"
    p[1].ink = True
    p[1].print_size.append("A4")

    p[2].create_by = "Cannon"
    p[2].ink = False
    p[2].print_size.append("A3")

    # 1 Scanner

    s = Scanner()

    s.create_by = "Epson"
    s.scan_size.append("A4")

    # 2 Copper

    c = [Copper() for _ in range(2)]

    c[0].create_by = "Xerox"
    c[0].ink = True
    c[0].print_size.append("A4")
    c[0].scan_size.append("A3")
    c[0].page_in_try = 300

    c[1].create_by = "Xerox"
    c[1].ink = True
    c[1].print_size.append("A3")
    c[1].scan_size.append("A4")
    c[1].page_in_try = 300

    try:
        store.filter_equip(EquipFilter(Printer))
    except EmptyStore:
        print("Store is empty")

    store.add_equip(*c)
    store.add_equip(*p, s)

    try:
        print(store.filter_equip(EquipFilter(Printer, count=10)))
    except StrongFilter:
        print("Filter is strong")

    try:
        req = store.filter_equip(EquipFilter(Printer, lambda x: x.ink == True, count=1))
        print(*req)
        store.applue_req("company", *req)
        print(store.filter_equip(EquipFilter(Copper, lambda x: "A3" in x.scan_size)))
    except StrongFilter:
        print("Filter is strong")


if __name__ == "__main__":
    main()