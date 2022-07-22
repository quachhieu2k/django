from django.urls import path
from .views import index, detail, login_view, logout_view, register_view, videoComment

urlpatterns = [
    path('',index, name= 'home'),
    path('detail/<pr_id>/<int:id>', detail, name= 'detail'),
    path('accounts/login/', login_view, name= 'loggin'),
    path('accounts/logout/', logout_view, name= 'logout'),
    path('accounts/register/', register_view, name= 'register'),
    path('detail/comment/', videoComment, name='videoComment'),
]