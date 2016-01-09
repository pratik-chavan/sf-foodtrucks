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
        if len(request.json) == 4:
            print "For filter - calling server "
            result = calculate_distance(request.json, radius = request.json['radius'], number_of_results = request.json['results_limit'])
            print "For filter - Printing result received from server"
            print result
            return result
        else:
            print "Initial non-filter based call"
            return calculate_distance(request.json)
