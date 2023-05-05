import re


def valida_email(email):
    email = str(email)
    email = re.sub(r'[^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$]', '', email)
