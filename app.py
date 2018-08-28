import datetime
import json
from flask import Flask, render_template, jsonify, request, redirect
from werkzeug.wrappers import Response

from Modules.simulation.helpers import csv_export
from Modules import core

app = Flask(__name__)





@app.route('/data')
def get_data():
    method = request.args.get('method')
#    if not method or method not in ['weighted', 'unweighted', 'random']:
#        return "The simulation method requested ({}) is invalid".format(method), 400
#    
#    print("The requested method was: {}".format(method))
#    
    simu = core.Multi_Agent_Simulation(100, 2, 2, 0.005, 0.5, method, _printing=True)
    simu.setup()
    simu.run()
    return core.string_export(simu)

@app.route('/')
def index():
    return render_template('home.html')


   


if __name__ == '__main__':
    app.run(debug=True)
    
  


    