from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<t>')
@app.route('/index/<t>')
def index(t):
    return render_template('base.html', title=t)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title=f'127.0.0.1:8080/training/{prof}', proffetion=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
