from django.urls import path
from . import views
from .views import signup_view, login_view, dashboard_view
from .views import update_user





urlpatterns = [
    # path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('user/<str:phone>/edit/', update_user, name='update_user'),
    # path('user/<str:phone>/delete/', views.delete_user, name='delete_user'),
    
]
