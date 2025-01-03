from django.urls import path
from .views import signup, signin, dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
]