dev:
	poetry run flask --app page_analyzer:app run

PORT ?= 8000
start:
	pip install --upgrade pip
	pip install gunicorn
	pip install validators
	poetry add gunicorn
	poetry add validators	
	createdb url_database
	psql url_database < database.sql

	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

install:
	poetry install

