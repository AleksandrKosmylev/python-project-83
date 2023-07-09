import psycopg2
import os
import validators
import time
from dotenv import load_dotenv
import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
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
    address = request.form['url']
    errors = validate(address)
    if errors:
        return "Error", 422

    conn = psycopg2.connect(DATABASE_URL)
    now = time.strftime("%Y-%m-%d")
    with conn.cursor() as curs:
        curs.execute(
            """
            INSERT INTO urls (name, created_at)
            VALUES(%s, %s);
            """,
            (address, now)
        )
        """
        curs.execute('SELECT * FROM urls')
        conn.commit()
        check = curs.fetchall()
        return f'{check}'
        """
    with conn.cursor() as curs:
        curs.execute(
            "SELECT id FROM urls WHERE name = %s", (address,)
        )
        check = curs.fetchall()
        print(check)
        return check
        # return redirect(url_for('analyze', id=id))


@app.route("/urls/<id>")
def analyze(id):
    return "check"


if __name__ == '__main__':
    index()
