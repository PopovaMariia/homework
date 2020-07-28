def validation(user_number):
    if not isinstance(user_number, (str, int)):
        return 'Fail'
    if isinstance(user_number, str) and user_number.isdigit():
        user_number = int(user_number)
        return
    return 'Fail'