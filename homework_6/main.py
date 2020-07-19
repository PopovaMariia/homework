import add, div, sub, mul

if __name__ == '__main__':
    value_1 = input('Value 1 ')
    symbol = input('Operation ')
    value_2 = input('Value 2 ')
    def calculate():
        if symbol == '+':
            add.add()
        elif symbol == '-':
            sub.sub()
        elif symbol == '*':
            mul.mul()
        elif symbol == '/':
            div.div()
        else:
            print('Please use mathematical symbol')
    try:
        value_1 = float(value_1)
        value_2 = float(value_2)
        calculate()
    except ValueError:
        print('Please use number')