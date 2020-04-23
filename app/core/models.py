from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class GestorUser(BaseUserManager):
    
    def criar_user(self, email, pwd=None, **prm):
        # Criar e salvar um novo usuário...
        if not email:
            raise ValueError('E-mail deve ser informado!!!')

        user = self.model(email=email, **prm)
        user.set_password(pwd)
        user.save(using=self._db)

        return user

    def criar_superuser(self, email, pwd):
        # Criar e salvar novo super usuário
        user = self.criar_user(email, pwd)
        user.inativo = True
        user.supervisor = True
        user.save(using=self._db)

        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    # Modelo de usuário personalizado utilizando email em vez de nome de usuário...
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    inativo = models.BooleanField(default=False)

    obj = GestorUser()

    USERNAME_FIELD = 'email'