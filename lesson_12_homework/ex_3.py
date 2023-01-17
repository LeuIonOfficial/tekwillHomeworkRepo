<<<<<<< HEAD
def sum_of_prime(x):
    def is_prime(n):
        if x<2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
=======
def is_prime(number: int):
    for a in range(2, number):
        if number % a == 0:
            return False
    return True
>>>>>>> 305ae2fa631e3a8a774e0cd38199337336183c60

    result = 0
    for i in range(2, x):
        if is_prime(i):
            result += i
    return result

print(sum_of_prime(10))