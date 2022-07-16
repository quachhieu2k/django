from django.urls import path
from .views import index, detail, login

urlpatterns = [
    path('',index, name= 'home'),
    path('detail/<pr_id>/<int:id>', detail, name= 'detail'),
    path('accounts/login/', login, name= 'login')
]