
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.urls import reverse_lazy

@login_required
def index_view(request):
    return render(request, "users/index.html")

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("web: ")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    