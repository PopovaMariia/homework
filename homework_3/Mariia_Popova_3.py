x = input()
y = input()
try:
    x = int(x)
    y = int(y)
    if x <= y:
        while x <= y:
            if x%5 == 0:
                print(x)
            x += 1
    else:
        while y <= x:
            if x%5 == 0:
                print(x)
            x -= 1
except ValueError:
    print('Please use the integer number')







