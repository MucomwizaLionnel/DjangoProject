from django.urls import path
from .import views


urlpatterns = [
    #path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('customer_register/',views.customer_register.as_view(), name='customer_register'),
    path('employee_register/',views.employee_register.as_view(), name='employee_register'),
    path('login/',views.login_view, name='login'),
]