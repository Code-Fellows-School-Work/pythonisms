import pytest

from pythonisms_lab.script import Stack


def test_for_in():

    foods = Stack(("apple", "banana", "cucumber"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert foods_list == ["apple", "banana", "cucumber"]


def test_list_comprehension():

    foods = Stack(("cherries", "avocados", "pineapples"))

    foods_list = []

    [foods_list.append(food) for food in foods]

    assert foods_list == ["cherries", "avocados", "pineapples"]


def test_set():

    foods = Stack(("apple", "banana", "cucumber"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert set(foods_list) == {"apple", "banana", "cucumber"}


def test_equal_stacks():

    stack1 = Stack(("apple", "banana", "cucumber"))
    stack2 = Stack(("apple", "banana", "cucumber"))

    assert stack1 == stack2
