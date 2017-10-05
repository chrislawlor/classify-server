import logging
import os
from urllib.parse import urlencode
import distance


logger = logging.getLogger('classify_server.foursquare')


FOURSQUARE_CLIENT_ID = os.environ.get('FOURSQUARE_CLIENT_ID')
FOURSQUARE_CLIENT_SECRET = os.environ.get('FOURSQUARE_CLIENT_SECRET')
FOURSQUARE_VERSION = os.environ.get('FOURSQUARE_VERSION', '20170823')

BASE = 'https://api.foursquare.com/v2/'


class ProviderException(Exception):
    pass


def get_foursquare_url(endpoint, **params):
    """
    Given an andpoint, and query string parameters as
    keyword arguments, return a URL suitable for submission
    to the Foursquare API.
    """
    endpoint = endpoint.lstrip('/')
    params.update({
        'client_id': FOURSQUARE_CLIENT_ID,
        'client_secret': FOURSQUARE_CLIENT_SECRET,
        'v': FOURSQUARE_VERSION})
    path = f"{BASE}{endpoint}"
    qs = urlencode(params)
    return f'{path}?{qs}'


async def make_request(client, url):
    logging.info(f"GET {url}")

    async with client.get(url) as resp:
        if resp.status == 200:
            data = await resp.json()
            if 'intent=match' in url:
                if not data['response']['venues']:
                    logging.debug("No match returned")
                    pass
            return data['response']
        logger.error(resp.status, url)


def match_venue_to_query(query, venues):
    """
    Given a query, and a list of Foursquare Venue objects, return the first
    venue to match the query.

    A match is determined by a pair of string distance functions: a normalized
    levenshtein distance function, and the jaccard distance function.
    """
    LEVENSHTEIN_THRESHOLD = 0.25
    JACCARD_THRESHOLD = 0.1
    for venue in venues:
        l_score = distance.nlevenshtein(query, venue['name'], method=1)
        j_score = distance.jaccard(query, venue['name'])
        # Lower score is a better match
        if l_score <= LEVENSHTEIN_THRESHOLD and j_score <= JACCARD_THRESHOLD:
            return venue
    return None


async def get_foursquare_category(client, row):
    try:
        ll = f"{row['lat']},{row['lon']}"
        query = row['name']
    except KeyError:
        raise ProviderException("Query must include 'lat', 'lon', and 'name' parameters")
    match_venue = None
    checkin_venue = None
    category = None
    # We get bad matches for municipalities. As a cheap way to
    # avoid them, short-circuit if there is a comma in the query.
    if ',' in query:
        return {
            'query': query,
            'checkin': None,
            'match': None,
            'category': None
        }
    match_url = get_foursquare_url('/venues/search', intent='match',
                                   query=query, ll=ll, radius=50)
    match_resp = await make_request(client, match_url)
    print(match_resp)

    if match_resp['venues']:
        try:
            match_venue = match_resp['venues'][0]
            category = match_venue['categories'][0]
        except IndexError:
            logger.info(f"No category for response: {match_venue}")
    else:
        checkin_url = get_foursquare_url('/venues/search', intent='checkin',
                                         query=query, ll=ll)
        checkin_resp = await make_request(client, checkin_url)
        checkin_venue = match_venue_to_query(query, checkin_resp['venues'])
        if checkin_venue and checkin_venue['categories']:
            category = checkin_venue['categories'][0]

    return {
        'query': query,
        'checkin': checkin_venue,
        'match': match_venue,
        'category': category}
