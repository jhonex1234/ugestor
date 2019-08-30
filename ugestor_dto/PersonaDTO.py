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


class PersonaDTO(Form):
		documento = IntegerField('', [validateNotNUll])
		nombre = StringField('', [validateNotNUll])
		tipoDocumento =  SelectField(label='Tipo Documento', choices=[('Seleccione','Seleccione'),('Cedula','cedula') ,('T.I','tarjetaIdentidad'),('Cedula Extranjera','cedulaextranjera')])
		apellido = StringField('', [validateNotNUll])
		paisOrigen = StringField('', [validateNotNUll])
		fechaNacimiento =  DateField('Fecha de Registro', [])
		sexo = SelectField(label='Grado de Agobio', choices=[('Seleccione','Seleccione'),('Masculino','male') ,('Femenino','fem'),('Otaku','ot')])
		