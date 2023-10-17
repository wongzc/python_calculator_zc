import pytest
from calculator import *


@pytest.mark.parametrize("x,y,z",[(1,2,3),(-1,-2,-3),(0,0,0)])
def test_add(x,y,z):
    assert(add(x, y)==z)

@pytest.mark.parametrize("x,y,z",[(5,2,3),(-5,-2,-3),(0,0,0)])
def test_subtract(x,y,z):
    assert(subtract(x, y)==z)

@pytest.mark.parametrize("x,y,z",[(5,2,10),(-5,-2,10),(0,0,0)])
def test_multiply(x,y,z):
    assert(multiply(x, y)== z)

@pytest.mark.parametrize("x,y,z",[(5,2,2.5),(6,-2,-3),(0,0,"Cannot divide by 0")])
def test_divide(x,y,z):
    assert(divide(x, y)==z)


def test_get_num(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_num("Enter a number: ") == 1
    monkeypatch.setattr('builtins.input', lambda _: "sdad")
    assert get_num(
        "Enter a number: ") == "Please enter a valid integer"