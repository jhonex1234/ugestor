# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import validators		
from wtforms.fields import SelectField
from wtforms import BooleanField
from wtforms.validators import DataRequired
from com_dao import ConnectionDB


def validateNotNUll(form, field):
    if len(field.data) <= 0:
        raise validators.ValidationError('El campo No debe ser Nulo')


class DisenadorDTO(Form):
		id = IntegerField('', [validateNotNUll])
		pasaporte = StringField('', [validateNotNUll])
		paisOrigen = StringField('', [validateNotNUll])
