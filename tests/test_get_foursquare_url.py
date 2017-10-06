from classify_server.foursquare import get_foursquare_url


async def test_endpoint_leading_slash():
    url = get_foursquare_url('/test')
    assert 'https://api.foursquare.com/v2/test' in url


async def test_client_params_in_url():
    url = get_foursquare_url('/test')
    assert 'client_id' in url
    assert 'client_secret' in url
