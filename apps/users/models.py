from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from crum import get_current_user

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
class Base(models.Model):
    """Modelo abstract base del que heredan todos 
    los modelos para manejar la auditoria"""
    fecha_registro = models.DateTimeField(
        'Fecha de registro', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        'Fecha de modificación', auto_now=True)
    estado = models.BooleanField('Estado', default=True)
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT,
                                    related_name='%(class)s_creado_por',
                                    null=True, blank=True,
                                    verbose_name='Usuario de creación')
    actualizado_por = models.ForeignKey(User, on_delete=models.PROTECT,
                                        related_name='%(class)s_modificado_por',
                                        null=True, blank=True,
                                        verbose_name='Usuario última actualización')

    class Meta:
        """
        docstring
        """
        abstract = True
        get_latest_by = 'creado_por'
        # ordering = ['-creado_por', '-fecha_actualizacion']
        ordering = ['-fecha_actualizacion']

    def traer_usuario(self):
        return get_current_user()

    def save(self, *args, **kwargs):
        if self.fecha_registro is None:
            self.creado_por = self.traer_usuario()
            self.actualizado_por = self.traer_usuario()
        else:
            self.actualizado_por = self.traer_usuario()
        super(Base, self).save(*args, **kwargs)