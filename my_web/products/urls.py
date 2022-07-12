from django.urls import path
from .views import index, detail

urlpatterns = [
    path('',index, name= 'home'),
    path('detail/<pr_id>/<int:id>',detail, name= 'detail')
]