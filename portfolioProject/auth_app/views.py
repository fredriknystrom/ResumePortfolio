from django.urls import reverse_lazy
from allauth.account.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'auth_app/custom_login.html'

class CustomLogoutView(LogoutView):
    template_name = 'auth_app/custom_logout.html'
    success_url = reverse_lazy('custom_login')
