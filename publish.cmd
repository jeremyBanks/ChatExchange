pip install pipenv -q
pipenv install

pipenv run python -m stackchat --version

pipenv run python setup.py sdist upload
