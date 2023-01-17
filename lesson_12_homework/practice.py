def every_prime(x, y):
    def is_prime(n):
        if x < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    result_list = []

    for i in range(x, y):
        if is_prime(i):
            result_list.append(i)
        else:
            continue
    return result_list

print(every_prime(2,10))


def select_student(students: list, threshold: int):
    accepted = []
    rejected = []

    for student in students:
        name, grade = students[0][0], students[0][1]
        if grade >= threshold:
            accepted.append(student)
        else:
            rejected.append(student)
    result = {'Accepted': accepted, 'Rejected': rejected}

    return result

