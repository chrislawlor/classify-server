import asyncio


class MockResponse(object):
    def __init__(self, data, status=200):
        self.data = {'response': data}
        self.status = status

    @asyncio.coroutine
    def json(self):
        return self.data

    @asyncio.coroutine
    def __aenter__(self):
        return self

    @asyncio.coroutine
    def __aexit__(self, *args, **kwargs):
        return


class MockClient(object):
    def __init__(self, response_data, response_status=200):
        self.responses = {}
        self.default_response = MockResponse(response_data, response_status)

    def get(self, url=None):
        try:
            return self.responses[url]
        except KeyError:
            return self.default_response

    def add_response(self, url, response_data, response_status=200):
        self.responses[url] = MockResponse(response_data, response_status)