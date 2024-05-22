
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from apps.main.models import User
from .forms import RegisterForm, ConnectForm
from django.urls import reverse_lazy

@login_required(login_url='/accounts/login/')
def index_view(request):
    user = User.objects.all()
    return render(request, "users/index.html", {'user': user})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'users/logout.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def alice_view(request):
    user = User.objects.all()
    return render(request, "users/alice.html", {'user': user})

def doc_view(request):
    return render(request, "users/index.html")

def support_view(request):
    return render(request, "users/support.html")    

def wait_view(request):
    form = ConnectForm()
    return render(request, "users/wait.html", {'form': form})

def ajax(request):
    return render(request, "users/ajax.html")