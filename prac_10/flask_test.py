from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'Hello {name}'

@app.route('/f')
@app.route('/f/<number>')
def convert_f_to_c(number):
    c = round((5 * (float(number) - 32)) / 9, 2)
    return str(c)


if __name__ == '__main__':
    app.run()
