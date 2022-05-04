from flask import Flask, render_template, request
import random
import json
import crawler

app = Flask(__name__)


@app.route('/')
def hello_world():
    currency = crawler.get_value()
    return render_template("main.html", currency=currency)


@app.route('/game/')
def guess_currency():
    currency = crawler.get_value()
    random.shuffle(currency)
    return render_template("game.html", value=currency[0])


@app.route('/game/answer', methods=['GET', 'POST'])
def check_answer():
    form = request.args
    currency = form['currency']
    ans = form['ans']
    print(type(ans))
    data = {}
    data['currency'] = currency
    data['name'] = ans
    return render_template("answer.html",data=data )


if __name__ == '__main__':
    app.run()
