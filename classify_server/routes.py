import pathlib

from .views import foursquare_category


PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/foursquare/category', foursquare_category, name='index')
    app.router.add_static('/static/', path=str(PROJECT_ROOT / 'static'),
                          name='static')
