from pathlib import Path

from classify_server.server import init_config


def test_init_config():
    config = init_config()
    assert 'classify_server' in config
    assert 'host' in config['classify_server']
    assert 'port' in config['classify_server']


def test_init_config_with_alternate_file():
    config_file_path = Path('.').absolute() / 'tests' / 'resources' / 'test_config.ini'
    config = init_config(config_file=config_file_path)
    assert 'classify_server' in config
    assert 'host' in config['classify_server']
    assert config['classify_server']['host'] == 'test'
