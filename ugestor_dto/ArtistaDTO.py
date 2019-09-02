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
        nombreArtistico = StringField('Nombre', [validateNotNUll])
        generoMusical = StringField('Genero musical', [validateNotNUll])
        tipoArtista =  SelectField(label='tipo de artista', choices=[('Seleccione','Seleccione'),('Grupo','Grupo') ,('Solista','Solista')])
        idpersona = IntegerField('Id persona', [validateNotNUll])
