from solver import Solver, TYPE_ERROR_TEXT, User
from unittest import TestCase
import pytest, os

import sys


class TestSolver(TestCase):

    def test_add(self):
        res = Solver.add(1, 2)
        self.assertEqual(3, res)

    def test_values(self):
        with self.assertRaises(TypeError):
            Solver.add('True', 2)


@pytest.mark.parametrize("args, results", [
    pytest.param(
        (1, 2), 3,
        id="1+2"
    ),
    pytest.param(
        (True, 3), 4,
        id="3+True"
    )

])
def test_add_pytest(args, results):
    res = Solver.add(*args)
    assert res == results


@pytest.mark.parametrize("args, results", [
    pytest.param(
        ("1", 2), TypeError, id='TypeError (str, int)'
    ),
    pytest.param(
        ("1", None), TypeError, id='TypeError (str, None)'
    )
])
def test_values_pytest(args, results):
    with pytest.raises(results) as ex:
        Solver.add(args)


# фикстура - объект, который иниц только для тестов
# одни фикстуры могут использовать другие

@pytest.fixture
def temp_user():
    return User("John", "Smith", 23)


@pytest.fixture
def temp_file():
    filepath = "test-text.txt"
    file = open(filepath, 'w')
    file.write(temp_user)
    file.close()

    return filepath


def test_remove_file():
    filepath = temp_file
    Solver.remove_file(filepath)
