from django.contrib.auth.views import LogoutView, PasswordResetView
from django.urls import path
from .views import SignUp

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        'signup/', SignUp.as_view(),
        name='signup'
    )
]
