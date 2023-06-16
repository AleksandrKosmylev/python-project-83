from flask import (
    Flask,
    render_template,
    request,
    redirect
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
    return fill


if __name__ == '__main__':
    index()
