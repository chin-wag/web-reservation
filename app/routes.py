from app import app
from flask import render_template, request
from app.logic import get_tables, reserve


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/reservation')
def reservation():
    return render_template('reservation.html', tables=get_tables())


@app.route('/reservation_result', methods=['POST'])
def reservation_result():
    reserve(request.form["table"], request.form["fio"])
    return render_template('index.html')
