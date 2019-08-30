# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import validators
from wtforms.fields.html5 import DateField
from wtforms.fields import SelectField
from wtforms import BooleanField
from wtforms.validators import DataRequired
from com_dao import ConnectionDB


def validateNotNUll(form, field):
    if len(field.data) <= 0:
        raise validators.ValidationError('El campo No debe ser Nulo')


class AgenciaDTO(Form):
	nombre = StringField('Nombre', [validateNotNUll])
	anocreacion =  DateField('Fecha de Creacion', [])
	idPersona = IntegerField('ID Dueño', [validateNotNUll])
	paisOrigen = StringField('Pais Origen', [validateNotNUll])
	correoElectronico =  StringField('E-mail', [validateNotNUll])
	relacionesOtrasAgencias = IntegerField('Cod Relacion Agencia ', [validateNotNUll])
	codAgencia = IntegerField('Cod Agencia', [validateNotNUll])

	