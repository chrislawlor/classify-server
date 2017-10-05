from classify_server.server import init as init_app


async def test_hookup():
    assert 2 + 2 == 4


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
