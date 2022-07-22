from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = RegistrationForm
    # template_name = 'users/register.html'
    # success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        form.save()
        email = self.request.POST["email"]
        user_name = self.request.POST["user_name"]
        password = self.request.POST["password1"]
        account = authenticate(email=email, user_name=user_name, password=password)
        login(self.request, account)
        return HttpResponseRedirect(reverse("catalog:index"))
