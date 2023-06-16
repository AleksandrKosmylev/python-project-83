import psycopg2
from flask import (
    Flask,
    render_template,
    request,
    redirect,
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


#@app.route("/", methods=['POST'])
@app.post("/urls")
def site_check():
    #fill  = request.form['url']
    # return redirect(url_for('success', name=user))
    #return render_template('urls/index.html' )
    #return fill

    conn = psycopg2.connect(host="127.0.0.1",
                            dbname="suppliers",
                            user="postgres",
                            password="paralich666")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM suppliers LIMIT 10')
    cursor.fetchall()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    index()
