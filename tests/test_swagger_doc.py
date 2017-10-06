from classify_server.server import init as init_app


async def test_swagger_doc_available(test_client, loop):
    app = init_app(loop, None)
    client = await test_client(app)
    resp = await client.get('/static/openapi.yml')
    assert resp.status == 200
