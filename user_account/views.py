from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View,CreateView
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import RegistrationForm


class LoginView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        form = AuthenticationForm()
        return render(request,'account/login.html',{'form':form})


    def post(self,request,*args,**kwargs):
        
        form = AuthenticationForm(request.POST,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        print("form is invalid")
        return render(request,'account/login.html',{'form':form})
    

class RegisterView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("account:login")
    template_name = "account/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)