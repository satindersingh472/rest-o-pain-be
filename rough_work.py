import re


def check_email(email):
    if(re.fullmatch(regex,email)):
        print('valid_email')
    else:
        print('invalid email')