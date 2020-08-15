import string
import random

def generator(password_lenght=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(password_lenght))
