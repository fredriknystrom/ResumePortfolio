from django.urls import reverse_lazy
from allauth.account.views import LoginView, LogoutView
from .forms import CustomLoginForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'auth_app/custom_login.html'

   
class CustomLogoutView(LogoutView):
    template_name = 'auth_app/custom_logout.html'
    success_url = reverse_lazy('custom_login')
