import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from app import add, subtract, login
from app import subtract

def test_add():
    assert add(2, 4) == 6
    assert add(3, 3) == 6

def test_subtract():
    assert subtract(4, 2) == 2
    assert subtract(3, 3) == 0

@pytest.mark.slow
def test_add_large_numbers():
    assert add(1000, 2000) == 3000

@pytest.mark.xfail
@pytest.mark.fixture1
def test_add_with_fixture(sample_data):
    result = add(sample_data["a"], sample_data["b"])
    assert result == 6

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (5,3, 8)])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_valid_login():
    response = login("user", "password123")
    assert response == "Login successful"

def test_empty_username():
    with pytest.raises(ValueError, match="Username cannot be empty."):
        login("", "password123")

def test_short_password():
    with pytest.raises(ValueError, match="Password must be at least 6 characters long."):
        login("user", "123")