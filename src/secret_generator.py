import secrets
import string
import random


def aleatorio():
    # alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    # alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # operation = '+-=/*'
    # special_car = '!@#$%&()?;:.,~[{}]\\|'

    caracteres = string.ascii_letters + string.digits + string.punctuation

    return "".join(secrets.choice(caracteres))
len_pass=int(input("Tamanho da senha:"))
password = ''
for i in range(len_pass):
    password += aleatorio()
print(password)
