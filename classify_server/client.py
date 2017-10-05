import aiohttp


async def init_client(app):
    app['client'] = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))


async def close_client(app):
    app['client'].close()
