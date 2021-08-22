# REGISTER FORM
from string import ascii_lowercase, ascii_uppercase, punctuation

username = input("Enter your username: ")
password = input("Enter a password: ")

username_list = []
password_list = []

##########################
# No first letter as number
# MIN 5 CHAR
# ACCEPT ONLY '.' '-' '_'
##########################


def check_valid_username(username):
    username_error_messages = {
        "Error 1": "Number in the first position not allowed",
        "Error 2": "Minimum of characters not reached",
        "Error 3": "Invalid character"
    }

    if username[0].isdigit():
        return username_error_messages["Error 1"]
    elif len(username) < 5:
        return username_error_messages["Error 2"]
    elif punctuation in username:
        if punctuation not in [".", "-", "_"]:
            return username_error_messages["Error 3"]
    else:
        return True


if check_valid_username(username):
    username_list.append(username)


##########################
# MIN 5 CHAR | MAX 12 CHAR
# 1 UPPER CASE
# 1 NUMBER
# 1 SPECIAL CHAR
##########################
def check_valid_password(password):
    password_error_messages = {
        "Error 1": "Out of range length for the password",
        "Error 2": "No upper case letter",
        "Error 3": "No numbers present",
        "Error 4": "No special char present"
    }

    if len(password) < 5 or len(password) > 12:
        return password_error_messages["Error 1"]

    count_upper = 0
    count_number = 0
    count_special = 0

    for letter in password:
        if letter in punctuation:
            count_special += 1
        elif letter in ascii_uppercase:
            count_upper += 1
        elif letter.isdigit():
            count_number += 1

    if count_upper == 0:
        return password_error_messages["Error 2"]
    elif count_number == 0:
        return password_error_messages["Error 3"]
    elif count_special == 0:
        return password_error_messages["Error 4"]

    return True


if check_valid_password(password):
    password_list.append(password)


with open("registration.txt", "a") as file:
    file.writelines(["Username: ", username, "\nPassword: ", password, "\n"])
