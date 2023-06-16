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
    fill  = request.form['url']
    # return redirect(url_for('success', name=user))
    #return render_template('urls/index.html' )
    #return fill
    try:
        conn = psycopg2.connect(dbname='urls', user='postgres', password='paralich666', host='host')
        return "success"
    except:
        print('Can`t establish connection to database')


if __name__ == '__main__':
    index()
