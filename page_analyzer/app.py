import psycopg2
from psycopg2.extras import NamedTupleCursor
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
conn = psycopg2.connect(DATABASE_URL)
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

    now = time.strftime("%Y-%m-%d")
    with conn.cursor() as curs:
        curs.execute(
            """
            INSERT INTO urls (name, created_at)
            VALUES(%s, %s);
            """,
            (address, now)
        )
        conn.commit()
    with conn.cursor() as curs:
        curs.execute(
            "SELECT * FROM urls WHERE name = %s", (address,)
        )
        extracted = curs.fetchone()
        print("fetch result=", extracted)
        print("get  int=", extracted[0], type(extracted[0]))
        id = extracted[0]
        return redirect(url_for('analyze', id=id))


@app.route("/urls/<id>")
def analyze(id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(
            # "SELECT name FROM urls WHERE id=%s", (id, )
            "SELECT  * FROM urls"
        )
        result_url = curs.fetchall()
        (url_id, name, created_at) = result_url[0]
        print("id=", type(id), id)
        print("urls_id=", type(id), id)
        print(type(result_url), result_url)
        return name


if __name__ == '__main__':
    index()
