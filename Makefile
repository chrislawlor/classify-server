server:
	PYTHONPATH=`pwd` pipenv run python -m classify_server

runtests:
	pipenv run pytest --cov

test: runtests
	pipenv run coverage html
	@echo "\nRun open htmlcov/index.html to view the coverage report"

check:
	pipenv run flake8

shell:
	pipenv run ipython

ci:
	pip install pipenv
	pipenv install --dev
