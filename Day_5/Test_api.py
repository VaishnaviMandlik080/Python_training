
'''
Use a pytest fixture to send an HTTP GET request.
Test whether the response status code is 200.
'''

import pytest
import requests


@pytest.fixture
def get_url():
    url = "https://www.google.com"
    response = requests.get(url, timeout=10)
    return response.status_code


def test_get_operation(get_url):
    assert get_url == 200