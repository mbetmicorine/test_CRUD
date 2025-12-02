from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.models import AbstractUser

# Manager personnalisé
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, username, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Le numéro de téléphone est requis")
        email = self.normalize_email(email) if email else None
        user = self.model(
            phone_number=phone_number,
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, username, email, password, **extra_fields)

# Modèle utilisateur personnalisé
class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=13, unique=True, primary_key=True)  # +2376XXXXXXX
    username = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username} ({self.phone_number})"


