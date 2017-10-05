import argparse
import asyncio
import configparser
import logging
from pathlib import Path

import jinja2
import aiohttp_jinja2
from aiohttp import web

from .routes import setup_routes
from .client import init_client, close_client


logger = logging.getLogger('classify_server')


def init_config(config_file=None):
    config = configparser.ConfigParser()
    # Load the defaults from config/defaults.ini
    cwd = Path(__file__).parent.absolute()
    defaults_path = cwd / 'config' / 'defaults.ini'
    with defaults_path.open() as defaults:
        config.read_file(defaults)
    # Load from the specified config file, if present
    if config_file:
        logging.debug(f'Loading config from {config_file}')
        with open(config_file) as cfg:
            config.read_file(cfg)
    else:
        # Look for optional local and system config files
        local_config_path = cwd / 'config' / 'local.ini'
        system_config_path = Path('/etc') / 'classify_server' / 'config.ini'
        files_read = config.read((str(local_config_path), str(system_config_path)))
        for f in files_read:
            logging.debug(f'Loading config from {f}')
    return config


def init(loop, config):
    app = web.Application(loop=loop)
    app['config'] = config

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('classify_server', 'templates'))

    app.on_startup.append(init_client)
    app.on_cleanup.append(close_client)

    setup_routes(app)
    return app


def main():
    parser = argparse.ArgumentParser(description="Location Classification Server")
    parser.add_argument('-c', '--config', dest='config')
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    config = init_config(config_file=args.config)
    app = init(loop, config['classify_server'])
    web.run_app(app,
                host=app['config']['host'],
                port=app['config'].getint('port'))


if __name__ == '__main__':
    main()
