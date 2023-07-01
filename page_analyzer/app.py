import psycopg2
import validators
from psycopg2.extras import NamedTupleCursor
from flask import (
    Flask,
    render_template,
    request
)
from validators import url



from dotenv import load_dotenv

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
    return "smt"


if __name__ == '__main__':
    index()
