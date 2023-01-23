import datetime

DATE_FORMAT = '%d/%m/%Y'


def customer_register():
    user_reg = {
        "first_name": input("Please enter your first name: "),
        "last_name": input("Please enter your last name: "),
        "dob": input("Please enter your date of birth in the format DD/MM/YYYY: "),
    }
    return user_reg


def customer_to_print():
    pass

print(customer_register())