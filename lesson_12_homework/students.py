def select_student(students, threshold):
    accepted = []
    rejected = []

    for student in students:
        name, grade = student[0], student[1]
        if grade < threshold:
            rejected.append(student)
        else:
            accepted.append(student)
    accepted = sorted(accepted, key=lambda x: x[1], reverse=True)
    rejected = sorted(rejected, key=lambda x: x[1])
    return {'Accepted': accepted, 'Rejected': rejected}


my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

print(select_student(my_class, 20))