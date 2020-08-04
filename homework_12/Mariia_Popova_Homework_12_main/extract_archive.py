def extract_archive(file_to_open, password):
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False
