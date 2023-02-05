from typing import Union

from logg import logging


def verification_nums(data: list, count: str, real_im = 0):
    while True:
        verif = [float(i) if "." in i else int(i) for i in data if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if len(verif) == 2:
            return verif
        else:
            logging.warning(f"Incorrect data entered: '{data[0]}', '{data[1]}'!")
            print(f"\n{'*' * 30}\n{'Try again!':^30}\n{'*' * 30}\n")
            match count:
                case '1':
                    data = [input(f"Enter {i + 1} number: ") for i in range(2)]
                case '2':
                    match real_im:
                        case 0:
                            data = [input(f"Enter 1 real part: "), input(f"Enter 1 imaginary number: ")]
                        case 1:
                            data = [input(f"Enter 2 real part: "), input(f"Enter 2 imaginary number: ")]

def ver_zero(data: str):
    while True:
        d = [float(i) if "." in i else int(i) for i in [data] if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if not (d and d[0]):
            print(f"\n{'*' * 50}\n{'You can t divide by zero! Try again!':^50}\n{'*' * 50}\n")
            logging.warning(f"Incorrect data entered: '{data}'!")
            data = input(f"Enter 2 number: ")
        else:
            return d[0]

def div_by_zero(data1: Union[int, float], data2: Union[int, float]):
    while True:
        try:
            data1 / data2
        except ZeroDivisionError:
            print(f"\n{'*' * 50}\n{'You can t divide by zero! Try again!':^50}\n{'*' * 50}\n")
            logging.warning(f"Incorrect data entered: '{data2}'!")
            data2 = complex(*verification_nums([input(f"Enter 2 real part: "), input(f"Enter 2 imaginary number: ")], "2", 1))
        else:
            return data2