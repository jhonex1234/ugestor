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


    class EmpleadoDTO(Form):
        idpersona = IntegerField('', [validateNotNUll])
        salario = IntegerField('', [validateNotNUll])
        cargo =  SelectField(label='Cargo', choices=[('Seleccione','Seleccione'),('Gerente','Gerente') ,('Auxiliar','Auxiliar'),('Contratista','contratista')])
        fechaIngreso =  DateField('Fecha de Registro', [])
