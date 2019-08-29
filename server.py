import os
import sys
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
from flask import session, flash
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append("{0}/ugestor_dto".format(script_dir))
sys.path.append("{0}/ugestor_tools".format(script_dir))
from DataManager import DataManager
from Persona import Persona

dataManager = DataManager();
app = Flask(__name__, template_folder="ugestor_template")
pass_url = '/'

@app.route('/cPersona', methods=['GET', 'POST'])
def indexcPersona():
	persona = Persona(1, 1241224, "Juna", "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.createPerson(persona)
	return redirect("{0}{1}/formPersona".format(request.url_root, pass_url), code=302)


@app.route('/formPersona', methods=['GET'])
def info():
	return render_template("info.html")


if __name__ == '__main__':
    app.run(port=8000, debug=True, threaded=True)