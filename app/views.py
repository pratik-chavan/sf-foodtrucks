from flask import Flask, render_template, request
from app import app
from processing import calculate_distance

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                            title = 'Home')

@app.route('/data_to_find_distance', methods = ["GET", "POST"])
def data_to_find_distance():
    if request.method == "POST":
        print 'In url call ', request.json
        return calculate_distance(request.json)
