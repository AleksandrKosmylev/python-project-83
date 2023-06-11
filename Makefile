dev:
	poetry run flask --app page_analyzer:app run

PORT ?= 8000
start:
	pip install --upgrade build setuptools && pip install
	pip install --upgrade pip
	pip install gunicorn
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

install:
	poetry install

