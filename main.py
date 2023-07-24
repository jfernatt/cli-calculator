def get_numbers():
    while True:
        str_a = input('Provide number a: ')
        str_b = input('Provide number b: ')
        try:
            a = float(str_a)
            b = float(str_b)
        except Exception as e:
            print('Please try again...')
            continue
        else:
            return a, b


def add():
    a, b = get_numbers()
    print(f'{a} + {b} = {a + b}')
    return


def subtract():
    a, b = get_numbers()
    print(f'{a} - {b} = {a - b}')
    return


def multiply():
    a, b = get_numbers()
    print(f'{a} * {b} = {a * b}')
    return


def divide():
    a, b = get_numbers()
    print(f'{a} / {b} = {a / b}')
    return


def main():
    operations = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': quit}
    while True:
        selection = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")
        try:
            operations[selection]()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()