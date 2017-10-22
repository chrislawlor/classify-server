import pytest

from .mocks import MockClient

"""
Tests basic mock functionality in order to verify issue #3 resolved
"""


@pytest.fixture
def testclient():
    client = MockClient({'tests': []})
    client.add_response(url='newurl.com/index.php',
                        response_data={'added_response': 'works'})
    return client


def test_default_response(testclient):
    response = testclient.get('unknown_value')
    assert response.data == {'response': {'tests': []}}


def test_known_response(testclient):
    response = testclient.get('newurl.com/index.php')
    assert response.data == {'response': {'added_response': 'works'}}
