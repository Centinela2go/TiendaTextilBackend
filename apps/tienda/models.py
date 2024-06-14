from django.db import models

from apps.users.models import Base
from  django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
#comentario
# validar numero telefonico
def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('El número de teléfono debe contener solo dígitos.')
    if len(value) != 9:
        raise ValidationError('El número de teléfono debe tener exactamente 9 dígitos.')
# Validador de dirección
def validate_home_address(value):
    """
    Valida que la dirección de casa contenga solo letras, números, espacios
    y los caracteres ,.-.
    """
    if not re.match(r'^[a-zA-Z0-9\s,.-]+$', value):
        raise ValidationError(
            'La dirección solo puede contener letras, números, espacios '
            'y los caracteres ,.-'
        )

# Create your models here.
class Categoria(Base):
    nombre = models.CharField('Nombre :', max_length=80)
    descripcion = models.CharField('Descripcion :', max_length= 200)

class Provedor(Base):
    nombre = models.CharField('Nombre :', max_length=80)
    direccion =models.CharField('Direccion :', max_length= 80,validators=[validate_home_address])
    telefono =models.CharField('Telefono :', max_length= 9,validators=[validate_phone_number])
    email =models.EmailField('Email :', max_length= 20)
    
class Cliente(Base):
    nombre = models.CharField('Nombre :', max_length=80)
    tireccion =models.CharField('Direccion :', max_length= 80,validators=[validate_home_address])
    telefono =models.CharField('Telefono :', max_length= 9,validators=[validate_phone_number])
    email =models.EmailField('Email :', max_length= 20)
    



