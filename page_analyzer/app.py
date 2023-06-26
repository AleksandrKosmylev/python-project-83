import psycopg2
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
    if  not validators.url(url_string):
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
    
    conn = psycopg2.connect('postgresql://postgres:2CySg27TBeJhsb8jZ6IM@containers-us-west-57.railway.app:6548/railway')
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute("""
        INSERT INTO urls (name, created_at)
        VALUES(%s, %s);
        """,
        (fill, 'now'))
        curs.execute('SELECT * FROM urls')
        check = curs.fetchall()
        return f'{check}'
        conn.close()


if __name__ == '__main__':
    index()
