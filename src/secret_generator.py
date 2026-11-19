import secrets
import string


len_pass = int(input("Tamanho da senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation

password = ""
password += "".join(secrets.choice(caracteres) for _ in range(len_pass))

print(f"Sua senha é: {password}")
