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


    class ModeloDTO(Form):
        id = IntegerField('', [validateNotNUll])
        colorOjos = SelectField(label='Color de ojos', choices=[('Seleccione','Seleccione'),('blanco','blanco') ,('Trigeno','Trigeno'),('Negro','Negro')])
        colorPiel =  SelectField(label='Color de piel', choices=[('Seleccione','Seleccione'),('Cedula','cedula') ,('T.I','tarjetaIdentidad'),('Cedula Extranjera','cedulaextranjera')])
        estatura = IntegerField('', [validateNotNUll])
        medidaCintura = IntegerField('', [validateNotNUll])
        medidaBusto = IntegerField('', [validateNotNUll])
        TallaZapatos = IntegerField('', [validateNotNUll])
        particularidades = StringField('', [validateNotNUll])
        peso = IntegerField('', [validateNotNUll])
        idpersona = IntegerField('', [validateNotNUll])
