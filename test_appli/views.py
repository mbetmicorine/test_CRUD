from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required  # protège la page
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from .models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm


# ---- INSCRIPTION ----

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie. Connectez-vous maintenant.")
            return redirect('login')  # redirige vers la page de login
        else:
            messages.error(request, "Veuillez corriger les erreurs du formulaire.")
    else:
        form = SignupForm()
    
    return render(request, 'test_appli/signup.html', {'form': form})

# ---- CONNEXION ----
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # seulement POST
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)  # connexion de l'utilisateur
            messages.success(request, "Connexion réussie.")
            return redirect('dashboard')
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
    else:
        form = LoginForm()

    return render(request, 'test_appli/login.html', {'form': form})

# ---DASHBOARD ---
@login_required
def dashboard_view(request):
    # Récupère tous les utilisateurs
    users = CustomUser.objects.all()
    return render(request, 'test_appli/dashboard.html', {'users': users})

# ----update user ----

User = get_user_model()

def update_user(request, phone):
    user = get_object_or_404(User, phone_number=phone)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'test_appli/update_user.html', {
        'form': form,
        'user': user
    })

# ---- delete user ----
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def delete_user(request, phone):
    # Décoder si nécessaire
    phone = phone.replace(' ', '+')  # si le + devient un espace dans l'URL

    user = get_object_or_404(User, phone_number=phone)
    user.delete()
    return redirect('dashboard')  # rediriger vers la page liste des utilisateurs

