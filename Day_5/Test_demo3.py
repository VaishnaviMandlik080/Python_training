# Created by Vaishnavi

'''
Use a pytest fixture to provide the value 39.
Test whether it is divisible by 3, 6 and 13.
'''

import pytest


@pytest.fixture
def input_data():
    return 39


def test_divisible_by_3(input_data):
    assert input_data % 3 == 0


def test_divisible_by_6(input_data):
    assert input_data % 6 == 0


def test_divisible_by_13(input_data):
    assert input_data % 13 == 0