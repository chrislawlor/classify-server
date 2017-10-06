from classify_server import foursquare

from .mocks import MockClient


async def test_match_venue_to_query_exact_match():
    venues = [{'name': 'test'}]
    query = 'test'
    result = foursquare.match_venue_to_query(query, venues)
    assert result == venues[0]


async def test_match_venue_to_query_small_difference():
    venues = [{'name': 'Manhattan'}]
    query = 'Manhatan'
    result = foursquare.match_venue_to_query(query, venues)
    assert result == venues[0]


async def test_make_request():
    test_data = {'venues': []}
    client = MockClient(test_data)
    resp = await foursquare.make_request(client, 'url?intent=match')
    assert resp == test_data


async def test_make_request_null_response():
    test_data = {'error': 'testing error'}
    client = MockClient(test_data, response_status=400)
    resp = await foursquare.make_request(client, 'url')
    assert resp == None
