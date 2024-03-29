import os
import sys
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
from flask import session, flash
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append("{0}/ugestor_dto".format(script_dir))
sys.path.append("{0}/ugestor_tools".format(script_dir))
from DataManager import DataManager
from Persona import Persona
from PersonaDTO import PersonaDTO

dataManager = DataManager();
app = Flask(__name__, template_folder="ugestor_template")
pass_url = '/'

@app.route('/cPersona', methods=['GET', 'POST'])
def indexcPersona():
	formPersona = objPersona(request.form)
	persona = Persona(formPersona.documento.data, formPersona.tipoDocumento.data, "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.createPerson(persona)#redirect("{0}{1}/formPersona".format(request.url_root, pass_url), code=302)
	return redirect("{0}{1}/v_cPersona".format(request.url_root, pass_url), code=302)

#rederiza html
@app.route('/v_cPersona', methods=['GET', 'POST'])
def indexcPersonaForm():
	formPersona = PersonaDTO(request.form)
	link = '{0}{1}'.format(request.url_root, pass_url)
    

	return render_template('v_cPersona.html', link=link, form=formPersona)
	


@app.route('/dPersona', methods=['GET', 'POST'])
def indexdPersona():
	persona = Persona(1, 1241224, "Juna", "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.deletePerson(persona)
	return redirect("{0}{1}/formPersona".format(request.url_root, pass_url), code=302)


@app.route('/uPersona', methods=['GET', 'POST'])
def indexuPersona():
	persona = Persona(1, 1241224, "Juna", "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.updatePerson(persona)
	return redirect("{0}{1}/formPersona".format(request.url_root, pass_url), code=302)


@app.route('/fPersona', methods=['GET', 'POST'])
def indexfPersona():
	persona = Persona(1, 1241224, "Juna", "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.buscarPerson(persona)
	return redirect("{0}{1}/formPersona".format(request.url_root, pass_url), code=302)


@app.route('/alPersona', methods=['GET', 'POST'])
def indexalPersona():
	persona = Persona(1, 1241224, "Juna", "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.obtenerPersonas()
	return redirect("{0}{1}/formPersona".format(request.url_root, pass_url), code=302)


"""
@app.route('/formPersona', methods=['GET'])
def info():
	return "Ejemplo de retorno apartir de la peticion </br>{0}".format(dataManager.obtenerPersonas())#render_template("info.html")



@app.route('/form_Persona', methods=['GET'])
def info_1():
	persona = Persona(1, 1241224, "Juna", "cedula", "jhonson", "colombia", "29-05-2019", "masculino")
	dataManager.v(persona.__class__.__name__)
	return	""
"""

if __name__ == '__main__':
    app.run(port=8000, debug=True, threaded=True)
