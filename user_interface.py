from excep import *
from mod_calc import *
from logg import logging

type_dict = {'1': 'rational', '2': 'complex'}
operator = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^", "6": "sqrt"}

def menu():
    print('Hello!\n')
    while True:
        type_num = input('\n'
                              'Select the type of number:   \n'
                              '* 1 - rational numbers       \n'
                              '* 2 - rational numbers       \n'
                              '* 3 - exit                   \n'
                              '_______________________      \n'
                              'Choice:                      \n')       
        match type_num:
            case '1' | '2':
                calc_menu(type_num)
            case '3':
                logging.info('Stop program.')
                print('Bye')
                break
            case _:
                logging.error('Error')
                print('Error, this option is not in the menu, please, try again')

def calc_menu(data_type):
    global operator
    logging.info(f"Start calc menu. With {type_dict[data_type]}.")
    num1, num2 = 0, 0
    result = 'q'
    sign = '/'
    while True:
        operation = input('\n'
                          'Choose the operation:    \n'
                          '* 1 - sum                \n'
                          '* 2 - diff               \n'
                          '* 3 - mult               \n'
                          '* 4 - div                \n'
                          '* 5 - pow                \n'
                          '* 0 - Back to menu       \n'
                          '_______________________  \n'
                          'Your choice:             \n')
        
        if operation.isdigit() and int(operation) in range(1, 5):
            if data_type == '1':
                num1, num2 = verification_nums([input(f"Enter {i + 1} number: ") for i in range(2)], data_type)
            elif data_type == '2':
                num1, num2 = [complex(verification_nums([input(f"Enter {i + 1} real part: "),
                                                    input(f"Enter {i + 1} imaginary number: ")], data_type, i))
                                 for i in range(2)]
        match operation:
            case '1':
                result = sum_data(num1, num2)
            case '2':
                result = diff_data(num1, num2)
            case '3':
                result = mult_data(num1, num2)
            case '4':
                if data_type == '1':
                    num2 = ver_zero(str(num2))
                    sign = menu_divisions()
                    operator[operation] = sign
                else:
                    num2 = div_by_zero(num1, num2)
                    operator[operation] = "/"
                if sign:
                    result = div_data(num1, num2)
            case '5':
                result = pow_data(num1, num2 = None)
            case '0':
                logging.info('Stop calc menu')
                print()
                break
            case _:
                logging.error('Error')
                print('Error, try again')
                continue
        if result != "q":
            print(f"Res: {num1} {operator[operation]} {num2} = {result}", end="\n\n") 
               
def menu_divisions():
    logging.info(f"Start menu divisions.")
    while True:
        operation = input("Operations:\n"
                   "1 - '/'\n"
                   "2 - '//'\n"
                   "3 - '%'\n"
                   "4 - previous menu\n")
        match operation:
            case "1":
                return "/"
            case "2":
                return "//"
            case "3":
                return "%"
            case "4":
                logging.info('Stop divisions menu')
                print()
                return 0
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("Error. Try again")
