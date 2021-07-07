import tempfile

from solver import Solver, User
from unittest import TestCase
import pytest, os
from faker import Faker

fake = Faker()


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


@pytest.fixture(params=[User("John", "Smith", 23), User("Jane", "Smith", 28)])
def temp_user(request):
    return request.param


@pytest.fixture
def tem_user_group(temp_user):
    return [User("James", "Potter", 33), temp_user]


@pytest.fixture
def temp_tree():
    path = os.path.join(os.getcwd(), "folder" + str(fake.pyint()))
    os.mkdir(path)
    yield
    # os.unlink(path) - PermissionError


@pytest.mark.usefixtures("temp_tree")
def test_adult(tem_user_group):
    assert all(map(User.is_user_adult, tem_user_group)) is True
    # do smth with folder from fixture


@pytest.mark.skip('test_elderly is skipped')
def test_elderly(tem_user_group):
    assert all(map(User.is_user_elderly, tem_user_group)) is False


