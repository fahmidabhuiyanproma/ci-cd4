from result import total, average, is_pass, get_grade


def test_total():
    assert total(80, 70, 90) == 240


def test_average():
    assert average(80, 70, 90) == 80


def test_pass():
    assert is_pass(50) is True
    assert is_pass(30) is False


def test_grade():
    assert get_grade(85) == "A"
    assert get_grade(75) == "B"
    assert get_grade(65) == "C"
    assert get_grade(45) == "D"
    assert get_grade(30) == "F"
