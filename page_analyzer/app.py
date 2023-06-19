import psycopg2
from psycopg2.extras import NamedTupleCursor
from flask import (
    Flask,
    render_template,
    request
)

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post("/urls")
def site_check():
    fill = request.form['url']
    # return redirect(url_for('success', name=user))
    # return render_template('urls/index.html' )
    # return fill
    conn = psycopg2.connect('postgresql://postgres:im3Dc5o5ENPMrEbQaU0x@containers-us-west-24.railway.app:7634/railway')
    

    """
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute('SELECT * FROM urls')
        check = curs.fetchall()
        return f'{check}'
    """
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute("""
        INSERT INTO urls (name, created_at)
        VALUES(%s, %s);
        """,
        ("data@", 'now'))
        curs.execute('SELECT * FROM urls')
        check = curs.fetchall()
        return f'{check}'
        conn.close()


if __name__ == '__main__':
    index()
    #app.run(host='0.0.0.0', port=8000, debug=True)
