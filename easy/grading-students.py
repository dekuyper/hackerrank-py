def roundGrade(grade):
    if grade < 38:
        return grade

    next_multiple = int((grade + 5) - (grade % 5))
    if next_multiple - grade < 3:
        return next_multiple

    return grade


grades = [73, 67, 38, 33]

for grade in grades:
    grade = roundGrade(grade)
    print(grade)
