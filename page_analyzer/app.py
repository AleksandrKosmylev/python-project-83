import psycopg2
import os
import validators
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request
)


DATABASE_URL = os.getenv('DATABASE_URL')
load_dotenv()
app = Flask(__name__)


def validate(url_string):
    errors = {}
    if not validators.url(url_string):
        errors['url_string'] = "Should be url"
    if len(url_string) > 256:
        errors['url_string'] = "Should be less than 255 characters"
    return errors


@app.route('/')
def index():
    return render_template('index.html')


@app.post("/urls")
def site_check():
    fill = request.form['url']
    errors = validate(fill)
    if errors:
        return "Error", 422

    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as curs:
        curs.execute(
        """
        INSERT INTO urls (name, created_at)
        VALUES(%s, %s);
        """,
        (fill, 'now')
        )
        curs.execute('SELECT * FROM urls')
        check = curs.fetchall()
        return f'{check}'


if __name__ == '__main__':
    index()
