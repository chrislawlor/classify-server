[![Build Status](https://travis-ci.org/chrislawlor/classify-server.svg?branch=master)](https://travis-ci.org/chrislawlor/classify-server) [![Coverage Status](https://coveralls.io/repos/github/chrislawlor/classify-server/badge.svg?branch=master)](https://coveralls.io/github/chrislawlor/classify-server?branch=master)

# Location Classifier Server

A small microservice for categorizing place data. Given a location name, and
a set of coordinates, returns categorization data obtained by combining one
or more Foursquare APIs.

This is an attempt to learn asyncio / aiohttp, by building something at least
slightly useful


## Consuming the API

[View the online documentation](https://location-classify-server.restlet.io/)


## Getting Started

1. Get your Foursquare API credentials at https://foursquare.com/developers/apps

1. Copy the ``env.sample`` file to ``.env``, and add your API creds.



### Prerequisites

This project is using Pipenv, available here: https://github.com/kennethreitz/pipenv



### Installing

Use Pipenv to install dependencies:

```
pipenv install --three --dev
```


## Running the tests

Most development tasks have a shortcut command in the Makefile. Run the tests
with

```
make runtests
```


### And coding style tests

```
make check
```

## Start the server

```
make server
```

## Built With

* [aiohttp](http://aiohttp.readthedocs.io/en/stable/index.html) - Asynchronous HTTP Client / Server
* [Pipenv](https://docs.pipenv.org/) - Dependency Management
* [Foursquare](https://developer.foursquare.com/) Places API

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Chris Lawlor**

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE.md](LICENSE.md) file for details
