from urllib.parse import urlencode
from classify_server.server import init as init_app
from classify_server.foursquare import get_foursquare_category

from .mocks import MockClient


async def test_405_for_post_request(test_client, loop):
    app = init_app(loop, None)
    client = await test_client(app)
    resp = await client.post('/foursquare/category')
    assert resp.status == 405


async def test_missing_qs_parameters(test_client, loop):
    app = init_app(loop, None)
    client = await test_client(app)
    resp = await client.get('/foursquare/category')
    assert resp.status == 400


async def test_ignore_queries_with_commaas(test_client, loop):
    app = init_app(loop, None)
    client = await test_client(app)
    qs = urlencode({'name': 'name, with, commas', 'lat': 1, 'lon': 1})
    resp = await client.get(f'/foursquare/category?{qs}')
    assert resp.status == 200, await resp.text()
    data = await resp.json()
    assert 'query' in data


async def test_match(loop):
    query_data = {'name': 'test', 'lat': 1, 'lon': 1}
    response_data = dict(
        venues=[
            dict(
                name='test',
                categories=[
                    dict(name='test_category')
                ]
            )
        ]
    )
    client = MockClient(response_data)
    resp = await get_foursquare_category(client, query_data)
    assert resp is not None
    assert 'query' in resp
    assert resp['query'] == 'test'
    assert 'category' in resp
    assert resp['category'] == {'name': 'test_category'}
