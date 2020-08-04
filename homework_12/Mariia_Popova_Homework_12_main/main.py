import zipfile
from password_generator import generator
from extract_archive import extract_archive


def hack_archive(file_name):
    file_to_open = zipfile.ZipFile(file_name)
    wrong_passwords = []
    tries = 0
    while True:
        password = generator()
        if extract_archive(file_to_open, password) == False:
            if password not in wrong_passwords:
                wrong_passwords.append(password)
                tries += 1
                continue
            continue
        break
    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


if __name__ == '__main__':
    hack_archive('archive.zip')
