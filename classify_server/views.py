from aiohttp import web

from .foursquare import get_foursquare_category, ProviderException


async def foursquare_category(request):
    client = request.app['client']
    try:
        response = await get_foursquare_category(client, request.query)
    except ProviderException as ex:
        return web.json_response({'error': str(ex)}, status=400)
    return web.json_response(response)
