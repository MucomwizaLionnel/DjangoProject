

from django.contrib.auth import login, logout,authenticate
from django.shortcuts import  render,redirect
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignupForm, EmpoyeeSignupForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User




def register(request):
    return render(request, '../templates/register.html')
class customer_register(CreateView):
    model=User
    form_class = CustomerSignupForm
    template_name='../templates/customer_register.html'

    def validation(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('/')

class employee_register(CreateView):
    model=User
    form_class = EmpoyeeSignupForm
    template_name='../templates/employee_register.html'

    def validation(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('/')
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"invalid username or password")
        else:
                messages.error(request,"invalid username or password")

    return render(request,'../templates/login.html',
                  context={'form':AuthenticationForm()})



