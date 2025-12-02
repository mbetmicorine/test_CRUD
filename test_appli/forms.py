# test_appli/forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import CustomUser
import re


# ------------ FORMULAIRE D'INSCRIPTION ------------
class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        label="Mot de passe"
    )

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'username', 'email', 'password']

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        if not re.match(r'^\d{9}$', phone):
            raise ValidationError("Entrez exactement 9 chiffres, sans +237.")

        if not phone.startswith("6"):
            raise ValidationError("Le numéro doit commencer par 6.")

        return "+237" + phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# ------------ FORMULAIRE DE CONNEXION ------------
class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Entrez votre email'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        pwd = cleaned_data.get("password")

        if email and pwd:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError("Email ou mot de passe incorrect.")

            if not user.check_password(pwd):
                raise forms.ValidationError("Email ou mot de passe incorrect.")

            cleaned_data['user'] = user

        return cleaned_data


# ------------ FORMULAIRE DE MODIFICATION USER ------------
class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label="Nouveau mot de passe"
    )

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.cleaned_data['password']:
            user.password = make_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
