import pytest

from fizz_buzz import fizz_buzz


def _check_fizz_buzz(value, expected):
    assert fizz_buzz(value) == expected


def test_return_1_with_1_passed_in():
    _check_fizz_buzz(1, "1")


def test_return_2_with_2_passed_in():
    _check_fizz_buzz(2, "2")


def test_return_fizz_with_3_passed_in():
    _check_fizz_buzz(3, "Fizz")


def test_return_buzz_with_5_passed_in():
    _check_fizz_buzz(5, "Buzz")


def test_return_fizz_with_multiple_of_3_passed_in():
    _check_fizz_buzz(6, "Fizz")


def test_return_buzz_with_multiple_of_5_passed_in():
    _check_fizz_buzz(10, "Buzz")


def test_return_fizzbuzz_with_multiple_of_3_and_5_passed_in():
    _check_fizz_buzz(15, "FizzBuzz")
