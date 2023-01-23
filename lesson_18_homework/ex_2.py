
def validate_numeric(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            result = int(result)
            return result
        except ValueError as ex:
            return f"Type of '{result}' - is not numeric."
    return wrapper


@validate_numeric
def str_func():
    return "Hello World"


@validate_numeric
def int_func():
    return 2


print(str_func())
print(int_func())
