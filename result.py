def total(m1, m2, m3):
    return m1 + m2 + m3


def average(m1, m2, m3):
    return total(m1, m2, m3) / 3


def is_pass(mark):
    return mark >= 50


def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"
