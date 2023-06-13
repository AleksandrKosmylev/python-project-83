from flask import (
    Flask,
    render_template,
    redirect
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/urls ", methods=['POST'])
def site_check():
    return "Hi!"
    #return render_template(
    #    'urls/index.html'
    #    )

if __name__ == '__main__':
    index()
