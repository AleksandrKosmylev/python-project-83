dev:
	poetry run flask --app page_analyzer:app run

PORT ?= 8000
start:
	pip install --upgrade pip
	pip install gunicorn
	pip install validators
	poetry add gunicorn
	poetry add validators	
	export DATABASE_URL=postgresql://postgres:im3Dc5o5ENPMrEbQaU0x@containers-us-west-24.railway.app:7634/railway

	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

install:
	poetry install

