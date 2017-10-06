server:
	PYTHONPATH=`pwd` pipenv run python -m classify_server

test:
	pipenv run pytest

check:
	pipenv run flake8

shell:
	pipenv run ipython

ci:
	pip install pipenv
	pipenv install --dev
