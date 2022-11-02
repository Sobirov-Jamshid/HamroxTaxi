from nturl2path import url2pathname
from django.urls import path
from .views import home,signin,signup

urlpatterns = [
    path('',home,name='home'),
    path('signin/',signin,name='signin'),
    path('signup/',signup,name='signup'),
]