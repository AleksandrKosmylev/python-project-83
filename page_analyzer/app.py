from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hey, hey. Hello, World!'


if __name__ == '__main__':
    hello_world()
