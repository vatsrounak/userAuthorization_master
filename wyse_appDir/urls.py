from django.urls import path
from .views import RegistrationView, ProfileView

urlpatterns = [
    # Authentication URLs
    path('accounts/register/', RegistrationView.as_view(), name='register'),
    path('accounts/login/', RegistrationView.as_view(), name='login'),

    # Profile URLs
    path('accounts/profile/view/', ProfileView.as_view(), name='view_profile'),
    path('accounts/profile/edit/', ProfileView.as_view(), name='edit_profile'),
]
