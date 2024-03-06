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


def test_equal_stacks_success():

    stack1 = Stack(("apple", "banana", "cucumber"))
    stack2 = Stack(("apple", "banana", "cucumber"))

    assert stack1 == stack2


def test_equal_stacks_failure():

    stack1 = Stack(("apple", "banana", "cucumber"))
    stack2 = Stack(("cherries", "avocados", "pineapples"))

    assert stack1 != stack2


def test_boolean_non_empty_stack():

    stack1 = Stack(("apple", "banana", "cucumber"))

    assert bool(stack1) == True


def test_boolean_empty_stack():

    stack1 = Stack()

    assert bool(stack1) == False
