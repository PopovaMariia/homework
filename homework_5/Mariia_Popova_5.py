def func(var_a, var_b):
    if type(var_a) == str or type(var_b) == str:
        print('str')
    elif var_a > var_b:
        print('>')
    elif var_a == var_b:
        print('=')
    elif var_a < var_b:
        print('<')

func('123',456)
func(456, 123)
func(123, 123)
func(123,456)

