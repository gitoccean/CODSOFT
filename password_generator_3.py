
# Enhanced Password Strength checker

#  choose your password by any user
def strongPasswaord():
    if len(password) <= 8:  # must be at least 8 characters long
        print("Password Strength: Weak 1 ")
        return False
    elif not any(c.isupper() for c in password):  # must contain at least one uppercase letter
        print("Password Strength: Weak 2 ")
        return False
    elif not any(c.islower() for c in password):  # must contain at least one lowercase letter
        print("Password Strength: Weak 3 ")
        return False
    elif not any(c.isdigit() for c in password):  # must contain at least one digit
        print("Password Strength: Weak 4 ")
        return False
    elif not any(c in '!@#$%^&*' for c in password):  # must contain at least one special character
        print("Password Strength: Weak 5 ")
        return False
    else:
        print("Password Strength: Strong")
        return True

password = input('Kindly choose your password : ')

if strongPasswaord():
    print('Congratulation!')
